from odoo import models, fields, api


class MaterialRequisition(models.Model):
    _name = 'material.requisition'
    _description = 'Material Requisition'
    _order = 'date desc, id desc'

    name = fields.Char(string='Requisition Number', required=True, copy=False, readonly=True, default='New')
    date = fields.Date(string='Requisition Date', required=True, default=fields.Date.context_today)
    department = fields.Char(string='Department')
    requested_by = fields.Many2one('res.users', string='Requested By', default=lambda self: self.env.user)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('done', 'Done'),
    ], string='Status', default='draft', tracking=True)
    
    line_ids = fields.One2many('material.requisition.line', 'requisition_id', string='Requisition Lines')
    notes = fields.Text(string='Notes')
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('material.requisition') or 'New'
        return super(MaterialRequisition, self).create(vals)
    
    def action_submit(self):
        self.state = 'submitted'
    
    def action_approve(self):
        self.state = 'approved'
    
    def action_reject(self):
        self.state = 'rejected'
    
    def action_reset_to_draft(self):
        self.state = 'draft'


class MaterialRequisitionLine(models.Model):
    _name = 'material.requisition.line'
    _description = 'Material Requisition Line'

    requisition_id = fields.Many2one('material.requisition', string='Requisition', ondelete='cascade')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Float(string='Quantity', required=True, default=1.0)
    notes = fields.Text(string='Notes')
    
    @api.onchange('product_id')
    def _onchange_product_id(self):
        if self.product_id:
            self.notes = self.product_id.description or ''