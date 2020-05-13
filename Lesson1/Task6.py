#6.  Спортсмен занимается ежедневными пробежками.  В первый день его результат
#составил a километров.  Каждый день спортсмен увеличивал результат на 10 %
#относительно предыдущего.  Требуется определить номер дня, на который общий
#результат спортсмена составить не менее b километров.  Программа должна
#принимать значения параметров a и b и выводить одно натуральное число — номер
#дня.
#
#Например: a = 2, b = 3.
#Результат:
#1-й день: 2
#2-й день: 2,2
#3-й день: 2,42
#4-й день: 2,66
#5-й день: 2,93
#6-й день: 3,22
#
#Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

#firstDayDistanceInput = input("Введите результат пробежки первого дня: ")
firstDayDistanceInput = "2";
firstDayDistance = float(firstDayDistanceInput)

#targetDistanceInput = input("Введите целевой результат пробежки в день: ")
targetDistanceInput = "3";
targetDistance = float(targetDistanceInput)

print()
print("Результат:")

todayDistance = firstDayDistance
day = 1

print(f"{day}-й день: {todayDistance:.2f}")

while(todayDistance < targetDistance):
    day+=1
    todayDistance = todayDistance * 1.1
    print(f"{day}-й день: {todayDistance:.2f}")

print()
print(f"Ответ: на {day}-й день спортсмен достиг результата — не менее {targetDistance} км.")