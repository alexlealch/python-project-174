Lo primero que debemos hacer en este proyecto es asegurarnos de que nuestra herramienta puede mostrar su información de ayuda. Esto es muy útil porque permite a cualquier usuario entender rápidamente cómo usarla.

Cuando ejecutas el siguiente comando en la terminal:

```
gendiff -h
```

Debería aparecer un mensaje como este:

```
usage: gendiff [-h] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

optional arguments:
  -h, --help            show this help message and exit
```

Este mensaje se genera automáticamente gracias a un módulo especial de Python llamado [`argparse`](https://docs.python.org/3/library/argparse.html), el cual nos facilita la creación de herramientas de línea de comandos. Durante este proyecto, vamos a usarlo bastante.

---

## Pasos para completar esta tarea

1️⃣ **Prepara el proyecto en tu computador**  
Primero, necesitas clonar el repositorio que creaste para este proyecto en tu máquina. Luego, dentro de la carpeta principal del proyecto, inicializa un nuevo paquete con el siguiente comando:

```
poetry init
```

Cuando te pida un nombre para el paquete, ingrésalo como `hexlet-code`.

2️⃣ **Crea la estructura de directorios**

1. Crea una carpeta llamada `gendiff` en la raíz del proyecto.
2. Dentro de la carpeta `gendiff`, crea una subcarpeta llamada `scripts`.

La estructura de carpetas debería ser la siguiente:

```
├── .github/
├── gendiff/
│   ├── scripts/
│   │   └── gendiff.py
├── pyproject.toml
├── README.md
```

3️⃣ **Crea el archivo `gendiff.py` con el código**

Dentro de la carpeta `gendiff/scripts/`, crea el archivo `gendiff.py` y coloca el siguiente código:

```
import argparse

def main():
 parser = argparse.ArgumentParser(
     description="Compares two configuration files and shows a difference."
 )
 parser.add_argument("first_file", help="First file to compare")
 parser.add_argument("second_file", help="Second file to compare")

 args = parser.parse_args()

if __name__ == "__main__":
 main()
```

o también

```
poetry run python -m gendiff.scripts.gendiff -- …
```

4️⃣ **Verifica que el código funcione**

Ahora que el archivo está listo, abre la terminal en la carpeta principal del proyecto y ejecuta el siguiente comando para probar el script con el mensaje de ayuda:

```
poetry run python -m gendiff.scripts.gendiff --help
```

---

## Consejos

- Si tienes dudas sobre cómo organizar tu proyecto, revisa cómo hiciste el primer proyecto de este curso. Ahí seguiste pasos similares para preparar el entorno.
- También puedes consultar este repositorio de ejemplo, donde ya hay un entorno configurado: [hexlet-boilerplates/python-package](https://github.com/hexlet-boilerplates/python-package).