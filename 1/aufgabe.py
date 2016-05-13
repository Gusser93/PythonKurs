# dict mit author zu PDB

import urllib2
from bs4 import BeautifulSoup


def get_author_pdb_dict(list_of_proteins):
    prefix = "http://www.rcsb.org/pdb/explore/explore.do?structureId="
    dic = dict()
    for protein in list_of_proteins:
        pdb = prefix + protein.upper()
        webpage = urllib2.urlopen(pdb).read()
        soup = BeautifulSoup(webpage, "lxml")
        for i in soup.find_all(id="entry-history"):
            author_str = ""
            for j in i.children:
                if type(i) is type(j):
                    if j.get("class")[0] == "panel-body":
                        author_str = j.div.div.ul.text.split("\n")[4].strip()
                        break

            author_list = author_str.split(",")
            author_list = [author_list[i].strip() + ", " + author_list[i + 1].strip()
                           for i in range(len(author_list)) if i % 2 == 0]
            for author in author_list:
                if (str(author)) in dic:
                    dic[str(author)].append(protein.upper())
                else:
                    dic[str(author)] = [protein.upper()]
    return dic

if __name__ == "__main__":
    P_LIST = ["4hhb", "1l2y", "5et3", "5hkn", "5hkr", "4z08", "5hpn", "5aei", "5f1r"]
    print get_author_pdb_dict(P_LIST)
