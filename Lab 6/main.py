import random
import matplotlib.pyplot as plt
import numpy as np


def perceptron(s, epoch, type, w=[]): # type 0/-1  unipolar/bipolar
    # zbiór uczący dla lub
    # wagi
    if w == []:
        w = [random.uniform(-1, 1) for _ in range(len(s[0][0]) + 1)]

    N = len(s)
    n = 0
    iter = 1

    def activation(value):
        return 1 if value >= 0 else type

    # uczenie
    for i in range(epoch):
        # y(n)
        suma_cząstkowa = w[0] + sum(w[i + 1] * s[n][0][i] for i in range(len(s[n][0])))
        y_n = activation(suma_cząstkowa)  # w_0 _ w_1*x_1 + w_2*x_2

        # błąd
        e_n = s[n][1] - y_n  # d_n - y_n

        # waga
        w_stare = w[:]
        w[0] = w[0] + e_n
        for i in range(1, len(s[0][0]) + 1):
            w[i] = w[i] + e_n * s[n][0][i-1]

        #print(f"Iteracja {iter}")
        #print(f"Badany xn: {s[n]}")
        #print(f"Suma cząstkowa: {suma_cząstkowa}")
        #print(f"Wejście: {s[n][0]}, Oczekiwane: {s[n][1]}, Wyjście: {y_n}")
        #print(f"Błąd: {e_n}")

        #print(f"Waga 0: {w_stare[0]} -> {w[0]}")
        for i in range(1, len(s[0][0]) +1):
            print(f"Waga {i}: {w_stare[i]} -> {w[i]}")



        print("\n\n")
        n += 1
        iter += 1
        if n >= N:
            n = 0
    return s,w


def show_chart_two_inputs(s,w,title,type):

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

# Unipolarny jedno wejście
# s, w = perceptron([([0], 0), ([1], 1)], 40, 0, [])

# Unipolarny dwa wejcia
# s, w = perceptron([([0,0], 0), ([0,1], 1), ([1,0], 1), ([1,1], 1)], 40, 0, [])

# Bipolarny jedno wejście
# s, w = perceptron([([-1], -1), ([1], 1)], 40, -1, [])

# Bipolarny dwa wejścia
# s, w = perceptron([([-1,-1], -1), ([-1,1], 1), ([1,-1], 1), ([1,1], 1)], 40, -1, [])
# show_chart_two_inputs(s, w, 'dwa wejścia', 'bipolar')


#2
''' lub '''
# Unipolarny
#s, w = perceptron([([0,0], 0), ([0,1], 1), ([1,0], 1), ([1,1], 1)], 100, 0, [0.2, 0.3, 0.7])

# Bipolarny
# s, w = perceptron([([-1,-1], -1), ([-1,1], 1), ([1,-1], 1), ([1,1], 1)], 40, -1, [])

''' i '''
# Unipolarny
# s, w = perceptron([([0,0], 0), ([0,1], 0), ([1,0], 0), ([1,1], 1)], 40, 0, [])

# Bipolarny
# s, w = perceptron([([-1,-1], -1), ([-1,1], -1), ([1,-1], -1), ([1,1], 1)], 40, -1, [])

''' nie '''
# Unipolarny
# perceptron([([0], 1), ([1], 0)], 40, 0, [0.5, 0.2])

# Bipolarny
# perceptron([([-1], 1), ([1], -1)], 40, -1, [-0.9, 0.8])

''' albo '''
# niewykonalne dla jednego perceptronu
s = [ [[1,1],0], [[1,0],1], [[0, 1],1], [[0,0], 0] ]
s,w = perceptron(s, 100, 0)
show_chart_two_inputs(s,w,'albo', 'unipolarny')

#3


#4
'''XOR = OR - AND'''
# Funkcja pomocnicza dla gotowych wag
"""
def Y(x, w, type):
    s = w[0] + sum(w[i + 1] * x[i] for i in range(len(x)))

    def activation(value):
        return 1 if value >= 0 else type
    return activation(s)

# dla warstwy ukrytej
dataset_and = [([0, 0], 0), ([0, 1], 0), ([1, 0], 0), ([1, 1], 1)]  # AND
dataset_or = [([0, 0], 0), ([0, 1], 1), ([1, 0], 1), ([1, 1], 1)]   # OR
dataset_xor = [([0, 0], 0), ([0, 1], 1), ([1, 0], 1), ([1, 1], 0)]  # XOR

# warstwa ukryta
_a, wagi_and = perceptron(dataset_and, epoch=100, type=0, w=[])
_o, wagi_or = perceptron(dataset_or, epoch=100, type=0, w=[])

#wykres and
show_chart_two_inputs(_a,wagi_and,'and', '')

#wykres or
show_chart_two_inputs(_o,wagi_or,'and', '')

# wyjścia warstwy ukrytej jako nowe wejścia dla perceptronu ostatecznego
dataset_ukryte_wyjścia = []
for x, d in dataset_xor:
    wynik = [
        Y(x, wagi_and, 0),  # Wyjście perceptronu AND
        Y(x, wagi_or, 0)   # Wyjście perceptronu OR
    ]
    dataset_ukryte_wyjścia.append((wynik, d))

# Trening perceptronu wyjściowego
_x, wagi_końcowe = perceptron(dataset_ukryte_wyjścia, epoch=100, type=0, w=[])
show_chart_two_inputs(_x,wagi_końcowe,'xor', '')

'''wyniki'''
print("Testowanie XOR:")
for x, oczekiwany in dataset_xor:
    wynik = [
        Y(x, wagi_and, 0),  # Wyjście perceptronu AND
        Y(x, wagi_or, 0)   # Wyjście perceptronu OR
    ]
    wyjście_ostateczne = Y(wynik, wagi_końcowe, 0)
    print(f"Wejście: {x}, Oczekiwane: {oczekiwany}, Wynik: {wyjście_ostateczne}")
"""