# # print("Hello world")
# # print("Bye")
# # c=20.67
# # b="string"
# # print(b)
# # print("Hi")
# class product:
#     def __init__(self,price, name,units,uniqe_code):
#         self.price= price
#         self.name=name
#         self.units=units
#         self.uniqe=uniqe_code
# class Cart:
#     def __init__(self,item_lis=None):
#         self.item_lis
#         if item_lis is not None:
#             self.item_lis=item_lis
#
#     def add_to_cart(self,quantity,product):
#         self.items_lis.append(dict(item=product,quantity=quantity))
#
#     def calculate_total(self):
#         total=0
#         for item in self.itme_lis:
#             total+= item["item"].price*item['quantity']
#         return total
# tomato=product(price=80,name="Red tomato",units="kg",uniqe_code="123q")
# bread=product(price=25,name="Bread",units="piece",uniqe_code="432qc")
# water=product(price=30,name="Water",units="l",uniqe_code="88wq")
# cart=Cart()
# cart.add_to_cart(bread,2)
# print(cart.calculate.total)
# class Product:
#     def __init__(self, price, name, units, unique_code):
#         self.price = price
#         self.name = name
#         self.units = units
#         self.unique_code = unique_code
#
#
# class Cart:
#     def __init__(self, items_list=None):
#         if items_list is not None:
#             self.items_list = items_list
#         else:
#             self.items_list = []
#
#     def add_to_cart(self, product, quantity):
#         self.items_list.append(dict(product=product, quantity=quantity))
#
#     def calculate_total(self):
#         total = 0
#         for item in self.items_list:
#             product = item['product']
#             quantity = item['quantity']
#             total += product.price * quantity
#         return total
#
#
# # items_list -> {product, quant} {product2, quantity}
# #                item               item
# #                 item['item'] -> Product
#
# if __name__ == '__main__':
#     tomato = Product(price=80,
#                      name="Red tomato",
#                      units="kg",
#                      unique_code="123wqe")
#     bread = Product(price=25,
#                     name="White bread",
#                     units="piece",
#                     unique_code="432qsc")
#     water = Product(price=30,
#                     name="Sparkling Water",
#                     units="piece",
#                     unique_code="098eiu")
#     cart = Cart()
#     cart.add_to_cart(bread, 2)
#     cart.add_to_cart(tomato, 0.6)
#     print(cart.calculate_total())
class Element:
    def __init__(self,temperature):
        if temperature >0:
            status="Твердий"
        elif temperature<0:
            status="Рідкий"
        return status