#  Python — Virtual Environments & Third-Party Libraries

##  Objetivo de la actividad

En esta actividad vamos a aprender a trabajar con **Virtual Environments (`venv`)**, **`pip`** y **librerías de terceros**.

Al terminar deberías poder:

- Crear un Virtual Environment.
- Activarlo y desactivarlo.
- Instalar librerías usando `pip`.
- Utilizar una librería de terceros dentro de un programa.
- Crear un archivo `requirements.txt`.
- Ejecutar un proyecto desde la terminal.
- Entender por qué los proyectos de Python utilizan entornos virtuales.

>  Esta actividad está diseñada para realizarse **remotamente**. Cada estudiante debe ejecutar los comandos en su propia computadora.

---

# 1.  Antes de empezar: ¿qué es una librería?

Una librería es código que otras personas ya programaron y que nosotros podemos reutilizar.

Por ejemplo, Python incluye algunas librerías automáticamente:

```python
import math

print(math.sqrt(25))
```

Pero también existen miles de librerías creadas por otras personas.

Estas son llamadas **third-party libraries** o **librerías de terceros**.

Por ejemplo:

```python
import requests
```

`requests` no forma parte de las funciones básicas de Python, así que tenemos que instalarla.

---

# 2.  ¿Qué es pip?

`pip` es el sistema que usamos para instalar paquetes de Python.

Por ejemplo:

```bash
pip install requests
```

También podemos instalar varias:

```bash
pip install requests rich
```

Para ver qué tenemos instalado:

```bash
pip list
```

Para desinstalar:

```bash
pip uninstall requests
```

---

# 3.  ¿Qué es un Virtual Environment?

Un Virtual Environment es un entorno aislado para un proyecto de Python.

Imagina que tenemos:

```text
Proyecto A
    requests 2.31

Proyecto B
    requests 2.32
```

Si instalamos todo globalmente, los proyectos pueden terminar interfiriendo entre ellos.

Con `venv`:

```text
Computadora
│
├── Proyecto A
│   └── .venv
│       └── requests 2.31
│
└── Proyecto B
    └── .venv
        └── requests 2.32
```

Cada proyecto puede tener sus propias dependencias.

---

# 4.  Crear nuestro primer proyecto

Abre una terminal.

Primero crea una carpeta:

### macOS / Linux

```bash
mkdir python-venv-class
cd python-venv-class
```

### Windows

```powershell
mkdir python-venv-class
cd python-venv-class
```

---

# 5.  Comprobar Python

### macOS / Linux

```bash
python3 --version
```

### Windows

```powershell
python --version
```

Deberías obtener algo parecido a:

```text
Python 3.12.x
```

Si Python no aparece, comunícate con el instructor antes de continuar.

---

# 6.  Crear el Virtual Environment

### macOS / Linux

```bash
python3 -m venv .venv
```

### Windows

```powershell
python -m venv .venv
```

Ahora aparecerá una carpeta:

```text
python-venv-class/
└── .venv/
```

No necesitamos modificar nada dentro de `.venv`.

---

# 7.  Activar el Virtual Environment

Crear el entorno no significa que ya lo estamos utilizando.

Tenemos que activarlo.

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
.venv\Scripts\activate
```

Si funcionó, deberías ver algo parecido a:

```text
(.venv) user@computer python-venv-class %
```

La parte:

```text
(.venv)
```

significa que el entorno está activo.

---


# 8. Ejemplo 1 — Internet con Python
 
Vamos a hacer un programa que consulte información de una ciudad usando una API.
 
Una API permite que diferentes programas se comuniquen entre sí.
 
Nuestro programa será:
 
```text
Python
   │
   │ request
   ↓
API
   │
   │ JSON
   ↓
Python
   │
   ↓
Terminal
```
 
## Paso 1 — Instalar `requests`
 
Con el `.venv` activado:
 
```bash
pip install requests
```
 
## Paso 2 — Crear `main.py`
 
Crea un archivo llamado:
 
```text
main.py
```
 
Coloca:
 
```python
import requests
 
 
city = input("Enter a city: ").lower()
 
url = f"https://wttr.in/{city}?format=j1"
 
response = requests.get(url)
 
 
if response.status_code == 200:
    data = response.json()
 
    weather = data["current_condition"][0]
 
    print()
    print("===== Weather =====")
    print(f"City: {city.title()}")
    print(f"Temperature: {weather['temp_C']}°C")
    print(f"Feels like: {weather['FeelsLikeC']}°C")
    print(f"Weather: {weather['weatherDesc'][0]['value']}")
 
else:
    print("City not found!")
