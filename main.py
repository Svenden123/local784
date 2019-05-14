import requests
import xmltodict

urlJson = 'https://raw.githubusercontent.com/netology-code/py-homework-basic-files/master/' \
          '3.1.formats.json.xml/newsafr.json'
response = requests.get(urlJson)
dataJson = response.json()['rss']['channel']['items']

urlXML = 'https://raw.githubusercontent.com/netology-code/py-homework-basic-files/' \
         'master/3.1.formats.json.xml/newsafr.xml'
response = requests.get(urlXML)
dataXML = xmltodict.parse(response.text)['rss']['channel']['item']

isJson = input("Сортировать JSON ? (1-да, 2-нет)")

fullText = ''
for e, item in enumerate(dataXML if isJson == '1' else dataJson):
    fullText += item['title'] + ' '
    fullText += item['description']

freq = dict()
for i in fullText.split():
    f = freq.get(i, 0)
    freq[i] = f + 1

freq = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
print(freq)