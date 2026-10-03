from datetime import date
import pytest

from que_como.application.controlador_evaluacion import ControladorEvaluacion
from que_como.domain.restaurante import Restaurante
from que_como.domain.transaccion import EstadoTransaccion, Transaccion
from que_como.infrastructure.repositories import (
    RepositorioEvaluacion,
    RepositorioRestaurante,
    RepositorioTransaccion,
)

class TestEvaluacionRestaurante:
    def setup_method(self):
        self.repo_transaccion = RepositorioTransaccion()
        self.repo_evaluacion = RepositorioEvaluacion()
        self.repo_restaurante = RepositorioRestaurante()

        self.restaurante = Restaurante(10, "Restaurante Demo", "Restaurante de prueba")
        self.repo_restaurante.agregar(self.restaurante)

        self.transaccion = Transaccion(
            100, 1, 10, date.today(), 250.00, EstadoTransaccion.COMPLETADA
        )
        self.repo_transaccion.agregar(self.transaccion)

        self.controlador = ControladorEvaluacion(
            self.repo_transaccion, self.repo_evaluacion, self.repo_restaurante
        )

    def test_T01_transaccion_completada_permite_evaluacion(self):
        evaluacion = self.controlador.evaluar_restaurante(1, 10, 100, 5, "Excelente servicio")
        assert evaluacion.calificacion == 5
        assert evaluacion.transaccion_id == 100

    @pytest.mark.parametrize("estado", [
        EstadoTransaccion.INICIADA,
        EstadoTransaccion.PENDIENTE,
        EstadoTransaccion.CONFIRMADA,
        EstadoTransaccion.CANCELADA,
    ])
    def test_T02_estados_no_completados_rechazan(self, estado):
        self.transaccion.estado = estado
        with pytest.raises(ValueError, match="no puede utilizarse"):
            self.controlador.evaluar_restaurante(1, 10, 100, 5, "Comentario válido")

    def test_T03_calificacion_1_es_valida(self):
        e = self.controlador.evaluar_restaurante(1, 10, 100, 1, "Comentario válido")
        assert e.calificacion == 1

    def test_T04_calificacion_5_es_valida(self):
        e = self.controlador.evaluar_restaurante(1, 10, 100, 5, "Comentario válido")
        assert e.calificacion == 5

    @pytest.mark.parametrize("calificacion", [0, 6])
    def test_T05_calificacion_fuera_de_limites_rechaza(self, calificacion):
        with pytest.raises(ValueError, match="Datos de evaluación inválidos"):
            self.controlador.evaluar_restaurante(1, 10, 100, calificacion, "Comentario válido")

    @pytest.mark.parametrize("comentario", ["", "   ", "\t"])
    def test_T06_comentario_vacio_o_blanco_rechaza(self, comentario):
        with pytest.raises(ValueError, match="Datos de evaluación inválidos"):
            self.controlador.evaluar_restaurante(1, 10, 100, 5, comentario)

    def test_T07_usuario_incorrecto_rechaza(self):
        with pytest.raises(ValueError, match="no pertenece al usuario"):
            self.controlador.evaluar_restaurante(999, 10, 100, 5, "Comentario válido")

    def test_T08_restaurante_incorrecto_rechaza(self):
        with pytest.raises(ValueError, match="no pertenece al restaurante"):
            self.controlador.evaluar_restaurante(1, 999, 100, 5, "Comentario válido")

    def test_T09_transaccion_inexistente_rechaza(self):
        with pytest.raises(ValueError, match="No existe"):
            self.controlador.evaluar_restaurante(1, 10, 999, 5, "Comentario válido")

    def test_T10_transaccion_ya_evaluada_rechaza_segunda_evaluacion(self):
        self.controlador.evaluar_restaurante(1, 10, 100, 5, "Primera evaluación")
        with pytest.raises(ValueError, match="no puede utilizarse"):
            self.controlador.evaluar_restaurante(1, 10, 100, 4, "Segunda evaluación")

    def test_T11_evaluacion_queda_vinculada_a_transaccion(self):
        e = self.controlador.evaluar_restaurante(1, 10, 100, 4, "Buena experiencia")
        assert self.transaccion.evaluacion is e
        assert e.transaccion_id == self.transaccion.id

    def test_T12_restaurante_actualiza_promedio(self):
        self.controlador.evaluar_restaurante(1, 10, 100, 4, "Buena experiencia")
        assert self.restaurante.calificacion_promedio == 4.0
        assert len(self.restaurante.evaluaciones) == 1
