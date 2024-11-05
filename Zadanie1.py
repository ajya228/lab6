#Создайте словарь, содержащий перечень стран и их столиц.
#a)   Выведите на экран все пары ключ-значение.
#b)  Выведите на экран столицу для определенной страны.
#c) Отсортируйте и выведите на экран содержимое словаря в алфавитном порядке названий стран.

countries_capitals = {'Россия' : 'Москва', 'Германия': 'Берлин', 'Эфиопия': 'Аддис-Абеба', 'Грузия': 'Тбилиси'}
for key, value in countries_capitals.items():
    print(f" {key}: {value}")

find_country = input("Введите страну: ")
if find_country in countries_capitals:
    print(f"Столицей страны {find_country} является {countries_capitals[find_country]}")
else:
    print(f"Столица для {find_country} не найдена")

sorted = sorted(countries_capitals.items())
print("Отсортированный список стран и их столиц:")
for country, capital in sorted:
    print(f"{country}: {capital}")

