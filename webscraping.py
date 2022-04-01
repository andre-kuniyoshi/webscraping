# -*- encoding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0'}

# ações JNJ Johnson & Johnson (JNJ)
url= "https://finance.yahoo.com/quote/JNJ/financials?p=JNJ"
html = requests.get(url, headers=header).content

soup = BeautifulSoup(html, 'html.parser')

operationIncomeLine = soup.find_all("div", {"data-test": "fin-row"})[4]
operationIncomeValues = operationIncomeLine.contents[0].contents
del operationIncomeValues[0]

for ops in operationIncomeValues:   
    # value = ops.string
    value = ops.next_element.contents[0]
    print(value)

# operationIncomeValue = operationIncomeLine.contents[0].contents[3].string
# operationIncomeValue2 = operationIncomeLine.contents[0].contents[3].next_element.contents[0]
# print(operationIncomeValue)
# print(operationIncomeValue2)
