# Bases de Datos: Modelo Entidad-Relación

## Estructura del Curso

Cada carpeta dentro de `data/` (por ejemplo, `data/3/`, `data/4/`, etc.) contiene un archivo `index.html` y los recursos relacionados. El número de la carpeta corresponde al orden de los temas tal como se presentan en el curso.

### Temas Principales

- **Objectius i coneixements previs**:  
  Se presentan los objetivos del curso y los conocimientos que se esperan de los estudiantes antes de comenzar, como nociones básicas de bases de datos y lógica.

- **1. Introducció**:  
  Introducción al modelo Entidad-Relación. Se explica su origen, utilidad en el diseño conceptual de bases de datos y cómo facilita la representación de la información de forma gráfica.

- **2. Exemple**:  
  Se expone un ejemplo práctico que sirve como hilo conductor del curso. Se modela una situación real usando entidades, relaciones y atributos, lo que ayuda a comprender mejor los conceptos teóricos.

- **3. Les Entitats del Model E/R**:  
  Describe qué son las entidades, cómo se representan y su papel central en el modelo.

  - **3.1 Entitats**:  
    Definición formal de entidad. Se presentan ejemplos de entidades y cómo identificarlas en el mundo real.

  - **3.2 Atributs**:  
    Introducción a los atributos, que son propiedades o características de las entidades. Se analizan atributos simples, compuestos, derivados y multivaluados.

  - **3.3 Dominis**:  
    Se explican los dominios de los atributos, es decir, los conjuntos de valores válidos que puede tomar un atributo.

- **4. Les Relacions del Model E/R**:  
  Se abordan las relaciones entre entidades, cómo se modelan y qué tipo de información representan.

  - **4.1 Relació**:  
    Definición de relación como una asociación entre dos o más entidades.

  - **4.2 Atributs de Relació**:  
    Se detallan los atributos que pueden tener las relaciones para añadir información adicional sobre la conexión entre entidades.

  - **4.3 Tipus de Relació o Cardinalitat**:  
    Estudia la cardinalidad (uno a uno, uno a muchos, muchos a muchos) y cómo afecta al diseño del modelo.

- **5. Relacions de grau major que dos**:  
  Explicación de relaciones de grado superior a dos (también llamadas relaciones ternarias o n-arias), y su modelado correcto.

- **6. Model E/R Estès**:  
  Se amplía el modelo E/R básico con conceptos más avanzados.

  - **6.1 Cardinalitat màxima i mínima. Participació total.**  
    Se introduce el concepto de participación total (obligatoriedad de la relación) y se define la cardinalidad mínima y máxima.

  - **6.2 Entitats dèbils**:  
    Definición y características de las entidades débiles, que dependen de otras entidades para existir y tienen claves parciales.

  - **6.3 Generalització i herència**:  
    Se presenta la generalización como proceso para abstraer entidades comunes en una entidad superior. Se discute también la herencia de atributos y relaciones.

- **7. Restriccions externes**:  
  Se abordan restricciones que no se pueden representar gráficamente en el modelo E/R pero que son necesarias, como reglas de negocio.

- **Resum**:  
  Recapitulación de todos los conceptos aprendidos en el curso, organizada de forma clara y esquemática.

- **Exercicis**:  
  Conjunto de ejercicios prácticos para reforzar los conocimientos adquiridos a lo largo del curso.

## Navegación

- Abre `data/3/index.html` en tu navegador para empezar desde el índice principal.
- Todos los enlaces internos han sido actualizados para apuntar a los archivos locales correctos.
- Cada tema y subtema se puede acceder desde el menú de navegación en los archivos HTML.

## Script: Corrección de Enlaces

Se incluye un script en Python (`script.py`) que actualiza automáticamente todos los enlaces internos de los archivos HTML para que funcionen correctamente de forma local y offline.

### Instrucciones de uso

1. Asegúrate de tener Python 3 instalado.
2. Ejecuta el script desde la raíz del repositorio:
   ```sh
   python script.py
   ```
3. El script actualizará todos los archivos `index.html` dentro del directorio `data/` utilizando rutas absolutas a archivos locales.

## Licencia

El contenido de este curso está publicado bajo la licencia [Creative Commons Reconocimiento No Comercial Compartir Igual 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/).
