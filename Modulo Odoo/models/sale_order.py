from Odoo import fields,models

class Ventas(models.model):
    
    _init_ = "sale.order"
    
    vat = fields.One2many("")