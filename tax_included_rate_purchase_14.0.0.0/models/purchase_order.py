from odoo import fields,models,api

class PurchaseOrder(models.Model):
    _inherit = "purchase.order.line"

    tax_included_rate = fields.Float(string="Tax Included Rate")

    @api.onchange('tax_included_rate','taxes_id')
    def compute_tax_excluded_price(self):
        for rec in self:
            tax = rec.taxes_id.amount
            tax_included_rate = rec.tax_included_rate
            tax_excluded_rate = tax_included_rate/((100+tax)/100)
            if rec.tax_included_rate > 0:
                rec.write({
                    'price_unit': tax_excluded_rate,
                })
