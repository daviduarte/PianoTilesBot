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

def processImage(img, cont):

	h, w, c = img.shape

	offsetX = 670
	offsetY = 80

	img = img[offsetY:850, offsetX:1015, 0:4]	

	coluna1 = 55
	coluna2 = 140
	coluna3 = 225
	coluna4 = 310
	index_coluna = [coluna1, coluna2, coluna3, coluna4]

	# - PRIMEIRO VAMOS CORTAR A IMAGE PARA FICAR SOMENTE A ÁREA DO JOGO - ok
	img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB) # RGBA to RGB
	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	ret, img = cv2.threshold(img,110,255,cv2.THRESH_BINARY)

	
	linha1 = img[100:600, coluna1]
	linha2 = img[100:600, coluna2]
	linha3 = img[100:600, coluna3]
	linha4 = img[100:600, coluna4]	

	"""
	img2 = copy.deepcopy(img)
	img2[100:600, coluna1] = 0
	img2[100:600, coluna2] = 0
	img2[100:600, coluna3] = 0
	img2[100:600, coluna4] = 0
	showArray(img2)

	print(linha1)
	time.sleep(30)	
	"""
	

	mouseY = 400
	if 0 in linha1:
		ocorrencias = np.where(linha1 == 0)[0] # Uma margem para evitar que o mouse caia fora do quadrado
		mouse1 = ocorrencias[ocorrencias.shape[0]-1]
		
	else:
		mouse1 = -1

	if 0 in linha2:
		ocorrencias = np.where(linha2 == 0)[0] # Uma margem para evitar que o mouse caia fora do quadrado
		mouse2 = ocorrencias[ocorrencias.shape[0]-1]
	else:
		mouse2 = -1

	if 0 in linha3:
		ocorrencias = np.where(linha3 == 0)[0] # Uma margem para evitar que o mouse caia fora do quadrado
		mouse3 = ocorrencias[ocorrencias.shape[0]-1]
	else:
		mouse3 = -1

	if 0 in linha4:
		ocorrencias = np.where(linha4 == 0)[0] # Uma margem para evitar que o mouse caia fora do quadrado
		mouse4 = ocorrencias[ocorrencias.shape[0]-1]
	else:
		mouse4 = -1

	if mouse1 == mouse2 == mouse3 == mouse4 == -1:
		return

	index_mouse = [mouse1, mouse2, mouse3, mouse4]
	maiorY = np.argmax(index_mouse)

	mouse.position = (offsetX + index_coluna[maiorY], offsetY + index_mouse[maiorY] + 100)
	mouse.click(Button.left)
	
		#mouse.press(Button.left)
		#mouse.release(Button.left)

		#print("Clicou em: " + str(offsetX + mouseX) + " " + str(offsetY + mouseY))

	#return mouseX
	#im = Image.fromarray(img)
	#im.save("screenshots/" + str(cont) + ".png")
	#cont += 1
	#showArray(linha)
	#time.sleep(10)
	#time.sleep(10)

def main():
	# Bora

	cont = 0
	start = time.time()
	anterior = -1
	while 1:
		img = capture()	
		processImage(img, cont)
		#time.sleep(0.005)

		#cont += 1
		#if cont > 100:
			#end = time.time()
			#print("Frames por segundo: " + str(cont/(end-start)))
		#	break
		#cont += 1


if __name__ == '__main__':
	signal.signal(signal.SIGINT, panic_button)
	main()
