from spotify.objects.base import Descriptor, PropertyProxy

import logging

log = logging.getLogger(__name__)


class Genre(Descriptor):
    name = PropertyProxy
    templateName = PropertyProxy
    iconUrl = PropertyProxy

    type = PropertyProxy

    @staticmethod
    def __parsers__():
        return [Tunigo]

class Tunigo(Genre):
    __tag__ = 'genre'

    @classmethod
    def parse(cls, sp, data, parser):
        return Genre(sp, {
            'name': data.get('name'),
            'templateName': data.get('templateName'),
            'iconUrl': data.get('iconUrl'),
        }, parser.Tunigo, parser)
