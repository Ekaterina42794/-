example='АбВгДеЁжЗи'
a=len(example)//2 # половина символов в строке
print(a)
print(example[:]) # вывод всех
print(example[0])    # 2  вывод первого символа
print(example[-1:])  # 3 последн. символ с отриц индексом
print(example[len(example)//2::1])  # 4 вторая половина
print(example[::-1]) # 5 слово наоборот
print(example[1::2]) # каждый второй