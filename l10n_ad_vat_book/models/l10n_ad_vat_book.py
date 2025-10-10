from odoo import models, fields, api


class VatBook(models.TransientModel):
    _name = 'l10n.ad.vat.book'
    _description = 'Llibre IGI (VAT Book)'

    # Campos del asistente
    date_from = fields.Date(string="Desde", required=True)
    date_to = fields.Date(string="Fins a", required=True)
    invoice_type = fields.Selection([
        ('received', 'Factures rebudes'),
        ('issued', 'Factures emeses')
    ], string="Tipus de llibre", required=True, default='received')

    # -------------------------------------------------------------
    # ACCIÓN PRINCIPAL
    # -------------------------------------------------------------
    def get_vat_book(self):
        """
        Acción del botón que genera el llibre IGI (XLSX).
        Llama al controlador /web/binary/xlsx_vat_book/<book_id>
        """
        self.ensure_one()

        # Verificación rápida
        if not self.date_from or not self.date_to:
            return

        # Devuelve acción URL para abrir el Excel en una nueva pestaña
        return {
            'type': 'ir.actions.act_url',
            'url': f'/web/binary/xlsx_vat_book/{self.id}',
            'target': 'new',
        }

    # -------------------------------------------------------------
    # OBTENER FACTURAS (usado por el controlador)
    # -------------------------------------------------------------
    @api.model
    def get_invoices(self, date_from, date_to, invoice_type):
        """Devuelve las facturas según rango de fechas y tipo (emitidas o recibidas)."""
        AccountMove = self.env['account.move'].sudo()

        domain = [
            ('state', '=', 'posted'),
            ('invoice_date', '>=', date_from),
            ('invoice_date', '<=', date_to),
        ]

        if invoice_type == 'issued':
            domain.append(('move_type', 'in', ['out_invoice', 'out_refund']))
        elif invoice_type == 'received':
            domain.append(('move_type', 'in', ['in_invoice', 'in_refund']))

        return AccountMove.search(domain)
