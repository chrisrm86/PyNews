#!/usr/bin/python3
# -*- coding UTF-8 -*-
"""
##########################################################

Name: 		PyNews
Created by: Christian Morán
e-mail: 	christianrmoran86@gmail.com
More code: 	http://github.com/chrisrm86

##########################################################
"""
import ssl
from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
from datetime import *

def get_news(xml_news_url):
    actual_date = datetime.now()
    date_format = actual_date.strftime('%d / %m / %y')              # Add hour, minutes and seconds ->  %H:%M:%S'
    context = ssl._create_unverified_context()
    client = urlopen(xml_news_url, context=context)
    xml_page = client.read()
    client.close()

    from_page_soup = soup(xml_page, "xml")
    news_list = from_page_soup.find_all("item")

    line_separator =  "-"*50
    print(line_separator + "NEWS" + line_separator + '\n')
    print("Date: {} \n".format(date_format))
    print(line_separator + line_separator)

    for new in news_list:
        print(f'new title: {new.title.text}')
        print(f'new link: {new.link.text}')
        print(f'new publication date: {new.pubDate.text}')
        print(line_separator + "\n\n")

    def print_to_file(news_list):
        user_input = str(input("Print news in a text file? y/n: "))
        if user_input == 'y' or user_input == 'Y':
            filename = 'NEWS.txt'
            nf = open(filename, 'w+')
            nf.write("NEWS of {}\n\n\n".format(date_format))
            nf.write(line_separator + '\n')
            for new in news_list:
                nf.write(f'new title: {new.title.text} \n')
                nf.write(f'new link: {new.link.text} \n')
                nf.write(f'new publication date: {new.pubDate.text} \n\n')
                nf.write(line_separator + "\n\n")
            nf.close()
        elif user_input == 'n' or user_input == 'N':
            pass
        else:
            return print_to_file(news_list)

    print_to_file(news_list)


# news_url = "https://news.google.com/news/rss/?ned=us&gl=US&hl=en"   
sports_url = "https://news.google.com/news/rss/headlines/section/topic/SPORTS.en_in/Sports?ned=in&hl=en-IN&gl=IN"

get_news(sports_url)

print("Press Enter/Intro to exit")
input()