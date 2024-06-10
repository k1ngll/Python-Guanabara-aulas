'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

import pygame

pygame.init()

pygame.mixer.music.load('C:\\Users\\anton\\Music\\Musics\\gringa\\Lady Gaga - Greatest Hits Full Album - Best Songs Collection 2023_YTnDbUu6kBM.mp3')

pygame.mixer.music.play()

input()

pygame.mixer.music.stop()