```
 
---
 
# 9. Ejecutar el programa
 
Con el Virtual Environment activo:
 
**macOS / Linux**
 
```bash
python3 main.py
```
 
**Windows**
 
```bash
python main.py
```
 
Prueba:
 
```text
Enter a city: Panama City
```
 
También puedes probar:
 
```text
Enter a city: Paris
```
 
o:
 
```text
Enter a city: Tokyo
```
 
El programa debería mostrar información como:
 
```text
===== Weather =====
City: Panama City
Temperature: 29°C
Feels like: 34°C
Weather: Partly cloudy
```
 
---
 
# 10. ¿Qué está pasando?
 
Esta línea:
 
```python
import requests
```
 
importa la librería que instalamos con `pip`.
 
Esta:
 
```python
requests.get(url)
```
 
le pide información a la API.
 
Esta:
 
```python
response.status_code
```
 
nos dice si la solicitud funcionó.
 
Por ejemplo:
 
```text
200
```
 
significa que la solicitud fue exitosa.
 
Esta:
 
```python
response.json()
```
 
convierte la respuesta JSON en información que podemos utilizar desde Python.
 
Por ejemplo, podemos guardar esa información:
 
```python
data = response.json()
```
 
y después acceder a diferentes partes:
 
```python
data["current_condition"]
```
 
---
 
## Challenge 1
 
Modifica el programa para mostrar también:
 
- Humedad.
- Velocidad del viento.
- Dirección del viento.
**Pista:**
 
Toda la información del clima actual está dentro de:
 
```python
data["current_condition"][0]
```
 
Puedes utilizar:
 
```python
print(data)
```
 
para ver toda la información que devuelve la API.
 
---
 
## Challenge 2
 
Haz que el programa pregunte:
 
```text
Search another city? (yes/no):
```
 
Si el usuario escribe `yes`, debe permitir buscar otra ciudad.
 
Por ejemplo:
 
```text
Enter a city: Panama City
 
===== Weather =====
City: Panama City
Temperature: 29°C
Feels like: 34°C
Weather: Partly cloudy
 
Search another city? (yes/no): yes
 
Enter a city: Madrid
 
===== Weather =====
City: Madrid
Temperature: 18°C
Feels like: 18°C
Weather: Clear
```
 
Si escribe:
 
```text
no
```
 
el programa debe terminar.
 
---
 
## ¿Por qué este ejemplo?
 
Este ejemplo utiliza exactamente los mismos conceptos que necesitamos aprender:
 
```text
input()
   ↓
requests
   ↓
API
   ↓
JSON
   ↓
data["..."]
   ↓
print()
```

---

# 9.  Ejecutar el programa

Con el Virtual Environment activo:

### macOS / Linux

```bash
python3 main.py
```

### Windows

```powershell
python main.py
```

Prueba:

```text
Enter a Pokémon: pikachu
```

Deberías obtener información sobre Pikachu.

También prueba:

```text
Enter a Pokémon: charizard
```

---

# 10.  ¿Qué está pasando?

Esta línea:

```python
import requests
```

importa la librería.

Esta:

```python
requests.get(url)
```

le pide información a la API.

Esta:

```python
response.status_code
```

nos dice si la solicitud funcionó.

Por ejemplo:

```text
200
```

significa que la solicitud fue exitosa.

Esta:

```python
response.json()
```

convierte la respuesta JSON en información que podemos utilizar desde Python.

---

#  Challenge 1

Modifica el programa para mostrar también:

- Tipo del Pokémon.
- HP.
- Ataque.

Pista:

Los stats están dentro de:

```python
data["stats"]
```

Puedes investigar la estructura de los datos utilizando:

```python
print(data)
```

---

#  Challenge 2

Haz que el programa pregunte:

```text
Search another Pokémon? (yes/no):
```

Si el usuario escribe `yes`, debe permitir buscar otro Pokémon.

---

# 11.  Ejemplo 2 — Una terminal más bonita

Ahora vamos a utilizar otra librería.

Instalaremos:

```text
rich
```

`rich` permite crear interfaces mucho más bonitas directamente en la terminal.

Instala:

```bash
pip install rich
```

Ahora nuestro proyecto tiene:

```text
requests
rich
```

---

# 12.  FRC Team Information Tool

Vamos a crear un pequeño programa relacionado con FRC.

El programa permitirá introducir información de un equipo y mostrarla en una tabla.

Crea:

```text
frc_info.py
```

Código:

```python
from rich.console import Console
from rich.table import Table


console = Console()


team_number = input("Team number: ")
team_name = input("Team name: ")
city = input("City: ")
country = input("Country: ")


table = Table(title="FRC Team")

table.add_column("Information")
table.add_column("Value")

