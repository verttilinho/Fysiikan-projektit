#!/usr/bin/env python
# coding: utf-8

# In[2]:


'''
Tämän koodin tarkoitus on määrittää pienin mahdollinen lähtönopeus, joka raketilla voi olla,
jonka avulla se pääsee kuuhun. Koodi määrittää siis numeerisesti halutin lähtönopeuden approksimoimalla
rakettiin kohdistuvan gravitaatiovoiman vakioksi aikavälillä dt. Tehtävä oli ryhmätyö, joten simuloinnin perusidea on laadittu ryhmässä.
Koodi on muuten minun tekemäni, mutta koodiin ollaan lisätty opiskelija toverini laatima haarukointi -menetelmä. 
Kyseinen menetelmä ajaa simulaation monilla eri nopeuksilla ja rajaa lähtönopeuden haluttuun tarkkuuteen.
'''


import numpy as np
import matplotlib.pyplot as pl



def raketti(dt):
    print("Aika-askel: ", dt, "s")
    t = 0.0  # t=0, ensimmäinen piste
    G =  6.674*10**(-11) #Gravitaatiovakio
    M =  5.794*10**24 #kg
    Mk = 7.342*10**22 #kg
    R = 384400.0*10**3 #maan ja kuun välinen etäisyys (m)

#Toisen opiskelijan tekemä osa1 alkaa    
    vMin = 1.0
    vMax = 20000.0
    vL = vMin + (vMax-vMin)/2


    tarkkuus = 10

    while True:
        
        paasi = True
#Toisen opiskelijan tekemä osa1 päättyy

        v = vL

        t = 0.0 
        r = 6371.0*10**3+500.0*10**3 #metriä, lähtökorkeus (t=0) #Lähtökorkeus mitattuna maankeskipisteestä
        rk = 1737.4*10**3 #metriä (kuun säde)

        tt = np.array([t]) #ensimmäiset datapisteet
        rt = np.array([r])
        vt = np.array([v])
        

        while r < 384400.0*10**3-rk-100*10**3: #Raketin kulkema kokonaismatka
                    
            #Lasketaan kiihtyvyys etäisyydellä r (Maasta)
            a = -G*M/(r**2)  + G*Mk/((R-r)**2)  
            vavg = (2*v + a*dt)/2 #v=v0+at
            ru = r + vavg*dt #paikan päivitys
            
#Toisen opiskelijan tekemä osa2 alkaa            
            if ru < r: #Jos ei paase perille, muokataan haarukkaa ylospain ja aloitetaan alusta
                vMin = vL
                vL = vL+(vMax-vL)/2
                paasi = False
                break
#Toisen opiskelijan tekemä osa2 päättyy

            r = ru  #paikan päivitys  
            t = t + dt #ajan päivitys
            v =  v + a*dt #nopeuden päivitys
            
            #Tallennetaan aika, paikka ja nopeus listoihin
            tt = np.append(tt,t)
            rt = np.append(rt, ru)
            vt = np.append(vt, v)

#Toisen opiskelijan tekemä osa3 päättyy            
        if paasi: # Jos paasi perille, muokataan haarukkaa alaspain
          

            vMax = vL
            vL = vMin + (vL-vMin)/2

            if vMax-vMin < tarkkuus: #Kun haarukka on pienempi kuin annettu tarkkuus
                break
#Toisen opiskelijan tekemä osa3 päättyy
                
    return tt,rt, vt

t1, r1, v1 = raketti(10)  #aika-askel

print(f"Lähtönopeus:{v1[0]:{10}.{7}}" + " m/s")
print("Kulunut aika: " + str(t1[-1]) + " s")
            
#tekee kuvaajat

fig1, ax = pl.subplots(3, 1, figsize = [12, 10])

ax[0].plot(t1, r1)
ax[0].set_title('Raketin paikan kuvaaja ajan funktiona')
ax[0].set_xlabel('t (s)')
ax[0].set_ylabel('r (m)')
ax[0].grid()

ax[1].plot(r1, v1)
ax[1].set_title('Raketin nopeuden kuvaaja paikan funktiona')
ax[1].set_xlabel('r (m)')
ax[1].set_ylabel('v (m/s)')
ax[1].grid()

ax[2].plot(t1, v1)
ax[2].set_title('Raketin nopeuden kuvaaja ajan funktiona')
ax[2].set_xlabel('t (s)')
ax[2].set_ylabel('v (m/s)')
ax[2].grid()

fig1.tight_layout()

pl.show()


# In[ ]:




