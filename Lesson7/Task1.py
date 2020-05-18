# Реализовать класс Matrix (матрица).  Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
#
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.
#
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31 22 --- 3 5 32 --- 3 5 8 3
# 37 43 --- 2 4 6 --- 8 3 7 1
# 51 86 --- -1 64 -8
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
#
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц).  Результатом сложения
# должна быть новая матрица.
#
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.
#
class Matrix:
    def __init__(self, value):
        self._value = value

    @property
    def elements(self):
        return self._value

    def __add__(self, other):
        result = []
        for y, row in enumerate(self.elements):
            result_row = []
            for x, item in enumerate(row):
                resul_item = item + other.elements[y][x]
                result_row.append(resul_item)
            result.append(result_row)
        return Matrix(result)

    def __str__(self):        
        result = ""
        for row in self._value:
            row_string = " ".join(map(lambda x: f"{x:3}", row))
            result += f"{row_string}\n"
        return result

matrix_1 = Matrix([[11, 3, 15], [16, 25, 79], [32, 39, 68]])
print(matrix_1)
print()

matrix_2 = Matrix([[4, 2, 1], [3, 7, 2], [5, 0, 2]])
print(matrix_2)
print()

matrix_sum = matrix_1 + matrix_2
print(matrix_sum)