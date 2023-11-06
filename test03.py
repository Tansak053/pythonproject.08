# OOP ชื่อ class ขึ้นต้นด้วยตัวใหญ่ camel

class IoTSAU :
    # data/property/field/attribute
    major = "SAU"
    name = ""

    # method การทำงาน (มันคือ function แต่เราไม่เรียกฟังก์ชัน)
    def showHi(self) :
        print('Hi....')

    def introduceMyself(self) :
        print(f'My name is {self.name}')
        print(f'My major is {self.major}')

# ----------
# สร้าง opject ขึ้นต้นด้วยตัวเล็ก camel และ snake
obA = IoTSAU( ) # เป็นการเรียกใช้ construtor ของคลาสให้ทำงาน (ถ้ามี)
obB = IoTSAU( )


# การใช้งาน Data ของ object คือ เอาค่าของมันมาใช้ หรือเปลี่ยนค่าให้มันใหม่
print(obA.major)
obA.major = "Wow"
obA.name = "ฟ้าร้อง"
obB.name = "ฝนตกแล้ว"

# การใช้งาน Data ของ object คือ สั่งให้เมธอดของ object นั้นๆ ทำงาน
obA.introduceMyself()
obB.introduceMyself()