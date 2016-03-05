from bs4 import BeautifulSoup
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
    ##for c in ascii_lowercase:
    address = url.format('a', 1)
    r = requests.get(address)

    #print r.text
    soup = BeautifulSoup(r.text, "html.parser")
    for link in soup.find_all('tr'):
        print type(link.a)


if __name__ == "__main__":
    tree = GetUrlFile()
    playersurl = GetPlayerUrl(tree)
    AssembleListOfAllPlayers(playersurl)

