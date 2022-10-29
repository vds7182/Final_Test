# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



# number= None
def counter(number):
    if (number == 1):
        print("*")
    for i in range(number):
        if (i%2==0):
            continue
        if (i == 1):
            print("*")
        save_i = i + 2
        num=1

        list=["*"*save_i]

        # while(len(list)==num):
        #
        #     l=["        "]
        #     l=l-"    "
        print("*" * (save_i))
        num = num + 2
        # save_i=i+2
        # print("\t*"*(save_i))










while True:
    number = int(input("Введите целое положительное нечетное число"))
    if(number%2==0):

        print("Число четное")
        continue
    counter(number)
    break
while(number>=1):
            number-=1
            if number%2==0:
                continue
            print("*" * number)


# def counter(number):
#     if (number == 1):
#         print("\t\t*")
#     for i in range(number):
#         if (i%2==0):
#             continue
#         if (i == 1):
#             print("\t\t*")
#
#         save_i=i+2
#         # print(save_i)
#         print("\t*"*(save_i))