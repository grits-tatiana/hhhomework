from decorators import cache_decorator

def is_operation(str):
	operatorsSet = {'+', '-', '/', '*', '**'}
	if operation in operatorsSet:
		return True
	else:
		return False

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
	#print('In Calculator')
	if operation == '+':
		return a + b
	elif operation == '-':
		return a - b
	elif operation == '/':
		return a / b
	elif operation == '*':
		return a * b
	else:
		return a ** b

if __name__ == '__main__':

	flagA = False
	flagB = False

	while (flagA == False):
		try:
			a = int(input('Введите первое число: ')) # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
			flagA = True;
		except ValueError:
			print('Введите корректное первое число')

	while (flagB == False):
		try:
			b = int(input('Введите второе число: '))
			flagB = True;
		except ValueError:
			print('Введите корректное второе число: ')

    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
	operation = input('Введите операцию: ')

	if is_operation(operation):
		print('Результат: ', calculator(a, b, operation))
	else:
		print('Введите корректный оператор')

