import requests,re
from bs4 import BeautifulSoup
from Capdis import capdis

def login():
	douban=requests.session()
	url_login='https://accounts.douban.com/login'
	douban.cookies['User-Agent']='Mozilla/5.0 (X11; Linux i686; rv:52.0) Gecko/20100101 Firefox/52.0'
	postdata={
				'source':'None',
				'redir':'https://www.douban.com',
				'form_email':'18713761095@163.com',
				'form_password':'zyz20149',
				'remember':'on',
				'login':'登录'
			  }
	login_flag=0
	while(login_flag==0):
		try:
			response_cap=douban.get(url_login).text
			soup=BeautifulSoup(response_cap,'html.parser')
			cap_href=soup.find('img',id='captcha_image')['src']
			cap_id=re.findall('(?<==).*(?=&)',cap_href)[0]
			cap=capdis(cap_href).lower()
			postdata['captcha-solution']=cap
			postdata['captcha-id']=cap_id
		except Exception:
			print('.........没有发现验证码.........')
			login_flag=1
		response_login=douban.post(url_login,data=postdata)
		try:
			temp=douban.cookies['ck']
			login_flag=1
			print('成功登录豆瓣，当前COOKIES是：')
			print('bid:',douban.cookies['bid'],'   ck:',douban.cookies['ck'],'   ue:',douban.cookies['ue'],'   dbcl2:',douban.cookies['dbcl2'],'\n')
		except Exception:
			print('验证码错误，正在尝试重新登录................')
	return douban
