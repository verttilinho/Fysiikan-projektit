'''
KUVAUS

Tässä analysoidaan pienhiukkasten muodostumiseen liittyvien
laboratoriokokeiden tuloksia.
'''

# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 00:09:50 2020

@author: Vertti
"""
import numpy as np
import matplotlib.pyplot as plt

datat = np.loadtxt("measurement_data.dat")

t = datat[:,0]
h = datat[:,1]
s = datat[:,2]
rh = datat[:,3]
oy = datat[:,4]


def liukuva_keskiarvo(data, n):
    
    avg = np.array([])
    
    for i in range(len(data)):
       
        if i - (n-1)/2 < 0:
            #laske (data[0]...data[i]...data[i+(n-1)/2])/n
            summa  = 0
            
            for m in range(int(n-((n-1)/2-i))):
            
                
                summa += data[m]
                mean = summa/(n-((n-1)/2-i))
            avg = np.append(avg, mean)
            
            
            
    
        elif i + (n-1)/2 > len(data)-1:
            #laske (data[i+(n-1)/2]...data[i]...data[-1])/n
            summa  = 0
            
            for m in range(int((n-1)/2-i+len(data))):
    
                
                summa += data[-(m+1)]
                mean = summa/((n-1)/2-i+len(data))
            avg = np.append(avg, mean) 
             
            
            
        else:
            #laske (data[i-(n-1)/2]...data[i]...data[i+(n-1)/2])/n
            summa = 0
            
            for m in range(n):
        
                summa += data[int(i - (n-1)/2 + m)] 
                mean = summa/n
            avg = np.append(avg, mean) 
            
    return avg

def derivaatta(x, y):
    a = np.nan
    der = np.array([a])
    
    for i in range(1,len(x)-1):
        
        d = (y[i+1]-y[i-1])/(x[i+1]-x[i-1])
        der = np.append(der, d)
    
    der = np.append(der, a)
    return der


#Liukuvat keskiarvot hiukkaspitoisuus, rikkihappo, orgyhdiste    
lka_h = liukuva_keskiarvo(h, 5)
lka_rh = liukuva_keskiarvo(rh, 5)
lka_oy = liukuva_keskiarvo(oy, 5)


#KUVAAJIA

fig1, ax = plt.subplots(3, 1, figsize = [12, 10])


ax[0].set_xlim(0, 120)
ax[0].semilogy(t, lka_h)
ax[0].set_title("Keskiarvoistettu pienhiukkaspitoisuus ajan funktiona")
ax[0].set_xlabel("Aika (h)")
ax[0].set_ylabel("Keskiarvoistettu pienhiukkaspitoisuus \n hiukkasta/(cm^3))")

ax[1].set_xlim(0, 120)
ax[1].semilogy(t, lka_rh)
ax[1].set_title("Keskiarvoistettu rikkihappopitoisuus ajan funktiona")
ax[1].set_xlabel("aika (h)")
ax[1].set_ylabel("Keskiarvoistettu rikkihappopitoisuus \n hiukkasta/(cm^3))")

ax[2].set_xlim(0, 120)
ax[2].semilogy(t, lka_oy)
ax[2].set_title("Keskiarvoistettu orgaanisten yhdisteidenpitoisuus ajan funktiona")
ax[2].set_xlabel("aika (h)")
ax[2].set_ylabel("Keskiarvoistettu orgaanisten yhdisteidenpitoisuus \n hiukkasta/(cm^3))")

fig1.tight_layout()

fig1.savefig("kuva1.png")


fig2, bx = plt.subplots(figsize =  [12, 8])

bx.set_xlim(75, 78)
bx.semilogy(t, h, label = "Pienhiukkaspitoisuus")
bx.semilogy(t, lka_h, label = "5-pisteen liukuva keskiarvo pienhiukkaspitoisuudelle")
bx.set_xlabel("Aika (h)")
bx.set_ylabel("1/(cm^3)")
bx.legend()

fig2.savefig("kuva2.png")


#aika sekunneiks
t_s = t*3600


#Muodostumisnopeus
j = derivaatta(t_s,h) + s

#LISÄÄ KUVAAJIA
fig3, cx = plt.subplots(figsize =  [12, 8])


cx.loglog(rh, j, "b.", markersize = 8 )
cx.set_xlabel("Rikkihappopitoisuus \n(hiukkasta/cm^3)")
cx.set_ylabel("Muodostumisnopeus \n(hiukkasta/cm^3/s)")

fig3.savefig("kuva3.png")

fig4, dx = plt.subplots(figsize =  [12, 8])


dx.loglog(oy, j,"b.", markersize = 8)
dx.set_xlabel("Orgaanistenyhdisteiden pitoisuus \n(hiukkasta/cm^3)")
dx.set_ylabel("Muodostumisnopeus \n(hiukkasta/cm^3/s)")

fig4.savefig("kuva4.png")

tulo = rh*oy

fig5, ex = plt.subplots(figsize =  [12, 8])

ex.loglog(tulo, j,"b.", markersize = 8)
ex.set_xlabel("Orgaanistenyhdisteiden*rikkihapon pitoisuus (1/cm^3)")
ex.set_ylabel("Muodostumisnopeus \n(1/cm^3/s)")

fig5.savefig("kuva5.png")




#VAKAA-TILA OSUUS

vakaa_tila = np.loadtxt("experiment_steady.dat")

start = vakaa_tila[:,0]
end = vakaa_tila[:,1]


#VAKAAAT LISTAT

meansrh = np.array([])
meansoy = np.array([])
meansj = np.array([])


#tarkista, mitkä listan t arvoista ovat välillä  start[i] <= t <= end[i] ja sit lisää vakaille listoille
for i in range(len(start)):
    
    v_j = np.array([]) 
    v_rh = np.array([])
    v_oy = np.array([])
    
    for m in range(len(t)):
         if  t[m] >= start[i] and t[m] <= end[i]:
            
             v_rh = np.append(v_rh, rh[m])
             v_oy = np.append(v_oy, oy[m])
             v_j = np.append(v_j, j[m])
             
    meansrh = np.append(meansrh,np.array([np.nanmean(v_rh)]))
    meansoy = np.append(meansoy,np.array([np.nanmean(v_oy)]))
    meansj = np.append(meansj,np.array([np.nanmean(v_j)]))


fig6 = plt.figure(figsize=(12,8))

x = np.log10(meansrh*meansoy)
y = np.log10(meansj)
params = np.polyfit(x, y, 1)

xx = np.logspace(np.min(x), np.max(x), 50)
yy = 10**params[1] * xx**params[0]
plt.plot(xx, yy, label = "Sovitettu suora")
plt.loglog(meansrh*meansoy, meansj, ".", markersize = 8 ,label = "Steady-state -arvojen keskiarvot") 
plt.ylabel("Hiukkasten muodostumisnopeus \n (1/cm^3/s)")
plt.xlabel("Rikkihappopitoisuus*orgaanisten yhdisteiden pitoisuus \n 1/cm^3")
plt.title("Hiukkasten muodostumisnopeus C10*H2SO4:n suhteen steady-state -hetkillä")
plt.legend()


fig6.savefig("kuva6.png")
