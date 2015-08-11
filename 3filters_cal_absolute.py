import os, sys, subprocess
import pyfits
import matplotlib.pyplot as plt
import numpy as np
from pylab import*
cat_path_gp = '/transit/results_ChangXu/Project/match_gp/'
image_path_gp = '/transit/results_ChangXu/Project/sn2013aa_gp/'

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
        if (x[j] == 1709.715):       
            R.append(mag[j])
            R0.append(mag0[j])
    for k in range(len(x)):
	    if (x[k] == 1050.443):
		if len(R) != 0:
		    sn2013aa_gp.append(mag[k]*sum(R0)/sum(R))
   		    image=pyfits.open(cat_location_gp.replace(cat_path_gp,image_path_gp).replace('lsc1m004_kb77_20130221_PSNJ143233_gp_l','l').replace('_matched.cat','.fits'))
		    date_str = image[0].header['MJD-OBS']
		    image_time_list_gp.append(date_str)
    print 'gp plot complete   ', np.int(index), '/80'

z=19.3+np.min(sn2013aa_gp)
sn2013aa_gp-=z

cat_path_ip = '/transit/results_ChangXu/Project/match_ip/'
image_path_ip = '/transit/results_ChangXu/Project/sn2013aa_ip/'

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

    print 'ip plot complete   ', np.int(index), '/65'

z=19.3+np.min(sn2013aa_ip)
sn2013aa_ip-=z

cat_path_rp = '/transit/results_ChangXu/Project/match_rp/'
image_path_rp = '/transit/results_ChangXu/Project/sn2013aa_rp/'

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
    print 'rp plot complete   ', np.int(index), '/75'

z=19.3+np.min(sn2013aa_rp)
sn2013aa_rp-=z

plt.plot(image_time_list_gp,sn2013aa_gp,'bo')
plt.plot(image_time_list_ip,sn2013aa_ip,'ro')
plt.plot(image_time_list_rp,sn2013aa_rp,'yo')
plt.ylim(-13,-19.5)
#plt.xlim(56534.26,56370.31)
#plt.savefig('plottest2.pdf')
plt.show()
