import requests,json
from bs4 import BeautifulSoup

def parser(html,amount):
	print('.........正在解析第'+str(amount)+'页数据.........\n')
	comments=[]
	try:
		soup = BeautifulSoup(html,'html.parser')
		commentitem=soup.find_all('div',class_='comment-item')
		if(len(commentitem)==0):
			raise Exception
		for item in commentitem:
			comment=item.find('p').string
			comments.append(comment)
		print('.........第'+str(amount)+'页数据解析完毕.........\n')
		return comments
	except Exception:
		return None
