# Devops1 — Microservicio Demo

Microservicio FastAPI usado como base para el pipeline DevOps.
Integrantes: [Francisca Alarcón] y [Jaime Barrales]

## ¿Por qué GitFlow?
Elegimos GitFlow porque separa claramente producción (`main`) de desarrollo (`develop`), facilita el trabajo en pareja con ramas independientes por funcionalidad, y da trazabilidad clara vía Pull Requests. Trunk-based exige más disciplina y CI/CD maduro, que no aplica a un proyecto académico.

## Ramas
- `main`: producción
- `develop`: integración de features
- `feature/<nombre>`: nace de develop, vuelve a develop
- `hotfix/<nombre>`: nace de main, vuelve a main y develop

## Commits (Conventional Commits)
`feat:` nueva funcionalidad · `fix:` corrección · `docs:` documentación · `ci:` pipeline · `test:` pruebas

## Estructura
microservicio-demo/
├── app/ # código fuente
├── tests/ # pruebas
└── requirements.txt

## Revisión de PRs
Cada PR debe ser revisado por el compañero antes de mergear, verificando que Actions pase en verde y los tests no se rompan.

## Uso de IA
Se usó Claude para depurar errores de configuración (Python/pip, GitHub Actions) y redactar este README. Decisiones técnicas y reflexiones son propias del equipo.

## Reflexiones individuales
**[Jaime Barrales]:** En el transcurso de la evaluación vimos distintas formas de trabajar en conjunto mediante github como la creación de ramas para mantener el código estable, aprendí desde lo más básico como un commit hasta la configuración del entorno para trabajar de forma fluida, entre demás cosas.

**[Francisca Alarcón]:** Durante este trabajo, aprendí a colaborar en GitHub, mediante branches, Pull Request, Workflows, entre otras cosas. 
A resolver problemas como instalación de pip, a entender lo que era un HotFix, a como funcionaba los workflows y los distintos tipos que existen.
