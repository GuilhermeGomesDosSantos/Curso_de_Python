# Faça um programa em Python que abra e reproduza o áudio de um arquivo

from pygame import init, mixer, event

init()
mixer.music.load('ImagineDragons.mp3')
mixer.music.play()
event.wait()

# Não Rodou 