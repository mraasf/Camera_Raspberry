#Gambiarrista MRAASF
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1280,920)



print("Insira um nome para a foto")
name = input()
saida ="/home/pi/Documents/"+name+".jpg"
#print(saida)
#print(name)
camera.capture(saida)
print("imagem capturada salva em /home/pi/Documents")
