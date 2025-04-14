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

# 메뉴선택(숫자입력)
n = input("메뉴선택(숫자입력): ")
print(f"당신이 입력한 값은? {n}")

# 만약에 1을 입력하면
# 멜론 100 출력
if n == "1":
    print("멜론 100")
    #수집한 데이터 출력
    for i in range(100):
         print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

# 만약에 2를 입력하면
# 멜론 50 출력
elif n == "2":
    print("멜론 50")
    #수집한 데이터 출력
    for i in range(50):
         print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

# 만약에 3를 입력하면
# 멜론 10 출력
elif n == "3":
    print("멜론 10")
    for i in range(10):
         print(f"{songs[i][0]}. {songs[i][1]} - {songs[i][2]}")

# 만약에 4를 입력하면
# AI 추천곡 출력
    print("AI 추천곡")
    #랜덤 1곡 추천
    ai_song = random.choice(songs)
    print(f"추천곡은 {ai_song[1]} - {ai_song[2]} 입니다.") 

# 만약에 5를 입력하면
# 가수 이름 검색 출력
elif n == "5":
    print("가수 이름 검색")
    artist_name = input("가수 이름: ")
# 5를 입력하면 가수 이름 검색할 수 있게 입력창이 또 나와야 함
# 이름을 입력하면 해당 가수 이름의 노래 리스트가 출력

# 만약에 6을 입력하면
# 파일에 저장장
if n == "6":
    print("파일에 저장")


else:
    print("1~5까지 입력하세요")
    