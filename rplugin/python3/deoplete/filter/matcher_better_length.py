# ============================================================================
# FILE: matcher_better_length.py
# AUTHOR: Shougo Matsushita <Shougo.Matsu at gmail.com>
# AUTHOR: Christian Höltje <docwhat at gerf.org>
# License: MIT license
# ============================================================================

from .base import Base


class Filter(Base):

    def __init__(self, vim):
        super().__init__(vim)

        self.name = 'matcher_length'
        self.description = 'length matcher'

    def filter(self, context):
        input_len = len(context['complete_str'])
        return [x for x in context['candidates']
                if input_len <= len(x['word'])]
