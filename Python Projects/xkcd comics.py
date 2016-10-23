#-------------------------------------------------------------------------------
# Name:        XKCD Comic downloader
#
# Author:      Shreyas Bangera
#
# Created:     18-05-2016
#
# Copyright:   (c) www.shreyasbangera.php-dev.net
#-------------------------------------------------------------------------------

import os
import wget
import requests
from bs4 import BeautifulSoup


def main():
    i = 1

    if not os.path.exists("XKCD Comics"):
       os.makedirs("XKCD Comics")

    print "Processing .....\n"
    print "***XKCD Comic downloader***"

    for i in range(1,1680):
         try:
             url = "http://xkcd.com/"+str(i)+"/"
             r = requests.get(url)
             soup = BeautifulSoup(r.content, "html.parser")

             for comic in soup.findAll("div", {"id":"comic"}):
                image = comic.find("img")['src']
                print "\n\nComic number : "+str(i)
                final_comic = "http:"+image
                print final_comic
                wget.download(final_comic,"XKCD Comics")
             i += 1
         except:
                pass

    print "\n\nDownload completed!\n"
    print "Enjoy\n"
    os.system("pause")

main()