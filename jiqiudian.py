import config
from time import sleep
import pyautogui
from pyautogui import position
import math
def jqd():
    tan=abs((config.b-config.y))/abs((config.a-config.x))
    arctan=math.atan(tan)           #计算夹角（弧度制）
    if config.a>config.x and config.b>config.y:
        config.j=config.a+(math.cos(arctan)*config.n)          # 计算j,k                   
        config.k=config.b+(math.sin(arctan)*config.n)
        print('击球点坐标：',config.j,config.k)
    elif config.a>config.x and config.b<config.y:
        config.j=config.a+(math.cos(arctan)*config.n)          # 计算j,k                   
        config.k=config.b-(math.sin(arctan)*config.n)
        print('击球点坐标：',config.j,config.k)
    elif config.a<config.x and config.b>config.y:
        config.j=config.a-(math.cos(arctan)*config.n)          # 计算j,k                   
        config.k=config.b+(math.sin(arctan)*config.n)
        print('击球点坐标：',config.j,config.k)
    elif config.a<config.x and config.b<config.y:
        config.j=config.a-(math.cos(arctan)*config.n)          # 计算j,k                   
        config.k=config.b-(math.sin(arctan)*config.n)
        print('击球点坐标：',config.j,config.k)

    sleep(2)                                    #休眠两秒
    pyautogui.moveTo(config.j,config.k)                       #鼠标移到jk坐标
