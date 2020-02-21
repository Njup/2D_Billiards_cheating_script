import config
import pyautogui
from pyautogui import position              
def mbq():
    config.a,config.b=pyautogui.position()                    #获取当前鼠标位置
    print('目标球坐标：',config.a,config.b)
