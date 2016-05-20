from spotify.components.base import Component
from spotify.core.uri import Uri
from spotify.objects.base import Descriptor, PropertyProxy
from spotify.objects.image import Image
from spotify.proto import search_pb2


def create_image(uri):
    uri = Uri.from_uri(uri)

    if uri is None:
        return None

    return Image.from_id(uri.code)

class SearchUser(Descriptor):
    __protobuf__ = search_pb2.User

    username = PropertyProxy()
    full_name = PropertyProxy
    image = PropertyProxy('image', 'Image')
    followers = PropertyProxy

class User(Component):
    def __init__(self, sp, username):
        super(User, self).__init__(sp)

        self.username = username

    def playlists(self, start=0, count=100, callback=None):
        return self.sp.playlists(
            self.username,
            start, count,
            callback
        )

    def collection(self, source, params=None, callback=None):
        return self.sp.collection(
            self.username,
            source, params,
            callback
        )
