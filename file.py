num=int(input("Введите первое число для суммы"))
num2=int(input("Введите второе число для суммы"))
num3=int(input("Введите третье число для суммы"))
num4=int(input("Введите  число для деления суммы"))
num5=int(input("Введите  остаток от деления"))
final_num=num+num2+num3
if(final_num%num4==num5):
    print("True")
else:
    print("False")