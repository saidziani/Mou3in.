#!/usr/bin/python3

import os, nltk, pickle
from stop_words import get_stop_words
from string import punctuation
from bs4 import BeautifulSoup


stopWords = get_stop_words('arabic')
punctuation += '،؟'

class PreProcess():
    def __init__(self,lang = 1, article = False):
        self.article = article
        self.lang = lang

    def getArticleContent(self, article):
        if os.path.exists(article):
            return open(article, 'r').read() 

    def getTokenizedArticle(self, content):
        content = ''.join(c for c in content if c not in punctuation)
        words = nltk.word_tokenize(content)     
        cleandWords = set(words) - set(stopWords)
        return list(set(cleandWords))

    def getPickleContent(self, pklFile):
        with open (pklFile, 'rb') as fp:
            itemlist = pickle.load(fp)
        return itemlist

    def setPickleContent(self, fileName, itemList):
        with open(fileName+'.pkl', 'wb') as fp:
            pickle.dump(itemList, fp)

    def getSents(self, content):
        sents = content.split('.')
        sents = [sent for sent in sents if sent.strip() != ""]
        return sents


    def getXMLsents(self, content):
        soup = BeautifulSoup(content,'lxml')
        packet = soup.find_all("source")
        toReturn, cpt = [], 0
        for pack in packet:
            if pack.attrs['operation'] == '?':
                toReturn.append((pack, 1))
                cpt += 1
            else:
                toReturn.append((pack, 0))
        return cpt, toReturn

    def getXMLtext(self, item):
        soup = BeautifulSoup(str(item), 'lxml')
        source = soup.find("source")
        return source.text









    

