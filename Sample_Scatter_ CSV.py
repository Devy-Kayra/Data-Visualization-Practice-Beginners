import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("seaborn-dark")

data = pd.read_csv("PlayTimes.csv")

plt.xlabel("Age")
plt.ylabel("Play Times (Hour)") 

plt.title("Play Times")

plt.scatter(data.Age , data.Times , color = "red" , s = 50) 

plt.legend()
plt.show()
