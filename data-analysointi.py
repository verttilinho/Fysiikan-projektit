#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#datan lataus
data = pd.read_excel("data.xlsx")


#Poistaa Nan arvot
data = data[data["E1"].notna()]


#data.iloc[:0], ottaa ensimmäisen sarakkeen kaikki arvot
dat1 = data.iloc[:,2]
dat2 = data.iloc[:,3]
dat3 = data.iloc[:,4]
print(dat1)
print(dat2)

#mean, std
#keskiarvolista
dat_avg = [np.average(k) for k in zip(dat2, dat3)]

#Laskee saman alkion toistojen keskihajonnan
dat_std = [np.std(k) for k in zip(dat2, dat3)]

#keskiarvolistan keskiarvo
avg = np.mean(dat_avg)


#käyrän sovitus
sovitus = np.polyfit(dat1, dat_avg, 1)
poly = np.poly1d(sovitus)
X = np.linspace(0, 6, 1000)


#virhekäyrät

alaraja = []
for i in range(len(dat_avg)):
    y = dat_avg[i] - dat_std[i]
    alaraja.append(y)

yläraja = []

for i in range(len(dat_avg)):
    y = dat_avg[i] + dat_std[i]
    yläraja.append(y)

sovitus_a = np.polyfit(dat1, alaraja, 1)
poly_a = np.poly1d(sovitus_a)

sovitus_y = np.polyfit(dat1, yläraja, 1)
poly_y = np.poly1d(sovitus_y)



#kuvaajat luodaan subplot, koska tällöin kuvaajia on helppo tehdä lisää
fig1, ax = plt.subplots(1, 1, figsize = [6, 4])

ax.errorbar(dat1, dat_avg, yerr = dat_std, fmt = "o", label = "Virherajat")
ax.plot(X,  np.polyval(poly, X), label="Sovitettu käyrä")
ax.plot(X,  np.polyval(poly_y, X), color = "black", label="Yläraja")
ax.plot(X,  np.polyval(poly_a, X), color = "gray", label="Alaraja")
ax.set_title("Y x:n funktiona")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.grid()
ax.legend()
plt.show()

# In[ ]:





# In[ ]:




