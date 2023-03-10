import os
import sys

class classstudy():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def region(self,region):
        self.region = region
    
class showdisp(classstudy):
    def __init__(self,name,age,region):
        super().__init__(name,age)
        self.region(region)
    
    def showdisp(self):
        print(f"{self.name}は{self.age}です。 {self.region}に住んでます。")

if __name__ == "__main__":
    doclass = classstudy(input("名前を入力してください："),int(input("年齢を入力してください：")))
    region = input("地域を入力してください：")
    doclass.region(region)
    doshow = showdisp(doclass.name, doclass.age, region)
    doshow.showdisp()
    if doclass.age >=30:
        print("三十路です")
    else:
        print("若いです")
    
