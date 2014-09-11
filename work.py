# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
from trytond.model import ModelSQL, ModelView, fields
from trytond.pyson import Eval
from trytond.transaction import Transaction
from trytond.pool import Pool, PoolMeta

__all__ = ['Work']
__metaclass__ = PoolMeta


class Work:
    __name__ = 'project.work'

    @classmethod
    def __setup__(cls):
        super(Work, cls).__setup__()
        milestone = ('milestone', 'Milestone')
        if milestone not in cls.type.selection:
            cls.type.selection.extend([milestone])
