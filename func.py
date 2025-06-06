import requests
from bs4 import BeautifulSoup
import random


def m000(a, c):
    print(a)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= c:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 가수: {artist}')

def m100(a):
    print(a)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
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

def m50(a):
    print(a)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
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

def m10(a):
    print(a)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
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


def m000(a, c):
    print(a)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

    songs = soup.select('tr[data-song-no]')

    for index, song in enumerate(songs):
        if index >= c:
            break
        rank = song.select_one('span.rank').text.strip()
        title = song.select_one('div.ellipsis.rank01 a').text.strip()
        artist = song.select_one('div.ellipsis.rank02 a').text.strip()
        print(f'{rank}위 | 제목: {title} | 가수: {artist}')

def m_random(d):
    print(d)
    url = 'https://www.melon.com/chart/index.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(url, headers=headers)
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
    else:
        print(f'[불러오기 실패]')