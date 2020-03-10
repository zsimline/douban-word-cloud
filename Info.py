import requests,re
from bs4 import BeautifulSoup

def info(douban):
	url_nowplaying='https://movie.douban.com/cinema/nowplaying/beijing/'
	response=douban.get(url_nowplaying).text	
	html_nowplaying=BeautifulSoup(response,'html.parser')
	playinglist=html_nowplaying.find('ul',class_='lists')
	movielists=playinglist.find_all('li',class_='list-item')
	movieinfo=[]
	for movie in movielists:
		info={}
		info['ID']=movie['data-subject']
		info['name']=movie['data-title']
		movieinfo.append(info)
	print('当前正在热映的电影列表：')
	for movie in movieinfo:
		print(movie)
	ID=input("\n请输入电影ID:  ")
	html=requests.get('https://movie.douban.com/subject/'+str(ID)+'/comments').text
	st=BeautifulSoup(html,'html.parser').find('li',class_='is-active').find('span').string
	number=re.findall('\d+',st)[0]
	return ID,number
