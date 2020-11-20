import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.style.use("ggplot")
plt.figure("Person Kilos Figure")

Person_Kilos = pd.read_csv("PersonKilos.csv")

plt.xlabel("Kilos")
plt.ylabel("Person Count")
plt.title("Person Kilos Graphic")

plt.hist(Person_Kilos.PersonKilos , bins = 250 , edgecolor = "black" , color= "red")
plt.show()
