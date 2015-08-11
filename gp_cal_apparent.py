import os, sys, subprocess
import pyfits
import matplotlib.pyplot as plt
import numpy as np
from pylab import*

cat_path_gp = '/transit/results_ChangXu/Project/match_gp/'
image_path_gp = '/transit/results_ChangXu/Project/sn2013aa_gp/'

#image_path_gp = 'C:/Users/Chang/OneDrive/02. Courses/14. Senior Spring/04. PHYS 134L/04. Final/sn2013aa_gp/'
#cat_path_gp = 'C:/Users/Chang/OneDrive/02. Courses/14. Senior Spring/04. PHYS 134L/04. Final/match_gp/'

cat_list_gp = []
for root, dirs, files in os.walk(cat_path_gp):
    for filename in files:
        if filename.endswith('.cat'):
            cat_list_gp.append(root+filename)

image_list_gp = []
for root, dirs, files in os.walk(image_path_gp):
    for filename in files:
        if filename.endswith('.fits'):
            image_list_gp.append(root+filename)
    #print 'scanning   '+filename

starcal_gp=[]
sn2013aa_gp=[]
image_time_list_gp=[]
for cat_location_gp in cat_list_gp:
    data=np.loadtxt(cat_location_gp)
    x=data[:,0]
    mag0=data[:,4]
    mag=data[:,16]
    R=[]
    R0=[]
    index=cat_list_gp.index(cat_location_gp)
    for j in range(len(x)):
	if (x[j] == 1550.303):
            R.append(mag[j])
	    R0.append(mag0[j])
        if (x[j] == 1949.537):
            R.append(mag[j])
	    R0.append(mag0[j])
        if (x[j] == 1709.240):       
            R.append(mag[j])
            R0.append(mag0[j])
        if (x[j] == 1401.570):
            R.append(mag[j])
	    R0.append(mag0[j])
        if (x[j] == 742.968):
            R.append(mag[j])
	    R0.append(mag0[j])
	if (x[j] == 1167.955):
            R.append(mag[j])
	    R0.append(mag0[j])
	if (x[j] == 666.131):
            R.append(mag[j])
	    R0.append(mag0[j])
	if (x[j] == 860.731):
            R.append(mag[j])
	    R0.append(mag0[j])
	if (x[j] == 1189.508):
            R.append(mag[j])
	    R0.append(mag0[j])
    for k in range(len(x)):
	    if (x[k] == 1050.443):
		if len(R) != 0:
		    sn2013aa_gp.append(mag[k]*sum(R0)/sum(R))
   		    image=pyfits.open(cat_location_gp.replace(cat_path_gp,image_path_gp).replace('lsc1m004_kb77_20130221_PSNJ143233_gp_l','l').replace('_matched.cat','.fits'))
		    date_str = image[0].header['MJD-OBS']
		    image_time_list_gp.append(date_str)
            if (x[k] == 1226.209):
                if len(R) !=0:
                    starcal_gp.append(mag[k]*sum(R0)/sum(R))
                    
    print 'gp plot complete   ', np.int(index), '/80'

#DISTANCE
magavg_gp = np.average(starcal_gp)
k_gp = 12.0596 - magavg_gp
sn2013aa_gpf = k_gp + sn2013aa_gp
peakmag_gp = np.min(sn2013aa_gpf)
sn_peak = -19.3
m_gp = peakmag_gp - sn_peak
distance_gp = 10**((m_gp+5)/5)
print distance_gp

plt.plot(image_time_list_gp,sn2013aa_gpf,'bo')

#plt.ylim(17,11)
#plt.xlim(56534.26,56370.31)
#plt.savefig('plottest2.pdf')
plt.show()
