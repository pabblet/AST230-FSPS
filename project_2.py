import os
import fsps
import numpy as np
from astropy.io import ascii
import matplotlib.pyplot as plt
import time

inicio= time.time()

plt.style.use('ggplot')


sps_home= os.environ.get('SPS_HOME')
print('The environment SPS_HOME is in:', sps_home)

#SSP

#age (edad inicial t=0)
'''
sp= fsps.StellarPopulation(compute_vega_mags=False, zcontinuous=1, logzsol=0.0, sfh=0, imf_type=0, dust_type=2, dust2=0.2)
print('SSP calculated')

n=0
ages= ['1 [Gyr]', '5 [Gyr]', '9 [Gyr]', '13 [Gyr]']
color= ['#BD87BB', '#3ABB6F', '#D6234A', '#3A4ABB']
for i in range(1,14,4):
    wave, spec= sp.get_spectrum(tage=i, peraa=True)
    print('Spectrum {} calculated'.format(n+1))

    #Plot of the spectrum
    plt.plot(wave, spec, c=color[n], label=ages[n])
    plt.xlabel('log(Wavelength [$\AA$])')
    plt.ylabel('log(Flux [erg/s/cm$^{2}$/ $\AA$])')
    plt.title('Spectrum of SSP at different ages')
    plt.xscale('log')
    plt.yscale('log')
    plt.xlim(1e3, 1e4)
    plt.ylim(1e-8, 2e-4)
    plt.legend(loc='best')
    n+=1
plt.savefig('SSP_age', dpi=300)
plt.show()
'''

#metalicity (metalicidad inicial logzsol=0.5)
'''
sp= fsps.StellarPopulation(compute_vega_mags=False, zcontinuous=1, logzsol=0.5, sfh=0, imf_type=0, dust_type=2, dust2=0.2)
print('SSP calculated')

t=13.7 #si vemos diferentes metalicidades a diferentes edades encontramos relacion de edad metalicidad
metalicity= ['0.5 [$M/M_\odot$]', '0 [$M/M_\odot$]', '-0.5 [$M/M_\odot]$', '-1 [$M/M_\odot$]']
color= ['#BD87BB', '#3ABB6F', '#D6234A', '#3A4ABB']
for i in range(4):
    wave, spec= sp.get_spectrum(tage=t, peraa=True)
    print('Spectrum {} calculated'.format(i+1))
    #Plot of the spectrum
    plt.plot(wave, spec, c=color[i], label=metalicity[i])
    sp.params['logzsol']-=0.5
plt.xlabel('log(Wavelength [$\AA$])')
plt.ylabel('log(Flux [erg/s/cm$^{2}$/ $\AA$])')
plt.title('SED of SSP with different metalicities at {} [Gyr]'.format(t))
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e3, 1e4)
plt.ylim(5e-9, 4e-5)
plt.legend(loc='best')
plt.savefig('SSP_metalicity', dpi=300)
plt.show()
'''

#IMF (IMF inicial imf_type=0)
'''
sp= fsps.StellarPopulation(compute_vega_mags=False, zcontinuous=1, logzsol=0.0, sfh=0, imf_type=0, dust_type=2, dust2=0.2)
print('SSP calculated')

t=13.7
imf= ['Salpeter (1955)', 'Chabrier (2003)', 'Kroupa (2001)', 'van Dokkum (2008)', 'Dave (2008)']
color= ['#BD87BB', '#3ABB6F', '#D6234A', '#3A4ABB', '#E98425']
n=1.6
for i in range(5):
    wave, spec= sp.get_spectrum(tage=t, peraa=True)
    print('Spectrum {} calculated'.format(i+1))
    #Plot of the spectrum
    plt.plot(wave, spec, c=color[i], lw=n, label=imf[i])
    sp.params['imf_type']+=1
    n-=0.2
plt.xlabel('log(Wavelength [$\AA$])')
plt.ylabel('log(Flux [erg/s/cm$^{2}$/ $\AA$])')
plt.title('SED of SSP with different IMFs at {} [Gyr]'.format(t))
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e3, 1e4)
plt.ylim(1e-8, 4e-5)
plt.legend(loc='best')
plt.savefig('SSP_IMF', dpi=300)
plt.show()
'''

