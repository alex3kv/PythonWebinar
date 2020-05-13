#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.

#inputNumber = input("Введите целое положительное число: ")
inputNumber = "545482"
number = int(inputNumber)

workNumber = number
maxValue = 0

while workNumber > 0:
    modulo = workNumber % 10
    if(modulo > maxValue):
        maxValue = modulo

    workNumber = workNumber // 10

print(f"Самой большой цифрой в числе {number} является {maxValue}")