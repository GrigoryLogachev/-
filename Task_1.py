numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

numbers_list_1 = numbers[0:4]
numbers_list_2 = numbers[5:]
count_numbers = len(numbers)
sum_numbers = sum(numbers_list_1) + sum(numbers_list_2)
average = sum_numbers / count_numbers

right_numbers = numbers_list_1 + [average] + numbers_list_2

print("Измененный список:", right_numbers)
