import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0,1,1000)

A= 2
f= 9
phi = np.pi/4

x = A*np.sin(2*np.pi*f*t+phi)

plt.plot(t,x,'green', linewidth=2)
print("макс f = 9")
print(f"мин f дискретизации = {f*2}")

f_s = f*8


t2 = np.linspace(0,1, f_s, endpoint=False)
samles = A*np.sin(2*np.pi*f*t2+phi)
print(f"Количество отсчетов: {len(samles)}")
print("Массив отсчетов:", samles)
plt.show()
N= len(samles)

F = []

for k in range(N):
    summa = 0
    for n in range(N):
        summa += samles[n] * np.exp(-1j * 2 * np.pi * k * n / N)
    F.append(summa)
spectrum = [abs(val) for val in F]
freqs = list(range(N))

plt.stem(freqs, spectrum)
plt.title("Прямое преобразование Фурье (по формуле)")
plt.xlabel("Частота, Гц")
plt.ylabel("Амплитуда")
plt.grid(True)

plt.show()

print(f"Объем памяти массива: {samles.nbytes} байт")

plt.plot(t,x,'green', linewidth=2)
plt.plot(t2,samles,'red', linewidth=2)
plt.show()
