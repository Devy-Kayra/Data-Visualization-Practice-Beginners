import matplotlib.pyplot as plt
import pandas as pd

plt.style.use("dark_background")

Cities = pd.read_csv("Cities.csv")

plt.xlabel("Cities")
plt.ylabel("Population (Million)")

plt.title("Cities Populations")

plt.bar(Cities.Cities , Cities.Population , color = "blue" , edgecolor= "white") 

plt.legend()
plt.show()
