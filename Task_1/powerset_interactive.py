def powerset(s):
# Вычисление булеана заданного множества
    power_set = [[]]  # Начинаем с пустого множества
    for elem in s:
        # Добавляем каждое подмножество, содержащее текущий элемент
        power_set.extend([subset + [elem] for subset in power_set])
    return power_set


if __name__ == '__main__':
    # 1. Ввод элементов множества от пользователя. Пример с числами
    input_str = input("Введите элементы множества через пробел: ")
    elements = input_str.split()

    # Преобразование введенных элементов в список чисел (или можно оставить строками)
    try:
        my_set = [int(elem) for elem in elements]
    except ValueError:
        my_set = elements

    # Вычисление булеана
    power_set = powerset(my_set)

    # Вывод булеана
    print("Множество:", my_set)
    print("Булеан:")
    for subset in power_set:
        print(subset)
print("\n--- Примеры с предопределенными множествами ---")

 # 2. Пример с предопределенным множеством чисел
example_set_numbers = [1, 2, 3]
example_powerset_numbers = powerset(example_set_numbers)
print("Множество (числа):", example_set_numbers)
print("Булеан (числа):", example_powerset_numbers)

# 3. Пример с предопределенным множеством строк
example_set_strings = ["a", "b", "c"]
example_powerset_strings = powerset(example_set_strings)
print("Множество (строки):", example_set_strings)
print("Булеан (строки):", example_powerset_strings)

# 4. Пример с пустым множеством
example_set_empty = []
example_powerset_empty = powerset(example_set_empty)
print("Множество (пустое):", example_set_empty)
print("Булеан (пустое):", example_powerset_empty)