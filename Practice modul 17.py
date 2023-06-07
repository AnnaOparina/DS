def main():
    raw_sequence = input("Введите последовательность чисел, разделенных пробелами: ")
    user_number = input("Введите число: ")
    sequence = raw_sequence.split()
    try:
        user_number = int(user_number)
        sequence = [int(i) for i in sequence]  # Преобразуем список из строк в список из чисел
        sorted_sequence = sorted(sequence)  # Сортируем список
    except ValueError:
        print("Вы ввели некорректные данные")
        return
    index = binary_search(sorted_sequence, user_number)  # Ищем индекс элемента
    if index is None:
        print("Указанное число не соответствует условиям задачи")
    elif index == len(sorted_sequence) - 1:
        print("Указанное число является наибольшим в последовательности")
    else:
        print(sorted_sequence[index+1])

def binary_search(sorted_list, number):
    """Реализация двоичного поиска"""
    low = 0
    high = len(sorted_list) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = sorted_list[mid]
        if guess == number:
            return mid
        if guess > number:
            high = mid - 1
        else:
            low = mid + 1
    return None
