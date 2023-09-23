import matplotlib.pyplot as plt
import numpy as np

def c1():
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, popularity, color='blue')
    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
    plt.xticks(x_pos, x)

    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')

    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()


def c2():
    x = ['Java', 'Python', 'PHP', 'JS', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    x_pos = [i for i, _ in enumerate(x)]
    plt.barh(x_pos, popularity, color='green')
    plt.xlabel("Popularity")
    plt.ylabel("Languages")
    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
    plt.yticks(x_pos, x)

    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')

    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()


def c3():
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    x_pos = [i for i, _ in enumerate(x)]
    plt.bar(x_pos, popularity, color=['red', 'black', 'green', 'blue', 'yellow', 'cyan'])
    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
    plt.xticks(x_pos, x)
    # Turn on the grid
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    # Customize the minor grid
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()


def c4():
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    x_pos = [i for i, _ in enumerate(x)]
    fig, ax = plt.subplots()
    rects1 = ax.bar(x_pos, popularity, color='b')
    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
    plt.xticks(x_pos, x)
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')

    def autolabel(rects):
        """
        Attach a text label above each bar displaying its height
        """
        for rect in rects:
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2., 1.05 * height,
                    '%f' % float(height),
                    ha='center', va='bottom')

    autolabel(rects1)
    plt.show()


def c5():
    x = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
    popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    x_pos = [i for i, _ in enumerate(x)]
    plt.xlabel("Languages")
    plt.ylabel("Popularity")
    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago")
    plt.xticks(x_pos, x)
    width = [0.1, 0.2, 0.5, 1.1, 0.2, 0.3]
    y_pos = [0, .8, 1.5, 3, 5, 6]
    plt.bar(y_pos, popularity, width=width)
    plt.xticks(y_pos, x)
    plt.minorticks_on()
    plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
    plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
    plt.show()


def c6():
    n_groups = 5
    men_means = (22, 30, 33, 30, 26)
    women_means = (25, 32, 30, 35, 29)
    fig, ax = plt.subplots()
    index = np.arange(n_groups)
    bar_width = 0.35
    opacity = 0.8
    rects1 = plt.bar(index, men_means, bar_width,
                     alpha=opacity,
                     color='g',
                     label='Men')
    rects2 = plt.bar(index + bar_width, women_means, bar_width,
                     alpha=opacity,
                     color='r',
                     label='Women')
    plt.xlabel('Person')
    plt.ylabel('Scores')
    plt.title('Scores by person')
    plt.xticks(index + bar_width, ('G1', 'G2', 'G3', 'G4', 'G5'))
    plt.legend()
    plt.tight_layout()
    plt.show()


def p1():
    languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
    popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
    explode = (0.1, 0, 0, 0, 0, 0)
    plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()


def p2():
    languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
    popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
    colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
    explode = (0.1, 0, 0, 0, 0, .1)
    plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2017 compared to a year ago",
              bbox={'facecolor': '0.8', 'pad': 5})
    plt.show()


c1()
c2()
c3()
c4()
c5()
c6()
p1()
p2()
