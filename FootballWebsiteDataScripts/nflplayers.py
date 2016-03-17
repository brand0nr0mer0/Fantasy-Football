from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import xml.etree.ElementTree
from string import ascii_lowercase
import os
import requests
import csv
import numpy as np
import pandas as pd



playersurl = ""


def GetUrlFile():
    directory = os.getcwd()
    tree = xml.etree.ElementTree.parse(directory + '/staturls.xml')
    return tree

def GetPlayerUrl(xmltree):
    base = xmltree.find('base').text
    extension = xmltree.find('extensions').find('player').text

    return base + extension

def AssembleListOfAllPlayers(url):

    dataframe = pd.DataFrame(columns=['url', 'lastName', 'firstName'])
    for c in ascii_lowercase:
        page = 1
        while True:
            address = url.format(c, page)

            links = ExtractLinks(address)
            if not links: break
            for link in links:
                href = link.get('href').encode('ascii', 'ignore')
                playerName = link.text.encode('ascii', 'ignore')
                firstName, lastName = ParsePlayerName(playerName)

                if firstName and lastName:
                    dataframe = dataframe.append(pd.DataFrame({'url' : [href], 'lastName' : [lastName], 'firstName' : [firstName]}))
            page += 1

        print c + ' | page: ' + str(page)


    dataframe.to_csv('PlayerUrls.csv', sep=',')


def ParsePlayerName(playerName):
    nameSplit = playerName.split(',')
    if len(nameSplit) > 2: raise ValueError('Name has more than 2 values' + nameSplit)
    if len(nameSplit) == 2: ##log somehow for names that have 1 name or more than 2
        lastName = nameSplit[0]
        firstName = nameSplit[1].strip()
        return firstName, lastName

    return None, None

def ExtractLinks(address):
    r = requests.get(address)
    soup = BeautifulSoup(r.text, "html.parser", parse_only=SoupStrainer('table', 'statistics scrollable'),
                         from_encoding='UTF-8')
    links = soup.findAll('a')
    return links


if __name__ == "__main__":
    tree = GetUrlFile()
    playersurl = GetPlayerUrl(tree)
    AssembleListOfAllPlayers(playersurl)

