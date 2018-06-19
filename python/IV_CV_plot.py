#!usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
#import pylab as plb
import string



#color_list = ['#fff400','g','#FFA500','#47005a','b','#a2c8a2','#da251c','#40b0b5', '#d3ffce', '#83859a', '#156029', 'k']
fig = plt.figure()
ax = fig.add_subplot(111)
plt.ylabel('1/C$^2$ [1/F$^2$]')
#plt.ylabel('Current (A)')
plt.xlabel('Voltage [V]')
#labels=['Pure', 'Impure', 'Impure_guard']
count = 0

lines_type = ['-','--','-.']

labels = []



file_in = ["/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/redo_24Aug2017/Sensor_31_CV_2",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/redo_24Aug2017/Sensor_32_CV_2",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/redo_24Aug2017/Sensor_33_CV_2",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/9Aug2017/Sensor_34_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/9Aug2017/Sensor_35_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/9Aug2017/Sensor_36_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/9Aug2017/Sensor_37_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/9Aug2017/Sensor_38_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/10Aug2017/Sensor_39_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/10Aug2017/Sensor_40_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/10Aug2017/Sensor_41_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/redo_24Aug2017/Sensor_42_CV_2",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/redo_25Aug2017/Sensor_43_CV_2",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/11Aug2017/Sensor_44_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/21Aug2017/Sensor_45_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/21Aug2017/Sensor_46_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/21Aug2017/Sensor_47_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/22Aug2017/Sensor_48_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/22Aug2017/Sensor_49_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/22Aug2017/Sensor_50_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/22Aug2017/Sensor_51_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/22Aug2017/Sensor_52_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/23Aug2017/Sensor_53_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/23Aug2017/Sensor_54_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/23Aug2017/Sensor_55_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/23Aug2017/Sensor_56_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/23Aug2017/Sensor_57_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/24Aug2017/Sensor_58_CV_1",
"/afs/desy.de/group/flc/pool/tpc/share/External_Tracker/ProbeStation/24Aug2017/Sensor_59_CV_1"]


print file_in[0].find("Sensor")


for x in file_in:
	labels.append(x[x.find("Sensor"):x.find("_CV_")])
	print x[x.find("Sensor"):x.find("_CV_")]
	with open(x) as r_file:
		start = False
		x = []
		y = []
		for line in r_file:
			if ("BEGIN" in line):
				start = True
				r_file.next()
				continue
			if (start is True) and not ("END" in line):
				line_split = str(line).split( )
				x.append(float(line_split[0]))
				y.append(1/np.power(float(line_split[2]),2))
	#ax.set_yscale('log')
	#ax.set_xscale('log')
	#plt.errorbar(x,y, linestyle='ro', label=labels[count], linewidth=3, markersize=4)
	
	#plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
	plt.plot(x,y, linestyle=lines_type[count%3], label=labels[count])
	count = count + 1
print labels
plt.legend(loc = 4, ncol = 5, fontsize=8.5)
Name_of_File = 'All_sensors_CV.pdf'
Folder = "./"
print "Saving file as: ", Folder+Name_of_File
plt.savefig(Folder+Name_of_File, dpi = 500)	



