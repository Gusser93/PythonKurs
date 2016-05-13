# dict mit author zu PDB

from bs4 import BeautifulSoup
import urllib2

list_of_proteins = ["4hhb", "1l2y"]
prefix = "http://www.rcsb.org/pdb/explore/explore.do?structureId="
dic = dict()
for protein in list_of_proteins:
    pdb = prefix + protein.upper()
    webpage = urllib2.urlopen(pdb).read()
    soup = BeautifulSoup(webpage, "lxml")
    for i in soup.find_all(id="experimentaldatabottom"):
        dic[protein.upper()] = i.li.text.split("\n")[2].strip()

print dic