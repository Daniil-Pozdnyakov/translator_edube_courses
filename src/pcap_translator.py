import logging
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from translate import Translator


credentials_dict = {
            0: {
                'email@domen1': True,
            },
            1: {
                'email@domen2': True,
            },
            2: {
                'email@domen3': True,
            }
        }


class PCAPTranslate:

    def __init__(self, url:str ='https://edube.org/study'):
        self.driver = self.get_driver()
        self.url = url
        self.items_to_translate = list()
        self.translated_list = list()
        self.credentials_dict = credentials_dict

    @staticmethod
    def get_driver():
        driver = webdriver.Chrome()
        return driver

    def get_next_available_email(self, start: int = 0):
        i = start
        is_available = list(self.credentials_dict[i].values())[0]
        if is_available:
            return list(self.credentials_dict[i].keys())[0]
        try:
            self.credentials_dict[i].values()[0] == False
            print(self.credentials_dict[i].values())
            raise KeyError
            return self.get_next_available_email(i + 1)
        except KeyError as err:
            logging.error(f'{err=}')
            return 'no available emails'

    def process(self):
        self.driver.get(self.url)
        last = self.driver.title

        is_last = False
        count = 0
        while not is_last:
            try:
                if self.driver.title != last:
                    time.sleep(3)
                    last = self.driver.title
                    paragraphs = self.driver.find_elements(By.CSS_SELECTOR, 'p')
                    list_items = self.driver.find_elements(By.CSS_SELECTOR, '#left-box > div.lab li')
                    for i in range(len(paragraphs)):
                        if paragraphs[i].text != '':
                            self.items_to_translate.append(paragraphs[i].text)
                            count += len(paragraphs[i].text.split())
                            self.translated_list = self.translate_list(self.items_to_translate)
            except BaseException:
                pass

    def translate_list(self, list_to_translate: list) -> list:
        email = self.get_next_available_email()
        translator = Translator(to_lang='ru', provider='mymemory', email=email)
        for item in list_to_translate:
            translated_item = translator.translate(item)
            if 'MYMEMORY WARNING' in translated_item:


