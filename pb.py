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
def get_list_by_like(pid):
    for page in range(SCAN_PAGES):
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

def get_list_by_keyword(pid):
    for page in range(SCAN_PAGES):
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

podcast_dict = {
    '법륜스님': 1805,
    '신과함께': 15781,
    '매불쇼': 16898,
}

if __name__ == '__main__':
    # pname = '법륜스님'
    pname = '신과함께'
    # pname = '매불쇼'
    elist = get_list_by_like(podcast_dict[pname])
    newlist = sorted(elist, key=lambda k: k['like'], reverse=True) 
    cnt = 1
    for ep in newlist:
        if NUM_DOWNLOADS < cnt:
            break

        if not 'P2-Live' in ep['title']:
            # print(ep)
            mp3_download(ep['pid'], ep['eid'], ep['title'])

        cnt += 1
