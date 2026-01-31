# TODO Напишите функцию find_common_participants

def find_common_participants(group1_str, group2_str, delimiter=','):
    list1 = group1_str.split(delimiter)
    list2 = group2_str.split(delimiter)

    set1 = set(list1)
    set2 = set(list2)

    common = set1.intersection(set2)

    return sorted(list(common))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

common_participants = find_common_participants(participants_first_group, participants_second_group, delimiter='|')

print(f"Общие участники: {common_participants}")