table.add_row("Team Number", team_number)
table.add_row("Team Name", team_name)
table.add_row("City", city)
table.add_row("Country", country)


console.print(table)
```

---

# 13.  Ejecutar

### macOS / Linux

```bash
python3 frc_info.py
```

### Windows

```powershell
python frc_info.py
```

Ejemplo:

```text
Team number: 10211
Team name: CyberColts
City: Panama City
Country: Panama
```

La información aparecerá organizada en una tabla.

---

# 14.  ¿Qué cambió?

Antes hacíamos:

```python
print("Team:", team_name)
print("City:", city)
```

Ahora usamos una librería externa:

```python
from rich.console import Console
from rich.table import Table
```

Y podemos hacer:

```python
table = Table(title="FRC Team")
```

Esto nos permite construir una interfaz más organizada sin tener que programar todo desde cero.

---

#  Challenge 3

Agrega:

- Nombre del driver.
- Nombre del coach.
- Año de fundación.
- Número de miembros.

---

#  Challenge 4

Agrega un menú:

```text
====================
     FRC TOOL
====================

1. Team information
2. Exit

Choose:
```

El usuario debe poder elegir una opción.

---

# 15.  requirements.txt

Ahora tenemos un problema.

Si enviamos nuestro código a otra persona, esa persona no sabe qué librerías necesitamos.

Para eso usamos:

```text
requirements.txt
```

Con el Virtual Environment activo, ejecuta:

```bash
pip freeze > requirements.txt
```

Ahora tendrás:

```text
python-venv-class/
│
├── .venv/
├── main.py
├── frc_info.py
└── requirements.txt
```

---

# 16.  Instalar desde requirements.txt

Otra persona puede crear su propio entorno:

```bash
python -m venv .venv
```

Activarlo:

```bash
source .venv/bin/activate
```

Y después instalar todo:

```bash
pip install -r requirements.txt
```

¡No necesita instalar cada librería manualmente!

---

# 17.  No subir `.venv`

Si utilizan Git/GitHub, normalmente **NO subimos `.venv`**.

Creamos un archivo:

```text
.gitignore
```

Y escribimos:

```text
.venv/
__pycache__/
```

Nuestro proyecto puede quedar:

```text
python-venv-class/
│
├── .venv/
├── .gitignore
├── main.py
├── frc_info.py
└── requirements.txt
```

---

# 18.  Salir del Virtual Environment

Cuando terminemos:

```bash
deactivate
```

La parte:

```text
(.venv)
```

desaparecerá de la terminal.

---

#  Cheat Sheet

| Acción | Comando |
|---|---|
| Crear venv | `python -m venv .venv` |
| Activar macOS/Linux | `source .venv/bin/activate` |
| Activar Windows | `.venv\Scripts\activate` |
| Instalar librería | `pip install nombre` |
| Ver librerías | `pip list` |
| Desinstalar | `pip uninstall nombre` |
| Guardar dependencias | `pip freeze > requirements.txt` |
| Instalar dependencias | `pip install -r requirements.txt` |
| Salir | `deactivate` |

---

#  Entrega

Al finalizar debes tener:

```text
python-venv-class/
│
├── .gitignore
├── main.py
├── frc_info.py
└── requirements.txt
```

El `.venv` debe existir en tu computadora, pero **no es necesario entregarlo ni subirlo a GitHub**.

## Checklist

- [ ] Creé un Virtual Environment.
- [ ] Activé el Virtual Environment.
- [ ] Instalé `requests`.
- [ ] Instalé `rich`.
- [ ] Ejecuté los dos programas.
- [ ] Completé al menos 2 challenges.
- [ ] Creé `requirements.txt`.
- [ ] Creé `.gitignore`.
- [ ] Entiendo para qué sirve `.venv`.
- [ ] Entiendo para qué sirve `pip`.
- [ ] Entiendo para qué sirve `requirements.txt`.

---

#  ¿Qué sigue?

En la próxima actividad vamos a utilizar lo que aprendimos aquí para empezar a construir programas más cercanos a proyectos reales.

La idea es que el flujo se vuelva natural:

```text
Idea
 ↓
Buscar una librería
 ↓
Crear .venv
 ↓
pip install
 ↓
Leer documentación
 ↓
Programar
 ↓
Probar
 ↓
requirements.txt
```

**No memorices todos los comandos.**

Lo importante es entender **qué problema resuelve cada herramienta y cuándo utilizarla**.

**Cuando termines escribeme al privado de whatsapp.**

# Si tienen preguntas PORFAVOR escribanme estoy para ayudarlos!

*Intenten no usar IA, al menos de que no entiendan*