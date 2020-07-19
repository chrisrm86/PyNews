#!/usr/bin/python3
# -*- coding UTF-8 -*-
"""
##########################################################

Name:       PyNews
Created by: Christian Morán
e-mail:     christianrmoran86@gmail.com
More code:  http://github.com/chrisrm86

##########################################################
"""
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from datetime import *

def get_news(xml_news_url):
    actual_date = datetime.now()
    date_format = actual_date.strftime('%d / %m / %y')
    hour_format = actual_date.strftime('%H:%M:%S')
    context = ssl._create_unverified_context()
    client = urlopen(xml_news_url, context=context)
    xml_page = client.read()
    client.close()

    from_page_soup = soup(xml_page, "xml")
    news_list = from_page_soup.find_all("item")

    line_separator =  "-"*50
    print('\n' + " " * 25 + "NEWS" + '\n')
    print("Date: {}".format(date_format) + ' '*18 + "Hour: {} \n".format(hour_format))
    print(line_separator + '\n')

    for new in news_list:
        print(f'Title: {new.title.text}' + '\n')
        print(f'Link: {new.link.text}'+ '\n')
        print(f'Publication date: {new.pubDate.text}')
        print(line_separator + '\n')

    def print_to_file(news_list):
        user_input = str(input("Print news in a text file? y/n: "))
        if user_input == 'y' or user_input == 'Y':
            filename = 'NEWS.txt'
            nf = open(filename, 'w+')
            nf.write(' '*25 + 'NEWS' + '\n')
            nf.write("Date: {}".format(date_format) + ' ' * 18 + "Hour: {} \n".format(hour_format))
            nf.write(line_separator + '\n')
            for new in news_list:
                nf.write(f'Title: {new.title.text} \n')
                nf.write(f'Link: {new.link.text} \n')
                nf.write(f'Publication date: {new.pubDate.text} \n\n')
                nf.write(line_separator + "\n\n")
            nf.close()
        elif user_input == 'n' or user_input == 'N':
            pass
        else:
            return print_to_file(news_list)
        print("News saved in 'NEWS.txt' file")

    print_to_file(news_list)


# news_url = "https://news.google.com/news/rss/?ned=us&gl=US&hl=en"   
sports_url = "https://news.google.com/news/rss/headlines/section/topic/SPORTS.en_in/Sports?ned=in&hl=en-IN&gl=IN"

get_news(sports_url)

print("Press Enter/Intro to exit")
input()