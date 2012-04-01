#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.
from trytond.model import Workflow, ModelView, ModelSQL
from trytond.pyson import Eval
from trytond.pool import Pool

class Invoice(Workflow, ModelSQL, ModelView):
    _name = 'account.invoice'

    def __init__(self):
        super(Invoice, self).__init__()
        # TODO: Ensure we're updating correctly transitions and buttons
        # TODO: Do we have to add copy()?
        self._transitions |= set((
                ('open', 'cancel'),
                ('paid', 'cancel'),
                ))
        self._buttons.update({
                'cancel': {
                    'invisible': Eval('state') == 'cancel',
                    },
                })

    def cancel(self, ids):
        pool = Pool()
        move_obj = pool.get('account.move')

        super(Invoice, self).cancel(ids)
        todelete = []
        for invoice in self.browse(ids):
            if invoice.move:
                todelete.append(invoice.move.id)
        if todelete:
            move_obj.draft(todelete)
            move_obj.delete(todelete)

Invoice()
