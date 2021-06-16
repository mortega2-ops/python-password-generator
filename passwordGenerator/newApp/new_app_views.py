from django.shortcuts import render
from django.http import HttpResponse
import requests
import re
from bs4 import BeautifulSoup

# Create your views here.


def scraper(self):
    article_list = []

    try:
        r = requests.get('http://www.holidayinsights.com/moreholidays/june.htm')
        # return HttpResponse('The scraping job succeded: ', r.status_code)
        soup = BeautifulSoup(r.content, "lxml")
        # tags = soup.find_all('p')
        # articles = soup.get_text()

        # for tag in tags:
        #     print(tag.text)
        #     article_list.append(tag.text)

        return render(self, 'newApp/scraper.html', {'list': soup.find_all(string=re.compile("Day$"))})

    except Exception as e:
        print('The Scraping Job failed. see exception: ')
        print(e)
        return HttpResponse('The Scraping Job failed. see exception: ' + str(e))