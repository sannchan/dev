import os
import sys
import time #カレンダーのように時刻以外の日付や曜日なども扱う場合は「datetime」
import tkinter as tk
from tkinter import ttk

class app:
    def __init__(self):
        pass
    def disp(self):
        print("disp")
    def clock(self):
        print("clock")
    def memo(self):
        print("memo")
        self.clock()
        
apprun = app()
apprun.disp()
apprun.clock()
apprun.memo()