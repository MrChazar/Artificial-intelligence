import random


def perceptron(s, epoch, type, w=[]):
    # zbiór uczący dla lub
    # wagi
    if w == []:
        w = [random.uniform(-1, 1) for _ in range(len(s[0][0]) + 1)]

    N = len(s)
    n = 0

    # błąd nauczania
    iter = 1

    def activation(value, w_0):
        return 1 if value > w_0 else type

    # uczenie
    for i in range(epoch):

        # y(n)
        s_n = w[0] + sum(w[i + 1] * s[n][0][i] for i in range(len(s[n][0])))

        y_n = activation(s_n, w[0])  # w_0 _ w_1*x_1 + w_2*x_2

        # błąd
        e_n = s[n][1] - y_n  # d_n - y_n

        # waga
        w[0] = w[0] + e_n
        for i in range(1, len(s[0][0]) + 1):
            w[i] = w[i] + e_n * s[n][0][i-1]

        print(f"Iteracja {iter}")
        print(f"Badany xn {s[n]}")
        print(f"Wartość s(n) {s_n}")
        print(f"y_n {y_n}")
        print(f"błąd {e_n}")

        print(f"waga 0 {w[0]}")
        for i in range(1, len(s[0][0]) +1):
            print(f"Waga {i} {w[i]}")

        print("\n\n")
        n += 1
        iter += 1
        if (n >= N):
            n = 0
    return s,w


def show_chart_two_inputs(s,w,title,type):
    import matplotlib.pyplot as plt
    import numpy as np

    x1 = [item[0][0] for item in s]
    x2 = [item[0][1] for item in s]
    labels = [item[1] for item in s]

    plt.figure(figsize=(6, 6))
    for i in range(len(s)):
        if labels[i] == 1:
            plt.scatter(x1[i], x2[i], color='blue', label='1', s=100, marker='o')
        else:
            plt.scatter(x1[i], x2[i], color='red', label='0', s=100, marker='.')

    x = np.linspace(0, 1, 100)
    y = (w[0] + w[1] * x) / -w[2]
    plt.plot(x, y, color='green', label='Linia: w0 + w1*x1 + w2*x2 = 0')

    plt.xlabel("x1")
    plt.ylabel("x2")
    plt.title(f"wykres nauczonej sieci dla operacji {title} perceptron {type}")

    handles, labels = plt.gca().get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    plt.legend(by_label.values(), by_label.keys())

    plt.grid()
    plt.show()