#Gambiarrista MRAASF
from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1280,920)



print("Insira um nome para o video")
name = input()
name ="/home/pi/Documents/"+name+".h264"
print("Digite o tempo do video em segundos")
tempo = input()
# gravação de video
camera.start_recording(name)
camera.start_preview()
sleep(int(tempo))
camera.stop_preview()
camera.stop_recording()
print("Video salvo em /home/pi/Documents")
