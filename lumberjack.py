# write by paros 13/10/2016
import PIL.ImageGrab
import PIL.ImageOps
import os
import time
from numpy import *
import pyautogui

# x,y start 300 790 left 217 790 right 385 790 
#left box 212+40 ,460+40 right box 345 +40 ,460 + 40

start_i,start_j = 300,790 
left_button_i,left_button_j = 217,790
right_button_i,right_button_j = 385,790
left_box_i, left_box_j = 232,480
right_box_i, right_box_j = 365, 480
isleft = True
left,right = 0,0 
left_temp,right_temp = 0,0


def identifyArea(i,j): 
	boxx = (i-5,j-5,i+5,j+5)
	imc = PIL.ImageOps.grayscale(PIL.ImageGrab.grab(boxx));
	a = array(imc.getcolors())
	return a.sum()

def startGame(): #capture pixel near the head of the man for reference
	global left 
	left = identifyArea(left_box_i,left_box_j)
	global right 
	right = identifyArea(right_box_i,right_box_j)
	print(left,right)

def playGame():
	global isleft # position of the man
	box = (0,0,503,586) # game area
	im = PIL.ImageGrab.grab(box)

	l_temp = left_box_j
	r_temp = right_box_j

	while (l_temp > 100): # each time screen capture can make 6 move 

		left_temp_box = (left_box_i -5 , l_temp - 5, left_box_i + 5, l_temp + 5  )
		imcc = PIL.ImageOps.grayscale(im.crop(left_temp_box))
		a=array(imcc.getcolors())
		left_temp = a.sum()

		right_temp_box = (right_box_i -5 , r_temp - 5, right_box_i + 5, r_temp + 5  )
		imccc = PIL.ImageOps.grayscale(im.crop(right_temp_box))
		b=array(imccc.getcolors())
		right_temp = b.sum()

		print("pixel position" + str(l_temp)+ str(left_box_i) + str(r_temp)+ str(right_box_i))
		print ("pixel value " + str(left_temp) + str(right_temp))

		if ((left == left_temp) and (right == right_temp)): # when nothing above head
			if (isleft == True):		
				pyautogui.click(217,790)
				print("left,same")
				pyautogui.click(217,790)
				print("left,same")
				isleft = True

			else:
				pyautogui.click(385,790)
				print("right,same")
				pyautogui.click(385,790)
				print("right,same")
				isleft = False
		
		elif ((left == left_temp) and (right != right_temp)): # when branch at right
			pyautogui.click(217,790)
			print("left,not")
			pyautogui.click(217,790)
			print("left,not")
			isleft = True
		
		elif ((left != left_temp) and (right == right_temp)): # when branch at left 
			pyautogui.click(385,790)
			print("right,not")
			pyautogui.click(385,790)
			print("right,not")
			isleft = False

		l_temp = l_temp - 100 # read higher()next branch on screen 
		r_temp = r_temp - 100 # in fact l_temp and r_temp are one variable, just keep it so i dont have to rewrite

def main():
	startGame()
	i = 0;
	pyautogui.click(217,790) # a click to focus on the game window
	while (i<70): # as game go faster and faster, ~400 score is limit of this program 70 x 6 move ~ 400 
		playGame()
		time.sleep(0.008) # wait for chopping animation to over
		print("mainloop" + str(i)) # state
		i=i+1


if __name__ =='__main__':
	main()
