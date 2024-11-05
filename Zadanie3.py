#Есть множество студентов. Каждый из них знает некоторое количество языков. Нужно определить сколько различных языков знают студенты.
# Выведите отсортированный список этих языков. Выведите список студентов, которые знают китайский язык.
students = {
    "Виктор": ["Английский", "Русский", "Испанский"],
    "Костя": ["Русский", "Казахский"],
    "Чарли": ["Английский", "Китайский"],
    "Давид": ["Русский", "Японский", "Китайский"]
}

dict_languages = set()
for languages in students.values():
    dict_languages.update(languages)

sorted_l = sorted(dict_languages)
print("Различные языки, которые знают студенты:")
for language in sorted_l:
    print(language)

chinese = [student for student, languages in students.items() if "Китайский" in languages]
print("Список студентов, знающих китайский язык:")
for student in chinese:
    print(student)
