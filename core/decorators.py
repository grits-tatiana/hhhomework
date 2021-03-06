def cache_decorator(calc):
    # Реализовать декоратор который кэширует результаты вызова функции (есть в лекции)
    # Применить для функции calculator (в calculator.py уже есть import функции cache_decorator)
    # Настоятельно прошу написать декоратор руками, а не копировать, т.к. важно запомнить как это работает
    #cache = {(4,5,'+'): 9}
    cache = {}
    def wrapper(*args):
    	if args not in cache:
    		cache[args] = calc(*args)
    	return cache[args]
    return wrapper
