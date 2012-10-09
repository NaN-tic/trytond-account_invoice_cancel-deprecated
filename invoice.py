#This file is part account_invoice_cancel module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import Workflow, ModelView, ModelSQL
from trytond.pyson import Eval
from trytond.pool import Pool, PoolMeta

__all__ = ['Invoice']
__metaclass__ = PoolMeta

class Invoice:
    __name__ = 'account.invoice'

    @classmethod
    def __setup__(cls):
        super(Invoice, cls).__setup__()
        # TODO: Ensure we're updating correctly transitions and buttons
        # TODO: Do we have to add copy()?
        cls._transitions |= set((
                ('open', 'cancel'),
                ('paid', 'cancel'),
                ))
        cls._buttons.update({
                'cancel': {
                    'invisible': Eval('state') == 'cancel',
                    },
                })

    @classmethod
    @ModelView.button
    @Workflow.transition('cancel')
    def cancel(self, invoices):
        pool = Pool()
        Move = pool.get('account.move')

        super(Invoice, self).cancel(invoices)
        todelete = []
        for invoice in invoices:
            if invoice.move:
                todelete.append(invoice.move)
        if todelete:
            Move.draft(todelete)
            Move.delete(todelete)
