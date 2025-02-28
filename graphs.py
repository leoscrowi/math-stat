import matplotlib.pyplot as plt


def histogram(series):
    keys = sorted(list(series.keys()))
    values = list()
    for key in keys:
        values.append(series[key])

    plt.bar(keys, values, color='blue', edgecolor='black', align='center')
    plt.xlabel('Величина')
    plt.ylabel('Частота')
    plt.title('Гистограмма')
    plt.xticks(keys, rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def polygon(series):
    keys = sorted(list(series.keys()))
    values = list()
    for key in keys:
        values.append(series[key])

    plt.plot(keys, values, marker='o', linestyle='-', color='blue')
    plt.xlabel('Величина')
    plt.ylabel('Частота')
    plt.title('Полигон')
    plt.xticks(keys, rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def function_distribution(series):
    keys = sorted(list(series.keys()))
    n = sum(series.values())
    freq = []
    s = 0
    for key in keys:
        s += series[key]
        freq.append(s / n)

    plt.step(keys, freq, where='post', color='blue')
    plt.xticks(keys, rotation=45)
    plt.xlabel('Величина')
    plt.ylabel('F*(x)')
    plt.title('Выборочная функция распределения')
    plt.grid(True)
    plt.show()
