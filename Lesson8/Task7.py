# Реализовать проект «Операции с комплексными числами».  Создайте класс
# «Комплексное число», реализуйте перегрузку методов сложения и умножения
# комплексных чисел.  Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.
class ComplexNumber:
    def __init__(self, real, imag):
       self._real = real
       self._imag = imag

    def __add__(self, other):
        return ComplexNumber(self._real + other._real, self._imag + other._imag)    

    def __mul__(self, other):
        real = self._real * other._real - self._imag * other._imag
        imag = self._real * other._imag + self._imag * other._real
        return ComplexNumber(real, imag)

    def __str__(self):
        sign = "+" if self._imag > 0 else "-"
        return f"({self._real}{sign}{abs(self._imag)}j)"

    @property
    def real(self):
        return self._real

    @property
    def imag(self):
        return self._imag

    def conjugate(self):
        return ComplexNumber(self._real, -self._imag)

complexNumber1 = ComplexNumber(2, 3)
print(complexNumber1)
print(complexNumber1.conjugate())

complexNumber2 = ComplexNumber(5, -8)
print(complexNumber2)
print(complexNumber2.conjugate())

print(complexNumber1 + complexNumber2)

print(complexNumber1 * complexNumber2)