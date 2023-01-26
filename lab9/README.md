# Лабораторная работа №9
## Вариант: 1
------
*Количество элементов:* 50000

*Количество файлов (лент):* 4

*Максимальное количество элементов в оперативной памяти:* 60 </br>
**Для удобства я разделил программу на два файла** </br>
В файле [sorts.py](https://github.com/Zohoto/Andrew/blob/master/lab9/sorts.py "sorts.py") находится метод сортировки пузырьком, а также класс для работы с элементами в массиве

Основной файл [main.py](https://github.com/Zohoto/Andrew/blob/master/lab9/main.py "main.py"). </br>
В конце программа показывает в каком файле сохранена сортировка, а также время за которое программа провела сортировку  


------------


## Контрольные вопросы

**1. Дайте определение термину "внутренняя сортировка"?**

Внутрення сортировка - это сортировка, где используется только оперативная память. Части сортируемого массива не сохраняются во внешнюю память.

**2. Дайте определение термину "внешняя сортировка"?**

Внешняя сортировка -  это сортировка, где используется не только оперативная, но и внешняя память. Обычно ее используют для сортировки большого списка данных.


**3. Дайте определение термину "отрезок"?**

Отрезок - это упорядоченная часть файла
или
Отрезок - это часть списка, который переходит в ОЗУ для сортировки.

**4. В чем суть метода слияния отрезков?**

Метод слияния отрезков - это метод, при котором исходные данные делятся на части, которые позже сортируются. Сортировка проходит в оперативной памяти, а после методом слияния сортируется во внешней памяти.

**5. Перечислите методы внешней сортировки?**

К наиболее известным алгоритмам внешних сортировок относятся:
- простое слияние
- естественное слияние
- многопутевое слияние
- многофазная сортировка 
- каскадная сортировка