#Desafio 21 Fazer um programa que leia um arquivo MP3
import pygame
print('{:=^20}'.format('Desafio 21'))
pygame.init()
pygame.mixer.music.load('nome do arquivo')
pygame.mixer.music.play()
pygame.event.wait()
