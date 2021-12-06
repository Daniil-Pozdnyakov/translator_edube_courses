# translator_edube_courses
Python script for translate edube courses. Standard translator extensions not work on edube. You can use that programm. You can see both the original and the translated text at the same time.
![Script work example](https://i.imgur.com/Ei76a1p.png)
Installation: 
1. Install Google Chrome.
2. Download project and unpack.
3. Move project folder translator_edube_courses-main to your home folder.

Example:
  
  MacOS:
    
Use Finder panel. Select "Go" > "Home" for install ![MacOS Finder panel](https://www.cnet.com/a/img/nv6yIA6MZtMm7NV9hs4ZkK2Pqto=/2017/01/27/e5d49edd-f9c8-4e3a-b211-5a91d07526c1/go-home.jpg)
    
4. Register on https://translated.com/top/sign-up. After get keys on https://mymemory.translated.net/doc/keygen.php.
5. Open project folder and **change keys, where have comment # please add email and change output language on your, where have two comments # replace language if you need in "main.py"** (You can open that with TextEdit. Use right mouse button and select "Open With" > TextEdit)
6. Open terminal and install Selenium module ```pip install selenium```
7. Open terminal and install translate module ```pip install translate```
8. Open terminal and use ```cd translator_edube_courses-main``` 
9. Use ```python main.py```
10. Profit!

That script translate course page every redirect on new page. Pause on translation: 5-10 seconds. That normal, just wait. You can see all information and errors in terminal.

Info:
- Number of "p" elements: Script see block text elements and send that on translate server
- Number of "li" elements: Script see table elements and send that on translate server
- Original: That original text from site on English
- Translate: That translated on your destination language text
- document.querySelectorAll: that js script for add translate on page
- Number of words for this session: message have number of words for now programm session (not all last sessions)

Exceptions messages:
- MYMEMORY WARNING: You use all your words today. You can see in terminal time for reset limit
- MyMemory acc sleep: Account have block after limit usage. Program switch account on another
- Index next acc: Next acc for using. That info about switch accounts. Just see
- Error on server translate: Problems on remote translate server or you have problems with internet. Check your internet and restart program
- All your accounts have pause: All account have block after limit usage. Wait unblock or add new accounts
- Page switch error or you use all limits per day: Problem with page switch or your accounts not work. Go another page or fix your accounts

Switch account function have test mode. Please, chat me if that have errors.

Script created by Daniil Pozdnyakov. Search me in chats or message me for help on pozd20001@yandex.ru
