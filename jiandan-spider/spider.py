#!/usr/bin/env python3
from pprint import pprint
from urllib import request
from bs4 import BeautifulSoup
import hashlib
import base64
import gzip
import io
import re


def md5(src):
    m = hashlib.md5()
    m.update(src.encode('utf-8'))
    return m.hexdigest()

def decode_base64(data):
    missing_padding=4-len(data)%4
    if missing_padding:
        data += '='* missing_padding
    return base64.b64decode(data)

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cookie':'nsfw-click-load=on; _gat_gtag_UA_462921_3=1; _ga=GA1.2.1395154870.1513853310; _gid=GA1.2.304204835.1513853310'
    }

def get_raw_html(url):
    req = request.Request(url=url, headers=headers)
    response = request.urlopen(req)
    text = response.read()
    encoding = response.getheader('Content-Encoding')
    if encoding == 'gzip':
        buf = io.BytesIO(text)
        translated_raw = gzip.GzipFile(fileobj=buf)
        text = translated_raw.read()
    text = text.decode('utf-8')
    return text

def get_hashes_constant_preurl (url):
    html = get_raw_html(url)
    soup = BeautifulSoup(html, 'lxml')
    preurl = 'http:'+soup.find(class_='previous-comment-page').get('href')
    #print("preurl: ", preurl)

    hashes = []
    for each in soup.find_all(class_='img-hash'):
        hashes.append(each.string)
        #print(each.string)
    
    js = re.search(r'<script\ssrc=\"\/\/(cdn.jandan.net\/static\/min\/.*?)\">.*?<\/script>', html)
    jsFileURL = 'http://'+js.group(1)
    jsFile = get_raw_html(jsFileURL)

    target_func = re.search(r'f_\w*?\(e,\"(\w*?)\"\)', jsFile)
    constant_hash = target_func.group(1)
    #print(constant_hash)

    return hashes, constant_hash, preurl


if __name__ == '__main__':
    url = 'http://jandan.net/ooxx/'

    #get hashes, constant-hash, previous page's url
    params = get_hashes_constant_preurl(url)
    hashes = params[0]
    constant_hash = params[1]
    preurl = params[2]
    
    index = 1
    for each in hashes:
        print("{} : {}".format(index, each))
        index += 1

    print("\n\n\n")
    print("constant_hash: ", constant_hash)
    print("\n\n\n")
    print("preurl: ", preurl)


