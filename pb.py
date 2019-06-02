import cmd2
import re
import requests
from itertools import count
from pathlib import Path
from bs4 import BeautifulSoup
from clint.textui import progress
import sys

SCAN_PAGES = 2
NUM_DOWNLOADS = 17

CHARS_TO_REMOVE_FROM_FILENAME = "|\\?*<\":>+[]/'·\.,()’"
episode_list = []

podcast_dict = {
    '법륜스님': 1805,
    '신과함께': 15781,
    '매불쇼': 16898,
}

class CmdLineApp(cmd2.Cmd):    
    elist = []
    def do_names(self, args):
        print(podcast_dict)

    def do_get_list(self, args):
        '''get_list PID NUM_PAGES
        '''
        items = args.split()
        pid = int(items[0])
        pages = int(items[1])
        print(pid, pages)
        self.elist = get_list_by_like(pid, pages)

    def do_sort_list_by_like(self, args):
        self.elist = sorted(self.elist, key=lambda k: k['like'], reverse=True) 

    def do_print_list(self, args):
        for ep in self.elist:
            print(ep)

    def do_download(self, args):
        for ep in self.elist:
            mp3_download(ep['pid'], ep['eid'], ep['title'])

    def do_search_keyword(self, args):
        '''Get episodes including keyword
        '''
        keyword = args
        new_list = []
        for ep in self.elist:
            if keyword in ep['title']:
                new_list.append(ep)

        self.elist = new_list

    def do_exclude_keyword(self, args):
        ''' Get episodes not including keyword
        '''
        keyword = args
        new_list = []
        for ep in self.elist:
            if not keyword in ep['title']:
                new_list.append(ep)

        self.elist = new_list

    def do_head(self, args):
        items = args.split()
        max_number = int(items[0])
        self.elist = self.elist[:max_number]

    def do_clear_list(self, args):
        self.elist = []


def get_list_by_like(pid, pages=SCAN_PAGES):
    for page in range(pages):
        page += 1
        url = 'http://www.podbbang.com/podbbangchnew/episode_list?id={pid}&page={page}'.format(pid=pid, page=page)

        print(url)
        response = requests.get(url)
        response.encoding = 'utf8'
        html = response.text

        soup = BeautifulSoup(html, 'lxml')

        for dl_tag in soup.select('li > dl'):
            # print(dl_tag)
            try:
                title = dl_tag.find('dt')['title']
                new_title = get_android_filename(title)
                like = int(dl_tag.find('dd', class_ ='dd_heart').text.replace(',', ''))
                js = dl_tag['onclick']
                matched = re.search(r"'(\d+)',\s*'(\w+/\w+)'", js)
                if matched:
                    eid, content_type = matched.groups()
                    if 'video' in content_type:
                        continue
                    episode_list.append({
                        'pid': pid,
                        'eid': eid,
                        'title': new_title,
                        'like': like
                        })
                    print(content_type)
                    assert('audio' in content_type)
                    # print('{}=>{} ({})'.format(title, new_title, like))
                    # open(new_title+'.mp3', 'a').close()
            except KeyError:
                print('Ended')
                return None
    
    return episode_list


def mp3_download(pid, eid, title):
    url = 'http://www.podbbang.com/download?pid={pid}&eid={eid}'.format(pid=pid, eid=eid)

    headers = {
        'Referer': 'http://www.podbbang.com/ch/{pid}'.format(pid=pid),
    }
    r = requests.get(url, headers=headers, stream=True)

    if r.status_code == 200:
        filepath = Path('{}.mp3'.format(title))
        total_length = int(r.headers.get('content-length'))

        if filepath.exists() and filepath.stat().st_size == total_length:
            print('{} - File exists.'.format(title))
        else:
            print('{} - Downloading'.format(title))
            with filepath.open('wb') as f:
                chunk_size = 1024
                expected_size = (total_length//chunk_size) + 1

                for chunk in progress.bar(r.iter_content(chunk_size=chunk_size), expected_size=expected_size):
                    f.write(chunk)
    else:
        print('download failed. status code = {}'.format(r.status_code))

def get_android_filename(filename):
    new_fn = filename
    for c in CHARS_TO_REMOVE_FROM_FILENAME:
        new_fn = new_fn.replace(c, '')
    return new_fn


if __name__ == '__main__':
    app = CmdLineApp()
    sys.exit(app.cmdloop())