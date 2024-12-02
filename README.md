# Proyecto: Automatizacion de la Farmacia 25 de JULIO


---

## Requisitos previos

Antes de comenzar, asegúrate de tener instalado:
- **Git**: [Descargar Git](https://git-scm.com/)
- Un entorno de desarrollo como [Visual Studio Code](https://code.visualstudio.com/).

---
---

## Requisitos para la Automatización del Sistema

Este repositorio utiliza **Python** y varias bibliotecas esenciales para automatizar un sistema. Asegúrate de tener instaladas las siguientes bibliotecas antes de ejecutar el proyecto.

### Bibliotecas necesarias

El proyecto requiere las siguientes bibliotecas de Python:

- `selenium`: Para controlar el navegador web.
- `webdriver-manager`: Para gestionar automáticamente los controladores de los navegadores.
- `time`: Para gestionar retardos en la ejecución de comandos.
- `unicodedata`: Para trabajar con caracteres Unicode.

### Instalación de las bibliotecas

Para instalar todas las bibliotecas necesarias, ejecuta el siguiente comando:

```bash
pip install selenium webdriver-manager



## Clonar el Proyecto

### Clonar desde la rama principal (main)
Para descargar el proyecto desde la rama `main`, utiliza los siguientes comandos:

```bash
# Clonar el repositorio (por defecto descargará la rama 'main')
git clone https://github.com/innovatesolutionstudio/Automatizacion_Farmacia.git
```

### Clonar desde una rama específica
Si necesitas clonar directamente una rama específica, usa:

```bash
# Clonar el repositorio especificando una rama
git clone -b [nombre de tu rama] https://github.com/innovatesolutionstudio/Automatizacion_Farmacia.git
```

---

## Descargar una rama específica después de clonar

Si ya tienes el repositorio clonado y necesitas cambiar a otra rama:

1. Abre la terminal y navega al directorio del proyecto:
   ```bash
   cd [nombre_del_repositorio]
   ```

2. Cambia a la rama deseada:
   ```bash
   git checkout [nombre_de_la_rama]
   ```

3. Si la rama no existe localmente, primero tráela del repositorio remoto:
   ```bash
   git fetch origin [nombre_de_la_rama]
   git checkout [nombre_de_la_rama]
   ```

---

## Subir Cambios a una Rama

Sigue estos pasos para subir tus cambios:

1. Asegúrate de estar en la rama correcta:
   ```bash
   git checkout [nombre_de_la_rama]
   ```

2. Agrega los cambios realizados:
   ```bash
   git add .
   ```

3. Realiza un commit con un mensaje descriptivo:
   ```bash
   git commit -m "Descripción de los cambios realizados"
   ```

4. Sube los cambios al repositorio remoto:
   ```bash
   git push origin [nombre_de_la_rama]
   ```

---

## Actualizar una Rama

Para mantener tu rama sincronizada con los cambios más recientes de `main`:

### Si estás en la rama principal (`main`):
1. Asegúrate de estar en `main`:
   ```bash
   git checkout main
   ```

2. Trae los cambios más recientes:
   ```bash
   git pull origin main
   ```

### Si estás en otra rama:
1. Cambia a tu rama:
   ```bash
   git checkout [nombre_de_la_rama]
   ```

2. Combina los cambios de `main` en tu rama:
   ```bash
   git pull origin main
   git merge main
   ```

3. Resuelve conflictos (si los hay) y confirma:
   ```bash
   git add .
   git commit -m "Resolviendo conflictos de merge"
   ```

---

## Crear nueva rama

Si deseas crear una nueva rama al proyecto:

1. Haz un **fork** de este repositorio.
2. Crea una nueva rama para tus cambios:
   ```bash
   git checkout -b [nombre_de_tu_rama]
   ```

3. Realiza los cambios necesarios y súbelos a tu fork:
   ```bash
   git push origin [nombre_de_tu_rama]
   ```

4. Crea un **Pull Request** hacia la rama `main` de este repositorio.

---

5. Por si tienen algun fallo intentar estos pasos
   Activar su entorno virtual, les tiene que aparecer env en color verde al inicio
```bash
   .\env\Scripts\activate
```
   Verificar librerías a instalar
```bash
   pip install selenium webdriver-manager
   pip install pytest
```
   código para hacer correr el sistema de testeo del sistema para empleados
```bash
    pytest -s -v .\test_sistema_empleados\test_sistema.py
```
