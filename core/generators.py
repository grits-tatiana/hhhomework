import random

N = 10;
# написать генераторную функцию, которая принимает число N возвращает N рандомных чисел от 1 до 100
def genF(N):
	for x in range(N):
		yield random.randint(1,100)

# написать генераторное выражение, которое делает то же самое
genE = (random.randint(1,100) for x in range(N))

print("Генераторная функция: ")
for i in genF(N):
	print(i)

print("Генераторное выражение: ")
for i in genE:
	print(i)