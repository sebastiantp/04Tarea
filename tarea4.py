from planeta import Planeta
import numpy as np
import matplotlib.pyplot as plt
dty0=0.3#condicion inicial de velocidad en y
condicion_inicial = np.array([10., 0, 0, dty0])

p = Planeta(condicion_inicial)

t_fin =  3000.#tiempo maximo
num_pasos = 2000+1#intervalos
dt= t_fin / (float)(num_pasos)#discretisacion
#crear los arreglos a usar mas adelante
x = np.zeros(num_pasos)
y = np.zeros(num_pasos)
dtx = np.zeros(num_pasos)
dty = np.zeros(num_pasos)
energia = np.zeros(num_pasos)
#se inician los valores para las variables
[x[0],y[0],dtx[0],dty[0]] = condicion_inicial
energia[0] = p.energia_total()

"""implementacion de verlet con alfa distinto de cero"""


"""
#da el primer paso usando RK 4, para continuar con el metodo de verlet
p.avanza_rk4(dt)
aux = p.y_actual
x[1] = aux[0]
y[1] = aux[1]
dtx[1] = aux[2]
dty[1] = aux[3]
energia[1] = p.energia_total()
#inicia el metodo de verlet
for i in range (2,num_pasos):

    p.avanza_verlet(dt,x[i-2],y[i-2])
    aux = p.y_actual
    x[i] = aux[0]
    y[i] = aux[1]
    dtx[i] = aux[2]
    dty[i] = aux[3]
    energia[i] = p.energia_total()
"""

"""implementacion de euler con alfa distinto de cero"""

"""
for i in range (1,num_pasos):

    p.avanza_euler(dt)
    aux = p.y_actual
    x[i] = aux[0]
    y[i] = aux[1]
    dtx[i] = aux[2]
    dty[i] = aux[3]
    energia[i] = p.energia_total()
"""
"""implementacion de RK-4 con alfa distinto de cero"""

""
for i in range (1,num_pasos):

    p.avanza_rk4(dt)
    aux = p.y_actual
    x[i] = aux[0]
    y[i] = aux[1]
    dtx[i] = aux[2]
    dty[i] = aux[3]
    energia[i] = p.energia_total()
""

"""implementacion de los graficos"""

#grafico de trayectoria
fig=plt.figure(1)
plt.subplot(2 ,1 ,1)
plt.plot(x , y, label = "Trayectoria")
plt.xlabel("X")
plt.ylabel("Y")
#grafico energia vs tiempo
t_aux = np.linspace(1,t_fin,num_pasos)
plt.subplot(2 ,1 ,2)
plt.plot(t_aux,energia)
plt.xlabel("Tiempo")
plt.ylabel("Energia")
plt.title("E(t)")


plt.show()
