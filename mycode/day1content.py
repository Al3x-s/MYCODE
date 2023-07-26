import random
wordbank= ["indentation", "spaces"] 
tlgstudents= ['Alex', 'Benji', 'Cayla', 'Demetra', 'Derek', 'Deshawn', 'James', 'Maria', 'Marylyn', 'Nor', 'Sal', 'Sammy']
wordbank.append(4)
num = input("pick a number between 0 and 11" )
if num.isnumeric():
    num = int(num)
    student_name = tlgstudents[num]
else:
    student_name = num

print(f"{student_name} always uses {wordbank[-1]} {wordbank[1]} to indent")

print(f"random student is {random.choice(tlgstudents)}")
