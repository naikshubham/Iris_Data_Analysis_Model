import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#Load iris.csv into a pandas dataframe 
iris = pd.read_csv("iris.csv")


#Using 2-D Scatter plot I can't make sense out of data so I tried to use 3-D plot,but it also did'nt turn to give nice result for visualization,
#and humans cant visualize 4-D plots ,so I decided to use Pair Plot
#Pairwise scatter plot :Pair Plot  

sns.set_style("whitegrid")
sns.pairplot(iris,hue='species',size=3)
plt.show()

#Predicting the flower based on visualization of Pair Plots

petal_length = float(input("Enter the petal length:"))
petal_width  = float(input("Enter the petal width :"))

if petal_length <= 2.2 and petal_width <= 1.0 : 
	print("The given properties are of Setosa flower")
elif (petal_length >= 2.5 and petal_length <= 5.2) and (petal_width >= 0.8 and petal_width <= 1.8):
	print("The given properties are of Versicolor flower")
elif (petal_length >= 5.3 and petal_length <= 7.0) and (petal_width >= 1.8 and petal_width <= 2.5):
	print("The given properties are of Virginica flower")
else:
	print("Properties dont match any of the flowers")
	
