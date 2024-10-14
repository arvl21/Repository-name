numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
none_=4
first_part=numbers[:none_]
second_part=numbers[none_+1:]

full_list=first_part+second_part
average=sum(full_list)/len(numbers)
numbers[none_]=average
print("Измененный список:", numbers)