#Isochrones
'''
sp= fsps.StellarPopulation(compute_vega_mags=False, zcontinuous=1, logzsol=0.0, sfh=0, imf_type=0, dust_type=2, dust2=0.2)
print('SSP calculated')
sp.isochrones('isochrones_SSP')
print('Isochrones calculated')
'''
'''
iso= ascii.read('isochrones_SSP.cmd')
L= iso['col5']
T= iso['col6']

n=0
n5= 0
n6= 0
n7= 0
n8= 0
n9= 0
n10= 0
for i in iso['col1']:
    if float(str(i)[:5])==5.0:
        dots5= plt.scatter(T[n],L[n],c='#ed7cd0',s=0.4)
        n5+= 1
    elif float(str(i)[:5])==6.0:
        dots6= plt.scatter(T[n],L[n],c='#3ABB6F',s=0.4)
        n6+= 1
    elif float(str(i)[:5])==7.0:
        dots7= plt.scatter(T[n],L[n],c='#c24242',s=0.4)
        n7+= 1
    elif float(str(i)[:5])==8.0:
        dots8= plt.scatter(T[n],L[n],c='#5a6cd0',s=0.4)
        n8+= 1
    elif float(str(i)[:5])==9.0:
        dots9= plt.scatter(T[n],L[n],c='#e6962f',s=0.4)
        n9+= 1
    elif float(str(i)[:5])==10.0:
        dots10= plt.scatter(T[n],L[n],c='#71c4c3',s=0.4)
        n10+= 1
    if n5==1:
        dots5.set_label('5 [Gyr]')
    elif n6==1:
        dots6.set_label('6 [Gyr]')
    elif n7==1:
        dots7.set_label('7 [Gyr]')
    elif n8==1:
        dots8.set_label('8 [Gyr]')
    elif n9==1:
        dots9.set_label('9 [Gyr]')
    elif n10==1:
        dots10.set_label('10 [Gyr]')
    n+=1

plt.xlabel('log(Temperature [K])')
plt.ylabel('log(Luminosity [L$_\odot$])')
plt.title('SSP Isochrones')
plt.legend(loc='best')
plt.xlim(max(T), min(T))
plt.savefig('Isochrones SSP', dpi=300)
plt.show()
'''

#Dust
'''
sp= fsps.StellarPopulation(compute_vega_mags=False, zcontinuous=1, logzsol=0.0, sfh=0, imf_type=0, dust_type=2, dust2=0.0)
print('SSP calculated')

t=13.7
dust= ['No attenuation', 'dust2= 0.2', 'dust2= 0.4', 'dust2= 0.6']
color= ['#BD87BB', '#3ABB6F', '#D6234A', '#3A4ABB']
for i in range(4):
    wave, spec= sp.get_spectrum(tage=t, peraa=True)
    print('Spectrum {} calculated'.format(i+1))
    #Plot of the spectrum
    plt.plot(wave, spec, c=color[i], label=dust[i])
    sp.params['dust2']+=0.2
plt.xlabel('log(Wavelength [$\AA$])')
plt.ylabel('log(Flux [erg/s/cm$^{2}$/ $\AA$])')
plt.title('SED of SSP with Calzetti attenuation curve at {} [Gyr]'.format(t))
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e3, 1e4)
plt.ylim(5e-9, 4e-5)
plt.legend(loc='best')
plt.savefig('SSP_dust', dpi=300)
plt.show()
'''

#---------------------------------------------------------------------------------------------------------

#CSP

