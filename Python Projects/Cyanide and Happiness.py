#-------------------------------------------------------------------------------
# Name:        Cyanide and Happiness comic downloader
#
# Author:      Shreyas Bangera
#
# Created:     18-05-2016
#
# Copyright:   (c) www.shreyasbangera.php-dev.net
#-------------------------------------------------------------------------------

import os
import time
import wget
import requests
from bs4 import BeautifulSoup


def main():
    i = 39

    if not os.path.exists("Cyanide and Happiness"):
       os.makedirs("Cyanide and Happiness")

    print "Processing .....\n"
    print "***Cyanide and Happiness***"

    for i in range(39,4000):
        try:
             url = "http://explosm.net/comics/"+str(i)+"/"
             r = requests.get(url)
             soup = BeautifulSoup(r.content, "html.parser")

             for comic in soup.findAll("img", {"id":"main-comic"}):
                r_link = comic.get("src")
                image_link = "http:"+r_link
                print "\n\nComic no : "+str(i)+"\n"
                wget.download(image_link, "Cyanide and Happiness")
             i += 1
        except:
               pass

    print "\n\nDownload completed!\n"
    print "Enjoy\n"
    os.system("pause")

main()