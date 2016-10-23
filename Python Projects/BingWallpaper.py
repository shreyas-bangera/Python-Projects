import os
import os.path
import requests
import urllib,cStringIO,wget,time,ctypes
from PIL import Image
from bs4 import BeautifulSoup

xml = 'http://www.bing.com/HPImageArchive.aspx?format=xml&idx=0&n=1&mkt=en-US'


def Wallapaper(xml_file):
    r = requests.get(xml_file)
    soup = BeautifulSoup(r.text, "html.parser")

    for link in soup.findAll("url"):
        imageLink = "http://www.bing.com"+link.text
        split_link = imageLink.split("rb/")
        img = split_link[1]

        if os.path.isfile(img):
           print "Checking........................\n"
           time.sleep(2)
           print "You have already downloaded today's image!\n"
           print "Come back tomorrow for new image\n"
           os.system("pause")
        else:
             print "Checking......................\n"
             time.sleep(2)
             print "Python is doing its magic.....\n"
             wget.download(imageLink)
             print "\n\nImage Name : " + img + "\n"
             print "Done!"
             os.system("pause")


Wallapaper(xml)
