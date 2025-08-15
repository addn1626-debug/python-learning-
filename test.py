print("hello world ")
#alwyas put print in () and for a indepedent one use ""
a = 5 
b =3
# anything with "=" will be use to assing a variable 
print(a+b)
print(a/b)
print(a-b)
print (type(a))
#this will be used to know type of data 
c=[2,5,3]
# anything in a [] is a list a collec tion of data 
for i in c :
    print(i+1,i-1,i*2)
    print ("i am good:", i+3)
# this is called a for loop used to do function on list where i is a single thing or data point in your  list 
if a > 6 :
 print(a+B)
else : print("nothing")
#this is called a if else statement used to do condition so if a happen do b or else c 
for i in c :
   if i > 6 :
      print("good boy")
   else: print("doom")
   #this is how you use for and if-else loop togsather 
import yfinance as yf
import pandas as pd
import pandas_datareader as pdr
import datetime as dt 
#this is how to install librarises in pythion but remember before importing you need to do "pip install" on terminal 
end_date= dt.datetime.now()
print( "todays date:" ,end_date)
#this is how to do todays date 
start_date= end_date - dt.timedelta(days= 365*3)
CRYPTO= ["SOL-USD" ]
df= yf.download(CRYPTO , start=start_date , end= end_date)
print(df.head())
Volume=df['Volume']
print(Volume)
#yahoo finance and date time library are most important for scrapping price data 
