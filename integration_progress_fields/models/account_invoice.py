# -*- coding: utf-8 -*-
# © <YEAR(S)> <AUTHOR(S)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import _, fields, models


class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    freight_expense_id = fields.Integer(
        _('Expense on Progress'),
    )
