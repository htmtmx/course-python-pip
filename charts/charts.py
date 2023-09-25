import matplotlib.pyplot as plt

def generate_pie_chart():
    labels = ['Python', 'C++', 'Ruby', 'Java']
    values = [215, 130, 245, 210]
    
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.set_title('Programming language usage')
    plt.savefig('./pie_chart.png')
    