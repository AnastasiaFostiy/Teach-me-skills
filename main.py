import os
from dotenv import load_dotenv

load_dotenv()

items = os.getenv('ITEMS')
sum = os.getenv('SUM')
order_num = os.getenv('ORDER_NUM')

print("Чек")
print("Количество пицц в заказе:", items)
print("Сумма заказа: %s дублонов" %(sum))
print("Номер в очереди:", order_num, "\n")

#1. Касса перепутала номер в очереди с суммой. Надо поменять эти переменные местами
#sum, order_num = order_num, sum
print("Исправленный чек")
print("Количество пицц в заказе:", items)
print("Сумма заказа: %s дублонов" %(sum))
print("Номер в очереди:", order_num)

#2. Для отчёта боссу, нужно посчитать среднюю стоимость каждой пиццы в заказе
sr_sum = sum / items
print("Средняя стоимость пицц в заказе:", sr_sum)

#3. Если в сумме заказа нету дробей (.00), нужно, чтобы нули не отрисовывались
if sum/int(sum) == 1:
    sum = int(sum)
print("Стоимость пиццы:", sum)

#4. Если у клиента в номере заказа есть цифра 2, ему положена скидка в 50%
order_num_str = str(order_num)
if order_num_str[0] == '2' or order_num_str[1] == '2' or order_num_str[2] == '2':
    sum = sum * 0.5
    print("Цена со скидкой 50%:", sum)

#5. Если кол-во пицц в заказе меньше 2, от номер в очереди нужно сократить на 5
if items == 1:
    order_num = order_num - 5
    print("Новый номер в очереди:", order_num)


