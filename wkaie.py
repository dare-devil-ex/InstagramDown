import re
import requests as r
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver import Chrome

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920,1080')
options.add_argument('--no-sandbox')


class Wkaie:
    def down(key):
        _priv = "https://imginn.com/p/" + key + ""
        print(_priv)
        
        try:
            x = Chrome(options=options)
            x.get(_priv)
            
            ddex = x.page_source
            wkan = x.
            
            print(wkan)
            
            
        except:
            pass
        
    
    def Process(_url):
        process = _url.split("/")
        print(process)
        try:
            if re.findall("instagram.com", _url) and re.findall("/reel/", _url):
                Wkaie.down(process[4])
                print("pass")
            else:
                print("Only Reels")
        except:
            print("Invalid url")
            
Wkaie.Process("https://instagram.com/reel/DDjngVug51t/?igsh=bXlvNzN1OXZtNzB4")