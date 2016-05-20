from spotify.objects.base import Descriptor, PropertyProxy
from spotify.proto import search_pb2

import logging

log = logging.getLogger(__name__)


class SearchReply(Descriptor):
    __protobuf__ = search_pb2.SearchReply

    hits = PropertyProxy

    tracks = PropertyProxy('track', 'Track')
    albums = PropertyProxy('album', 'Album')
    artists = PropertyProxy('artist', 'Artist')
    playlists = PropertyProxy('playlist', 'SearchPlaylist')

    did_you_mean = PropertyProxy

    users = PropertyProxy('user', 'SearchUser')
