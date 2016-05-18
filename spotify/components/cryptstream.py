from spotify.components.base import Component

from hashlib import sha1
import binascii
import hmac
import logging

log = logging.getLogger(__name__)

class EncryptedStream(Component):
    def __init__(self, sp, songKey):
        """Stream decrypts encrypted MP3_160_ENC files

        :param songKey: song key given in `trackUri` result
        :type songKey: str
        """
        self.songKey = songKey

        # required for RC4
        self.box = []
        self.x = 0
        self.y = 0

        key = self.generateStreamKey()
        log.debug("EncryptedStream: key(%s)", key)

        key = binascii.unhexlify(key)

        # initialize scheduling
        self.box = range(0, 256)

        self.x = 0
        for i in range(0, 256):
            self.x = (self.x + self.box[i] + ord(key[i % len(key)])) % 256

            t = self.box[self.x]
            self.box[self.x] = self.box[i]
            self.box[i] = t

        # play 4096 pick-up
        self.x = 0
        self.y = 0
        for i in range(0, 4096):
            self.x = (self.x + 1) % 256
            self.y = (self.y + self.box[self.x]) % 256

            t = self.box[self.x]
            self.box[self.x] = self.box[self.y]
            self.box[self.y] = t

    def generateStreamKey(self):
        """Generates stream key based off `album_art` result.

        :param songKey: songKey from `album_art` result.
        :type songKey: str

        :return: streamKey
        """
        param1 = binascii.unhexlify(self.songKey)
        swfKey = binascii.unhexlify("ed02752011affd6290ea42cf73fe0b99")

        keys = ["8cb926e087917795914a339035fa3bc6",
                "a3285211c9d1f2364e4237c7b47cc71d",
                "72ed1f6317d1923b94ebfd8a3d867c97"]

        finalKey = param1[-16:]

        j = 0
        for i in range(0, len(keys)):
            msg = param1[j:j + 16]
            correctHmac = param1[j + 16:j + 32]
            checkHmac = hmac.new(binascii.unhexlify(keys[i]), msg, sha1).digest()

            if correctHmac in checkHmac:
                finalHmac = hmac.new(swfKey, msg, sha1).digest()

                result = ""
                for k in range(0, len(finalKey)):
                    result += chr(ord(finalHmac[k][0]) ^ ord(finalKey[k][0]))

                return binascii.hexlify(result)
            j += 32

    def decrypt(self, chunk):
        chunk = bytearray(chunk)

        buf = bytearray()
        for i in range(0, len(chunk)):
            self.x = (self.x + 1) % 256
            self.y = (self.y + self.box[self.x]) % 256

            t = self.box[self.x]
            self.box[self.x] = self.box[self.y]
            self.box[self.y] = t

            buf.append(chunk[i] ^ self.box[(self.box[self.x] + self.box[self.y]) % 256])

        return buf