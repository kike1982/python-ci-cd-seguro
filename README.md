# Python CI/CD Seguro

Este proyecto es un ejemplo de **puesta en producción segura** de una aplicación Python usando **integración continua (CI)** con **GitHub Actions**.

## Qué hace

- Ejecuta **tests unitarios automáticamente** cada vez que se hace un push o pull request a la rama principal.
- Calcula el **coverage** del código con `pytest-cov`.
- Garantiza que solo código **probado y seguro** llegue a la rama principal.
- Base para futuras mejoras:
  - Análisis estático con SonarQube
  - Generación y firma de binarios
  - Despliegue en contenedores Docker
  - Orquestación con Jenkins

## Estructura del proyecto
python-ci-cd-seguro/
├── app/                # Carpeta del código principal
│   └── main.py         # Funciones de la aplicación
├── tests/              # Carpeta de tests unitarios
│   └── test_main.py    # Test para main.py
├── pytest.ini          # Configuración de pytest
└── .github/
    └── workflows/
        └── ci.yml     # Pipeline CI/CD con GitHub Actions


## Tecnologías

- Python 3.10  
- Pytest y pytest-cov  
- GitHub Actions
