from spotify.hermes.request import HermesRequest
from spotify.objects.search_reply import SearchReply
from spotify.proto import search_pb2

import logging
import operator

log = logging.getLogger(__name__)


class SearchRequest(HermesRequest):
    types = {
        'tracks': search_pb2.SearchRequest.TRACK,
        'albums': search_pb2.SearchRequest.ALBUM,
        'artists': search_pb2.SearchRequest.ARTIST,
        'playlists': search_pb2.SearchRequest.PLAYLIST,
        'users': search_pb2.SearchRequest.USER
    }

    def __init__(self, sp, query, query_type='tracks', start=0, count=10):
        super(SearchRequest, self).__init__(sp, {
                'method': 'GET',
                'uri': 'hm://search/search'
            }, SearchReply
        )

        self.request_payload = search_pb2.SearchRequest()
        self.request_payload.query = query
        self.request_payload.type = self.types[query_type]
        self.request_payload.limit = count * 2 if not count % 10 else 20 # WTF Spotify?! Ya drunk?
        self.request_payload.offset = start
