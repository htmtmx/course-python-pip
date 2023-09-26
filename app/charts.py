import matplotlib.pyplot as plt

def generate_bar_char(country, labels, values):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  plt.savefig(f'./imgs/{country}_bar_update.png')

def generate_pie_chart(country, labels, values):
  fig, ax = plt.subplots()
  ax.pie(values, labels = labels)
  ax.axis('equal')
  plt.savefig(f'./imgs/{country}_pie_update.png')

if __name__ == '__main__':
  labels = ['a', 'b', 'c']
  values = [1000, 200, 800]
  generate_bar_char(labels, values)
  generate_pie_chart(labels, values)