#2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.

#inputAllSeconds = input("Введите число в секундах: ")
inputAllSeconds = "54853"
allSeconds = int(inputAllSeconds)

hours = allSeconds // 3600
minutes = (allSeconds - hours * 3600) // 60
seconds = allSeconds - hours * 3600 - minutes * 60

print(f"{hours:02}:{minutes:02}:{seconds:02}")