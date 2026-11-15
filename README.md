# Plataforma de Vinculación para Prácticas Profesionales

Proyecto integrador para la materia de **Cómputo en la Nube** - Universidad Autónoma de Sinaloa (UAS).

**Equipo:** Los Ingenieros
*   Valencia Zavala Gael Edgardo (Arquitecto de solución y documentación)
*   Román Zamora José Humberto (Responsable de desarrollo, seguridad y costos)

## Descripción del Proyecto
Plataforma web centralizada que conecta a estudiantes con empresas para facilitar la búsqueda y gestión de prácticas profesionales y residencias. Desplegada en AWS con una arquitectura tolerante a fallos, separación de subredes públicas/privadas y servicios gestionados.

## Arquitectura Implementada
*   **Red:** Amazon VPC de dos capas (pública/privada).
*   **Cómputo:** Instancias EC2 (Ubuntu + Apache) gestionadas por un Auto Scaling Group.
*   **Balanceo:** Application Load Balancer (ALB).
*   **Base de Datos Relacional:** Amazon RDS (MySQL) para datos transaccionales.
*   **Base de Datos NoSQL:** Amazon DynamoDB para búsquedas rápidas de vacantes.
*   **Serverless:** AWS Lambda para consultas bajo demanda.
*   **Almacenamiento:** Amazon S3 para sitio estático y archivos.

## Estructura del Repositorio
*   `/sql`: Scripts de creación de tablas en MySQL (RDS).
*   `/lambda_python`: Código de la función Serverless y operaciones a DynamoDB.
*   `/web`: Archivos del sitio web estático y plantilla de servidor.