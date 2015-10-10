#!/usr/bin/python
''' DON'T TOUCH THESE FIRST LINES! '''
''' ============================== '''
from PyoConnect import *
myo = Myo(sys.argv[1] if len(sys.argv) >= 2 else None) 
''' ============================== '''

''' OK, edit below to make your own fancy script ^.^ '''

# Edit here:
import time
import turtle

def onPeriodic():
	myo.unlock("hold")
	pose=myo.getPose()	
	if(pose=="doubleTap"):
		myo.vibrate(2)
		myo.rotSetCenter();
		#print('Spread')
	yaw=myo.getYaw()
	if (yaw>0):
		turtle.left(yaw+1)
	elif(yaw<0):
		turtle.right(-yaw+1)
	#turtle.right(roll)
	pitch=myo.getPitch()
	turtle.forward(1+pitch*2)
	#time.sleep(1)


# Stop editting

# Comment out below the events you are not using
#myo.onLock = onLock
#myo.onUnlock = onUnlock
#myo.onPoseEdge = onPoseEdge
myo.onPeriodic = onPeriodic
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
