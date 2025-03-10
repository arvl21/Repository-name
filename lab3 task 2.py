# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):

    set_group1 = set(group1.split(separator))
    set_group2 = set(group2.split(separator))

    common_participants = sorted(set_group1 & set_group2)

    return common_participants

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
common = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники:", common)