import seaborn as sb
from matplotlib import pyplot as plt


def g1():
    df = sb.load_dataset('iris')
    sb.distplot(df['petal_length'])
    plt.show()


def g2():
    fig, ax = plt.subplots()
    plt.xlabel('x')
    plt.ylabel('y')
    x = [i for i in range(100)]
    y = [2*i for i in range(100)]
    ax.plot(x, y)
    axin = ax.inset_axes([0.6, 0.5, 0.2, 0.2])
    axin.plot(x, y)
    plt.show()


def g3():
    fig, ax = plt.subplots()
    plt.axis('off')
    plt.xlabel('x')
    plt.ylabel('y')
    x1 = [i for i in range(100)]
    y1 = [2*i for i in range(100)]
    p1 = ax.inset_axes([0.0, 0.0, 1.0, 0.5])
    p1.plot(x1, y1, color='blue', linewidth=5)
    x2 = [i for i in range(100)]
    y2 = [i * i for i in range(100)]
    p2 = ax.inset_axes([0.0, 0.5, 1.0, 0.5])
    p2.plot(x2, y2, color='red', linewidth=5, linestyle='dashed')
    plt.show()


g1()
g2()
g3()

