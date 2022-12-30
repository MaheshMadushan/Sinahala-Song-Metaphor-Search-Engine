import requests
from string import ascii_lowercase as alc
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium import webdriver
import xlsxwriter
workbook = xlsxwriter.Workbook('songs.xlsx')
worksheet = workbook.add_worksheet()
row_num = 0
driver = webdriver.Edge()
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0','Accept-Language': 'en-US,en;q=0.5',"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"}
for i in alc:
    response = requests.get(f"http://lyricslk.com/lyrics/sort/{i}",headers = HEADERS)
    soup = BeautifulSoup(response.content, 'html.parser')
    divs = soup.find_all('div', class_='ResTitleSin')
    for div in divs:
        song_link = div.a['href']
        driver.get(song_link)
        song = driver.find_element(By.ID, 'lyricsBody')
        songInfo = driver.find_element(By.ID, 'lyricsTitle')
        worksheet.write(row_num, 0, song.text)
        worksheet.write(row_num, 1, songInfo.text)
        row_num += 1
driver.quit()
workbook.close()