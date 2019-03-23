#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from astropy import constants as const
from glob import glob

###########################################
###	Read in data from files:	###

file1 = "quasar_data/J0003-2603_flux.dat"
w1, f1 = np.loadtxt(file1, skiprows=1, usecols=(0,1), unpack = True)
file2 = "quasar_data/BR1202-0725_flux.dat"
w2, f2 = np.loadtxt(file2, skiprows=1, usecols=(0,1), unpack = True)
file3 = "quasar_data/CTQ247_flux.dat"
w3, f3 = np.loadtxt(file3, skiprows=1, usecols=(0,1), unpack = True)
file4 = "quasar_data/CTQ460_flux.dat"
w4, f4 = np.loadtxt(file4, skiprows=1, usecols=(0,1), unpack = True)
file5 = "quasar_data/HE0001-2340_flux.dat"
w5, f5 = np.loadtxt(file5, skiprows=1, usecols=(0,1), unpack = True)
file6 = "quasar_data/HE0151-4326_flux.dat"
w6, f6 = np.loadtxt(file6, skiprows=1, usecols=(0,1), unpack = True)
file7 = "quasar_data/HE0940-1050_flux.dat"
w7, f7 = np.loadtxt(file7, skiprows=1, usecols=(0,1), unpack = True)
file8 = "quasar_data/HE1122-1648_flux.dat"
w8, f8 = np.loadtxt(file8, skiprows=1, usecols=(0,1), unpack = True)
file9 = "quasar_data/HE1158-1843_flux.dat"
w9, f9 = np.loadtxt(file9, skiprows=1, usecols=(0,1), unpack = True)
file10 = "quasar_data/HE1341-1020_flux.dat"
w10, f10 = np.loadtxt(file10, skiprows=1, usecols=(0,1), unpack = True)
file11 = "quasar_data/HE1347-2457_flux.dat"
w11, f11 = np.loadtxt(file11, skiprows=1, usecols=(0,1), unpack = True)
file12 = "quasar_data/HE2217-2818_flux.dat"
w12, f12 = np.loadtxt(file12, skiprows=1, usecols=(0,1), unpack = True)
file13 = "quasar_data/HE2243-6031_flux.dat"
w13, f13 = np.loadtxt(file13, skiprows=1, usecols=(0,1), unpack = True)
file14 = "quasar_data/HE2347-4342_flux.dat"
w14, f14 = np.loadtxt(file14, skiprows=1, usecols=(0,1), unpack = True)
file15 = "quasar_data/HS1140+2711_flux.dat"
w15, f15 = np.loadtxt(file15, skiprows=1, usecols=(0,1), unpack = True)
file16 = "quasar_data/PKS0237-23_flux.dat"
w16, f16 = np.loadtxt(file16, skiprows=1, usecols=(0,1), unpack = True)
file17 = "quasar_data/Q0002-422_flux.dat"
w17, f17 = np.loadtxt(file17, skiprows=1, usecols=(0,1), unpack = True)
file18 = "quasar_data/Q0055-269_flux.dat"
w18, f18 = np.loadtxt(file18, skiprows=1, usecols=(0,1), unpack = True)
file19 = "quasar_data/Q0109-3518_flux.dat"
w19, f19 = np.loadtxt(file19, skiprows=1, usecols=(0,1), unpack = True)
file20 = "quasar_data/Q0122-380_flux.dat"
w20, f20 = np.loadtxt(file20, skiprows=1, usecols=(0,1), unpack = True)
file21 = "quasar_data/Q0216+08_flux.dat"
w21, f21 = np.loadtxt(file21, skiprows=1, usecols=(0,1), unpack = True)
file22 = "quasar_data/Q0329-385_flux.dat"
w22, f22 = np.loadtxt(file22, skiprows=1, usecols=(0,1), unpack = True)
file23 = "quasar_data/Q0347-3819_flux.dat"
w23, f23 = np.loadtxt(file23, skiprows=1, usecols=(0,1), unpack = True)
file24 = "quasar_data/Q0420-388_flux.dat"
w24, f24 = np.loadtxt(file24, skiprows=1, usecols=(0,1), unpack = True)
file25 = "quasar_data/Q0453-423_flux.dat"
w25, f25 = np.loadtxt(file25, skiprows=1, usecols=(0,1), unpack = True)
file26 = "quasar_data/Q0913+0715_flux.dat"
w26, f26 = np.loadtxt(file26, skiprows=1, usecols=(0,1), unpack = True)
file27 = "quasar_data/Q1151+068_flux.dat"
w27, f27 = np.loadtxt(file27, skiprows=1, usecols=(0,1), unpack = True)
file28 = "quasar_data/Q1209+0919_flux.dat"
w28, f28 = np.loadtxt(file28, skiprows=1, usecols=(0,1), unpack = True)
file29 = "quasar_data/Q1223+178_flux.dat"
w29, f29 = np.loadtxt(file29, skiprows=1, usecols=(0,1), unpack = True)
file30 = "quasar_data/Q1232+0815_flux.dat"
w30, f30 = np.loadtxt(file30, skiprows=1, usecols=(0,1), unpack = True)
file31 = "quasar_data/Q1249-0159_flux.dat"
w31, f31 = np.loadtxt(file31, skiprows=1, usecols=(0,1), unpack = True)
file32 = "quasar_data/Q1317-0507_flux.dat"
w32, f32 = np.loadtxt(file32, skiprows=1, usecols=(0,1), unpack = True)
file33 = "quasar_data/Q1409+095_flux.dat"
w33, f33 = np.loadtxt(file33, skiprows=1, usecols=(0,1), unpack = True)
file34 = "quasar_data/Q1451-15_flux.dat"
w34, f34 = np.loadtxt(file34, skiprows=1, usecols=(0,1), unpack = True)
file35 = "quasar_data/Q1621-0042_flux.dat"
w35, f35 = np.loadtxt(file35, skiprows=1, usecols=(0,1), unpack = True)
file36 = "quasar_data/Q2139-4434_flux.dat"
w36, f36 = np.loadtxt(file36, skiprows=1, usecols=(0,1), unpack = True)
file37 = "quasar_data/Q2206-1958_flux.dat"
w37, f37 = np.loadtxt(file37, skiprows=1, usecols=(0,1), unpack = True)

