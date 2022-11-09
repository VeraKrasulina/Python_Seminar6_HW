# 2. Есть два списка: tutors - имена учеников, groups - названия их классов. Необходимо сформировать список кортежей вида (tutor, group).
# Техническое задание
#     Программа должна работать со списками tutors, groups любой длины.
#     Длина результирующего списка не должна быть больше длины списка tutors.
#     Если в списке groups меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например: ('Станислав', None)
#     Если в списке tutors меньше элементов, чем в списке groups, то смотри пункт 2.
#     Вы можете использовать в этом задании функции zip и zip_longest, но лучше обойтись без них
#     Не меняйте исходные списки tutors и groups и не создавайте промежуточных списков. Только список результат.
#     Подтвердите работоспособность(выведите в консоль результаты) для обоих вариантов: groups меньше tutors и tutors меньше groups.
#     Сделайте сначала задание через циклы обычным образом, затем оформите решение в "одну строку" в виде comprehensions
# Примеры/Тесты:
# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# groups = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
# Результат, где учеников меньше
# Ученики: ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# Классы: ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
# Список:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ('Петр', '9Б')
# ('Сергей', '9В')
# ('Дмитрий', '8Б')
# ('Борис', '10А')
# ('Елена', '10Б')
# Результат, где учеников больше
# Ученики: ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# Классы: ['9А', '7В', '9Б', '9В']
# Список:
# ('Иван', '9А')
# ('Анастасия', '7В')
# ('Петр', '9Б')
# ('Сергей', '9В')
# ('Дмитрий', None)
# ('Борис', None)
# ('Елена', None) 

# tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
# groups = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
groups = ['9А', '7В', '9Б', '9В']

result = [(tutors[i], groups[i]) if i < len(groups) else (tutors[i], None) for i in range(len(tutors))]

print(result)


