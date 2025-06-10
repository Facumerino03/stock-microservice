# Ingeniería de Software - Proyecto

## 📚 Información de la Materia

**Asignatura:** Ingeniería de Software  
**Curso:** 4º Año  
**Carrera:** Ingeniería en Informática  
**Profesor Titular:** Lic. Pablo Andrés Prats  

## 📝 Descripción del Microservicio de Stock

Este microservicio gestiona el stock de productos de la aplicación. Permite registrar, consultar, actualizar y eliminar información relacionada con las existencias de artículos, lotes y movimientos de inventario (entradas y salidas). Se encarga de mantener actualizado el inventario, calcular el stock disponible por artículo y asegurar la integridad de los datos relacionados con los productos almacenados.

Entre sus funcionalidades principales se encuentran:
- Registrar movimientos de stock (entradas y salidas) asociados a artículos y lotes.
- Consultar el stock actual de un producto.
- Gestionar la relación entre artículos, lotes y comprobantes de movimientos.
- Integrarse con otros microservicios para mantener la coherencia de la información en el sistema.

## 🛠️ Tareas del Proyecto

### Gestión del Proyecto
- [ ] Redacción de **historias de usuario**
- [ ] **Planificación y ejecución de Sprints** a través de **GitHub Projects**

### Diseño y Arquitectura
- [ ] Implementación de **diagramas de clases** (carpeta docs)
- [ ] Creación de **diagramas de secuencia** (carpeta docs)
- [ ] Aplicación de **arquitectura de microservicios**
- [ ] Patrones de **microservicios**:
    - Patrón API Gateway
    - Strangler
    - Decompose by Business Capability
- [ ] Diseño de **APIs** para comunicación entre servicios

### Desarrollo y Despliegue
- [ ] Creación y despliegue de **contenedores Docker**
    - Dockerfile
    - docker-compose.yml
    - Para construir:docker build -t microservice-stock:TAG .
    - Para construir una red:docker network create mired
    - Para ejecucción:docker compose up -d
- [ ] Implementación de servicios independientes (PostgreSQL) a través de contenedores.
- [ ] Aplicación de patrones de diseño

### Control de Versiones
- [ ] Uso de **Git** con flujos de trabajo **Trunk-based Development**
- [ ] **Versionado** adecuado del código

- Una arquitectura [Monolítica](https://github.com/Juanimaz10/Ingenieria_de_software)
- Metodologías ágiles utilizando Scrum a través de **GitHub Projects**
- Contenedor para servicios y para el proyecto con Docker (carpeta docker)

## 🏗️ Estructura del Proyecto

```
Gestión de Stock/
├── docs/
│   └── (diagramas)
├── app/
│   ├── models/
│   ├── controllers/
│   ├── mappings/
│   ├── services/
│   ├── routes/
│   └── repositories/
├── app/
├── docker/
│   ├── db
│   │   ├── data/
│   │   └── docker-compose.yml
│   └── app
│        └── docker-compose.yml
├── tests/
└── README.md
└── Dockerfile
```

## 🔧 Tecnologías Utilizadas

- **Lenguaje:** Python
- **Framework:** Flask
- **Arquitectura:** Microservicio Stock - Aplicación Cliente Servidor (Backend)
- **Control de Versiones:** Git
- **Comunicación:** APIs REST/JSON
- **Principios y Patrones:** YAGNI, SOLID, DRY, MVC, Repository

## 👥 Equipo de Desarrollo

- **Mauro Eliel Mato**
- **Facundo Merino**