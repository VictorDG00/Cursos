# faça um programa que abra e reproduza o áudio de arquivo mp3
from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Agora você escuta?')
