import csv, matplotlib.pyplot as plt
import pandas as pd

def plot_csv(country):
  df = pd.read_csv("./data.csv")
  data = df[df["Country"]==country].iloc[:,5:13]
  plt.bar(data.columns, data.values[0])
  plt.rcParams["figure.figsize"] = (5,4)
  plt.xticks(rotation=45) 
  plt.show()
      

if __name__ == '__main__':
  plot_csv("Mexico")