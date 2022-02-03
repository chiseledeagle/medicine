from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests
import bs4
from bs4 import BeautifulSoup as bs
import pywhatkit as kit
import mysql.connector
from django.contrib import messages

FirstName=''
LastName=''
username=''
email=''
passws=''
passc=''
email1=''
complain=''


def heading(request):
    return render(request,'home.html')

def patient(request):
    if request.method=="GET":
        val4=request.GET['patientnum']
        val4="+91"+val4
        med=request.GET['patientmed']
        name=request.GET['patientname']
        ap=request.GET['ap']
        hour=request.GET['hour']
        minute=request.GET['min']
        
        if ap=="am" or ap=="AM" or ap=="Am":
            min=int(minute)
            hrs=int(hour)
        elif ap=="pm" or ap=="PM" or ap=="Pm":
            hrs = int(hour)
            hrs=hrs+12
            min = int(minute)
        msg=name+", Greetings from Medical Journal. Hope you are doing well. It is "+hour+":"+minute+" "+ap+", kindly take your dose of "+med+"."
        kit.sendwhatmsg(val4,msg,hrs,min)
        return render(request, 'result3.html')

    else:
        return render(request, 'result3.html')
    
def home(request):
    return render(request, 'home.html')

def medicinesfind(request):
    return render(request, 'Find_Medicine.html')

def reminder(request):
    return render(request, 'reminder.html')

def login(request):
    global username,passwd
    if request.method=='POST':
        m=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='users')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='username':
                username=value
            elif key=='passwd':
                passwd=value
        c="select * from users where username='{}' and passwd='{}'".format(username,passwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            messages.warning(request, "Invalid username/password")
        else:
            messages.success(request, "Logged in/Signed up successfully")
            return render(request, 'welcome.html')
    return render(request, 'login.html')

def count_chars(str):
     upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
     for i in range(len(str)):
          if str[i] >= 'A' and str[i] <= 'Z': upper_ctr += 1
          elif str[i] >= 'a' and str[i] <= 'z': lower_ctr += 1
          elif str[i] >= '0' and str[i] <= '9': number_ctr += 1
          else: special_ctr += 1
     return upper_ctr, lower_ctr, number_ctr, special_ctr
           
def signup(request):
    global FirstName,LastName,username,email,passwd
    if request.method=='POST':
        m=mysql.connector.connect(host='localhost',user='root',passwd='1234',database='users')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=='FirstName':
                FirstName=value
            elif key=='LastName':
                LastName=value
            elif key=='username':
                username=value
            elif key=='email':
                email=value
            elif key=='passwd':
                passwd=value
            elif key=='passc':
                passc=value
        up, lo, nu, sp = count_chars(passwd)
        q=len(passc)
        if passwd==passc:
            if up>0 and lo>0 and nu>0 and sp>0:
                c="insert into users Values('{}','{}','{}','{}','{}')".format(FirstName,LastName,username,email,passwd)
                cursor.execute(c)
                m.commit()
                messages.success(request, "Logged in/Signed up successfully")
                return render(request, 'welcome.html')
            else:
                messages.warning(request, "Entered password doesn't have characters from A-Z,a-z,0-9 and/or special characters.")
        else:
            messages.warning(request, "Entered password doesn't match confirm password")
    return render(request, 'signup.html')

def pharmacy(request):
    return render(request, 'Find_Healthcare.html')

def custom(request):
    return render(request, 'Customer_care.html')

def welcome(request):
    messages.success(request, "Logged in/Signed up successfully")
    return render(request, 'welcome.html')
  
def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        url = 'https://www.ask.com/web?q=what+is+'+search
        res = requests.get(url)
        soup = bs(res.text, 'lxml')

        result_listings = soup.find_all('div', {'class': 'PartialSearchResults-item'})

        final_result = []
        count=0

        for result in result_listings:
            result_title = result.find(class_='PartialSearchResults-item-title').text
            result_url = result.find('a').get('href')
            result_desc = result.find(class_='PartialSearchResults-item-abstract').text

            final_result.append((result_title, result_url, result_desc))
            count+=1
            if count==2:
                break

        context = {
            'final_result': final_result
        }
        

        return render(request, 'Search_Result.html', context)
        

    else:
        return render(request, 'Search_Result.html')

def search1(request):
    if request.method == 'POST':
        search1 = request.POST['search1']
        url = 'https://www.ask.com/web?q=find+'+search1
        res = requests.get(url)
        soup = bs(res.text, 'lxml')

        result_listings = soup.find_all('div', {'class': 'PartialSearchResults-item'})

        final_result = []
        count=0

        for result in result_listings:
            result_title = result.find(class_='PartialSearchResults-item-title').text
            result_url = result.find('a').get('href')
            result_desc = result.find(class_='PartialSearchResults-item-abstract').text

            final_result.append((result_title, result_url, result_desc))
            count+=1
            if count==3:
                break

        context = {
            'final_result': final_result
        }
        

        return render(request, 'Search_Result.html', context)
        

    else:
        return render(request, 'Search_Result.html')

def searchhelp(request):
    if request.method == 'POST':
        searchhelp = request.POST['searchhelp']
        url = 'https://www.ask.com/web?q=find+'+searchhelp
        res = requests.get(url)
        soup = bs(res.text, 'lxml')

        result_listings = soup.find_all('div', {'class': 'PartialSearchResults-item'})

        final_result = []
        count=0

        for result in result_listings:
            result_title = result.find(class_='PartialSearchResults-item-title').text
            result_url = result.find('a').get('href')
            result_desc = result.find(class_='PartialSearchResults-item-abstract').text

            final_result.append((result_title, result_url, result_desc))
            count+=1
            if count==3:
                break

        context = {
            'final_result': final_result
        }
        

        return render(request, 'Search_Result.html', context)
        

    else:
        return render(request, 'Search_Result.html')
