#coding:utf-8
import random
if __name__=="__main__":
	result=""

	while result!="012":
		rand=random.randint(0,2)
		if len(result)==3:
			result=result[1:]+str(rand)
		else:
			result+=str(rand)

		print(u"燃やせ",u"友情",u"パッションは")[rand]
	print (u"ミツボシ☆☆★")

	
