import requests
import urllib.request
from datetime import datetime
from bs4 import BeautifulSoup
import xlsxwriter

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36",
    "Accept-Language": "en-gb",
    "Accept-Encoding": "br",
}
now = datetime.now()
dt_string = now.strftime("%d%m%Y_%H%M%S")

outWorkbook = xlsxwriter.Workbook(dt_string+".xlsx")
outSheet = outWorkbook.add_worksheet()

url_site ="https://www.sagicor.com/en-JM/Personal-Solution/Investment/Sigma-Global-Funds"
response = requests.get(url_site)
soup = BeautifulSoup(response.text,'html.parser')

count = 0
x_count=0
y_count=0
while count <= 113:
    if x_count == 6:
        x_count = 0
        y_count+=1
    outSheet.write(y_count,x_count,soup.findAll('td')[count].text.strip())
    count+=1
    x_count+=1
outWorkbook.close()