###############################################################
###	Create the tuple of (x,y) arrays to be plotted:	    ###

plots = [(w1,f1), (w2,f2), (w3,f3), (w4,f4), (w5,f5), (w6,f6), (w7,f7), (w8,f8), (w9,f9), (w10,f10), (w11,f11), (w12,f12), (w13,f13), (w14,f14), (w15,f15), (w16,f16), (w17,f17), (w18,f18), (w19,f19), (w20,f20), (w21,f21), (w22,f22), (w23,f23), (w24,f24), (w25,f25), (w26,f26), (w27,f27), (w28,f28), (w29,f29), (w30,f30), (w31,f31), (w32,f32), (w33,f33), (w34,f34), (w35,f35), (w36,f36), (w37,f37)]

curr_pos = 0

#This next bit of code allows the user to scroll back and forth using the right and left arrow keys between plots in the matplotlib window. While in this window, scrolling over the plot with their cursor will display the x and y value they are hovering over in the lower left:

def key_event(e):
	global curr_pos

	if e.key == "right":
		curr_pos = curr_pos + 1
	elif e.key == "left":
		curr_pos = curr_pos - 1
	else:
		return
		curr_pos = curr_pos % len(plots)

	ax.cla()
	ax.plot(plots[curr_pos][0], plots[curr_pos][1])
	fig.canvas.draw()

#Now we create a simple wavelength vs. flux plot:

fig = plt.figure()
fig.canvas.mpl_connect('key_press_event', key_event)
ax = fig.add_subplot(111)
ax.set_xlabel('Wavelength (Angstroms)')
ax.set_ylabel('Flux')
ax.plot(w1, f1)
plt.show()
