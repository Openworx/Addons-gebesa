# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _, fields, models


class AccountInvoice(models.Model):
    _name = 'account.invoice'
    _inherit = 'account.invoice'

    factoring_customer_id = fields.Many2one(
        'factoring.customer',
        string=_(u'Factoring Customer'))

    factoring_supplier_id = fields.Many2one(
        'factoring.supplier',
        string=_(u'Factoring Supplier'))