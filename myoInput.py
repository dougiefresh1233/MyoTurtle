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

myo.unlock("hold")
def onPoseEdge(pose,edge):
		
	if(pose=="fist") and (edge=='on'):
		myo.vibrate(1)
		speed=myo.getPitch()*25	
		print('pitch:')
		print(speed)
		#print('Fist')
	elif(pose=="waveIn")and (edge=='on'):
		myo.vibrate(1)
		angle=abs(myo.getRoll())*25
		print('roll:' )
		print(angle)
		#print('Wave In')
		#print(myo.getRoll())
	elif(pose=='waveOut')and (edge=='on'):
		myo.vibrate(1)
		angle=myo.getYaw()
		print('yaw:')
		print( angle)
		#print('Wave Out')
	elif(pose=="fingersSpread")and (edge=='on'):
		myo.vibrate(2)
		myo.rotSetCenter();
		#print('Spread')
	elif(pose=='doubleTap')and (edge=='on'):
		myo.vibrate(1)
		loc=myo.getBox()
	
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
