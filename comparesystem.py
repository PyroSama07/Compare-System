from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests
from bs4 import BeautifulSoup
import mysql.connector


def checkconec():
  mycon=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1516")
  if mycon.is_connected():
    print("CONNECTED TO MYSQL")
  else:
    print("ERROR")
    
def createdatabase():
  mycon=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1516")
  c=mycon.cursor()
  c.execute("create database IF NOT EXISTS test")
  
def createtable():
  mycon=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1516")
  c=mycon.cursor()
  c.execute("use test")
  c.execute("create table IF NOT EXISTS test(NAME varchar(50) PRIMARY KEY,PRICE varchar(50),RATING int(3))")
  
def check(category):
  if(category=='Mobiles'):
    mobile()
  elif(category=='Laptops'):
    laptop()
  elif(category=='HeadPhones'):
    headphone()
  elif(category=='TeleVision'):
    tv()
  else:
    messagebox.showerror(message='Choose one of the given categories',title='ERROR')
    
def detail12(x,y):
  counter=0
  for i in range(len(det)):
    if(det[i].get_text()==x):
      counter=i
      break
  det1=soup1.find_all('li',class_='_21lJbe')
  list1=det1[counter].get_text()
  y.append(list1)

def error(x):
  if(x==(product1.get()).replace(" ","")):
    messagebox.showerror(message="Product 1 Not found",title="ERROR")
  else:
    messagebox.showerror(message="Product 2 Not found",title="ERROR")
    
def tv():
  global det
  global soup1
  prod1,prod2=(product1.get()).replace(" ",""),(product2.get()).replace(" ","")
  products=[prod1,prod2]
  n1=[]
  d1=[]
  r1=[]
  p1=[]
  o1=[]
  b1=[]
  c1=[]
  ra=[]

  ##Declaring the url
  for product in products:
      a='https://www.flipkart.com/televisions/pr?sid=ckf,czl&q='
      c='&otracker=categorytree'
      b=product
      url=a+b+c
      page=requests.get(url)

  ##Scraping website
      
      soup = BeautifulSoup(page.content,'html.parser')
      price = soup.select('div._30jeq3')
      name = soup.select('div._4rR01T')
      rating = soup.select('div._3LWZlK')
      try:
        
        p1.append(price[0].get_text())
        n1.append(name[0].get_text())
        ra.append(rating[0].get_text())
        print(p1)
        print(n1)
        print(ra)

        ##Opening the link to extract details
        detail=soup.find_all('a',class_='_1fQZEK')
        d=detail[0].get('href')
        url1=a+d
        page1=requests.get(url1)
        soup1=BeautifulSoup(page1.content,'html.parser')

          ##Finding the details
        det=soup1.find_all('td',class_='_1hKmbr col col-3-12')
    
        detail12('Display Size',d1)
        detail12('Screen Type',o1)
        detail12('Smart TV',r1)
        detail12('Power Consumption',b1)
      except:
        error(product)
        continue
  if(n1!=[]):    
    info=Tk()
    info.geometry("+400+300")
    info.title('Comparison')
          
    Label(info,text='PRICE : ',font=("Arial",15)).grid(row=1,column=0,pady=5)
    Label(info,text='RATING : ',font=("Arial",15)).grid(row=2,column=0,pady=5)
    Label(info,text='Display Size : ',font=("Arial",15)).grid(row=3,column=0,pady=5)
    Label(info,text='Screen Type : ',font=("Arial",15)).grid(row=4,column=0,pady=5)
    Label(info,text='Smart TV : ',font=("Arial",15)).grid(row=5,column=0,pady=5)
    Label(info,text='Power Consumption : ',font=("Arial",15)).grid(row=6,column=0,pady=5)
           
  for i in range(2):
    try:
      Label(info,text=n1[i],font=("Courier"),wraplength=300).grid(row=0,column=i+1,pady=5,padx=5)
      Label(info,text=p1[i],font=("Arial",15),fg='#C5C3C3').grid(row=1,column=i+1,pady=5)
      Label(info,text=ra[i],font=("Arial",15),fg='#C5C3C3').grid(row=2,column=i+1,pady=5)
      Label(info,text=d1[i],font=("Arial",15),fg='#C5C3C3').grid(row=3,column=i+1,pady=5)
      Label(info,text=o1[i],font=("Arial",15),fg='#C5C3C3').grid(row=4,column=i+1,pady=5)
      Label(info,text=r1[i],font=("Arial",15),fg='#C5C3C3').grid(row=5,column=i+1,pady=5)
      Label(info,text=b1[i],font=("Arial",15),fg='#C5C3C3').grid(row=6,column=i+1,pady=5)
    except:
      continue
           
