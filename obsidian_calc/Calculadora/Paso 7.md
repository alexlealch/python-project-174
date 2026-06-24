Los formatos _JSON_ y _YAML_ tienen una estructura especial: son recursivos. Esto significa que dentro de un archivo _JSON_ o _YAML_, un valor también puede ser otro _JSON_ o _YAML_. Por eso, cuando comparamos dos archivos de estos formatos, también debemos considerar sus estructuras internas, no solo los valores más superficiales.

Miremos un ejemplo de comparación entre dos archivos con estructuras anidadas:

```
gendiff filepath1.json filepath2.json
{
    common: {
      + follow: false
        setting1: Value 1
      - setting2: 200
      - setting3: true
      + setting3: null
      + setting4: blah blah
      + setting5: {
            key5: value5
        }
        setting6: {
            doge: {
              - wow:
              + wow: so much
            }
            key: value
          + ops: vops
        }
    }
    group1: {
      - baz: bas
      + baz: bars
        foo: bar
      - nest: {
            key: value
        }
      + nest: str
    }
  - group2: {
        abc: 12345
        deep: {
            id: 45
        }
    }
  + group3: {
        deep: {
            id: {
                number: 45
            }
        }
        fee: 100500
    }
}
```

Para trabajar con esto, usaremos dos archivos de ejemplo:

**file1.json**

```
{
  "common": {
    "setting1": "Value 1",
    "setting2": 200,
    "setting3": true,
    "setting6": {
      "key": "value",
      "doge": {
        "wow": ""
      }
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar",
    "nest": {
      "key": "value"
    }
  },
  "group2": {
    "abc": 12345,
    "deep": {
      "id": 45
    }
  }
}
```

**file2.json**

```
{
  "common": {
    "follow": false,
    "setting1": "Value 1",
    "setting3": null,
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "setting6": {
      "key": "value",
      "ops": "vops",
      "doge": {
        "wow": "so much"
      }
    }
  },
  "group1": {
    "foo": "bar",
    "baz": "bars",
    "nest": "str"
  },
  "group3": {
    "deep": {
      "id": {
        "number": 45
      }
    },
    "fee": 100500
  }
}
```

## ¿Qué debes hacer?

Dividiremos el proceso en dos partes importantes:

1. **Construir la diferencia (diff)** → Debemos analizar los archivos y marcar qué cambió en cada clave: si se agregó, eliminó o modificó.
2. **Formatear la salida** → Una vez que tenemos la información de la diferencia, la organizamos para mostrarla de manera entendible.

Al separar estos dos pasos, será más fácil añadir diferentes formatos de salida en el futuro sin repetir la lógica del análisis.

## Pasos a seguir

1️⃣ **Escribe pruebas automáticas (tests) antes de programar**

Antes de comenzar a escribir código, es fundamental definir qué se espera que haga tu herramienta. Para eso, debes crear pruebas automáticas. Estas pruebas te permitirán:

- Confirmar que tu código hace lo que debería hacer.
- Detectar rápidamente errores cuando hagas cambios.
- Tener una base sólida para avanzar con seguridad.

> Usa `pytest` para escribir pruebas. Crea un archivo como `tests/test_generate_diff.py` y define varios casos:

- Archivos iguales → sin diferencias.
- Archivos con claves nuevas, modificadas y eliminadas.
- Casos con estructuras anidadas.

2️⃣ **Crea archivos de prueba con YAML y estructuras anidadas**

Ya tienes archivos JSON de ejemplo, pero tu herramienta también debe soportar **archivos YAML**, y además debes probar que puede manejar **estructuras anidadas** (por ejemplo, diccionarios dentro de diccionarios).

> Crea archivos como `file1.yaml` y `file2.yaml` que contengan varios niveles de anidación. Por ejemplo:

```
common:
  setting1: Value 1
  setting2: 200
  setting3:
    nested1: true
    nested2: false
```

3️⃣ **Implementa la comparación para estructuras anidadas**

Tu herramienta ya puede comparar archivos con pares clave-valor planos. Ahora debes extender esa lógica para que también pueda encontrar diferencias dentro de estructuras más profundas (por ejemplo, dentro de un subdiccionario).

> Piensa en esto como una comparación "recursiva": si un valor es otro diccionario, hay que seguir comparando clave por clave.

4️⃣ **Separa el cálculo de diferencias del formato de salida**

Para que tu herramienta sea fácil de mantener y extender en el futuro, **separa responsabilidades**:

- Una parte del código _calcula las diferencias_ entre las estructuras (sin preocuparse por cómo se mostrarán).
- Otra parte (el "formateador") se encarga de _convertir esas diferencias en texto legible_ para el usuario.

5️⃣ **Crea un formateador llamado `stylish`**

Este formateador será responsable de mostrar las diferencias con indentaciones y símbolos para que sea fácil de leer:

- `-` si una clave fue eliminada.
- `+` si una clave fue agregada.
- Espacio si no cambió.
- Y si hay una diferencia en un valor, mostrar ambos.

_Ejemplo de salida:_

```
{
  common: {
    + follow: false
      setting1: Value 1
    - setting2: 200
    + setting2: 300
  }
}
```

6️⃣ **Usa `stylish` como formato por defecto**

Si el usuario no indica ningún formato específico, tu herramienta debe usar el formateador stylish de forma automática.

> Esto se hace pasando `stylish` como valor por defecto en la función `generate_diff()`:

```
def generate_diff(file1, file2, format_name='stylish'):
```

7️⃣ **Asegúrate de que el ejecutable también use el formato por defecto**

Cuando alguien ejecuta tu programa desde la terminal así:

```
gendiff file1.json file2.json
```

Tu herramienta debe usar el formateador `stylish` a menos que el usuario especifique otro con una opción como `--format`.

> Usa `argparse` para capturar el argumento `--format` y pásalo a `generate_diff()`. Si no se incluye, usa `stylish`.

## Consejos

- **Estructura tu código en dos partes:**
    
    1. **Cálculo de la diferencia** (dónde analizamos lo que cambió en los archivos).
    2. **Formatos de salida** (dónde convertimos las diferencias en un formato visual).
- **Organiza bien la información:** El comparador debe guardar todos los detalles de los cambios (claves agregadas, eliminadas, modificadas) sin depender del formato de salida.
    
- **Manejo de niveles de anidación:** Si dos estructuras son diccionarios y tienen la misma clave, sus diferencias deben compararse recursivamente dentro de esa clave.
    
- **Cálculo de indentación en el formato:** La cantidad de espacios antes de cada línea sigue una regla clara. Por ejemplo, cada nivel de profundidad agrega cuatro espacios. Si aparece un símbolo especial (`+` o `-`), va seguido de un espacio adicional, antes de mostrar el texto del cambio.
    

Miremos un ejemplo con puntos representando los espacios:

```
{
..  common: {
......+ follow: false
......  setting1: Value 1
......+ setting5: {
............key5: value5
........}
....}
}
```

Aquí puedes notar que:

- `common:` está a un nivel de profundidad.
- `follow: false` tiene un _+_ porque es un nuevo valor agregado.
- `setting5:` es otro nivel dentro `common`, con su clave `key5` anidada.

Con esto en mente, ¡ya tienes todo para completar el reto! Organiza bien tu código, separa la lógica en partes claras y prueba que todo funcione correctamente.