#age (edad inicial t=0)
'''
sp= fsps.StellarPopulation(compute_vega_mags=False, zcontinuous=1, logzsol=0.0, sfh=1, imf_type=2, dust_type=2, dust2=0.2)
print('CSP calculated')

n=0
ages= ['1 [Gyr]', '5 [Gyr]', '9 [Gyr]', '13 [Gyr]']
color= ['#BD87BB', '#3ABB6F', '#D6234A', '#3A4ABB']
for i in range(1,14,4):
    wave, spec= sp.get_spectrum(tage=i, peraa=True)
    print('Spectrum {} calculated'.format(n+1))

    #Plot of the spectrum
    plt.plot(wave, spec, c=color[n], label=ages[n])
    n+=1
plt.xlabel('log(Wavelength [$\AA$])')
plt.ylabel('log(Flux [erg/s/cm$^{2}$/ $\AA$])')
plt.title('Spectrum of CSP at different ages')
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e3, 1e4)
plt.ylim(1e-8, 7e-3)
plt.legend(loc='best')
plt.savefig('CSP_age', dpi=300)
plt.show()
'''

#metalicity (metalicidad inicial logzsol=0.5)
'''
sp= fsps.StellarPopulation(compute_vega_mags=False, zcontinuous=1, logzsol=0.5, sfh=1, imf_type=2, dust_type=2, dust2=0.2)
print('CSP calculated')

t=13.7 #si vemos diferentes metalicidades a diferentes edades encontramos relacion de edad metalicidad
metalicity= ['0.5 [$M/M_\odot$]', '0 [$M/M_\odot$]', '-0.5 [$M/M_\odot]$', '-1 [$M/M_\odot$]']
color= ['#BD87BB', '#3ABB6F', '#D6234A', '#3A4ABB']
for i in range(4):
    wave, spec= sp.get_spectrum(tage=t, peraa=True)
    print('Spectrum {} calculated'.format(i+1))
    #Plot of the spectrum
    plt.plot(wave, spec, c=color[i], label=metalicity[i])
    sp.params['logzsol']-=0.5
plt.xlabel('log(Wavelength [$\AA$])')
plt.ylabel('log(Flux [erg/s/cm$^{2}$/ $\AA$])')
plt.title('SED of CSP with different metalicities at {} [Gyr]'.format(t))
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e3, 1e4)
plt.ylim(1e-8, 7e-5)
plt.legend(loc='best')
plt.savefig('CSP_metalicity', dpi=300)
plt.show()
'''

#IMF (IMF inicial imf_type=0)
'''
sp= fsps.StellarPopulation(compute_vega_mags=False, zcontinuous=1, logzsol=0.0, sfh=1, imf_type=0, dust_type=2, dust2=0.2)
print('CSP calculated')

t=13.7
imf= ['Salpeter (1955)', 'Chabrier (2003)', 'Kroupa (2001)', 'van Dokkum (2008)', 'Dave (2008)']
color= ['#BD87BB', '#3ABB6F', '#D6234A', '#3A4ABB', '#E98425']
n=1.6
for i in range(5):
    wave, spec= sp.get_spectrum(tage=t, peraa=True)
    print('Spectrum {} calculated'.format(i+1))
    #Plot of the spectrum
    plt.plot(wave, spec, c=color[i], lw=n, label=imf[i])
    sp.params['imf_type']+=1
    n-=0.2
plt.xlabel('log(Wavelength [$\AA$])')
plt.ylabel('log(Flux [erg/s/cm$^{2}$/ $\AA$])')
plt.title('SED of CSP with different IMFs at {} [Gyr]'.format(t))
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e3, 1e4)
plt.ylim(1e-8, 4e-5)
plt.legend(loc='best')
plt.savefig('CSP_IMF', dpi=300)
plt.show()
'''

#Dust
'''
sp= fsps.StellarPopulation(compute_vega_mags=False, zcontinuous=1, logzsol=0.0, sfh=1, imf_type=2, dust_type=2, dust2=0.0)
print('CSP calculated')

t=13.7
dust= ['No attenuation', 'dust2= 0.2', 'dust2= 0.4', 'dust2= 0.6']
color= ['#BD87BB', '#3ABB6F', '#D6234A', '#3A4ABB']
for i in range(4):
    wave, spec= sp.get_spectrum(tage=t, peraa=True)
    print('Spectrum {} calculated'.format(i+1))
    #Plot of the spectrum
    plt.plot(wave, spec, c=color[i], label=dust[i])
    sp.params['dust2']+=0.2
plt.xlabel('log(Wavelength [$\AA$])')
plt.ylabel('log(Flux [erg/s/cm$^{2}$/ $\AA$])')
plt.title('SED of CSP with Calzetti attenuation curve at {} [Gyr]'.format(t))
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e3, 1e4)
plt.ylim(5e-9, 4e-5)
plt.legend(loc='best')
plt.savefig('CSP_dust', dpi=300)
plt.show()
'''

