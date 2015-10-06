# Tarea nro. 4
## FI3104B - Métodos Numéricos para la Ciencia y la Ingeniería
#### Prof. Valentino González

## P1

Software Carpentry es una fundación sin fines de lucro que tiene como objetivo
enseñar a científicos e ingenieros de diversas ramas las habilidades necesarias
*"to get more done in less time, and with less pain"*.

El siguiente tutorial desarrollado por Software Carpentry les ayudará a mejorar
el diseño del software que desarrollen para sus tareas y en el futuro. Véan el
tutorial y luego respondan las preguntas que se encuentran a continuación
(incluya sus respuestas en el informe).

[Tutorial en la página de Software
Carpentry](http://swcarpentry.github.io/v4/invperc/index.html): Incluye las
slides y una transcripción del video.

[También disponible como youtube
playlist.](https://www.youtube.com/playlist?list=PL5859017B018F03F4)


## P2

Para planetas que orbitan cerca del Sol, el potencial se puede escribir como:

> Latex: `U(r) = - \dfrac{GMm}{r} + \alpha\dfrac{GMm}{r^2}`

donde &alpha; es un número pequeño. Esta corrección a la ley de gravitación de
Newton es una buena aproximación derivada de la teoría de la relatividad general
de Einstein.

Bajo este potencial, las órbitas siguen siendo planas pero ya no son cerradas,
sino que precesan, es decir, el perihelio (punto más lejano de la órbita) gira
alrededor del Sol.

1. El archivo llamado `planeta.py` contiene el esqueleto la clase `Planeta`. Ud.
   debe implementar los métodos de esa clase. Los `docstrings` explican en qué
   debe consistir cada método. Ud. tiene libertad de agregar atributos y métodos
   a la clase según le parezca conveniente para resolver el problema descrito a
   continuación.

   El archivo llamado `solucion_usando_euler.py` muestra cómo incluir la clase
   Planeta en un script separado. Ud. también puede resolver todo dentro del
   mismo archivo, en cuyo caso puede descartar `solucion_usando_euler.py`

2. Parta por estudiar el caso &alpha;=0 y considere las siguientes condiciones
   iniciales:

   > Latex: 
   ```
   \begin{flalign*}
   x_0 &= 10\\
   y_0 &= 0\\
   v_x &= 0\\
   v_y &= ?
   \end{flalign*}
   ```


   Integre la ecuación de movimiento por aproximadamente 5 órbitas usando los
   métodos de *euler*, *RK4* y *Verlet*. Plotee las órbitas y la energía total
   del sistema como función del tiempo. Comente los resultados.

3. Ahora considere el caso &alpha;=XXX e integre la ecuación de movimiento
   usando el método de *Verlet* por al menos 30 órbitas. Determine la velocidad
   angular de precesión. ¿Cómo calculó la velocidad de precesión? En particular,
   ¿cómo determinó la posición del perihelio?


