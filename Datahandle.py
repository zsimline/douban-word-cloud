import jieba
import pandas
import numpy
import matplotlib.pyplot as plt
import matplotlib
from wordcloud import WordCloud

def datahandle():
	print('\n.....................正在处理数据.....................')
	print('\n...............正在对数据进行筛选...............')
	fd=open('comments.txt','r')
	segment = jieba.lcut(fd.read())
	words_df=pandas.DataFrame({'segment':segment})
	stopwords=pandas.read_csv("stopwords.txt",index_col=False,quoting=3,sep="\t",names=['stopword'], encoding='utf-8')
	words_df=words_df[~words_df.segment.isin(stopwords.stopword)]
	print('\n...............正在统计词汇频率...............')
	words_stat=words_df.groupby(by=['segment'])['segment'].agg({"计数":numpy.size})
	words_stat=words_stat.reset_index().sort_values(by=["计数"],ascending=False)
	print('\n...............正在生成词云图...............')
	matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
	wordcloud=WordCloud(font_path="simhei.ttf",background_color="white",max_font_size=80)
	word_frequence = {x[0]:x[1] for x in words_stat.head(1000).values}
	word_frequence_list = []
	for key in word_frequence:
		temp = (key,word_frequence[key])
		word_frequence_list.append(temp)
	wordcloud=wordcloud.fit_words(dict(word_frequence_list))
	plt.imshow(wordcloud)
	plt.savefig("result.jpg")
	print('\n\n\n***************恭喜，所有工作都已经完成了***************')
