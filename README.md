# Bases de Dades: Model Entitat-Relació

This repository contains a complete offline copy of a course on the Entity-Relationship (E/R) database model, originally hosted on the Aules GVA platform. The course is structured into multiple HTML files, each representing a section or topic, and organized into numbered folders under the `data/` directory.

## Course Structure

Each folder inside `data/` (e.g., `data/3/`, `data/4/`, etc.) contains an `index.html` file and related assets. The folder number corresponds to the order of the topics as presented in the course.

### Main Topics Covered

- **Objectius i coneixements previs**: Course objectives and prerequisites.
- **1. Introducció**: Introduction to the E/R model.
- **2. Exemple**: Example to illustrate the concepts.
- **3. Les Entitats del Model E/R**: Entities in the E/R model.
  - **3.1 Entitats**: Definition and examples of entities.
  - **3.2 Atributs**: Attributes of entities.
  - **3.3 Dominis**: Domains of attributes.
- **4. Les Relacions del Model E/R**: Relationships in the E/R model.
  - **4.1 Relació**: Definition of relationships.
  - **4.2 Atributs de Relació**: Attributes of relationships.
  - **4.3 Tipus de Relació o Cardinalitat**: Types of relationships and cardinality.
- **5. Relacions de grau major que dos**: Relationships of degree greater than two.
- **6. Model E/R Estès**: Extended E/R model.
  - **6.1 Cardinalitat màxima i mínima. Participació total.**
  - **6.2 Entitats dèbils**: Weak entities.
  - **6.3 Generalització i herència**: Generalization and inheritance.
- **7. Restriccions externes**: External constraints.
- **Resum**: Summary of the course.
- **Exercicis**: Exercises for practice.

## Navigation

- Open `data/3/index.html` in your browser to start with the main index.
- All internal links have been updated to point to the correct local files.
- Each topic and subtopic can be accessed via the navigation menu in the HTML files.

## Script: Link Correction

A Python script (`script.py`) is included to automatically update all internal links in the HTML files to point to the correct local paths. This ensures seamless offline navigation.

### Usage

1. Make sure you have Python 3 installed.
2. Run the script from the root of the repository:
   ```sh
   python script.py
   ```
3. The script will update all `index.html` files in the `data/` directory to use absolute file paths for navigation.

## License

The course content is published under the [Creative Commons Reconocimiento No comercial Compartir igual 3.0](http://creativecommons.org/licenses/by-nc-sa/3.0/) license.
