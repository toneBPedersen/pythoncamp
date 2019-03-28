first_num = input("Enter first number")
calc = input("What do you want to do? +,-,*,/")
sec_num = input("Enter second number")
first_num = int(first_num)
sec_num= int(sec_num)
if calc=='+':
    result = first_num+sec_num
elif calc == '-':
    result = first_num - sec_num
elif calc == '*':
    result = first_num * sec_num
elif calc == '/':
    result = first_num / sec_num
else:
    print('The calculation is not valid')
    result = None

print("The result is: {}".format(result))