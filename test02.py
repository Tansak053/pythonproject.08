# ******** Dictionary คือ ข้อมูลหลายข้อมูลที่เป็น key:value แก้ไขได้ ไม่มี index กำกับ ไม่มีลำดับ ซ้ำได้
# key เป็น String/Integer ห้ามเป็น True,False ส่วน value เป็นอะไรก็ได้ (number,string,boolean,list,tuple,set,dictionary)
my_dict1 = {'name':'mod', 'age':30, 555:999, 'flag':True, 'wow':[10,20,30]}

my_dict2 = {    'data1':[10, 30, 40],
                'data2':(2, 5, 6),
                'data3':{45, 3, 6},
                'data4':{ 'x':111,
                          'y':222
                        }
           }

# การเข้าถึงแต่ละข้อมูล
print(my_dict1['name'])
print(my_dict1[555])
# เปลี่ยนข้อมูล
my_dict1['age'] = 50
print(my_dict1)
# อยากแสดงผล 20 ออกมา
print(my_dict1['wow'][1])
# อยากแสดงผล 222 ออกมา
print(my_dict2['data4']['y'])
# เพิ่มข้อมูล สร้าง key ที่ไม่มีขึ้นมาที่ไม่มี
my_dict2['data5'] = 888
print(my_dict2)

# การเข้าถึงทุกข้อมูล
# อยากได้ key ไม่ต้อง .keys ก็ได้
for meow in my_dict1 :
    print(meow)

# อยากได้ข้อมูลให้มี .values
print('----------------')
for meow in my_dict1.values() :
    print(meow)

# ได้ทั้ง Key และ values ให้ใช้ .items สร้าง 2 ตัวแปร
print('----------------')
for meow, maw in my_dict1.items() :
    print(meow, '-', maw)

# Dictionary Method
# .popitem ข้อมูลสุดท้ายจะท้าย
my_dict1.popitem()
my_dict1.popitem()
my_dict1.popitem()
print(my_dict1)
# .pop เอาข้อมูลที่กำหนดออก
my_dict2.pop('data3')
print(my_dict2)
# .get เอาแค่ข้อมูลนั้น
print('---------------')
print(my_dict2['data2'])
print(my_dict2.get('data2'))