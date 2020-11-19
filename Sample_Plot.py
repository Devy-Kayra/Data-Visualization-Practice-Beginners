import matplotlib.pyplot as plt

days = ["Monday" , "Tuesday" , "Wednesday" , "Thursday" , "Friday"]
salesCount = [100 , 25 , 56 , 12 , 82]
salesCount2 = [150 , 120 , 75 , 0 , 10]

plt.style.use("ggplot")

plt.xlabel("Days")
plt.ylabel("Sales Count")

plt.title("Sales Graphic")

plt.plot(days , salesCount , color = "black" , marker = "." , markersize= 10 , label = "X Company") 
plt.plot(days , salesCount2 , color = "red" , marker = "." , markersize = 10 , label = "Y Company")

plt.legend()
plt.show()
