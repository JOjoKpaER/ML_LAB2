import matplotlib.pyplot as plt


def g1():
    x = [10, 20, 30, 40,  50]
    y = [28, 56, 84, 112, 140]
    plt.title('Draw a line')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.plot(x, y, color='blue')
    plt.show()


def g2():
    x = [10, 20, 30]
    y1 = [20, 40, 10]
    y2 = [40, 10, 30]
    plt.title('Two or more lines with different widths and colors with suitable legends')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.plot(x, y1, color='blue', linewidth=3, label='line1-width-3')
    plt.plot(x, y2, color='red', linewidth=5, label='line2-width-5')
    plt.legend()
    plt.show()


def g3():
    x = [10, 20, 30]
    y1 = [20, 40, 10]
    y2 = [40, 10, 30]
    plt.title('Plot with two or more lines with different styles')
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.plot(x, y1, color='blue', linewidth=3, label='line1-dotted', linestyle='dotted')
    plt.plot(x, y2, color='red', linewidth=5, label='line2-dashed', linestyle='dashed')
    plt.legend()
    plt.show()


def g4():
    x = [1, 4, 5, 6, 7]
    y = [2, 6, 3, 6, 3]
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.title('Display marker')
    plt.plot(x, y, color='red', linestyle='dashdot', linewidth=3, marker='o', markerfacecolor='blue', markersize=12)
    plt.ylim(1, 8)
    plt.xlim(1, 8)
    plt.show()


def g5():
    x1 = [2, 3, 5, 6, 8]
    y1 = [1, 5, 10, 18, 20]
    x2 = [3, 4, 6, 7, 9]
    y2 = [2, 6, 11, 20, 22]
    plt.plot(x1, y1, 'bo')
    plt.plot(x2, y2, 'ro')
    plt.show()


def g6():
    x = ['2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07']
    y = [772.5, 776.45, 776.5, 776.85, 775.1]
    plt.title('Closing stock value of Alphabet Inc.')
    plt.xlabel('Date')
    plt.ylabel('Closing value')
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.minorticks_on()
    plt.plot(x, y, 'r-o')
    plt.show()


g1()
g2()
g3()
g4()
g5()
g6()


