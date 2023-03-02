import os
import sys

dir = "./result"
print("ファイル生成を行います。")
if os.path.exists(dir):
    pass

else:
    print("ディレクトリが存在しません。フォルダを新規します。")
    os.mkdir(dir)  

filename = input("ファイル名を入力してください。")

 
while True:
    inputnum = input("生成するファイル数をint型で入力してください: ")
    if inputnum.isdigit():
        fornam = int(inputnum) + 1
        for i in range (fornam):
            path = f"{dir}/{i}_{filename}"
            with open(path,"w") as f:
                f.write(f"make{i}")
        break
    else:
        print("エラー: int型で入力してください")

#帰ったら治したいところ
#フォルダはresult指定
#ファイル名の命名規則をユーザに選ばせる

 