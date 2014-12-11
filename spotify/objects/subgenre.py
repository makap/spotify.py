from spotify.objects.base import Descriptor, PropertyProxy

import logging

log = logging.getLogger(__name__)


class Subgenre(Descriptor):
    name = PropertyProxy
    key = PropertyProxy

    type = PropertyProxy

    @staticmethod
    def __parsers__():
        return [Tunigo]

class Tunigo(Subgenre):
    __tag__ = 'subgenre'

    @classmethod
    def parse(cls, sp, data, parser):
        return Subgenre(sp, {
            'name': data.get('name'),
            'key': data.get('key')
        }, parser.Tunigo, parser)