#SFH
'''
sp= fsps.StellarPopulation(compute_vega_mags=False, zcontinuous=1, logzsol=0.0, sfh=1, tau=1, imf_type=2, dust_type=2, dust2=0.2)
print('CSP calculated')

#Primero veamos sus espectros
t=13.7
tau= ['tau= 1', 'tau= 4', 'tau= 7', 'tau= 10']
color= ['#BD87BB', '#3ABB6F', '#D6234A', '#3A4ABB']
n=0
pos=[1, 4, 7, 10]
for i in pos:
    wave, spec= sp.get_spectrum(tage=t, peraa=True)
    print('Spectrum calculated')
    #Plot of the spectrum
    plt.plot(wave, spec, c=color[n], label=tau[n])
    sp.params['tau']+=3
    n+=1
plt.xlabel('log(Wavelength [$\AA$])')
plt.ylabel('log(Flux [erg/s/cm$^{2}$/ $\AA$])')
plt.title('SED of CSP with different tau values at {} [Gyr]'.format(t))
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e3, 1e4)
plt.ylim(1e-8, 4e-4)
plt.legend(loc='best')
plt.savefig('CSP tau Spectrum', dpi=300)
plt.show()

#Ahora veamos sus SFH
sp.params['tau']=1
n=0
for i in pos:
    wave, spec= sp.get_spectrum(tage=t, peraa=True)
    print('Spectrum calculated')
    #Plot of the spectrum
    ages= np.arange(0, t, step=0.05)
    sfr= np.flipud(sp.sfr_avg(ages))
    plt.plot(ages, sfr, c=color[n], label=tau[n])
    sp.params['tau']+=3
    n+=1
plt.xlabel('Look back time [Gyr]')
plt.ylabel('SFR [M$_\odot$\yr$^{-1}$]')
plt.title('SFH with different tau values')
plt.xlim(t, 0)
plt.legend(loc='best')
plt.savefig('SFH tau {} Gyr'.format(str(t)[0]), dpi=300)
plt.show()
'''

#---------------------------------------------------------------------------------------------------------

#Modelo consistente con un starburst
#Vamos a hacer un modelo con y sin starburst para poder compararlos
'''
sp= fsps.StellarPopulation(compute_vega_mags=False, zcontinuous=1, logzsol=0.0, sfh=1, tau=1, tburst=11, fburst=0, sf_start=9, imf_type=2, zred=0.0, dust_type=2, dust2=0.08, add_neb_emission=1)
print('CSP calculated')

t= 13.7 
wave1, spec1= sp.get_spectrum(tage=t, peraa=True)
print('Spectrum without burst calculated')
plt.plot(wave1, spec1, c='#4273ed', label='No burst')

ages1= np.arange(0, t, step=0.05)
sfr1= np.flipud(sp.sfr_avg(ages1))

sp.params['tburst']=13.5
sp.params['fburst']=0.04
wave2, spec2= sp.get_spectrum(tage=t, peraa=True)
print('Spectrum with burst calculated')
plt.plot(wave2, spec2, c='#e84f33', label='Burst at 5 [Gyr]')

ages2= np.arange(0, t, step=0.05)
sfr2= np.flipud(sp.sfr_avg(ages2))

#plt.axvline(x=4000, c='#d2b4de', label='4000 $\AA$-Break') #4000 A-Break
plt.xlabel('log(Wavelength [$\AA$])')
plt.ylabel('log(Flux [erg/s/cm$^{2}$/ $\AA$])')
plt.title('SED of Starburst Galaxy at {} [Gyr]'.format(t))
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e3, 1e4)
plt.ylim(5e-6, 3e-4)
plt.legend(loc='best')
plt.savefig('CSP burst {} Gyr'.format(str(t)[0]), dpi=300)
plt.show()

#SFH
plt.plot(ages1, sfr1, c='#4273ed', label='No burst')
plt.plot(ages2, sfr2, c='#e84f33', label='Burst at 5 [Gyr]', ls='--')

plt.xlabel('Look back time [Gyr]')
plt.ylabel('SFR [M$_\odot$\yr$^{-1}$]')
plt.title('SFH with and without burst')
plt.xlim(t, 0)
plt.legend(loc='best')
plt.savefig('SFH burst {} Gyr'.format(str(t)[0]), dpi=300)
plt.show()
'''

