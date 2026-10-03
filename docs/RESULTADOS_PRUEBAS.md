# Resultados de pruebas — ¿Qué Como?

## Pruebas automatizadas

Comando:

```bash
pytest -v
```

Resultado real:

```text
18 passed
```

La suite tiene 12 funciones de prueba y 18 casos ejecutados debido a los casos parametrizados.

## Cobertura

Comando:

```bash
pytest --cov=que_como --cov-report=term-missing
```

Resultado real:

```text
src/que_como/application/controlador_evaluacion.py  100%
src/que_como/domain/evaluacion.py                    89%
src/que_como/domain/restaurante.py                   88%
src/que_como/domain/transaccion.py                   96%
src/que_como/domain/usuario.py                        0%
src/que_como/infrastructure/repositories.py         86%
TOTAL                                                83%
```

## Análisis estático

Comando previsto:

```bash
ruff check .
```

En el entorno utilizado para esta verificación local, Ruff no estaba instalado. El repositorio **sí incluye Ruff en `requirements-dev.txt` y en el Quality Gate de GitHub Actions**, por lo que GitHub lo ejecutará automáticamente después de instalar las dependencias.

## Evidencias recomendadas

1. Captura de `pytest -v`.
2. Captura de cobertura.
3. Resultado de `ruff check .` en GitHub Actions.
4. Evidencia de la ejecución del workflow `Quality Gate`.
5. Pull Request revisada, si se trabaja con ramas.

## Interpretación

Las pruebas verifican:

- transacción completada;
- estados no completados;
- límites 1 y 5;
- valores 0 y 6;
- comentarios vacíos o con espacios;
- usuario incorrecto;
- restaurante incorrecto;
- transacción inexistente;
- evaluación duplicada;
- trazabilidad de la evaluación;
- actualización del promedio del restaurante.

La cobertura del 83% es evidencia de ejecución de una parte importante del código, pero no demuestra por sí sola la corrección total del software. También existen módulos o ramas que requieren pruebas adicionales, especialmente `Usuario` y algunas ramas defensivas de dominio/repositorios.
