import requests, json
from spotify.commands.base import Command

import logging

log = logging.getLogger(__name__)


class PingFlash2(Command):
    def process(self, ping):
        spotlite_host = "http://spotlite.cloudapp.net/api/pong/"
        spotifypy_host = "http://spflash.herokuapp.com/generic/get?ping="
        nodespotifyweb_host = "http://ping-pong.spotify.nodestuff.net/"

        # Try spotlite api
        try:
            req = requests.get(spotlite_host + ping.replace(' ', '_'), timeout=5)
            pong = req.content.strip('"')
            if (pong == "None") or (req.status_code != 200):
                raise Exception()
        except Exception, err:
            log.debug('spotlite API seems down. Now trying spotify.py API. ' + str(err))
            # Try spotify.py api
            try:
                req = requests.get(spotifypy_host + ping, timeout=5)
                pong = req.content
                if req.status_code != 200:
                    raise Exception()
            except Exception:
                log.debug('spotify.py API seems down. Now trying node-spotify-web API.')
                # Try node-spotify-web api
                try:
                    req = requests.get(nodespotifyweb_host + ping.replace(' ', '-'), timeout=5)
                    json = json.loads(req.content)
                    if (json['status'] != 100) or (req.status_code != 200):
                        raise Exception()
                    pong = json['pong'].replace('-', ' ')
                except Exception:
                    log.debug('node-web-spotify API seems down.')
                    log.debug('All available APIs seemed down.')
                    return

        log.debug('received ping %s, sending pong: %s' % (ping, pong))

        return self.send('sp/pong_flash2', pong)