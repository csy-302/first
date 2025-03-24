import requests
from bs4 import BeautifulSoup

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
    print(f"{idx}. {title} - {artist}")
