def find_secondlow_student(list_student):
    lower_value = a[0][2]
    second_lower_value = a[0][2]
    for item in list_student:
        if lower_value>(item[2]):
            second_lower_value = lower_value
            lower_value = (item[2])
        elif second_lower_value>(item[2]):
            second_lower_value = (item[2])
    return second_lower_value
a = [["Subhan", "Nursery", 80],["Bital", "Prep", 70],["Arham", "Pg", 60]]
ans = find_secondlow_student(a)
print("return value is")
print(ans)




     