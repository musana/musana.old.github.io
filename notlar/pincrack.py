import hashlib
'''ccc Musa Reis'''
hesh = "FA4DB51573984882209218E2BCF6F1E8D0E77AD5279DE71801B30FB92C0F5D07670AA2F4"
salt = "1690238848975470272"
md5pw  = hesh[40:]
for i in range(4,10):
	for j in range(pow(10,i)):
			pin = str(j).zfill(i)
			bfstr = pin + salt
			md5bf = hashlib.md5(bfstr.encode('utf-8')).hexdigest()
			if(md5pw == md5bf):
				print("Found! Pin=",pin)
				exit()
