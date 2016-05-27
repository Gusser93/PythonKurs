"""
parser for rcsb
"""
import urllib2
from bs4 import BeautifulSoup, SoupStrainer


def get_author_pdb_dict(list_of_proteins):
    """
    parses authors for given list of proteins
    :param list_of_proteins: given list of proteins
    :return: dict with author as key and a list of his proteins as value
    """

    prefix = "http://www.rcsb.org/pdb/explore/explore.do?structureId="
    dic = dict()
    for protein in list_of_proteins:
        pdb = prefix + protein.upper()
        page = urllib2.urlopen(pdb).read()
        strainer = SoupStrainer("meta", {"name": "citation_author"})
        soup = BeautifulSoup(page, "lxml", parse_only=strainer)

        authors = soup.find_all("meta")
        for author in authors:
            dic.setdefault(str(author.get("content")), []).append(protein.upper())
    return dic


def get_pdb_method_dict(list_of_proteins):
    """
    parses methods for given list of proteins
    :param list_of_proteins: given list of proteins
    :return: dict with protein as key and method as value
    """

    prefix = "http://www.rcsb.org/pdb/explore/explore.do?structureId="
    dic = dict()
    for protein in list_of_proteins:
        pdb = prefix + protein.upper()
        page = urllib2.urlopen(pdb).read()
        soup = BeautifulSoup(page, "lxml")
        for i in soup.find_all("strong", string="Method"):
            method = i.next_sibling[1:].strip()
            dic[protein.upper()] = str(method)
    return dic


if __name__ == "__main__":
    P_LIST = ["4hhb", "1l2y", "5et3", "5hkn", "5hkr", "4z08", "5hpn", "5aei", "5f1r"]
    print get_author_pdb_dict(P_LIST)
    print get_pdb_method_dict(P_LIST)
