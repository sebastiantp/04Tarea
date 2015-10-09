# Tarea nro. 4
## FI3104B - Métodos Numéricos para la Ciencia y la Ingeniería
#### Prof. Valentino González

## P1

Software Carpentry es una fundación sin fines de lucro que tiene como objetivo
enseñar a científicos e ingenieros de diversas ramas las habilidades necesarias
*"to get more done in less time, and with less pain"*.

El siguiente tutorial desarrollado por Software Carpentry les ayudará a mejorar
el diseño del software que desarrollen para sus tareas y en el futuro.
**Estudien** el tutorial y respondan las preguntas que se encuentran a
continuación (incluya sus respuestas en el informe).

[Tutorial en la página de Software
Carpentry](http://swcarpentry.github.io/v4/invperc/index.html): Incluye las
slides y una transcripción del video.

[También disponible como youtube
playlist.](https://www.youtube.com/playlist?list=PL5859017B018F03F4)

#### Preguntas

- Describa la idea de escribir el *main driver* primero y llenar los huecos
  luego. ¿Por qué es buena idea?

- ¿Cuál es la idea detrás de la función `mark_filled`? ¿Por qué es buena idea
  crearla en vez del código original al que reemplaza?

- ¿Qué es *refactoring*?

- ¿Por qué es importante implmentar tests que sean sencillos de escribir? ¿Cuál
  es la estrategia usada en el tutorial?


- El tutorial habla de dos grandes ideas para optimizar programas, ¿cuáles son
  esas ideas? Descríbalas.

- ¿Qué es `lazy evaluation`?

- Describa la *other moral* del tutorial (es una de las más importantes a la
  hora de escribir buen código).


## P2

Para planetas que orbitan cerca del Sol, el potencial se puede escribir como:

<img src='eqs/potencial.png' alt='' height='50'>

> Latex: `U(r) = - \dfrac{GMm}{r} + \alpha\dfrac{GMm}{r^2}`

donde &alpha; es un número pequeño. Esta corrección a la ley de gravitación de
Newton es una buena aproximación derivada de la teoría de la relatividad general
de Einstein.

Bajo este potencial, las órbitas siguen siendo planas pero ya no son cerradas,
sino que precesan, es decir, el perihelio (punto más lejano de la órbita) gira
alrededor del Sol.

1. El archivo llamado `planeta.py` contiene el esqueleto la clase `Planeta`.
   Ud.  debe implementar los métodos de esa clase. Los `docstrings` explican en
   qué debe consistir cada método. Ud. tiene libertad de mejorar los
   `docstrings`, y agregar atributos y métodos a la clase según le parezca
   conveniente para resolver el problema descrito a continuación.

   El archivo llamado `solucion_usando_euler.py` muestra cómo incluir la clase
   Planeta en un script separado. Ud. también puede resolver todo dentro del
   mismo archivo, en cuyo caso puede descartar `solucion_usando_euler.py`

2. Parta por estudiar el caso &alpha;=0 y considere las siguientes condiciones
   iniciales:

   <img src='eqs/condiciones-iniciales.png' alt='' height='100'>

   > Latex:
   ```
   \begin{flalign*}
   x_0 &= 10\\
   y_0 &= 0\\
   v_x &= 0\\
   \end{flalign*}
   ```

   Además, utilice unidades tales que GMm = 1 y escoja v<sub>y</sub> según le
   parezca (asegúrese the la energía total sea menor que cero).

   Integre la ecuación de movimiento por aproximadamente 5 órbitas usando los
   métodos de *Euler explícito*, *RK4* y *Verlet*. Plotee las órbitas y la
   energía total del sistema como función del tiempo en los 3 casos. Comente
   los resultados.

3. Ahora considere el caso &alpha;=10<sup>-2.XXX</sup> (donde XXX son los 3
   últimos digitos de su RUT, antes del dígito verificador). Integre la
   ecuación de movimiento usando el método de *Verlet* por al menos 30 órbitas.
   Determine la velocidad angular de precesión. ¿Cómo lo hizo? En particular,
   ¿cómo determinó la posición del perihelio? Plotee la órbita y la energía
   como función del tiempo.


__Otras Notas.__

- Utilice `git` durante el desarrollo de la tarea para mantener un historial de
  los cambios realizados. La siguiente [*cheat
  sheet*](https://education.github.com/git-cheat-sheet-education.pdf) le puede
  ser útil. Evaluar el uso efectivo de `git`. Recuerde hacer cambios
  significativos pero relativamente pequeños y guardar seguido.  Evite hacer
  `commits` de código que no compila y deje mensajes que permitan entender los
  cambios realizados.

- También evaluaremos su uso correcto de python. Si define una función
  relativamente larga o con muchos parámetros, recuerde escribir el *doctsring*
  que describa los parametros y que es lo que hace la función.  También
  recuerde usar nombres explicativos para las variables y las funciones.  El
  mejor nombre es aquel que permite entender que hace la función sin tener que
  leer su implementación.

- La tarea se entrega como un *pull request* en github. El *pull request* debe
  incluir todos los códigos usados además de su informe.

- El informe debe ser entregado en formato *pdf*, este debe ser claro sin
  información ni de más ni de menos.
