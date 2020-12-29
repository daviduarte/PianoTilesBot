import numpy as np
from mss import mss
from PIL import Image
import cv2
import time
import signal
import sys
#import pyautogui
import copy
import uinput
from pynput.mouse import Button, Controller
mouse = Controller()


#pyautogui.PAUSE = 0.01


def capture():
	with mss() as sct:
			monitor = sct.monitors[1]
			img = np.array(sct.grab(monitor))

			return img

def showArray(array):
	img = cv2.cvtColor(array, cv2.COLOR_BGR2RGB)
	oi = Image.fromarray(img)
	oi.show()


# !!! PUSH ctr IF THINGS GOING WRONG !!! (useless)
def panic_button(sig, frame):
    print('falous')
    sys.exit(0)

def processImage(img, cont, anterior):

	h, w, c = img.shape

	offsetX = 700
	offsetY = 80

	img = img[offsetY:850, offsetX:1000, 0:4]	

	# - PRIMEIRO VAMOS CORTAR A IMAGE PARA FICAR SOMENTE A ÁREA DO JOGO - ok
	img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB) # RGBA to RGB
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret, img = cv2.threshold(img,110,255,cv2.THRESH_BINARY)

	#showArray(img)
	im = Image.fromarray(img)
	im.save("screenshots/" + str(cont) + ".png")

	#print(img.shape)
	#exit()
	#img = img[]
	#showArray(img)
	
	# - PEGO UMA FAIXA DA METADE DA TELA DO JOGO
	#img_teste = copy.deepcopy(img)
	#img_teste[500,:] = 0
	#showArray(img_teste)
	linha = img[400, :]
	#print(linha)
	# reshape
	#linha = np.reshape(linha, (300,1,3))
	#print(linha.shape)
	#exit()

	# CONVERTE PARA TONS DE CINZA
	

	# BINARIZA A IMAGEM (APENAS PRETO E BRANCO)
	

	

	mouseY = 400
	if 0 in linha:
		mouseX = np.where(linha == 0)[0][0] + 50 # Uma margem para evitar que o mouse caia fora do quadrado
		#print("ENCONTROU UM PIXEL PRETO")
		#print("LEVAR O MOUSE NA POSIÇÃO: " + str(mouseX))
		#exit()
		#print(linha)
		if mouseX == anterior:
			return mouseX
		

		#ret,img = cv2.threshold(img,220,255,cv2.THRESH_BINARY)
		#showArray(img)

		#pyautogui.moveTo(offsetX + mouseX, offsetY + mouseY)
		#pyautogui.click(offsetX + mouseX, offsetY + mouseY)
		#pyautogui.click(offsetX + mouseX, offsetY + mouseY)

		mouse.position = (offsetX + mouseX, offsetY + mouseY)
		mouse.click(Button.left)
	
		#mouse.press(Button.left)
		#mouse.release(Button.left)

		#print("Clicou em: " + str(offsetX + mouseX) + " " + str(offsetY + mouseY))

		return mouseX
	#im = Image.fromarray(img)
	#im.save("screenshots/" + str(cont) + ".png")
	#cont += 1
	#showArray(linha)
	#time.sleep(10)
	#time.sleep(10)

def main():
	# Bora

	cont = 0
	#start = time.time()
	anterior = -1
	while 1:
		img = capture()	
		anterior = processImage(img, cont, anterior)
		#time.sleep(0.005)

		cont += 1
		#if cont > 1000:
		#	end = time.time()
		#	print("Frames por segundo: " + str(cont/(end-start)))
		#	break
		#cont += 1


if __name__ == '__main__':
	signal.signal(signal.SIGINT, panic_button)
	main()