#Galaxia espiral
'''
sp= fsps.StellarPopulation(compute_vega_mags=False, zcontinuous=1, logzsol=0.0, sfh=1, imf_type=2, sf_start=1, tau=9, zred=0.0, dust_type=2, dust2=0.4)
print('CSP calculated')

t=13.7
wave, spec= sp.get_spectrum(tage=t, peraa=True)
print('Spectrum calculated')

sfr= sp.sfr
print('SFR:', sfr, '[Msun/yr]')
#Normalizados
dust= sp.dust_mass
print('Dust:', dust, '[Msun]')
mass= sp.formed_mass
print('Mass:', mass, '[Msun]')
stellar_m= sp.stellar_mass
print('Stellar mass:', stellar_m, '[Msun]')

plt.plot(wave, spec, c='#4273ed', label='Galaxia Espiral')

plt.xlabel('log(Wavelength [$\AA$])')
plt.ylabel('log(Flux [erg/s/cm$^{2}$/ $\AA$])')
plt.title('SED of an Spiral Galaxy at {} [Gyr]'.format(t))
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e3, 1e4)
plt.ylim(8e-6, 1e-4)
plt.savefig('Galaxia espiral', dpi=300)
plt.show()

#SFH
ages= np.arange(0, t, step=0.05)
sfr= np.flipud(sp.sfr_avg(ages))

plt.plot(ages, sfr, c='#444444')

plt.xlabel('Look back time [Gyr]')
plt.ylabel('SFR [M$_\odot$\yr$^{-1}$]')
plt.title('SFH of a Spiral Galaxy')
plt.xlim(t, 0)
plt.savefig('SFH Spiral {} Gyr'.format(str(t)[0]), dpi=300)
plt.show()
'''

#Galaxia eliptica
'''
sp= fsps.StellarPopulation(compute_vega_mags=False, zcontinuous=1, logzsol=0.5, sfh=1, imf_type=2, sf_start=1, tau=1, zred=0.0, dust_type=2, dust2=0.05)
print('CSP calculated')

t=13.7
wave, spec= sp.get_spectrum(tage=t, peraa=True)
print('Spectrum calculated')

sfr= sp.sfr
print('SFR:', sfr, '[Msun/yr]')
#Normalizados
dust= sp.dust_mass
print('Dust:', dust, '[Msun]')
mass= sp.formed_mass
print('Mass:', mass, '[Msun]')
stellar_m= sp.stellar_mass
print('Stellar mass:', stellar_m, '[Msun]')

plt.plot(wave, spec, c='#e84f33', label='Galaxia Elíptica')

plt.xlabel('log(Wavelength [$\AA$])')
plt.ylabel('log(Flux [erg/s/cm$^{2}$/ $\AA$])')
plt.title('SED of an Eliptical Galaxy at {} [Gyr]'.format(t))
plt.xscale('log')
plt.yscale('log')
plt.xlim(1e3, 1e4)
plt.ylim(5e-9, 3e-5)
plt.savefig('Galaxia eliptica', dpi=300)
plt.show()

#SFH
ages= np.arange(0, t, step=0.05)
sfr= np.flipud(sp.sfr_avg(ages))

plt.plot(ages, sfr, c='#444444')

plt.xlabel('Look back time [Gyr]')
plt.ylabel('SFR [M$_\odot$\yr$^{-1}$]')
plt.title('SFH of an Eliptical Galaxy')
plt.xlim(t, 0)
plt.savefig('SFH Eliptical {} Gyr'.format(str(t)[0]), dpi=300)
plt.show()
'''
fin= time.time()
print('Tiempo:', fin-inicio,'[s]')