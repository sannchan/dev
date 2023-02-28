from PIL import Image
import glob
from tkinter import messagebox
import os
import sys
import webbrowser
dirpath = './result'

messagebox.showinfo('バーコード切り抜きソフトウェア v1.0.0 build by 入村', '処理を開始します。')
ask=messagebox.askquestion("確認", "このプログラムと同じフォルダにバーコードを保存しましたか？いいえを押した場合バーコード作成webページを開きます。")
if ask == "yes":
  pass

else:
  webbrowser.open("https://barcode-place.azurewebsites.net/Barcode/code39", new=1, autoraise=True)
  sys.exit()
  
if os.path.isdir(dirpath):
  pass
  
else:
  ask=messagebox.askquestion("処理後のフォルダがありません", "作成しますか？")
  
  if ask == 'yes':
    os.mkdir(dirpath)
  else:
    sys.exit()
       
img_files = glob.glob('*.png')

for file_name in img_files:

  im = Image.open(file_name)

  img_roi = im.crop((0, 0, 161, 42)) # (left, upper, right, lower)

  img_roi.save('./result/Nonamber_'+str(file_name))
  
messagebox.showinfo('バーコード切り抜きソフトウェア v1.0.0 build by 入村', '完了しました。')