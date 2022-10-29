number_of_appartament=int(input("Введите номер квартиры"))
count_of_appartament=int(input("Введите колличество квартир на этаж"))
count_of_floors=int(input("Введите колличество этажей на дом"))
floor=number_of_appartament/count_of_appartament
num=floor-count_of_floors
entrance=1
while(num>0):
    entrance+=1



# entrance=floor/count_of_floors
final_floor=round(floor)
final_entrance=round(entrance)
print("Заказчик находиться на ",final_floor,"этаже в",final_entrance,"подъезде","в квартире под номером ",number_of_appartament)
