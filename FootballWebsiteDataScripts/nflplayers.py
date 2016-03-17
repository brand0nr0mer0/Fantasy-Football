from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import xml.etree.ElementTree
from string import ascii_lowercase
import os
import urllib2
import requests

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
    ##for c in ascii_lowercase: need to iterate through all letters
    ## for each letter then iterate through all pages
    address = url.format('a', 1)
    r = requests.get(address)


    soup = BeautifulSoup(r.text, "html.parser", parse_only=SoupStrainer('table', 'statistics scrollable'), from_encoding='UTF-8')
    links = soup.findAll('a')

    playerList = []
    for link in links:
        href = link.get('href').encode('ascii', 'ignore')
        playerName = link.text.encode('ascii', 'ignore')
        tup = (href, playerName)
        playerList.append(tup)

    for row in playerList:
        print row




if __name__ == "__main__":
    tree = GetUrlFile()
    playersurl = GetPlayerUrl(tree)
    AssembleListOfAllPlayers(playersurl)

