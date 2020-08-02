import cv2
import imutils


class Window:

	def __init__(self,myFrame='BPlay',Filter="HSV",lwr=(0,0,0),upr=(255,255,255)):
		self.myFrame=myFrame
		self.range_filter=Filter
		self.enableTrackbar= False
		self.RangeValues=[]
		self.enableMask= False
		self.enableROI= True
		self.setROI= False
		self.lwr,self.upr=lwr,upr

	def update(self,Frame):
		self.frame=Frame

	def nothing(self,value):
		pass

	def createTrackbar(self,*args):
		cv2.namedWindow('TrackBar')

		for limit,value in {"MIN":0,"MAX":255}.items():
			for channel in self.range_filter:
				cv2.createTrackbar(f'{channel}_{limit}','TrackBar',value,255,self.nothing)

	def removeTrackbar(self):
		cv2.destroyWindow('TrackBar')

	def updateRangeValues(self):
		self.RangeValues=[]
		for limit in ["MIN","MAX"]:
			for channel in self.range_filter:
				val=cv2.getTrackbarPos(f'{channel}_{limit}','TrackBar')
				self.RangeValues.append(val)
		if self.RangeValues==[0,0,0,255,255,255]:
			self.RangeValues=[]

	def createMask(self):
		if self.range_filter =="HSV":
			blurry=cv2.GaussianBlur(self.frame,(3,3),0)
			frame_to_mask=cv2.cvtColor(blurry,cv2.COLOR_BGR2HSV)
		else:
			frame_to_mask=self.frame.copy()

		if len(self.RangeValues)!=0:
			self.mask=cv2.inRange(frame_to_mask,tuple(self.RangeValues[:3]),tuple(self.RangeValues[3:]))
		else:
			assert self.lwr != None and self.upr != None , "Provide Range Values for Mask"
			self.mask=cv2.inRange(frame_to_mask,self.lwr,self.upr)

		self.mask=cv2.erode(self.mask,(3,3),iterations=2)
		self.mask=cv2.dilate(self.mask,(3,3),iterations=2)

	def findROI(self):
		self.createMask()

		cnts=cv2.findContours(self.mask.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
		cnts=imutils.grab_contours(cnts)

		if len(cnts)>0:
			c = max(cnts,key=cv2.contourArea)
			(x,y),radius=cv2.minEnclosingCircle(c)

			return (int(x),int(y)),radius

		else:
			return None , None

	def showMask(self):

		center , _ =self.findROI()
		cv2.putText(self.mask,"Mask", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.65, (0,255,0), 2)

		if center is not None:
			cv2.circle(self.mask,center,3,(0,0,255),-1)
		cv2.imshow(self.myFrame,self.mask)

	def showROI(self):
	

		cv2.putText(self.frame, "Set Region of Action", (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.65, (0, 0, 0), 2)
		center , _ =self.findROI()
		
		if center is not None:
			cv2.circle(self.frame,center,3,(0,0,255),-1)
			cv2.circle(self.frame,center,self.Radius,(0,0,255),1)
			
		self.Center=center#Fixed my region
		cv2.imshow(self.myFrame,self.frame)

    
	def resetSettings(self):
		self.enableMask= False
		self.enableTrackbar= False
		self.enableROI= True
		self.setROI= False

	def showWindow(self):

		if self.enableTrackbar:
			self.updateRangeValues()
			self.showMask()

		elif self.enableMask:
			self.showMask()
		
		elif self.setROI:
			center , _ =self.findROI()
		
			if center is not None:
				cv2.circle(self.frame,center,3,(0,0,255),-1)
				
			
			cv2.putText(self.frame,self.command, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,0.65, (0, 0, 0), 3)
			cv2	.putText(self.frame, f"Change in x: {self.Dx}		Change in y: {self.Dy}",(10, self.frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX,0.35, (0, 0, 0), 3)
			
			cv2.circle(self.frame,self.Center,self.Radius,(0,255,0),1)
			
			cv2.imshow(self.myFrame,self.frame)
		
		else:
			self.showROI()

















