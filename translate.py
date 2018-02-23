import os
import sys
import requests
from bs4 import BeautifulSoup

def translate(fpath, opath=None):
    if not opath:
        opath='%s.csv'%(os.path.splitext(fpath)[0])
    with open(fpath) as f:
        dna_data = f.read()
        URL='https://web.expasy.org/cgi-bin/translate/dna_aa'
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        payload = {'pre_text' : dna_data, 'output' : 'Compact ("M", "-", no spaces)', 'code' : 'Standard'}
        res = requests.request('POST', URL, headers=headers, data=payload)

        soup = BeautifulSoup(res.text, 'lxml') #要素を抽出
        post_texts = [a.get_text().replace('\n', '') for a in soup.find_all('pre')]
        forword = post_texts[:3]
        reverse = post_texts[3:]
        # print(forword)
        # print(reverse)

        with open(opath,'w') as output:
            for i, data in enumerate(forword):
                output.write('forword, %d, %s\n'%(i+1,data))
            for i, data in enumerate(reverse):
                output.write('reverse, %d, %s\n'%(i+1,data))

argc=len(sys.argv)
if argc>=2:
    fpath = sys.argv[1]
    if argc==3:
        translate(fpath,sys.argv[2])
    else:
        translate(fpath)
else:
    print('USAGE python translate.py input_file [output_file]')
