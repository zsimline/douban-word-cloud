from Login import login
from Info import info
from Download import download
from Parser import parser
from Dataclean import dataclean
from Datahandle import datahandle
import time 

if __name__=="__main__":
	starttime=time.time()
	douban=login()
	ID,number=info(douban)
	print('\n*********************爬行开始*********************\n')
	print('\n*********将要抓取'+number+'条评论*********')	
	url_downloadstart='https://movie.douban.com/subject/'+ID+'/comments?'
	amount=1676
	comments=[]

	try:
		while(1):
			time.sleep(2)
			print('\n------------------正在爬行第'+str(amount)+'页数据------------------\n')
			url_download=url_downloadstart+'start='+str(amount*20)+'&limit=20'
			print('当前URL是：',url_download,'\n')
			html=download(douban,url_download,amount)
			if(html==None):
				raise Exception
			temp=parser(html,amount)
			if(temp==None):
				raise Exception
			comments.append(temp)
			print('------------------第'+str(amount)+'页数据爬行完毕------------------\n')
			amount=amount+1
	except KeyboardInterrupt:
			print('\n#########人为终止爬行#########\n')
	except Exception:
			pass
	
	dataclean(comments)
	datahandle()
	endtime=time.time()
	numtime=(endtime-starttime)-(endtime-starttime)%1
	hour=str(int(numtime/3600))
	minute=str(int(numtime%3600/60))
	seconds=str(int(numtime%3600%60))	
	print('\n信息 ： 共计爬行'+str(amount-1)+'页		抓取到'+str(amount*20-20)+'条评论,		耗时'+hour+'小时'+minute+'分钟'+seconds+'秒\n\n\n\n\n')
