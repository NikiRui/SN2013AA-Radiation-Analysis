# -*- coding: utf-8 -*-
import os, sys, subprocess
import pyfits
import matplotlib.pyplot as plt
import numpy as np
from pylab import*

#B_StarX=12.42
#V_StarX=11.78
#g = V + 0.64*(B-V) - 0.13
#r = V - 0.46*(B-V) - 0.11

#cat_path_gp = '/transit/results_ChangXu/Project/match_gp/'
#image_path_gp = '/transit/results_ChangXu/Project/sn2013aa_gp/'

image_path_gp = 'C:/Users/Chang/OneDrive/02. Courses/14. Senior Spring/04. PHYS 134L/04. Final/sn2013aa_gp/'
cat_path_gp = 'C:/Users/Chang/OneDrive/02. Courses/14. Senior Spring/04. PHYS 134L/04. Final/match_gp/'

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

'''#Nicle
sec_JD=2457176.500012-2457176.500000
image_time_gp=np.asarray(image_time_list_gp)
image_time'''
    
#DISTANCE
magavg_gp = np.average(starcal_gp)
k_gp = 12.0596 - magavg_gp
sn2013aa_gpf = k_gp + sn2013aa_gp
peakmag_gp = np.min(sn2013aa_gpf)
sn_peak = -19.3
m_gp = peakmag_gp - sn_peak
distance_gp = 10**((m_gp+5)/5)
print distance_gp

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

#cat_path_rp = '/transit/results_ChangXu/Project/match_rp/'
#image_path_rp = '/transit/results_ChangXu/Project/sn2013aa_rp/'

image_path_rp = 'C:/Users/Chang/OneDrive/02. Courses/14. Senior Spring/04. PHYS 134L/04. Final/sn2013aa_rp/'
cat_path_rp = 'C:/Users/Chang/OneDrive/02. Courses/14. Senior Spring/04. PHYS 134L/04. Final/match_rp/'

cat_list_rp = []
for root, dirs, files in os.walk(cat_path_rp):
    for filename in files:
        if filename.endswith('.cat'):
            cat_list_rp.append(root+filename)

image_list_rp = []
for root, dirs, files in os.walk(image_path_rp):
    for filename in files:
        if filename.endswith('.fits'):
            image_list_rp.append(root+filename)
    #print 'scanning   '+filename

sn2013aa_rp=[]
image_time_list_rp=[]
starcal_rp=[]
for cat_location_rp in cat_list_rp:
    data=np.loadtxt(cat_location_rp)
    x=data[:,0]
    mag0=data[:,4]
    mag=data[:,16]
    R=[]
    R0=[]
    index=cat_list_rp.index(cat_location_rp)
    for j in range(len(x)):
	if (x[j] == 310.943):
            R.append(mag[j])
	    R0.append(mag0[j])
        if (x[j] == 248.370):       
            R.append(mag[j])
            R0.append(mag0[j])
	if (x[j] == 991.235):       
            R.append(mag[j])
            R0.append(mag0[j])
	if (x[j] == 1216.592):       
            R.append(mag[j])
            R0.append(mag0[j])
    for k in range(len(x)):
        if (x[k] == 1050.126):
            if len(R) != 0:
                sn2013aa_rp.append(mag[k]*sum(R0)/sum(R))
   		image=pyfits.open(cat_location_rp.replace(cat_path_rp,image_path_rp).replace('lsc1m004_kb77_20130222_PSNJ143233_rp_l','l').replace('_matched.cat','.fits'))
		date_str = image[0].header['MJD-OBS']
		image_time_list_rp.append(date_str)
	if (x[k] == 1225.836):
	    if len(R) !=0:
                starcal_ip.append(mag[k]*sum(R0)/sum(R))
    print 'rp plot complete   ', np.int(index), '/75'

#DISTANCE
magavg_rp = np.average(starcal_rp)
k_rp = 11.6384 - magavg_rp
sn2013aa_rpf = k_rp + sn2013aa_rp
peakmag_rp = np.min(sn2013aa_rpf)
sn_peak = -19.3
m_rp = peakmag_rp - sn_peak
distance_rp = 10**((m_rp+5)/5)
print distance_rp


plt.plot(image_time_list_gp,sn2013aa_gpf,'bo')
plt.plot(image_time_list_ip,sn2013aa_ipf,'ro')
plt.plot(image_time_list_rp,sn2013aa_rpf,'yo')
#plt.ylim(17,11)
#plt.xlim(56534.26,56370.31)
#plt.savefig('plottest2.pdf')
plt.show()