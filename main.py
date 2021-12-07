from selenium import webdriver
from selenium.webdriver.common.by import By
from translate import Translator
import time

t_num = 0


def init_pcap():
    browser = webdriver.Chrome()
    browser.get('https://edube.org/study')
    return browser


def translate_list(list_txt):
    res_list = []
    global t_num
    email_list = ["email1",
                  "email2"]  # please add email from https://mymemory.translated.net/doc/keygen.php
    translator = Translator(to_lang="ru", provider="mymemory", email=email_list[t_num])  # replace language if you need
    print('Index acc now:', t_num)
    for i in list_txt:
        while (True):
            try:
                trans = translator.translate(i)
                break
            except Exception:
                print('Error on server translate')
        while 'MYMEMORY WARNING' in trans:
            print(trans)
            print('MyMemory acc sleep')
            print('Index next acc:', t_num)
            if t_num + 1 < len(email_list):
                t_num += 1
                translator = Translator(to_lang="ru", provider="mymemory",
                                        email=email_list[t_num])  # replace language if you need
                while (True):
                    try:
                        trans = translator.translate(i)
                        break
                    except Exception:
                        print('Error on server translate')
            else:
                raise Exception("All your accounts have pause")
        res_list.append(trans)
    return res_list


def check_pcap(browser):
    last = browser.title
    count = 0
    while True:
        try:
            if browser.title != last:
                time.sleep(3)
                last = browser.title
                element_p = browser.find_elements(By.CSS_SELECTOR, 'p')
                element_li = browser.find_elements(By.CSS_SELECTOR, '#left-box > div.lab li')
                print('Number of "p" elements:', len(element_p))
                list_p = []
                for i in range(len(element_p)):
                    if element_p[i].text != '':
                        print("Original:", element_p[i].text)
                        list_p.append(element_p[i].text)
                        count += len(element_p[i].text.split())
                result = translate_list(list_p)
                kol_empty = 0
                for i in range(len(element_p)):
                    if element_p[i].text != '':
                        print("Translate:", result[i - kol_empty])
                        print("document.querySelectorAll('p')[" + str(i) + "].insertAdjacentHTML('beforeBegin', '" +
                              result[
                                  i - kol_empty].replace("'", "") + "')")
                        try:
                            browser.execute_script(
                                "document.querySelectorAll('p')[" + str(i) + "].insertAdjacentHTML('beforeBegin', '" +
                                result[
                                    i - kol_empty].replace("'", "") + "')")
                        except Exception:
                            print("Error:", type(Exception).__name__)
                    else:
                        kol_empty += 1
                print('Number of "li" elements:', len(element_li))
                list_li = []
                for i in range(len(element_li)):
                    if element_li[i].text != '':
                        print("Original:", element_li[i].text)
                        list_li.append(element_li[i].text)
                        count += len(element_li[i].text.split())
                result_li = translate_list(list_li)
                kol_empty = 0
                for i in range(len(element_li)):
                    if element_li[i].text != '':
                        print("Translate:", result_li[i - kol_empty])
                        print("document.querySelectorAll('#left-box > div.lab li')[" + str(
                            i) + "].insertAdjacentHTML('beforeBegin', '" + result_li[
                                  i - kol_empty].replace("'", "") + "')")
                        try:
                            browser.execute_script(
                                "document.querySelectorAll('#left-box > div.lab li')[" + str(
                                    i) + "].insertAdjacentHTML('beforeBegin', '" + result_li[
                                    i - kol_empty].replace("'", "") + "')")
                        except Exception:
                            print("Error:", Exception.__name__)
                    else:
                        kol_empty += 1
                print("Number of words for this session:", count,
                      "Remember you have 10000 words per day limit on one account")
        except Exception:
            print('Page switch error or you use all limits per day')


def main():
    browser = init_pcap()
    check_pcap(browser)


main()
