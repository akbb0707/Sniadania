import random
print("Hello World")
lista = ['Chleb', 'Cebula', 'Pomidor', 'Szynka', 'Ser', 'Papryka', 'Stół', 'Twarożek', 'Żotkiewka', 'Jajka', 'Herbata',]

#People's names to assign tasks to
tata = []
bartek = []
piotrek = []
aga =[]

random.shuffle(lista)

while len(lista) != 0:
    try:
        tata.append(lista.pop())
        bartek.append(lista.pop())
        piotrek.append(lista.pop())
        aga.append(lista.pop())
    except IndexError:
        break

print(f"Tata = {tata}")
print(f"Bartek = {bartek}")
print(f"Piotrek = {piotrek}")
print(f"Aga = {aga}")