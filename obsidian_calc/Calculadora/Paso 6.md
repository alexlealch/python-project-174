A partir de este punto, escribir pruebas será una parte clave de tu desarrollo. Para ello, usaremos el framework **pytest**, con el que ya has trabajado antes. Ahora lo exploraremos más a fondo para que puedas escribir tus propias pruebas.

## **¿Qué es Github Actions y por qué lo usamos?**

**Funciona así:** cada vez que subes un cambio al repositorio (generalmente en la rama principal, `main`), un sistema automatizado revisa el código, lo ejecuta y verifica su correcto funcionamiento.

Una ventaja adicional es que Github Actions nos permite agregar una **insignia** (_badge_) a nuestro archivo _README.md_. Este nos muestra si la última revisión del código fue exitosa o si hubo algún error. Con solo hacer clic en esta insignia, podemos ver los detalles de cada ejecución.

---

## **¿Qué debes hacer?**

Verifica siempre con el [repositorio de referencia](https://github.com/hexlet-boilerplates/nodejs-package). Es especialmente importante configurar la ejecución de pruebas tal como está definido en el archivo package.json. Presta atención al archivo [.npmrc](https://github.com/hexlet-boilerplates/nodejs-package/blob/main/.npmrc), ya que es necesario para que Jest funcione correctamente con módulos ECMAScript (ESM).

1️⃣ **Configura un linter**

```
make lint
```

y recibir una revisión del código.

2️⃣ **Habilita Github Actions, CodeClimate y las insignias ("badges")**

- Activa **Github Actions** en tu repositorio para automatizar la revisión del código.
- Agrega **CodeClimate**, una herramienta que mide la calidad y cobertura de tu código.
- Inserta insignias (badges) en tu **README.md** para mostrar el estado de las verificaciones.  
    Para hacerlo, sigue la configuración de [este flujo de trabajo](https://github.com/hexlet-boilerplates/python-package/blob/main/.github/workflows/pyci.yml), que puedes usar como referencia.

3️⃣ **Escribe pruebas para comparar archivos JSON planos**

- Tu tarea es escribir pruebas automatizadas que verifiquen si dos archivos JSON simples se comparan correctamente.
- Usa **pytest** para escribir estas pruebas.

4️⃣ **Ejecuta pruebas y linters en Github Actions**

- Configura Github Actions para que, cada vez que hagas un cambio en el código, se ejecuten automáticamente las pruebas y los linters.

5️⃣ **Mide la cobertura de código en CodeClimate**

- Configura Github Actions para enviar información sobre la cobertura de código a **CodeClimate**.
- Agrega la insignia de cobertura (**Test Coverage**) a tu **README.md** para ver qué porcentaje del código está cubierto por pruebas.

---

## **Consejos**

- En las pruebas, a veces necesitas usar archivos adicionales como ejemplos o datos de prueba. Estos archivos se llaman **fixtures** y, por convención, deben guardarse dentro de la carpeta `tests/fixtures/`.
- Si el resultado esperado en tus pruebas es muy grande y difícil de manejar dentro del código, puedes guardarlo en un archivo de texto dentro de `tests/fixtures/` y leerlo desde allí. Esto hará que tu código de pruebas sea más claro y ordenado.