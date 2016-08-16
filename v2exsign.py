import requests
from bs4 import BeautifulSoup
import time

username='aaaaaaaaaa'
password='12345678'

base_url='http://www.v2ex.com'
login_url=base_url+'/signin'
daily_url=base_url+"/mission/daily"
my_headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36',
	'Referer':'http://www.v2ex.com/signin',
	'Host':'www.v2ex.com',
}


login_data={'next':'/'}

def newSession():
	return requests.session()

def getLogin(session):
	response=session.get(login_url,headers=my_headers)
	return response

def setLoginData(response):
	soup=BeautifulSoup(response.content,"html.parser")
	once=soup.find('input',attrs={'name':'once'}).get('value').encode('utf8')
	uname=soup.find('input',attrs={'type':'text','class':'sl'}).get('name').encode('utf8')
	upasswd=soup.find('input',attrs={'type':'password'}).get('name').encode('utf8')
	login_data["once"]=once
	login_data[uname]=username
	login_data[upasswd]=password

def doLogin(session):
	session.post(login_url,login_data,headers=my_headers)

def doSignin(session):
	response=session.get(daily_url,headers=my_headers)
	soupDaily=BeautifulSoup(response.text,"html.parser")
	item=soupDaily.find('input',class_='super normal button').get('onclick')
	signin_url=base_url+item.split("'")[1]
	session.get(signin_url,headers=my_headers)

def routine():
	session=newSession()
	response=getLogin(session)
	setLoginData(response)
	doLogin(session)
	doSignin(session)

if __name__=='__main__':
	routine()
