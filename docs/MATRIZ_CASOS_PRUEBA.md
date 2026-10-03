# Matriz de casos de prueba

## Estado de transacción

| Caso | Entrada | Clase | Resultado |
|---|---|---|---|
| T01 | COMPLETADA | Válida | Aceptar |
| T02 | INICIADA/PENDIENTE/CONFIRMADA/CANCELADA | Inválida | Rechazar |

## Calificación

Regla: `1 <= calificación <= 5`

| Caso | Entrada | Clase | Resultado |
|---|---:|---|---|
| T03 | 1 | Límite inferior válido | Aceptar |
| T04 | 5 | Límite superior válido | Aceptar |
| T05 | 0 | Debajo del límite | Rechazar |
| T05 | 6 | Encima del límite | Rechazar |

## Comentario

| Caso | Entrada | Clase | Resultado |
|---|---|---|---|
| T01 | Texto | Válida | Aceptar |
| T06 | vacío/espacios/tab | Inválida | Rechazar |

## Relación con la transacción

| Caso | Situación | Resultado |
|---|---|---|
| T07 | Usuario diferente | Rechazar |
| T08 | Restaurante diferente | Rechazar |
| T09 | Transacción inexistente | Rechazar |
| T10 | Transacción ya evaluada | Rechazar |

## Trazabilidad e integración

| Caso | Verificación | Resultado |
|---|---|---|
| T11 | Evaluación vinculada a transacción | Correcto |
| T12 | Restaurante recibe evaluación y recalcula promedio | Correcto |
