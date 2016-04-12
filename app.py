#coding:utf-8
import random
if __name__=="__main__":
	result="000"

	while result!="012":
		rand=random.randint(0,2)
		result=result[1:]+str(rand)
		print(u"燃やせ",u"友情",u"パッションは")[rand]
	print (u"ミツボシ☆☆★")

	
