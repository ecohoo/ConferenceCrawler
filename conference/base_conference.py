from selenium import webdriver
from slugify import slugify
import os
import time
import random
import requests


class BaseConference(object):
    def __init__(self, year, download_paper, download_path, include, exclude):
        self.__year__ = year
        self.__driver__ = None
        self.__links__ = []
        self.__titles__ = []
        self.__root__ = f"{download_path}/{self.get_conference_name()}"
        self.__download_paper__ = download_paper
        self.__include__ = include
        self.__exclude__ = exclude

    def __init_driver__(self):
        self.__driver__ = webdriver.Chrome('conference/chromedriver.exe')
        if self.url() is not None:
            self.__driver__.get(self.url())
        else:
            print("[ERR] ", self.get_conference_name(), " url is None!")

    def get_conference_name(self):
        return self.__class__.__name__ + str(self.__year__)

    def retrieve(self):
        return None, None

    def url(self):
        pass

    def quit(self):
        if self.__driver__ is not None:
            self.__driver__.quit()

    def crawl(self):
        self.__init_driver__()
        self.retrieve()
        if self.__download_paper__:
            if len(self.__links__) > 0:
                os.makedirs(self.__root__, exist_ok=True)
            for i, link in enumerate(self.__links__):
                self.download(self.__titles__[i], link)
                time.sleep(random.uniform(4, 5))
        self.quit()

    def download(self, title, link):
        headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:57.0) Gecko/20100101 Firefox/57.0'}

        if link is not None:
            pdf_name = slugify(title)[:80]
            if os.path.isfile(self.__root__ + '/' + pdf_name + ".pdf"):
                print('existed', '\t', title, '\t', link)
            else:
                print(title, '\t', link)
                data = requests.get(link, timeout=80, headers=headers).content

                with open(self.__root__ + '/' + pdf_name + ".pdf", 'wb') as f:
                    f.write(data)

    def ignore(self, title):
        paper_title = title.casefold()
        for key in self.__include__:
            if key not in paper_title:
                return True
        for key in self.__exclude__:
            if key in paper_title:
                return True
        return False
