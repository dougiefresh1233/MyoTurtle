#!/usr/bin/python
''' DON'T TOUCH THESE FIRST LINES! '''
''' ============================== '''
from PyoConnect import *
myo = Myo(sys.argv[1] if len(sys.argv) >= 2 else None) 
''' ============================== '''

''' OK, edit below to make your own fancy script ^.^ '''

# Edit here:
import time
import os
import turtle
myo.unlock("hold")
def onPoseEdge(pose,edge):
		
	if(pose=="fist") and (edge=='on'):
		myo.vibrate(1)
		speed=myo.getPitch()*25	
		turtle.forward(speed)	
		#print('Fist')
	elif(pose=="waveIn")and (edge=='on'):
		myo.vibrate(1)
		angle=abs(myo.getRoll())*25
		turtle.left(angle)
		#print('Wave In')
		#print(myo.getRoll())
	elif(pose=='waveOut')and (edge=='on'):
		myo.vibrate(1)
		angle=-(myo.getRoll()*25)
		turtle.right(angle)
		#print('Wave Out')
	elif(pose=="fingersSpread")and (edge=='on'):
		myo.vibrate(2)
		myo.rotSetCenter();
		#print('Spread')
	elif(pose=='doubleTap')and (edge=='on'):
		myo.vibrate(1)
		loc=myo.getBox()
		if (loc==0):
			coordx=0
			coordy=0
		elif(loc==1):
			coordx=0
			coordy=-100
		elif(loc==2):
			coordx=100
			coordy=-100
		elif(loc==3):
			coordx=100
			coordy=0
		elif(loc==4):
			coordx=100
			coordy=100
		elif(loc==5):
			coordx=0
			coordy=100
		elif(loc==6):
			coordx=-100
			coordy=100
		elif(loc==7):
			coordx=-100
			coordy=0
		elif(loc==8):
			coordx=-100
			coordy=-100

		turtle.setposition(coordx,coordy)
		#print('Double Tap')


# Stop editting

# Comment out below the events you are not using
#myo.onLock = onLock
#myo.onUnlock = onUnlock
myo.onPoseEdge = onPoseEdge
#myo.onPeriodic = onPeriodic
#myo.onWear = onWear
#myo.onUnwear = onUnwear
#myo.onEMG = onEMG
#myo.onBoxChange = onBoxChange

''' DON'T TOUCH BELOW THIS LINE! '''
''' ============================ '''
myo.connect()
while True:
	myo.run()
	myo.tick()
