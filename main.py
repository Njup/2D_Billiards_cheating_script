import config
import qiudong
import mubiaoqiu
import jiqiudian
import pygame
import sys
import time
pygame.init()
screen = pygame.display.set_mode((300,200))
print('     ----  Copyright [2020] by [NJUP]  ----   ')
print('按下F1，获取球洞坐标')

def check_key():
    for event in pygame.event.get():
       
        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_F1:                 
                qiudong.qd()
                print('按下F2，获取目标球坐标')

        if event.type ==pygame.KEYDOWN:
            if event.key == pygame.K_F2:
                mubiaoqiu.mbq()
                print('按下F3，获取击球位置，2s后移动到击球点')

        if event.type ==pygame.KEYDOWN:
            if event.key ==pygame.K_F3:
                jiqiudian.jqd()
                print('按下F1，获取球洞坐标')
while True:
    time.sleep(0.1)
    check_key()
