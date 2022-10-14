from ast import Try
from time import sleep
from turtle import update
from unicodedata import category
from urllib import response
import newspaper
from newspaper import article
import requests
import json

class newScrapper():
    def __init__(self, categories) -> None:
        self.__categories = categories
        self.__url = []
        self.__key = "7a7c94979e8f4ad0a6d8c1848a7052e7"
        self.__responses = {

            "status": "ok",
            "totalResults" : 0,
            "articles" : []
        }
        self.__data = {
            "status" : "ok",
            "total results" : 0,
            "articles" : []
        }

    def getData(self, url):
        url_i = newspaper.Article(url="%s" % (url), language='en')
        url_i.download()
        url_i.parse()
        return url_i.text
    def parser(self, response):
        return [response["articles"][0],response["articles"][1]]
    def ___updateContent(self):
        articles = self.__responses["articles"]
        for article in articles:
            url = article["url"]
            url_i = newspaper.Article(url="%s" % (url), language='en')
            
            try:
                url_i.download()
                url_i.parse()
                url_i.nlp()
            except:
                pass
            
            #sleep(10)
            temp = {
                "source" : article["source"]["name"],
                "url" : article["url"],
                "img" : article["urlToImage"],
                "time" : article["publishedAt"],
                "summary": url_i.summary.replace("\n", "")
            }
            self.__data["articles"].append(temp)
        
    def updateGeneralNews(self):
        link = "https://newsapi.org/v2/everything?q="
        rest = "&apiKey="
        
        for category in self.__categories:
            response = requests.get(link + category + rest + self.__key)
            r = self.parser(response.json())
            self.__responses["articles"].append(r[0])
            self.__responses["articles"].append(r[1])
            
        self.___updateContent()
        return 1

    def getGeneralNews(self):
         
        if (self.updateGeneralNews() == 1):
            return self.__data
    def jsonDump(self, name = "news.json"):
        with open("news.json", "w") as outfile:
            json.dump(self.__data, outfile)

class gifNews():
    def __init__(self) -> None:
        pass
        



    





