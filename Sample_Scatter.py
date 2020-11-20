import matplotlib.pyplot as plt

Month = ["January" , "February" , "March" , "April" , "May" , "June" , "July" , "Agust"]
salesCount = [3000 , 1200 , 1300 , 3020 , 1670 , 1435 , 3542 , 700]
salesCount2 = [1500 , 1350 , 750 , 4050 , 3129 , 1265 , 3246 , 4024]

plt.style.use("dark_background") # Black Backgorund Style

plt.xlabel("Month")
plt.ylabel("Sales Count")

plt.title("Sales Graphic")

plt.scatter(Month , salesCount , color = "white" , marker = "x" , s = 50 , label = "X Company") 
plt.scatter(Month , salesCount2 , color = "red" , marker = "x" , s = 50 , label = "Y Company")

plt.legend()
plt.show()
