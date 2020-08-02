import pyautogui
import numpy as np
from bplay.control_window_frame import Window
import cv2

class MasterControl(Window):
	Radius=30
	Center=None
	Dx=0
	Dy=0
	steps=2
	def __init__(self,myFrame='BPlay',Filter="HSV",lwr=(0,0,0),upr=(255,255,255),senstivity=0.2):
		Window.__init__(self,myFrame,Filter,lwr,upr)
		self.enableControl= True #Can be used to disable keys
		self.basicCommands={"Jump":'up',"Dodge":'down',"Left":'left',"Right":'right'}
		self.command=None
		self.prevCommand=None
		self.senstivity=senstivity

	def executeBasicCommands(self):
		center , _ =self.findROI()
		self.prepareCommand(center)
		if self.prevCommand!=self.command and int(np.sqrt(self.Dx**2+self.Dy**2))<2*self.Radius and self.command!="Steady":
				pyautogui.press(self.basicCommands[self.command])

		self.prevCommand=self.command

	def prepareCommand(self,center):
		self.Dx=center[0] - self.Center[0]
		self.Dy=center[1] - self.Center[1]
		dirx,diry = "",""

		if np.abs(self.Dx) > int(self.Radius*(1-self.senstivity)) :
			dirx= "Right" if np.sign(self.Dx) == 1 else "Left"

		if np.abs(self.Dy) > int(self.Radius *(1 - self.senstivity)):
			diry= "Jump" if np.sign(self.Dy) == -1 else "Dodge"

		if dirx=="" and diry=="" :
			self.command= "Steady"

		else:
			self.command=diry if diry !="" else dirx


	def keyControl(self,key):
		if self.enableControl:
			if key==ord('q'):
				cv2.destroyAllWindows()
				exit()

			if key==ord('s') and self.Center is not None:
				self.setROI= not self.setROI

			if key==ord('r'):
				self.resetSettings()

			if key==ord('m'):
				self.enableMask=not self.enableMask

			if key==ord('+') and not self.setROI:
				self.Radius+=self.steps

			if key==ord('-') and not self.setROI:
				self.Radius-=self.steps


			if key==ord('t'):
				self.enableTrackbar=not self.enableTrackbar

				if self.enableTrackbar:
					self.createTrackbar()

				else:
					self.removeTrackbar()