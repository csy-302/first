import requests
from bs4 import BeautifulSoup
import random

# 멜론 차트 URL (2025년 기준 최신 URL이 다를 수 있음)
url = "https://www.melon.com/chart/index.htm"

# 멜론은 User-Agent 없으면 접근을 막을 수도 있음
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36'
}
 
# 웹 페이지 요청
response = requests.get(url, headers=headers)

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(response.text, 'html.parser')

#리스트
songs = []

# 노래 제목과 가수 찾기
for entry in soup.select('tr.lst50, tr.lst100'):  # 상위 50위 및 100위 목록
    rank = entry.select_one('span.rank').get_text()
    title = entry.select_one('div.ellipsis.rank01 a').get_text()
    artist = entry.select_one('div.ellipsis.rank02 a').get_text()
    songs.append((rank, title, artist))

# 1. 멜론 100 출력
# 2. 멜론 50 출력
# 3. 멜론 10 출력
# 4. AI 추천 노래 출력
# 5. 가수 이름 검색
# 6. 파일에 저장
print("===================")
print("1. 멜론 100")
print("2. 멜론 50")
print("3. 멜론 10")
print("4. AI 추천 노래")
print("5. 가수 이름 검색")
print("6. 파일에 저장(멜론100)")
print("===================")

a = "<멜론 TOP 100>"
b = "<멜론 TOP 50>"
c = "<멜론 TOP 10>"
d = "<멜론 AI 추천>"
e = "<가수 이름 검색>"
f = "<파일에 저장하기>"

n = input("메뉴 입력: ")
if n == "1":
    print(a)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 100:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 가수: {artist}')

elif n == "2":
    print(b)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 50:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 가수: {artist}')

elif n == "3":
    print(c)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= 10:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 가수: {artist}')

elif n == "4":
    print(d)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        songs = soup.select('tr[data-song-no]')
        song_list = []

        for song in songs:
            rank = song.select_one('span.rank').text.strip()
            title = song.select_one('div.ellipsis.rank01 a').text.strip()
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            song_list.append((rank, title, artist))

        random_song = random.choice(song_list)
        print(f'\n[추천 곡: {random_song[1]} | 가수: {random_song[2]}]')

elif n == "5":
    print(e)
    s = input("가수 이름: ")

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        songs = soup.select('tr[data-song-no]')
        found_songs = []

        for song in songs:
            artist = song.select_one('div.ellipsis.rank02 a').text.strip()
            if s.lower() in artist.lower():
                rank = song.select_one('span.rank').text.strip()
                title = song.select_one('div.ellipsis.rank01 a').text.strip()
                found_songs.append((rank, title, artist))

        if found_songs:
            print(f"[<{s}> 노래 목록.]")
            for song in found_songs:
                print(f'{song[0]}위 | 제목: {song[1]} | 가수: {song[2]}')