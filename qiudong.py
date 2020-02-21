import config
import pyautogui
from pyautogui import position              
def qd():
    config.x,config.y=pyautogui.position()                    #获取当前鼠标位置
    print('球洞坐标',config.x,config.y)
