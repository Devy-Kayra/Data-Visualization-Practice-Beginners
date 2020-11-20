import matplotlib.pyplot as plt

Year = [2000 , 2001 , 2002 , 2003 , 2004 , 2005 , 2006 , 2007 , 2008 , 2009 , 2010 , 2011 , 2012 , 2013 , 2014 , 2015 , 2016 , 2017 , 2018 , 2019 , 2020]
salesCount = [30000 , 12000 , 13000 , 30200 , 16700 , 14350 , 35420 , 7000 , 13435 , 25364 , 24747 , 1232 , 2463 , 8907 , 1235 , 1768 , 9742 , 1853 , 8935 , 23453 , 23445]

plt.style.use("dark_background") # Black Backgorund Style

plt.xlabel("Year")
plt.ylabel("Sales Count")

plt.title("Sales Graphic")

plt.bar(Year , salesCount , color = "Purple" , label = "X Company") 

plt.legend()
plt.show()
