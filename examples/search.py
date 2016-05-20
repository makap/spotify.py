from spotify.client import Spotify

import logging
import os

log = logging.getLogger(__name__)


class App(object):
    def __init__(self):
        self.sp = Spotify()

    def run(self):
        @self.sp.login(os.environ['USERNAME'], os.environ['PASSWORD'])
        def on_login():
            self.sp.search('daft punk', count=20, callback=self.on_search)

    def on_search(self, result):
        # Artists
        if result.artists:
            print 'artists (%s)' % len(result.artists)

            def on_artists(artists):
                for artist in artists:
                    print '\t[%s] "%s"' % (artist.uri, artist.name)

            self.sp.metadata([ar.uri for ar in result.artists], on_artists)

        # Albums
        if result.albums:
            print 'albums (%s)' % len(result.albums)

            def on_albums(albums):
                for album in albums:
                    print '\t[%s] "%s" - %s' % (album.uri, album.name, ', '.join([ar.name for ar in album.artists]))

            self.sp.metadata([al.uri for al in result.albums], on_albums)

        # Tracks
        if result.tracks:
            print 'tracks (%s)' % len(result.tracks)

            def on_tracks(tracks):
                for track in tracks:
                    print '\t[%s] "%s" - %s' % (track.uri, track.name, ', '.join([ar.name for ar in track.artists if ar.name]))

            self.sp.metadata([tr.uri for tr in result.tracks], on_tracks)

        # Playlists
        if result.playlists:
            print 'playlists (%s)' % len(result.playlists)

            for playlist in result.playlists:
                print '\t[%s] "%s"' % (playlist.uri, playlist.name)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)

    app = App()
    app.run()

    while True:
        raw_input()
