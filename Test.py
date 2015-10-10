#!/usr/bin/python
''' DON'T TOUCH THESE FIRST LINES! '''
''' ============================== '''
from PyoConnect import *
myo = Myo(sys.argv[1] if len(sys.argv) >= 2 else None) 
''' ============================== '''

''' OK, edit below to make your own fancy script ^.^ '''

# Edit here:
myo.unlock("hold")
def onPoseEdge(pose,edge):
	if(pose=="fist") and (edge=='on'):
		myo.vibrate(1)		
		print('Fist')
	elif(pose=="waveIn")and (edge=='on'):
		myo.vibrate(1)
		print('Wave In')
	elif(pose=='waveOut')and (edge=='on'):
		myo.vibrate(1)
		print('Wave Out')
	elif(pose=="fingersSpread")and (edge=='on'):
		myo.vibrate(1)
		print('Spread')
	elif(pose=='doubleTap')and (edge=='on'):
		myo.vibrate(1)
		print('Double Tap')



#if myo.getpose()=="fist"
#	myo.vibrate(1)
#	print 'fist'







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
