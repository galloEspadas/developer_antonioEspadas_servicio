from Odoo import fields,models

class Clientes(models.model):
    
    _init_ = "res.partner"
    
    vat = fields.One2many("")