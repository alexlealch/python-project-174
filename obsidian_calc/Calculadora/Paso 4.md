El objetivo de esta tarea es crear una herramienta que compare archivos JSON y muestre las diferencias entre ellos. Imagínalo como un "detector de cambios" que te indica qué ha sido agregado, eliminado o modificado entre dos archivos.

Vamos a hacer que nuestra herramienta funcione de manera clara y organizada. Los resultados deben mostrarse en orden alfabético según las claves y deben seguir este formato:

```
gendiff file1.json file2.json
{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

Fíjate en los símbolos al inicio de cada línea:

- **menos (`-`)** significa que el valor está en el primer archivo pero ha sido eliminado o cambiado en el segundo archivo.
- **más (`+`)** indica que el valor no existía en el primer archivo y fue agregado en el segundo.
- Si un valor no tiene símbolo, significa que no ha cambiado en ambos archivos.

Por ejemplo, en la salida anterior:

- `timeout` aparece en ambos archivos, pero con valores distintos (50 en el primero y 20 en el segundo). Por eso, primero se muestra la línea con el valor que se eliminó y luego la que se agregó.
- `proxy` solo está en `archivo1.json`, así que aparece con un **`-`** indicando que fue eliminado.
- `verbose` solo está en `archivo2.json`, por lo que aparece con **`+`** mostrando que se agregó.

---

### Lo que debes hacer

1️⃣ **Convierte tu proyecto en una biblioteca reutilizable**

- Tu herramienta debe ser útil no solo desde la terminal, sino también permitir que otros la usen en su propio código.
- Para lograr esto, debes asegurarte de que tu proyecto esté estructurado de manera que exponga una función llamada `generate_diff()`. Esta función debe recibir dos rutas de archivos JSON y devolver un texto con las diferencias encontradas entre esos archivos.

_Ejemplo de uso:_

```
from gendiff import generate_diff

diff = generate_diff("file1.json", "file2.json")
print(diff)
```

2️⃣ **Haz que la herramienta funcione desde la terminal**

- Tu herramienta debe poder ejecutarse desde la terminal, permitiendo a los usuarios comparar archivos JSON desde la línea de comandos.
- Para hacer esto, usa la librería `argparse` para capturar las rutas de los archivos JSON cuando el usuario ejecute el comando. Luego, llama a la función `generate_diff()` pasándole esas rutas.

_Ejemplo de uso en la terminal:_

```
python gendiff/scripts/gendiff.py file1.json file2.json
```

3️⃣ **Implementa la comparación de archivos JSON**

- Los archivos JSON contienen pares clave-valor. Tu tarea es leer estos archivos y encontrar las diferencias entre ellos.
- Asegúrate de no comparar los archivos como texto plano. En lugar de eso, debes comparar sus estructuras internas (es decir, sus claves y valores).
- Para esto, usa un parser que convierta los archivos JSON en estructuras de datos (como diccionarios de Python) y luego compáralos.

4️⃣ **Organiza el resultado correctamente**

- La salida de tu herramienta debe estar bien organizada para que sea fácil de entender.
- Las claves de los archivos JSON deben mostrarse en orden alfabético.
- Si una clave tiene valores distintos en los dos archivos, muestra primero el valor del primer archivo, seguido del valor del segundo archivo.
- Usa los siguientes símbolos para mostrar las diferencias:

_Ejemplo de salida:_

```
{
  - follow: false
  - host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}
```

5️⃣ **Documenta tu trabajo**

- Es importante que otros usuarios puedan entender cómo funciona tu herramienta y cómo usarla.
- Crea un archivo _README.md_ donde expliques cómo instalar y usar tu herramienta. Incluye ejemplos prácticos de cómo ejecutar el comando desde la terminal y cómo utilizarla en un script de Python.
- Usa herramientas como _Asciinema_ para grabar una demostración de cómo funciona tu herramienta en acción y agregarla al archivo _README.md._