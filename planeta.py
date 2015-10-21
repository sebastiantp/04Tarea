import numpy  as np



G=1
m=1
Ms=1


class Planeta(object):
    '''
    Complete el docstring.
    '''

    def __init__(self, condicion_inicial, alpha=0):
        '''
        __init__ es un método especial que se usa para inicializar las
        instancias de una clase.
        Ej. de uso:
        >> mercurio = Planeta([x0, y0, vx0, vy0])
        >> print(mercurio.alpha)
        >> 0.
        '''
        self.y_actual = condicion_inicial
        self.t_actual = 0.
        self.alpha = alpha

    def ecu_de_mov(self,ds=np.array([0,0,0,0])):
        '''
        Implementa la ecuación de movimiento, como sistema de ecuaciónes de
        primer orden.
        '''
        x, y, dtx, dty = self.y_actual

        dx = ds[0]
        dy = ds[1]
        ddtx = ds[2]
        ddty = ds[3]

        x = x + dx
        y = y +  dy
        dtx = dtx + ddtx
        dty = dty + ddty



        fx = x*(G*Ms)*(((2.* self.alpha) / ((x**2 + y**2)**2)) -(1. / (np.sqrt(x**2 + y**2))**3))

        fy = y*(G*Ms)*(((2.* self.alpha) / ((x**2 + y**2)**2)) -(1. / (np.sqrt(x**2 + y**2))**3))



        return np.array([dtx,dty,fx,fy])

    def avanza_euler(self, dt):
        '''
        metodo que dado una condicion inicial, calcula de forma numerica, usando
        el metodo de Euler


        '''

        Yn = self.y_actual + dt * (self.ecu_de_mov())
        self.y_actual = Yn
        self.t_actual = self.t_actual + dt


        pass





    def avanza_rk4(self, dt):
        '''
        Similar a avanza_euler, pero usando Runge-Kutta de orden 4.


        '''


        k_1 = self.ecu_de_mov()
        k_2 = self.ecu_de_mov(dt/2. * k_1)
        k_3 = self.ecu_de_mov(dt/2. * k_2)
        k_4 = self.ecu_de_mov(dt * k_3)

        Yn = self.y_actual + dt/6. * (k_1 + 2*k_2 + 2*k_3 + k_4)

        self.y_actual = Yn
        self.t_actual = self.t_actual + dt




        pass

    def avanza_verlet(self, dt,x_pre,y_pre):
        '''
        Similar a avanza_euler, pero usando Verlet.
        '''


        Y_pre = np.array([x_pre,y_pre])
        x , y, dtx, dty = self.y_actual
        Y = np.array([x,y])
        Yn = 2 * Y - Y_pre + dt*dt * self.ecu_de_mov()[2:]
        Vn = (Yn - Y_pre) / (2*dt)

        aux = np.array([Yn[0],Yn[1],Vn[0], Vn[1]])
        self.y_actual = aux
        self.t_actual = self.t_actual + dt






        pass

    def energia_total(self):
        '''
        Calcula la enérgía total del sistema en las condiciones actuales.
        '''
        x, y, dtx, dty = self.y_actual
        U_t = - (G*Ms*m)/(np.sqrt(x**2 + y**2)) \
         + self.alpha*(G*Ms*m)/((x**2 + y**2))
        K_t = (dtx*dtx +dty*dty) * m/2.
        E_t = K_t + U_t


        return E_t



        pass
