import os, sys, subprocess
import pyfits
import matplotlib.pyplot as plt
import numpy as np
from pylab import*

#cat_path_ip = '/transit/results_ChangXu/Project/match_ip/'
#image_path_ip = '/transit/results_ChangXu/Project/sn2013aa_ip/'

image_path_ip = 'C:/Users/Chang/OneDrive/02. Courses/14. Senior Spring/04. PHYS 134L/04. Final/sn2013aa_ip/'
cat_path_ip = 'C:/Users/Chang/OneDrive/02. Courses/14. Senior Spring/04. PHYS 134L/04. Final/match_ip/'

cat_list_ip = []
for root, dirs, files in os.walk(cat_path_ip):
    for filename in files:
        if filename.endswith('.cat'):
            cat_list_ip.append(root+filename)

image_list_ip = []
for root, dirs, files in os.walk(image_path_ip):
    for filename in files:
        if filename.endswith('.fits'):
            image_list_ip.append(root+filename)
    #print 'scanning   '+filename

sn2013aa_ip=[]
image_time_list_ip=[]
starcal_ip=[]
for cat_location_ip in cat_list_ip:
    data=np.loadtxt(cat_location_ip)
    x=data[:,0]
    mag0=data[:,4]
    mag=data[:,16]
    R=[]
    R0=[]
    index=cat_list_ip.index(cat_location_ip)
    for j in range(len(x)):
	if (x[j] == 755.004):
            R.append(mag[j])
	    R0.append(mag0[j])
	if (x[j] == 965.298):
            R.append(mag[j])
	    R0.append(mag0[j])
        if (x[j] == 922.838):       
            R.append(mag[j])
            R0.append(mag0[j])
    for k in range(len(x)):
	    if (x[k] == 1050.243):
		if len(R) != 0:
		    sn2013aa_ip.append(mag[k]*sum(R0)/sum(R))
   		    image=pyfits.open(cat_location_ip.replace(cat_path_ip,image_path_ip).replace('lsc1m004_kb77_20130219_PSNJ143233_ip_l','l').replace('_matched.cat','.fits'))
		    date_str = image[0].header['MJD-OBS']
		    image_time_list_ip.append(date_str)
	    if (x[k] == 1225.967):
	        if len(R) !=0:
                    starcal_ip.append(mag[k]*sum(R0)/sum(R))

    print 'ip plot complete   ', np.int(index), '/65'

#DISTANCE
magavg_ip = np.average(starcal_ip)
k_ip = 12.06 - magavg_ip
sn2013aa_ipf = k_ip + sn2013aa_ip
peakmag_ip = np.min(sn2013aa_ipf)
sn_peak = -19.3
m_ip = peakmag_ip - sn_peak
distance_ip = 10**((m_ip+5)/5)
print distance_ip

plt.plot(image_time_list_ip,sn2013aa_ipf,'ro')

#plt.ylim(17,11)
#plt.xlim(56534.26,56370.31)
#plt.savefig('plottest2.pdf')
plt.show()
