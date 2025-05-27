# Consigna

Entregar informe escrito con la siguiente información: 

1. Plantear la función objetivo a maximizar y las restricciones que reflejan los supuestos dados.
2. Desarrollo/resultado del problema de acuerdo a la programación realizada (el programa debe ser parte del a entrega)
3. Interpretación del resultado obtenido

## Ejercicio

Un carpintero, para fabricar mesas y sillas utiliza 3 máquinas A, B, y C, en un orden indiferente.  Los tiempos unitarios de ejecución, en minutos, están dados por la siguiente tabla:

| | A | B | C |
|---|---|---|---|
| Mesas | 8 | 0 | 20 |
| Sillas | 2 | 6 | 0 |

Supondremos que las máquinas no tienen tiempos muertos al esperar un producto que se está procesando en otra máquina.

Las horas disponibles de cada máquina para una actividad de un mes son:

- 120 horas para máquinas del tipo A.
- 180 horas para las de tipo B.
- 110 horas para las de tipo C.

Una mesa le da una ganancia de \$ 40 y una silla de $ 10.

Dado que la mayoría de las veces vende los productos que fabrica como un juego, es necesario que la cantidad de sillas sea seis veces la cantidad de mesas.  

Además, por exigencias del mercado, debe fabricar como mínimo 3 mesas.

En esas condiciones, ¿cuántas mesas y sillas se deben fabricar mensualmente para maximizar la ganancia?

# Solución

1. La función a maximizar es la ganancia total, que se expresa como:

   $Z = 40x_1 + 10x_2$

   donde $x_1$ es el número de mesas y $x_2$ es el número de sillas.

2. Las restricciones del problema son:
    - $x_2 \geq 0, x_1 \geq 3$
    - Tiempo de la máquina A: $8x_1 + 2x_2 \leq 7200$
    - Tiempo de la máquina B: $6x_2 \leq 10800$
    - Tiempo de la máquina C: $20x_1 \leq 6600$
    - Relación entre mesas y sillas: $x_2 = 6x_1$

## Desarrollo del problema

Para poder alimentar el algoritmo de programación lineal vamos a definir las ecuaciones de las restricciones:

$$
\begin{array}{lllllllllll}
8x_1 & + 2x_2 & + x_3 & + 0 & + 0 & 
+ 0 &= 7200 \\
0 & + 6x_2 & + 0 & + x_4 & + 0 & +0 &= 10800 \\
20x_1 & + 0 & + 0 & + 0 & + x_5 & + 0 &= 6600 \\
6x_1 & - x_2 & + 0 & + 0 & + 0 & + x_6 &=0
\end{array}
$$

# Programa

## Requerimientos

- Python 3.12

### Librerías

- **scipy**:

Única librería que se requiere instalar. Es utilizada por el modulo `optimize` que provee las herramientas de programación lineal necesarias para resolver el ejercicio.

- **warnings**:

Libreria incluida ya en python, utilizada para silenciar la advertencia sobre el método simplex siendo deprecado.

## Instrucciones

### Con uv

1. Instalar uv: 

    - [Instrucciones](https://docs.astral.sh/uv/getting-started/installation/#__tabbed_1_2)

2. Cargar versión de python:

```bash
uv python install 3.12
```

3. Sincronizar el entorno:

```bash
uv python sync
```

4. Correr el script:

```bash
uv run main.py
```

Alternativamente, correr el archivo `run.bat` luego de haber instalado uv y sincronizado el entorno. Este archivo ejecuta el script main.py en el entorno virtual creado.

### Sin uv

1. Instalar python 3.12

    - [Instrucciones](https://www.python.org/downloads/)

2. Crear un entorno virtual

```bash
python -m venv .venv
```

3. Activar el entorno virtual

```bash
# Windows
.venv\Scripts\activate
# Linux
source .venv/bin/activate
```

4. Instalar las librerías necesarias

```bash
pip install scipy
```

5. Correr el script

```bash
python main.py
```

## Salida

```bash
D:\path\to\dir>.\.venv\Scripts\python.exe .\main.py
Optimal solution found:
Number of tables (x1): 300.0
Number of chairs (x2): 1800.0
Value of the objective function (Z): 30000.0
```