def laptop():
  global det
  global soup1
  
  prod1,prod2=(product1.get()).replace(" ",""),(product2.get()).replace(" ","")
  products=[prod1,prod2]
  n1=[]
  d1=[]
  r1=[]
  p1=[]
  o1=[]
  b1=[]
  c1=[]
  ra=[]

  ##Declaring the url
  for product in products:
      a='https://www.flipkart.com/laptops/pr?sid=6bo,b5g&q='
      c='&otracker=categorytree'
      b=product
      url=a+b+c
      page=requests.get(url)

  ##Scraping website
      soup = BeautifulSoup(page.content,'html.parser')
      price = soup.select('div._30jeq3')
      name = soup.select('div._4rR01T')
      rating = soup.select('div._3LWZlK')
      try:
        p1.append(price[0].get_text())
        n1.append(name[0].get_text())
        ra.append(rating[0].get_text())

        detail=soup.find_all('a',class_='_1fQZEK')
        d=detail[0].get('href')
        url1=a+d
        page1=requests.get(url1)
        soup1=BeautifulSoup(page1.content,'html.parser')

      ##Finding the details
        det=soup1.find_all('td',class_='_1hKmbr col col-3-12')

        detail12('Screen Size',d1)
        detail12('Operating System',o1)
        detail12('Weight',r1)
        detail12('Clock Speed',b1)
        detail12('Touchscreen',c1)
      except:
        error(product)
        continue
      ##Opening the link to extract details
      
  if(n1!=[]):      
    info=Tk()
    info.geometry("+400+300")
    info.title('Comparison')

    Label(info,text='PRICE : ',font=("Arial",15)).grid(row=1,column=0,pady=5)
    Label(info,text='RATING : ',font=("Arial",15)).grid(row=2,column=0,pady=5)
    Label(info,text='Screen Size : ',font=("Arial",15)).grid(row=3,column=0,pady=5)
    Label(info,text='Operating System : ',font=("Arial",15)).grid(row=4,column=0,pady=5)
    Label(info,text='Weight : ',font=("Arial",15)).grid(row=5,column=0,pady=5)
    Label(info,text='Clock Speed : ',font=("Arial",15)).grid(row=6,column=0,pady=5)
    Label(info,text='Touchscreen : ',font=("Arial",15)).grid(row=7,column=0,pady=5)
    
    for i in range(2):
      try:
        Label(info,text=n1[i],font=("Courier"),wraplength=300).grid(row=0,column=i+1,pady=5,padx=5)
        Label(info,text=p1[i],font=("Arial",15),fg='#C5C3C3').grid(row=1,column=i+1,pady=5)
        Label(info,text=ra[i],font=("Arial",15),fg='#C5C3C3').grid(row=2,column=i+1,pady=5)
        Label(info,text=d1[i],font=("Arial",15),fg='#C5C3C3').grid(row=3,column=i+1,pady=5)
        Label(info,text=o1[i],font=("Arial",15),fg='#C5C3C3').grid(row=4,column=i+1,pady=5)
        Label(info,text=r1[i],font=("Arial",15),fg='#C5C3C3').grid(row=5,column=i+1,pady=5)
        Label(info,text=b1[i],font=("Arial",15),fg='#C5C3C3').grid(row=6,column=i+1,pady=5)
        Label(info,text=c1[i],font=("Arial",15),fg='#C5C3C3').grid(row=7,column=i+1,pady=5)
      except:
        continue      
      
