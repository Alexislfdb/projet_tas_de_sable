import tkinter
import random

configuration_matrice = []


def configuration(n):
    ligne_configuration = []
    for i in range(n):
        for j in range(n):
            ligne_configuration.append(random.randint(0,9))
        configuration_matrice.append(ligne_configuration)
        ligne_configuration = []
    print(configuration_matrice)

configuration(3)



