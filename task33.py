# Задана натуральная степень k. 
# Cформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. 
# *Пример: k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint

a = 2
m=[]
polynomial = ''

for i in range (0, a + 1):
    m.append(randint(1, 101))

print(m)
file = open('Poly.txt', 'w')

for i in range (a, -1, -1):
    if i > 1:
        polynomial += str(m[-(i + 1)]) + ' * x ^ ' + str(i) + ' + '
    elif i == 1:
        polynomial += str(m[-(i + 1)]) + ' * x + '
    elif i == 0:
        polynomial += str(m[-(i + 1)]) + ' = 0'

print(polynomial)

file.write(polynomial)
file.close