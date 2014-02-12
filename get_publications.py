#! /usr/bin/env python

from Bio import Entrez, Medline
from datetime import datetime
import time

Entrez.email = 'BeatsonLab@gmail.com'

def fetch(t, s):
    h = Entrez.esearch(db='pubmed', term=t, retmax=10000, sort=s)
    idList = Entrez.read(h)['IdList']
    results = "Total publications for SA Beatson: **"+str(len(idList))+"**\n\n"
    results+="Chronologically sorted:\n\n"

    if idList:
        handle = Entrez.efetch(db='pubmed', id=idList, rettype='medline', retmode='text')
        records = Medline.parse(handle)
        max = len(idList)+1
        for record in records:
            title = record['TI']
            author = ', '.join(record['AU'])
            source = record['SO']
            pub_date = datetime.strptime(record['DA'], '%Y%m%d').date()
            pmid = record['PMID']
            cur_pub = "| **%i.** %s\n| %s\n| %s\n| http://www.ncbi.nlm.nih.gov/pubmed/%s\n|\n" % (max-1,title, author,
                        source, pmid)
            results = results+cur_pub
            max=max-1
    return results
with open("content/pages/Publications.rst", "w") as fout:
    
    fout.write("Publications\n")
    fout.write("============\n\n")
    fout.write("These were automatically extracted from PubMed on "+ time.strftime("%c\n\n"))
    fout.write(fetch('Beatson S[Author]', 'pub date'))

