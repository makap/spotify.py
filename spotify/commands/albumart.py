from spotify.commands.base import Command

import execjs
import logging
import re
import traceback

log = logging.getLogger(__name__)

WORK_RUNNER = """
var run = function() {
  var window = { eval: eval };
  var res = null;

  var Spotify = {
    Utils: {
      Base62: {
        fromHex: function(data, length) {
          res = data;
        }
      },
      base62hex: function() {}
    }
  };

  %s

  return res;
}
"""

class AlbumArt(Command):
    def process(self, payload):
        # workaround execjs eval bug
        js = re.sub("\w+\[\d+\.\.toString\(\d\d<<0\)\]", "eval", payload[1].replace("\\'", "'"))

        try:
            ctx = execjs.compile(WORK_RUNNER % js)
            result = ctx.eval('run()')
        except execjs.RuntimeUnavailable, ex:
            self.emit('error', 'JavaScript runtime is not available, try installing node.js (http://nodejs.org)')
            return
        except Exception, ex:
            log.warn('Unable to run album_art - %s - %s', ex, traceback.format_exc())
            return

        self.sp.trackKeyQueue.get()(result)
