# Создать список, состоязщий из кубов нечётных чисел от 1 до 1000 (куб Х - третья степень числа Х)


def sum_coube(calc_list):
    hub = 0
    for item in calc_list:
        number = 0

        item = str(item)
        for i in item:
            number = int(i) + number
        if (number % 7) == 0:
            item = int(item)
            hub += item
    return hub


storage = []
storage17 = []

for i in range(1, 1001, 2):
    i **= 3
    storage.append(i)
    i += 17
    storage17.append(i)

print(sum_coube(storage))
print(sum_coube(storage17))
