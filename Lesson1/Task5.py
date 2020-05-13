#5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, 
#или убыток — издержки больше выручки). Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке). 
#Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

#inputRevenue = input("Введите значение выручки фирмы: ")
inputRevenue = "125"
revenue = float(inputRevenue)

#inputCosts = input("Введите значение издержек фирмы: ")
inputCosts = "15"
costs = float(inputCosts)

print()

isProfit = revenue > costs
if(isProfit):
    print("Фирма отработала с прибылью")
    
    profit = revenue - costs

    profitMargin = profit / revenue
    print(f"Рентабельность выручки (соотношение прибыли к выручке): {profitMargin}")

    #unitCountInput = input("Введите численность сотрудников фирмы: ")
    unitCountInput = "5"
    unitCount = int(unitCountInput)

    profitPerUnit = profit / unitCount
    print(f"Прибыль фирмы в расчете на одного сотрудника: {profitPerUnit}")

isLesion = costs > revenue
if(isLesion):
    print("Фирма отработала в убыток")