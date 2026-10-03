# ¿Qué Como? — Sesión 6: Pruebas y Calidad

## Objetivo
Verificar la funcionalidad **Evaluar restaurante después de una transacción válida** mediante clases de equivalencia, valores límite, pruebas automatizadas, cobertura y análisis estático.

## Reglas verificadas
- La transacción debe existir.
- Debe pertenecer al usuario indicado.
- Debe pertenecer al restaurante indicado.
- Debe estar `COMPLETADA`.
- No debe haber sido evaluada previamente.
- La calificación debe estar entre 1 y 5.
- El comentario no puede estar vacío.
- La evaluación conserva la referencia de la transacción.
- El restaurante recibe la evaluación y actualiza su promedio.

## Estructura
```text
QueComo_Sesion6_GitHub/
├── src/que_como/
│   ├── domain/
│   ├── application/
│   └── infrastructure/
├── tests/
├── docs/
├── .github/workflows/quality.yml
├── pyproject.toml
├── requirements-dev.txt
└── .gitignore
```

## Instalar
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
```

## Ejecutar
```bash
pytest -v
pytest --cov=que_como --cov-report=term-missing --cov-report=html
ruff check .
```

## GitHub
```bash
git init
git add .
git commit -m "feat: implementa pruebas de calidad para evaluar restaurante"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/que-como.git
git push -u origin main
```

## Flujo
**Reglas → Equivalencias → Límites → Pruebas → Ejecución → Cobertura → Análisis → Mejora**
