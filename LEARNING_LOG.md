# Bitácora de Aprendizaje - Calculadora de Diferencias (Gendiff)

## Objetivo del Proyecto
Crear una herramienta de línea de comandos (CLI) en Python que compare dos archivos de configuración y muestre las diferencias entre ellos.

## Contexto Académico (Módulo 2 - Códica)
Este proyecto se desarrolla siguiendo los principios del Módulo 2, donde se ha transitado desde la programación funcional hacia el diseño orientado a objetos (POO). Los conceptos clave que debemos integrar en este proyecto incluyen:
- **Evitar la "Obsesión por Primitivos"**: No usar simples diccionarios o strings para lógica compleja; crear clases dedicadas (Value Objects) cuando sea necesario.
- **Principios SOLID**: Especialmente el SRP (Single Responsibility Principle) para dividir la lógica de lectura, comparación y formateo.
- **Encapsulamiento**: Uso de prefijos `_` para atributos internos.
- **Interfaces Fluentes y Patrones de Diseño**: Aplicar patrones como Builders si la configuración de la herramienta se vuelve compleja.
- **CI/CD**: Integración con GitHub Actions para validación automática.

## Progreso y Conceptos Educativos

### Fase 1: Configuración Inicial y Manejo de Argumentos
- **Concepto Clave: CLI (Command Line Interface)**
  - Aprendimos que una herramienta profesional debe ser intuitiva. El uso de mensajes de ayuda (`-h` o `--help`) es fundamental para la experiencia del usuario (UX).
- **Herramienta: `argparse`**
  - Implementamos el módulo `argparse` de Python. Este módulo permite definir los argumentos que el programa espera recibir (en este caso, `first_file` y `second_file`) y genera automáticamente la documentación de ayuda.
- **Gestión de Dependencias: Poetry**
  - Utilizamos `poetry` para gestionar el entorno virtual y las dependencias, asegurando que el proyecto sea reproducible en cualquier máquina.

### Implementaciones Realizadas
1. **Estructura de Directorios**: Organización siguiendo estándares de Python (`gendiff/scripts/`).
2. **Lógica de Entrada**: Creación de `gendiff.py` con la función `main()` y la protección `if __name__ == "__main__":` para asegurar que el script se ejecute correctamente solo cuando sea llamado directamente.

## Siguientes Pasos
- Implementar la lectura de archivos.
- Desarrollar la lógica de comparación de diccionarios/archivos.
- Formatear la salida de las diferencias.
