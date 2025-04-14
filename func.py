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


def m100(a):
    print(a)