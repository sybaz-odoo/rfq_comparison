# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    @api.model
    def purchase_comparison(self, records):
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        return {"type": "ir.actions.act_url", 'name': "Purchase Comparison Chart",
                "url": base_url + "/web/purchase_comparison?purchase_comp_rpt_type=htm&rfq_ids={}".format(records.ids),
                }
