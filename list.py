import random
from bs4 import BeautifulSoup
import time

songs = ["a노래", "b노래", "c노래", "d노래"]
print(songs)
print(songs[0])
print(songs[1])
print(songs[2])
print(songs[3])

for song in songs:
    print(song)

print("AI야 노래 한곡만 추천해줘.")
print("""
알겠습니다.
제가 열심히 분석해서
고객님께 노래를 한곡
추천합니다.
    """)

# 멜론 차트 URL (2025년 기준 최신 URL이 다를 수 있음)
url = "https://www.melon.com/chart/index.htm"

# 멜론은 User-Agent 없으면 접근을 막을 수도 있음
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# 웹 페이지 요청
response = requests.get(url, headers=headers)
html = response.text

# BeautifulSoup을 사용하여 HTML 파싱
soup = BeautifulSoup(html, "html.parser")

# 노래 제목과 가수 찾기
songs = soup.select("tr.lst50, tr.lst100")  # 멜론 1~100위
for idx, song in enumerate(songs, start=1):
    title = song.select_one("div.ellipsis.rank01 a").text.strip()  # 노래 제목
    artist = song.select_one("div.ellipsis.rank02 a").text.strip()  # 가수명
    print(f"TOP {idx}. {title} - {artist}")

ai_song = random.choice(songs)
dd = ["두", "두", "두", "두둥"]
for d in dd:
    print(d)
    time.sleep(1)

print(f"제가 추천한 곡은 {ai_song}입니다.")

song1 = "a노래"
song2 = "b노래"
song3 = "c노래"

#print(song1)
#print(song2)
#print(song3)
