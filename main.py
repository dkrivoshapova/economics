# Функция полезности потребителя имеет вид U=A*X**q*Y**p(0<q,p<=1). Доход потребителя равен I.
# Изначальные цены товаров Х,У заданы и равны соостветственно Рх,Ру. Известно также менение цены товара X.
# Найти и вывести изначальный и конечный(после изменения цены) оптимальный набор потребителя.
# По значениям эффекта дохода и эффекта замены определить вид товара Х.
a = int(input('Введите значение коэффициента А '))
q = float(input('Введите показатель степени Х '))
p = float(input('Введите показатель степени Y '))
i = int(input('Введите доход потребителя '))
px = int(input('Введите цену товара Х '))
py = int(input('Введите цену товара Y '))
px2 = int(input('Введите цену товара Х после изменения цены '))

if q < 0 or p < 0 or q > 1 or p > 1:
    print('Программа не может решить такую задачу')
# определение изначального оптимального набора
x1 = i / (px * (1 + p / q))
y1 = i / (py * (1 + q / p))
print('Оптимальный набор потреителя до изменения цен', x1, y1)
# определение  оптимального набора после изменения цен
x3 = i / (px2 * (1 + p / q))
y3 = i / (py * (1 + q / p))
print('Оптимальный набор потреителя до изменения цен', x3, y3)
# определение промежуточного набора
i1 = x1 * px2 + y1 * py
x3 = i1 / (px2 * (1 + p / q))
y3 = i1 / (py * (1 + q / p))
print('Эффект замены ', x3-x1)
print('Эффект дохода ', x2-x3)
z=x3-x1
d=x2-x3
if px>px2:
    if z>0 and d> 0:
        print('Нормальный товар')
    elif z>0 and d<0:
        if abs(z)>abs(d):
            print('низший товар')
        else:
            print('товар Гиффена')
else:
    if z<0 and d< 0:
        print('Нормальный товар')
    elif z<0 and d>0:
        if abs(z)>abs(d):
            print('низший товар')
        else:
            print('товар Гиффена')
