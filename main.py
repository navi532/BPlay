from imutils.video import VideoStream
import imutils
import argparse
import cv2
import time
import pyautogui
from bplay.control_commands import MasterControl

pyautogui.FailSafeException=False

def main():
	
	parser=argparse.ArgumentParser()
	parser.add_argument('-f', '--filter', required=True,help='Range filter. RGB or HSV')
	parser.add_argument('-w','--webcam',type=int,default=0,required=False,help='Input number for Video Source')					
	args=vars(parser.parse_args())

	if not args['filter'].upper() in ['RGB', 'HSV']:
		parser.error("Please speciy a correct filter.")

	vs=VideoStream(src=args["webcam"]).start()
	time.sleep(2)

	X_Frame=MasterControl('Bplay',args["filter"],lwr=(22,140,101),upr=(96,255,255))

	while True:
		frame=vs.read()
		frame = cv2.flip(frame, 1)
		frame=imutils.resize(frame,width=500)
		
		X_Frame.update(frame)

		X_Frame.showWindow()#Range_Filter Values lwr=(22,140,101),upr=(96,255,255)

		if X_Frame.setROI:
			X_Frame.executeBasicCommands()
			pass
			
		key = cv2.waitKey(1) & 0xFF
		X_Frame.keyControl(key)

if __name__=="__main__":
	main()