def headphone():
  global det
  global soup1
  ##Creating empty lists
  prod1,prod2=(product1.get()).replace(" ",""),(product2.get()).replace(" ","")
  products=[prod1,prod2]
  n1=[]
  d1=[]
  r1=[]
  p1=[]
  o1=[]
  b1=[]
  c1=[]
  ra=[]

  ##Declaring the url
  for product in products:
      a='https://www.flipkart.com/audio-video/headphones/pr?sid=0pm,fcn&q='
      c='&otracker=categorytree'
      b=product
      url=a+b+c
      page=requests.get(url)

  ##Scraping website
      soup = BeautifulSoup(page.content,'html.parser')
      price = soup.select('div._30jeq3')
      name = soup.select('a.s1Q9rs')
      rating = soup.select('div._3LWZlK')
      try:
        p1.append(price[0].get_text())
        n1.append(name[0].get_text())
        ra.append(rating[0].get_text())
       
       
    ##Opening the link to extract details
        detail=soup.find_all('a',class_='_2rpwqI')
        d=detail[0].get('href')
        url1=a+d
        page1=requests.get(url1)
        soup1=BeautifulSoup(page1.content,'html.parser')

    ##Finding the details
        det=soup1.find_all('td',class_='_1hKmbr col col-3-12')
        
        detail12('Color',d1)
        detail12('Headphone Type',o1)
        detail12('Water Resistant',r1)
        detail12('With Microphone',b1)
        detail12('Headphone Design',c1)
      except:
        error(product)
        continue
  if(n1!=[]):
    info=Tk()
    info.geometry("+400+300")
    info.title('Comparison')

    Label(info,text='PRICE : ',font=("Arial",15)).grid(row=1,column=0,pady=5)
    Label(info,text='RATING : ',font=("Arial",15)).grid(row=2,column=0,pady=5)
    Label(info,text='Color : ',font=("Arial",15)).grid(row=3,column=0,pady=5)
    Label(info,text='Headphone Type : ',font=("Arial",15)).grid(row=4,column=0,pady=5)
    Label(info,text='Water Resistant : ',font=("Arial",15)).grid(row=5,column=0,pady=5)
    Label(info,text='With Microphone : ',font=("Arial",15)).grid(row=6,column=0,pady=5)
    Label(info,text='Headphone Design : ',font=("Arial",15)).grid(row=7,column=0,pady=5)
  
  for i in range(2):
    try:
      Label(info,text=n1[i],font=("Courier"),wraplength=300).grid(row=0,column=i+1,pady=5,padx=5)
      Label(info,text=p1[i],font=("Arial",15),fg='#C5C3C3').grid(row=1,column=i+1,pady=5)
      Label(info,text=ra[i],font=("Arial",15),fg='#C5C3C3').grid(row=2,column=i+1,pady=5)
      Label(info,text=d1[i],font=("Arial",15),fg='#C5C3C3').grid(row=3,column=i+1,pady=5)
      Label(info,text=o1[i],font=("Arial",15),fg='#C5C3C3').grid(row=4,column=i+1,pady=5)
      Label(info,text=r1[i],font=("Arial",15),fg='#C5C3C3').grid(row=5,column=i+1,pady=5)
      Label(info,text=b1[i],font=("Arial",15),fg='#C5C3C3').grid(row=6,column=i+1,pady=5)
      Label(info,text=c1[i],font=("Arial",15),fg='#C5C3C3').grid(row=7,column=i+1,pady=5)
    except:
      continue
 
def mobile():
  global det
  global soup1
