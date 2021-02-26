#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import constants
import math




data = np.loadtxt("kompassi.txt")
I = data[:, 0]*10**(-3) #yksikkö = A
kulma = data[:, 1] # yksikkö = aste

Ierr = 1*10**(-3) #yksikkö = A
kerr = 2 #yksikkö = aste


 
#Kelojen aiheuttama magneettikenttälista
N = 500
R = 10.0*10**(-2) #yksikkö = m
Rerr = 0.5*10**(-2) #yksikkö = m


B_kela = []

for i in range(len(I)):
    b = (8*N*constants.mu_0*I[i])/(np.sqrt(125)*R)
    B_kela = np.append(B_kela, b, axis=None)




#Maan magneettikentän määritys
 
B_maa = []

for i in range(len(B_kela)):
    y  =  B_kela[i]/(math.tan(math.radians(kulma[i])))
    B_maa = np.append(B_maa, y, axis = None)

B_maa_std = np.std(B_maa)


#Virheen arviointia

#Osittaisderivaattahomma, virheen kasautuminen

def df(Is, Rs, theta):
    dI_p = (8*N*constants.mu_0)/(np.sqrt(125)*Rs)*1*Ierr 
    dR_p = -(8*N*constants.mu_0*Is)/(np.sqrt(125)*Rs**2)*1*Rerr
    dtheta_p = -(8*N*constants.mu_0*Is)/(np.sqrt(125)*Rs)*1*math.radians(kerr)
    d = math.sqrt((dI_p)**2 + (dR_p)**2 + (dtheta_p)**2)
    return d

dB = []

for i in range(len(B_maa)):
    x = df(I[i], R, kulma[i])
    dB = np.append(dB, x, axis = None)



    
#kuvaajat
fig1, ax = plt.subplots(2, 1, figsize = [20,20])


ax[0].errorbar(kulma, B_maa, xerr = kerr, yerr = dB, fmt = "o", color = "blue", label = "Virherajat")


ax[0].set_title("Magneettikenttä sähkövirran funktiona")

ax[0].plot(kulma, B_maa, ".", color = "blue", label = "B_maa")
ax[0].set_xlabel("Kulma (aste)")
ax[0].set_ylabel("Maan magneettikentän \n vaakasuorakomponentti (T)")
ax[0].grid()
ax[0].legend()




ax[1].set_title("Magneettikenttä sähkövirran funktiona")

ax[1].errorbar(I, B_maa, xerr = Ierr, yerr = dB, fmt = "o", color = "blue", label = "Virherajat")
ax[1].plot(I, B_maa, ".", color = "blue", label = "B_maa")
ax[1].set_xlabel("Virta (A)")
ax[1].set_ylabel("Maan magneettikentän \n vaakasuorakomponentti (T)")
ax[1].grid()
ax[1].legend()

print("Maan magneettikentän vaakasuorakomponentti: " + str(np.mean(B_maa)))
print("Keskihajonta: " + str(np.std(B_maa)))


plt.show()

fig1.tight_layout()

fig1.savefig("labra3.3.png")


# In[ ]:




