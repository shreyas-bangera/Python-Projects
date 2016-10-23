import requests
import urllib2
import json
import wget
import os
#from bs4 import BeautifulSoup

def ImagesSearch(link,q):
    try:
        json_data = json.load(urllib2.urlopen(link))
        for item in json_data['hits']:
            print "\n\nProcessing....................\n"
            image_link = str(item['webformatURL'])
            if not os.path.exists(q):
        		os.makedirs(q)
            wget.download(image_link, q)
    except:
           print "\nLooks like something went wrong :( \nPlease try again!"
           os.system("pause")

def main():
	try:
		query = raw_input("Enter your keyword : ")
		q = query.replace(' ', '%20')
		api_key = '2585067-fc19df3bc433d3e814950993f'
		url = r'http://pixabay.com/api/?key='+api_key+'&q='+q+'&image_type=photo'
		ImagesSearch(url,q)
	except:
		print "\nLooks like something went wrong :( \nPlease try again!"
		os.system("pause")

main()
