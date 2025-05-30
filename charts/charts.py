import matplotlib.pyplot as pylot

def generate_pie_chart():
    labels = ['A', 'B', 'C', 'D']
    sizes = [15, 30, 45, 10]

    fig, ax = pylot.subplots()
    ax.pie(sizes, labels=labels)
    pylot.savefig('pie.png')
    pylot.close()