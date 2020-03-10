import json,re

def dataclean(comments):
	print('++++++++++正在进行数据存储与清洗++++++++++')
	with open('comments.json','a') as fj:
		json.dump(comments,fj,indent=4,ensure_ascii=False)
	with open('comments.txt','a') as ft:
		for comment in comments:
			for comm in comment:
				stritem=''			
				filterdata = re.findall(u'[\u4e00-\u9fa5]+',str(comm))
				for item in filterdata:
					stritem=stritem+item
					ft.write(stritem)
	print('++++++++++++数据存储与清洗完毕++++++++++')
