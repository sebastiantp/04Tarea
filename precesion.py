from planeta import Planeta
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

dty0=1/3.

#verifica si  el valor de posicion entregado corresponde con
# el criterio de afelio
def ver_afelio(R,eps):
    if 10-eps < R:
        if 10+eps > R:
            return True
    else :
        return False


#recibe un arreglo con las coordenadas (t, x, y) de los afelios
#y calcula un arreglo de w haciendo diferencias entre
#un set de coordenadas y sus vecinos.

def cal_w(afelio):
    w = np.zeros(len(afelio[0])-1)
    phi_1 =  np.tan(afelio[2][0]/(afelio[1][0]))
    t_1 = afelio[0][0]

    for i in range(1,len(afelio[0])):
        phi = np.tan(afelio[2][i]/(afelio[1][i]))
        t = afelio[0][i]
        dphi = phi - phi_1
        dt = t - t_1
        w[i-1] = dphi/dt
        t_1 = t
        phi_1 = phi
    return w



condicion_inicial = np.array([10., 0, 0, dty0])
p = Planeta(condicion_inicial, 10**(-2.943))
t_fin =  3000
num_pasos = 30000+1
dt= t_fin / (float)(num_pasos)
x = np.zeros(num_pasos)
y = np.zeros(num_pasos)
dtx = np.zeros(num_pasos)
dty = np.zeros(num_pasos)
R = np.zeros(num_pasos)
energia = np.zeros(num_pasos)
afelio = [[], [],[] ]
[x[0],y[0],dtx[0],dty[0]] = condicion_inicial
R[0] = np.sqrt(x[0]*x[0]+y[0]*y[0])
energia[0] = p.energia_total()
#avanza un paso con RK4, para proseguir con verlet
p.avanza_rk4(dt)
aux = p.y_actual
x[1] = aux[0]
y[1] = aux[1]
dtx[1] = aux[2]
dty[1] = aux[3]
R[1] = np.sqrt(x[1]*x[1]+y[1]*y[1])
energia[1] = p.energia_total()
#metodo de verlet para alfa distinto de cero
for i in range (2,num_pasos):
    p.avanza_verlet(dt,x[i-2],y[i-2])
    aux = p.y_actual
    x[i] = aux[0]
    y[i] = aux[1]
    dtx[i] = aux[2]
    dty[i] = aux[3]
    energia[i] = p.energia_total()
    R[i] = np.sqrt(x[i]*x[i]+y[i]*y[i])
    eps = 0.000005
    if ver_afelio(R[i], eps):
        afelio[0].append(p.t_actual)
        afelio[1].append(x[i])
        afelio[2].append(y[i])
        print (i)
w_t=cal_w(afelio)

w_precesion = scipy.stats.mode(w_t)[0][0]
print("w de precesion = "+(str)(w_t))
print("w de precesion = "+(str)(w_precesion))


#crear un documento de texto y guardar la informacion
#velocidad angulares.
def creartxt():
    archi=open('datos.txt','w')
    archi.close()

def grabartxt():
    archi=open('datos.txt','a')
    archi.write("w de precesion = "+(str)(w_t))
    archi.write("w de precesion = "+(str)(w_precesion))
    archi.close()

creartxt()
grabartxt()

#grafico 1
fig=plt.figure(1)
plt.subplot(2, 1, 1)
fig.subplots_adjust(hspace=1.5)
plt.plot(x , y, label = "Trayectoria")
plt.xlabel("X")
plt.ylabel("Y")
plt.scatter(afelio[1],afelio[2],label="posicion afelio")
plt.legend(loc="lower right",fontsize=10)
#grafico 2
t_values = np.linspace(1,t_fin,num_pasos)
plt.subplot(2, 1, 2)
plt.plot(t_values,energia)
plt.xlabel("Tiempo")
plt.ylabel("E(t)")

plt.show()
