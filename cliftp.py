import ftplib
import glob
import os

class app:
    def __init__(self):
        pass

    def get_importfile(self):
        chkpass = os.path.isdir("/Users/sannchan/Desktop/upload")
        while chkpass:
            import_file = glob.glob(input("釜蓋の湯の求人情報のファイルパスを入力してください"))
            #import_file = glob.glob('/Users/sannchan/Desktop/upload/kamabuta(ippan).png')
            if import_file == "kamabuta(ippan).png":
                print("success")
            else:
                print("ファイル名が違います。ファイル名を修正しますか？")
                
              # os.rename(import_file)
                print(import_file)
            break
        else:
            print("make uploaddir")
            os.mkdir("/Users/sannchan/Desktop/upload")

run = app()
run.get_importfile()