##Creating empty lists
  prod1,prod2=(product1.get()).replace(" ",""),(product2.get()).replace(" ","")
  products=[prod1,prod2]  
  n1=[]
  d1=[]
  r1=[]
  p1=[]
  o1=[]
  b1=[]
  c1=[]
  ra=[]

  ##Declaring the url
  for product in products:
      a='https://www.flipkart.com/mobiles/pr?sid=tyy,4io&q='
      c='&otracker=categorytree'
      b=product
      url=a+b+c
      page=requests.get(url)

  ##Scraping website
      soup = BeautifulSoup(page.content,'html.parser')
      price = soup.select('div._30jeq3')
      name = soup.select('div._4rR01T')
      rating = soup.select('div._3LWZlK')
      try:
        p1.append(price[0].get_text())
        n1.append(name[0].get_text())
        ra.append(rating[0].get_text())
       
            
    ##Opening the link to extract details
        detail=soup.find_all('a',class_='_1fQZEK')
        d=detail[0].get('href')
        url1=a+d
        page1=requests.get(url1)
        soup1=BeautifulSoup(page1.content,'html.parser')
      
    ##Finding the details
        det=soup1.find_all('td',class_='_1hKmbr col col-3-12')

        detail12('Display Size',d1)
        detail12('Operating System',o1)
        detail12('RAM',r1)
        detail12('Battery Capacity',b1)
        detail12('Primary Camera',c1)
      except:
        error(product)
        continue
  if(n1!=[]):                   
    info=Tk()
    info.geometry("+400+300")
    info.title('Comparison')

    Label(info,text='PRICE : ',font=("Arial",15)).grid(row=1,column=0,pady=5)
    Label(info,text='RATING : ',font=("Arial",15)).grid(row=2,column=0,pady=5)
    Label(info,text='DISPLAY SIZE : ',font=("Arial",15)).grid(row=3,column=0,pady=5)
    Label(info,text='OS : ',font=("Arial",15)).grid(row=4,column=0,pady=5)
    Label(info,text='RAM : ',font=("Arial",15)).grid(row=5,column=0,pady=5)
    Label(info,text='BATTERY : ',font=("Arial",15)).grid(row=6,column=0,pady=5)
    Label(info,text='CAMERA : ',font=("Arial",15)).grid(row=7,column=0,pady=5)
  
  for i in range(2):
    try:
      Label(info,text=n1[i],font=("Courier"),wraplength=300).grid(row=0,column=i+1,pady=5,padx=5)
      Label(info,text=p1[i],font=("Arial",15),fg='#C5C3C3').grid(row=1,column=i+1,pady=5)
      Label(info,text=ra[i],font=("Arial",15),fg='#C5C3C3').grid(row=2,column=i+1,pady=5)
      Label(info,text=d1[i],font=("Arial",15),fg='#C5C3C3').grid(row=3,column=i+1,pady=5)
      Label(info,text=o1[i],font=("Arial",15),fg='#C5C3C3').grid(row=4,column=i+1,pady=5)
      Label(info,text=r1[i],font=("Arial",15),fg='#C5C3C3').grid(row=5,column=i+1,pady=5)
      Label(info,text=b1[i],font=("Arial",15),fg='#C5C3C3').grid(row=6,column=i+1,pady=5)
      Label(info,text=c1[i],font=("Arial",15),fg='#C5C3C3').grid(row=7,column=i+1,pady=5)
    except:
      continue
    
root = Tk()
root.geometry("+400+300")
root.title("CS PROJECT")

l1=Label(root,text='COMPARE SYSTEM',pady=10,padx=10,font=("Courier",50))
l1.grid(row=0,column=0,columnspan=5)

product1=Entry(root,width=35,borderwidth=5)
product1.grid(row=2,column=1)
Label(root,text='Enter The 1st Product name : ',font=("Arial",15)).grid(row=2,column=0,pady=5)

product2=Entry(root,width=35,borderwidth=5)
product2.grid(row=3,column=1)
Label(root,text='Enter The 2nd Product name : ',font=("Arial",15)).grid(row=3,column=0,pady=5)

Label(root,text='Choose Category : ',font=("Arial",15)).grid(row=1,column=0,pady=5)
category=ttk.Combobox(root,width=33)
category['values']=('Mobiles','Laptops','HeadPhones','TeleVision')
category.insert(0,'Mobiles')
category.grid(row=1,column=1)
category.current(0)

Button(text='SUBMIT',width=47,pady=20,border=2,font=("Arial",15),command=lambda: check(category.get())).grid(row=5,column=0,columnspan=2)

root.mainloop()




  
