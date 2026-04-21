# Tarea 1: Herramientas de Visualización de Datos

### Descripción del Proyecto
Este proyecto forma parte del curso de Visualización de Datos (Semestre I, 2026). El tema central seleccionado por el grupo es **Series de Televisión y Streaming**, el cual será analizado a través de distintas dimensiones a lo largo del semestre para contribuir a un trabajo de periodismo de datos final.

### Integrantes
* **Francisco Pino** - Rol: 202373051-3 - Dimensión: Audiencia y Recepción
* **Moisés Villarroel** - Rol:202373016-5 - Dimensión: Producción y Oferta

### Requisitos e Instalación (Ubuntu)
Para ejecutar el código de este proyecto, es necesario contar con Python 3 instalado y las siguientes librerías:

1. **Instalar dependencias:**
   ```bash
   pip install pandas matplotlib textblob numpy

Para generar el gráfico de Dumbbell Plot:
- Instalar las librerías que se importan en audiencia.py (en caso de no tenerlas)
- Descargar los modelos de lenguaje que usa internamente para procesar el texto, con los siguientes comandos:
1- pip install textblob 
2- python3 -m textblob.download_corpora