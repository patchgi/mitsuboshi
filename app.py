#coding:utf-8
import random
if __name__=="__main__":
	result=""

	while result!="012":
		rand=str(random.randint(0,2))
		if len(result)==3:
			result=result[1:]+rand
		else:
			result+=rand
		if rand=="0":
			print ("燃やせ")
		elif rand=="1":
			print ("友情")
		else:
			print ("パッションは")
	
	print ("ミツボシ☆☆★")

	
