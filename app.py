import math
import numpy as np
from matplotlib.pyplot import *
import scipy.io.wavfile as wave
from numpy.fft import fft


rate,data = wave.read('salam.wav')
n = data.size
duree = 1.0*n/rate


print(rate)

print(duree)


te = 1.0/rate
t = np.zeros(n)
for k in range(n):
    t[k] = te*k
figure(figsize=(12,4))
plot(t,data)
xlabel("t (s)")
ylabel("amplitude") 
axis([0,0.1,data.min(),data.max()])
grid()
			
   
   
def tracerSpectre(data,rate,debut,duree):
    start = int(debut*rate)
    stop = int((debut+duree)*rate)
    spectre = np.absolute(fft(data[start:stop]))
    spectre = spectre/spectre.max()
    n = spectre.size
    freq = np.zeros(n)
    for k in range(n):
        freq[k] = 1.0/n*rate*k
    vlines(freq,[0],spectre,'r')
    xlabel('f (Hz)')
    ylabel('A')
    axis([0,0.5*rate,0,1])
    grid()
			
figure(figsize=(12,4))
tracerSpectre(data,rate,0.0,0.5)
axis([0,5000,0,1])
