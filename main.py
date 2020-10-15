from imutils.video import VideoStream
import imutils
import argparse
import cv2
import time
import pyautogui
from bplay.control_commands import MasterControl
from bplay import control_window_frame

pyautogui.FailSafeException=False

def main():

	parser=argparse.ArgumentParser()
	parser.add_argument('-f', '--filter', default="HSV",help='Range filter. RGB or HSV')
	parser.add_argument('-w','--webcam',type=int,default=0,required=False,help='Input number for Video Source')
	args=vars(parser.parse_args())

	if not args['filter'].upper() in ['RGB', 'HSV']:
		parser.error("Please specfiy a correct filter.")

	vs=VideoStream(src=args["webcam"]).start()
	time.sleep(2)

	Frame=MasterControl('Bplay',args["filter"],lwr=(0,0,0),upr=(255,255,255))

	while True:
		frame=vs.read()
		frame = cv2.flip(frame, 1)
		frame=imutils.resize(frame,width=500)

		Frame.update(frame)

		Frame.showWindow()#Range_Filter Values lwr=(22,140,101),upr=(96,255,255)

		if Frame.setROI:
			Frame.executeBasicCommands()
			pass

		key = cv2.waitKey(1) & 0xFF
		Frame.keyControl(key)

if __name__=="__main__":
	main()















