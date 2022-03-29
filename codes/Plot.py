from os import sep
from turtle import color
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Get the Figure
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_facecolor((0,0,0)) # Set the background to black


def animate(i):
	ax.clear()
	xs = []
	ys = []
	emotions = open('emotext.csv').read() 

	for idx, em in enumerate(emotions[1:]):
		t = idx
		xs.append(t)
		ys.append(int(em))
	# n = len(emotions)	
	ax.clear()
	ax.plot(xs, ys,'o-', color = (0.7,0.3,0.3))
	# ax.set_xlim([0, n-1])
	ax.set_xticklabels([])
	ax.set_ylabel("Emotion")
	ax.set_xlabel("Time")
	ax.set_title("Live Plot of your Emotions")
	
	fig.tight_layout() # To remove outside borders
	ax.yaxis.grid(False)
	ax.set_ylim([0,8])
	ax.set_yticklabels(["Anger","Contempt","Disgust","Fear","Happy","Neutral","Sad","Surprise"])
	
# Lets call the animation function 	

ani = animation.FuncAnimation(fig, animate, interval=100)
plt.show()


# FFwriter = animation.FFMpegWriter()
# ani.save('video_your_emotions.mp4', writer = FFwriter)
# plt.close()

# path = '/static/video'
writergif = animation.PillowWriter(fps=30) 
ani.save('static/video/video_your_emotions.gif', writer=writergif)