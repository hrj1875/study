'''房子有户型，总面积和家具名称列表
注：新房子没有任何的家具
2.家具有名字和占地面积，其中：席梦思占地4平米；衣柜占地2平米；餐桌占地1.5平米
3.将以上三件家具添加到房子中
4.打印房子时要求输出：户型，总面积，剩余面积，家具名称列表'''
class Furniture:
    def __init__(self,name,area):
        self.name=name
        self.area=area
    def __str__(self):
        return '%s 占地面积为%.2f'%(self.name,self.area)
class House():
    def __init__(self,house_type,area):
        self.house_type=house_type
        self.area=area
        self.freearea=self.area
        self.f_item=[]
    def __str__(self):
        return ('户型为：%s,\n总面积：%.2f[剩余面积：%.2f],\n家具名称为%s'
                %(self.house_type,self.area,self.freearea,self.f_item))
    def add_item(self,item):
        if item.area<=self.freearea:
            self.f_item.append(item.name)
            self.freearea -= item.area
            return
        else:
            print('剩余面积不够用了')
            return
ximengsi=Furniture('席梦思',60)
yigui=Furniture('衣柜',40)
table=Furniture('餐桌',1.5)
print(ximengsi)
print(yigui)
print(table)
house1=House('三室一厅',100)
house1.add_item(ximengsi)
house1.add_item(yigui)
house1.add_item(table)
print(house1)