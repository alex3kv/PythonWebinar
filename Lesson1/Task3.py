#3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

#inputNumber = input("Введите число n: ")
inputNumber = "10"

n = int(inputNumber)
nn = int(f"{inputNumber}{inputNumber}")
nnn = int(f"{inputNumber}{inputNumber}{inputNumber}")

summ = n + nn + nnn
print(f"{n} + {nn} + {nnn} = {summ}")