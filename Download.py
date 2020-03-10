import requests,re
from bs4 import BeautifulSoup
from Capdis import capdis

def download(douban,url,amount):

	try:
		print('.........正在下载第'+str(amount)+'页数据.........\n')
		response=douban.get(url)
		if response.status_code==200:
			print('.........第'+str(amount)+'页数据下载完毕.........\n')
			return response.text
		if response.status_code==403:
			print('\n##########已被豆瓣监控，正在尝试绕过监控##########\n')
			url_forbidden='https://www.douban.com/misc/sorry'
			while(1):
				html=BeautifulSoup(response.text,'html.parser')
				print(response.text)
				cap_href=html.find('img',alt='captcha')['src']
				cap_id=re.findall('(?<==).*',cap_href)[0]
				cap=capdis(cap_href).lower()
				postdata={
							'captcha-solution':cap,
							'captcha-id':cap_id,
							'original-url':url,
							'ck':douban.cookies['ck']
		  				  }
				response=douban.post(url_forbidden,data=postdata)
				if response.status_code==200:
					print('.........第'+str(amount)+'页数据下载完毕.........\n')
					return response.text
				else:
					print('\n验证码错误，正在尝试重新绕过................\n')
				
	except Exception:
		print('##########很遗憾，豆瓣服务器传来403Forbidden，爬行结束#########\n')
		print(response.text)
		return None
