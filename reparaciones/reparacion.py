#-*- coding: utf-8 -*-
from odoo import models, fields, api

class reparacion(models.Model):
    _name = 'reparacion.reparacion'
    incidencia = fields.Char(string="Incidencia", required=True)
    cliente = fields.Char(string="Cliente", required=True)
    empleado = fields.Char(string="Empleado")
    fecha = fields.Date(string="Fecha Entrada", required=True)

    def borrar_dato(self):
        self.write({
            'incidencia': '',
            'cliente': '',
            'empleado': '',
            'fecha': ''
        })

    def nombre_get(self):
        lista = []
        for record in self:
            name = record.incidencia
            lista.append(record.incidencia)
        return lista