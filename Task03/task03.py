# 3. Задан список чисел. Необходимо создать список, содержащий те его элементы, значения которых больше предыдущего.
# Техническое задание
#     Можно использовать comprehensions.
#     Формально первый элемент сравнить не с чем. Решите сами, что с ним делать: включать в новый список или нет. 
#     Можете сравнить его с последним элементом.
# Примеры/Тесты:
# src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [12, 44, 4, 10, 78, 123]

## Этот подглядела. Но поняла, как работает :)
# input_data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# result = [j for i, j in zip(input_data, input_data[1:]) if j > i]
# print(result)

input_data = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = []
if input_data[0] > input_data[-1]:
    result.append(input_data[0])
else: None

for i in range(len(input_data)-1):
    if input_data[i] < input_data[i+1]:
        result.append(input_data[i+1])

print(result)

