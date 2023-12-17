class infor_item:
     def __init__(self,para_name):
         self.name= para_name
         self.img="data\\image\\item\\"+para_name+".png"

ShopDiscount = infor_item("ShopDiscount")
print(ShopDiscount.name,ShopDiscount.img)