import numpy as np
import matplotlib.pyplot as plt

def read_input(filename):
    params = {}
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            parts = line.split()
            key = parts[0]
            values = parts[1:]

            if key == "times":
                params[key] = np.array(list(map(float, values)))
            elif len(values) == 1:
                params[key] = float(values[0])
            else:
                params[key] = list(map(float, values))
    return params
params = read_input("/content/inpu.in")

L = params["L"]
N = int(params["N"])
a = params["alpha"]
t = params["t_final"]
dt = params["dt"]
b = params["times"]

dx = L/(N-1)
v = (a*dt)/(dx**2)

T_n = np.zeros(N)
for i in range(N):
  T_n[i]=params["T_init"]

T_n1 = np.zeros(N)

# boundary conditions
T_n1[0] = params["T_left"]
T_n1[-1] = params["T_right"]

for j in np.arange(0,t+dt,dt):
  for i in range(1,N-1):
    T_n1[i]=v*(T_n[i+1]-2*T_n[i]+T_n[i-1])+T_n[i]
  T_n=T_n1
  if j in b:
    x=np.linspace(0,L,N)
    plt.figure()
    plt.plot(x,T_n)
    plt.title("t="+str(j))
    plt.xlabel("x")
    plt.ylabel("T")
