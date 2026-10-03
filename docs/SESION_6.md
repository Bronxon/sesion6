# Actividad — Sesión 6

## Objetivo
Generar evidencia de que la funcionalidad construida en la Sesión 5 se comporta de acuerdo con las reglas del dominio.

## Funcionalidad
**Evaluar restaurante después de una transacción válida.**

## Flujo aplicado
1. Recuperar funcionalidad.
2. Identificar reglas de negocio.
3. Diseñar clases de equivalencia.
4. Diseñar valores límite.
5. Automatizar casos.
6. Ejecutar pruebas.
7. Medir cobertura.
8. Identificar zonas de atención.
9. Documentar resultados.

## Verificación
Se comprueba que la implementación respeta las reglas y decisiones de diseño.

## Validación
Se comprueba que el comportamiento atiende la necesidad para la que fue construido.

## Cobertura
La cobertura indica qué parte de la estructura interna fue ejecutada. No demuestra por sí sola que todo el comportamiento sea correcto.

## Análisis estático
Se incorpora Ruff:

```bash
ruff check .
```

## Quality Gate
El repositorio automatiza:

**Pruebas → Cobertura → Análisis estático → Integración**

## Conclusión
La evidencia debe utilizarse para afirmar únicamente los comportamientos realmente verificados y señalar las zonas que requieran mayor atención.
