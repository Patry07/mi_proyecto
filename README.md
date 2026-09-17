# Análisis de canciones y popularidad

## Descripción

Proyecto de análisis exploratorio de datos de canciones y artistas, utilizando Python para limpieza, análisis descriptivo y visualización de información relacionada con la popularidad musical.

## Dataset

- **Registros:** 8,058
- **Columnas:** 10
- **Archivo:** `data.csv`

El dataset contiene información sobre artistas, canciones, semanas en listas, posición máxima, streams y letras de canciones.

## Objetivo

Analizar la información del dataset para identificar patrones relacionados con la popularidad de las canciones, los artistas con mayor presencia y las canciones con mayor cantidad de streams.

El proyecto busca presentar los resultados mediante análisis descriptivo y visualizaciones.

## Estructura del proyecto

```text
mi_proyecto/
├── data.csv
├── proyecto.py
├── README.md
├── requirements.txt
├── .gitignore
├── grafica_artistas.png
└── grafica_streams.png
```

## Requisitos

- Python 3.12 o superior
- Git
- Entorno virtual de Python
- Pandas
- Matplotlib
- Seaborn

Las dependencias del proyecto se encuentran en `requirements.txt`.

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/Patry07/mi_proyecto.git
cd mi_proyecto
```

### 2. Crear el entorno virtual

```bash
python3 -m venv .venv
```

### 3. Activar el entorno virtual

```bash
source .venv/bin/activate
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

## Ejecución

Con el entorno virtual activado, ejecutar:

```bash
python proyecto.py
```

El programa carga el archivo `data.csv`, realiza el análisis y genera las visualizaciones.

## Análisis realizados

El proyecto realiza los siguientes análisis:

- Cantidad total de registros y columnas.
- Identificación de los artistas con mayor cantidad de canciones.
- Identificación de las canciones con mayor cantidad de streams.
- Estadísticas descriptivas de las semanas que las canciones permanecieron en listas.
- Generación de gráficas para facilitar la interpretación de los resultados.
- Generación de un resumen automático de los principales resultados.

## Resultados

El análisis del dataset obtuvo los siguientes resultados:

- El dataset contiene **8,058 registros** y **10 columnas**.
- **Drake** es el artista con mayor cantidad de canciones en el dataset.
- **Blinding Lights**, de The Weeknd, es la canción con mayor cantidad de streams.
- El promedio de semanas en listas es de **15.51 semanas**.

Las visualizaciones generadas permiten observar los artistas con mayor cantidad de canciones y las canciones con mayor cantidad de streams.

## Reproducibilidad

El proyecto está preparado para ser reproducido en otra computadora siguiendo estos pasos:

1. Clonar el repositorio.
2. Crear un entorno virtual nuevo.
3. Activar el entorno virtual.
4. Instalar las dependencias mediante `requirements.txt`.
5. Ejecutar `proyecto.py`.

El archivo `.gitignore` evita que el entorno virtual y archivos temporales sean incluidos en el repositorio.

## Autor

Patry07
