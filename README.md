# podbbang 에피소드 다운로더

## 배경
팟빵의 특정 팟캐스트에서 인기도가 높은 에피소드들을 추려내어 해당 에피소드의 제목을 파일명으로 하여 다운로드를 받는다.

## 사용법
팟빵 홈페이지를 통해 특정 팟캐스트의 ID 번호를 확인한 후 최근부터 몇 페이지의 내용들을 대상으로 할지를 정한다.
이후 인기도로 정렬하거나 제목에서 특정 문자열을 포함한 리스트 또는 특정 문자열을 포함하지 않은 리스트들을 추려내어 목록을 확인한 후 해당 에피소드들을 다운로드 받을 수 있다.


Usage:
```
(base) $ python pb.py 'get_list 15781 2'
15781 2
http://www.podbbang.com/podbbangchnew/episode_list?id=15781&page=1
audio/mp3
audio/mp3
audio/mp3
audio/mp3
audio/mp3
audio/mp3
audio/mp3
audio/mp3
audio/mp3
audio/mp3
http://www.podbbang.com/podbbangchnew/episode_list?id=15781&page=2
audio/mp3
audio/mp3
audio/mp3
audio/mp3
audio/mp3
audio/mp3
audio/mp3
audio/mp3
audio/mp3
audio/mp3
(Cmd) print_list 
{'pid': 15781, 'eid': '23043322', 'title': '투자는 책과함께#46 글로벌 투자가가 주목하는 파괴적 혁신기업의 조건f목대균', 'like': 225}
{'pid': 15781, 'eid': '23043320', 'title': '최준영 박사의 지구본 연구소-28 《시즌1 최종회》 아듀! 지구본 연구소 가을에 다시 만나요!', 'like': 290}
{'pid': 15781, 'eid': '23043310', 'title': '최준영 박사의 지구본 연구소-27 롱기스트 워와 9 11 21세기 아프가니스탄', 'like': 361}
{'pid': 15781, 'eid': '23043307', 'title': '신의 경제사 특강 시즌3#7 절묘한 시점의 토지개혁 경제성장의 초석이었다', 'like': 212}
{'pid': 15781, 'eid': '23041116', 'title': 'P2-Live 두고 보자는 놈 하나 안무섭다_꼼꼼한 금요일  증시 각도기_190531', 'like': 465}
{'pid': 15781, 'eid': '23040365', 'title': '신과함께 74 《2019 업종분석 시리즈》 반도체 최첨단산업을 낱낱이 파헤치다f 최도연', 'like': 520}
{'pid': 15781, 'eid': '23039238', 'title': 'P2-Live 이제 유럽도 볼때다!_담넘어 목요일  증시 각도기_190530', 'like': 466}
{'pid': 15781, 'eid': '23037639', 'title': 'P2-Live 인플레이션보다 무서운 디플레이션_묵직한 수요일  증시 각도기_190529', 'like': 504}
{'pid': 15781, 'eid': '23036131', 'title': 'P2-Live 지금 꼭 챙겨봐야될 경제지표는_귀쏙쏙 화요일  증시 각도기_190528', 'like': 528}
{'pid': 15781, 'eid': '23031221', 'title': 'P2-Live 충격! 제3인터넷뱅크 전원탈락!_발칙한 월요일  증시 각도기_190527', 'like': 518}
{'pid': 15781, 'eid': '23029574', 'title': '신의 경제사 특강 시즌3#6 명나라 때 왜구가 창궐했던 까닭은', 'like': 509}
{'pid': 15781, 'eid': '23029572', 'title': '신의 경제사 특강 시즌3#5 영국은 어떻게 ‘인구폭발을 피할 수 있었나', 'like': 526}
{'pid': 15781, 'eid': '23029556', 'title': '최준영 박사의 지구본 연구소-26 소련 몰락의 단초 아프간 전쟁! 과연 미국은', 'like': 541}
{'pid': 15781, 'eid': '23029543', 'title': '최준영 박사의 지구본 연구소-25 동서양의 교차로 비운의 아프가니스탄', 'like': 670}
{'pid': 15781, 'eid': '23027783', 'title': '투자는 책과함께#45 돈주고도 못 구하는 희귀품절 도서 세스클라만의 안전마진f 이건규', 'like': 485}
{'pid': 15781, 'eid': '23026720', 'title': 'P2-Live 저금리가 경제회복의 능사인가_꼼꼼한 금요일  증시 각도기_190524', 'like': 483}
{'pid': 15781, 'eid': '23025177', 'title': 'P2-Live 미국 빅브라더 시대 열리나_담넘어 목요일  증시 각도기_190523', 'like': 485}
{'pid': 15781, 'eid': '23024739', 'title': '신과함께 73-2 글로벌 전략가가 제안하는 한국 투자 전략 No5f박석중', 'like': 399}
{'pid': 15781, 'eid': '23024732', 'title': '신과함께 73-1 부상투혼 글로벌 전략가의 열강f 박석중', 'like': 469}
{'pid': 15781, 'eid': '23023522', 'title': 'P2-Live 수축사회에 적응하는 7가지 투자원칙_묵직한 수요일  증시 각도기_190522', 'like': 500}
(Cmd) sort_list_by_like 
(Cmd) print_list 
{'pid': 15781, 'eid': '23029543', 'title': '최준영 박사의 지구본 연구소-25 동서양의 교차로 비운의 아프가니스탄', 'like': 670}
{'pid': 15781, 'eid': '23029556', 'title': '최준영 박사의 지구본 연구소-26 소련 몰락의 단초 아프간 전쟁! 과연 미국은', 'like': 541}
{'pid': 15781, 'eid': '23036131', 'title': 'P2-Live 지금 꼭 챙겨봐야될 경제지표는_귀쏙쏙 화요일  증시 각도기_190528', 'like': 528}
{'pid': 15781, 'eid': '23029572', 'title': '신의 경제사 특강 시즌3#5 영국은 어떻게 ‘인구폭발을 피할 수 있었나', 'like': 526}
{'pid': 15781, 'eid': '23040365', 'title': '신과함께 74 《2019 업종분석 시리즈》 반도체 최첨단산업을 낱낱이 파헤치다f 최도연', 'like': 520}
{'pid': 15781, 'eid': '23031221', 'title': 'P2-Live 충격! 제3인터넷뱅크 전원탈락!_발칙한 월요일  증시 각도기_190527', 'like': 518}
{'pid': 15781, 'eid': '23029574', 'title': '신의 경제사 특강 시즌3#6 명나라 때 왜구가 창궐했던 까닭은', 'like': 509}
{'pid': 15781, 'eid': '23037639', 'title': 'P2-Live 인플레이션보다 무서운 디플레이션_묵직한 수요일  증시 각도기_190529', 'like': 504}
{'pid': 15781, 'eid': '23023522', 'title': 'P2-Live 수축사회에 적응하는 7가지 투자원칙_묵직한 수요일  증시 각도기_190522', 'like': 500}
{'pid': 15781, 'eid': '23027783', 'title': '투자는 책과함께#45 돈주고도 못 구하는 희귀품절 도서 세스클라만의 안전마진f 이건규', 'like': 485}
{'pid': 15781, 'eid': '23025177', 'title': 'P2-Live 미국 빅브라더 시대 열리나_담넘어 목요일  증시 각도기_190523', 'like': 485}
{'pid': 15781, 'eid': '23026720', 'title': 'P2-Live 저금리가 경제회복의 능사인가_꼼꼼한 금요일  증시 각도기_190524', 'like': 483}
{'pid': 15781, 'eid': '23024732', 'title': '신과함께 73-1 부상투혼 글로벌 전략가의 열강f 박석중', 'like': 469}
{'pid': 15781, 'eid': '23039238', 'title': 'P2-Live 이제 유럽도 볼때다!_담넘어 목요일  증시 각도기_190530', 'like': 466}
{'pid': 15781, 'eid': '23041116', 'title': 'P2-Live 두고 보자는 놈 하나 안무섭다_꼼꼼한 금요일  증시 각도기_190531', 'like': 465}
{'pid': 15781, 'eid': '23024739', 'title': '신과함께 73-2 글로벌 전략가가 제안하는 한국 투자 전략 No5f박석중', 'like': 399}
{'pid': 15781, 'eid': '23043310', 'title': '최준영 박사의 지구본 연구소-27 롱기스트 워와 9 11 21세기 아프가니스탄', 'like': 361}
{'pid': 15781, 'eid': '23043320', 'title': '최준영 박사의 지구본 연구소-28 《시즌1 최종회》 아듀! 지구본 연구소 가을에 다시 만나요!', 'like': 290}
{'pid': 15781, 'eid': '23043322', 'title': '투자는 책과함께#46 글로벌 투자가가 주목하는 파괴적 혁신기업의 조건f목대균', 'like': 225}
{'pid': 15781, 'eid': '23043307', 'title': '신의 경제사 특강 시즌3#7 절묘한 시점의 토지개혁 경제성장의 초석이었다', 'like': 212}
(Cmd) exclude_keyword Live
(Cmd) print_list 
{'pid': 15781, 'eid': '23029543', 'title': '최준영 박사의 지구본 연구소-25 동서양의 교차로 비운의 아프가니스탄', 'like': 670}
{'pid': 15781, 'eid': '23029556', 'title': '최준영 박사의 지구본 연구소-26 소련 몰락의 단초 아프간 전쟁! 과연 미국은', 'like': 541}
{'pid': 15781, 'eid': '23029572', 'title': '신의 경제사 특강 시즌3#5 영국은 어떻게 ‘인구폭발을 피할 수 있었나', 'like': 526}
{'pid': 15781, 'eid': '23040365', 'title': '신과함께 74 《2019 업종분석 시리즈》 반도체 최첨단산업을 낱낱이 파헤치다f 최도연', 'like': 520}
{'pid': 15781, 'eid': '23029574', 'title': '신의 경제사 특강 시즌3#6 명나라 때 왜구가 창궐했던 까닭은', 'like': 509}
{'pid': 15781, 'eid': '23027783', 'title': '투자는 책과함께#45 돈주고도 못 구하는 희귀품절 도서 세스클라만의 안전마진f 이건규', 'like': 485}
{'pid': 15781, 'eid': '23024732', 'title': '신과함께 73-1 부상투혼 글로벌 전략가의 열강f 박석중', 'like': 469}
{'pid': 15781, 'eid': '23024739', 'title': '신과함께 73-2 글로벌 전략가가 제안하는 한국 투자 전략 No5f박석중', 'like': 399}
{'pid': 15781, 'eid': '23043310', 'title': '최준영 박사의 지구본 연구소-27 롱기스트 워와 9 11 21세기 아프가니스탄', 'like': 361}
{'pid': 15781, 'eid': '23043320', 'title': '최준영 박사의 지구본 연구소-28 《시즌1 최종회》 아듀! 지구본 연구소 가을에 다시 만나요!', 'like': 290}
{'pid': 15781, 'eid': '23043322', 'title': '투자는 책과함께#46 글로벌 투자가가 주목하는 파괴적 혁신기업의 조건f목대균', 'like': 225}
{'pid': 15781, 'eid': '23043307', 'title': '신의 경제사 특강 시즌3#7 절묘한 시점의 토지개혁 경제성장의 초석이었다', 'like': 212}
(Cmd) head 5
(Cmd) print_list 
{'pid': 15781, 'eid': '23029543', 'title': '최준영 박사의 지구본 연구소-25 동서양의 교차로 비운의 아프가니스탄', 'like': 670}
{'pid': 15781, 'eid': '23029556', 'title': '최준영 박사의 지구본 연구소-26 소련 몰락의 단초 아프간 전쟁! 과연 미국은', 'like': 541}
{'pid': 15781, 'eid': '23029572', 'title': '신의 경제사 특강 시즌3#5 영국은 어떻게 ‘인구폭발을 피할 수 있었나', 'like': 526}
{'pid': 15781, 'eid': '23040365', 'title': '신과함께 74 《2019 업종분석 시리즈》 반도체 최첨단산업을 낱낱이 파헤치다f 최도연', 'like': 520}
{'pid': 15781, 'eid': '23029574', 'title': '신의 경제사 특강 시즌3#6 명나라 때 왜구가 창궐했던 까닭은', 'like': 509}
(Cmd) download 
최준영 박사의 지구본 연구소-25 동서양의 교차로 비운의 아프가니스탄 - Downloading
[################################] 70247/70247 - 00:01:00
최준영 박사의 지구본 연구소-26 소련 몰락의 단초 아프간 전쟁! 과연 미국은 - Downloading
[################################] 80085/80085 - 00:01:01
신의 경제사 특강 시즌3#5 영국은 어떻게 ‘인구폭발을 피할 수 있었나 - Downloading
[################################] 67933/67933 - 00:00:54
신과함께 74 《2019 업종분석 시리즈》 반도체 최첨단산업을 낱낱이 파헤치다f 최도연 - Downloading
[################################] 90240/90240 - 00:01:09
신의 경제사 특강 시즌3#6 명나라 때 왜구가 창궐했던 까닭은 - Downloading
[################################] 58301/58301 - 00:00:55
(Cmd) 
```
