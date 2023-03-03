import os
import sys

print("ファイル生成を行います。")
dir = input("ディレクトリを入力してください。")
if os.path.exists(dir):
    pass

else:
    ans = input("フォルダが存在しません。作成しますか？")
    if ans == "y":
        os.mkdir(dir)
    else:
        sys.exit(0)

filenum = input("作成するファイル数を指定してください")
fornam = int(filenum)


for i in range (fornam):
    path = f"{dir}/{i}.png"
    with open(path,"w") as f:
      f.write(f"make{i}")
      
#帰ったら治したいところ
#フォルダはresult指定
#ファイル名の命名規則をユーザに選ばせる