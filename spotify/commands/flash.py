import requests, json
from spotify.commands.base import Command

import logging

log = logging.getLogger(__name__)


class PingFlash2(Command):
    def process(self, ping):
        ab = ping.split(' ')
        a = {}

        for L in range(0, len(ab)):
            wa = int(ab[L])
            a[4 * L + 1] = wa & 255
            a[4 * L + 2] = wa >> 8 & 255
            a[4 * L + 3] = wa >> 16 & 255
            a[4 * L + 4] = wa >> 24 & 255

        n = a[0] = 1
        r = a[0]
        H = a[r + 4]
        b = a[0]
        C = a[b + 24]
        A = b + 24
        if H < C:
            b = a[0]
            c = a[b + 28]
            a[A] = c
            a[b + 28] = C
            C = c
        ha = a[0]
        b = a[ha + 64]
        G = b ^ 42
        a[ha + 64] = G
        l = a[0]
        b = a[l + 56]
        N = b ^ 42
        a[l + 56] = N
        b = a[0]
        h = b + 20
        Ba = a[b + 20]
        b = Ba ^ 23
        c = a[0]
        x = c + 68
        q = a[c + 68]
        c = q ^ 201
        if b >= c:
            b = a[0]
            va = a[b + 8]
        else:
            b = a[0]
            c = a[b + 72]
            c ^= 65
            a[b + 72] = c
            b = a[0]
            c = a[b + 8]
            va = c ^ 65
            a[b + 8] = va
        B = a[0]
        b = a[B + 48]
        da = b ^ 136
        a[B + 48] = da
        v = a[0]
        b = a[v + 52]
        Y = b ^ 136
        a[v + 52] = Y
        Ja = a[0]
        J = a[Ja + 36]
        za = a[n]
        a[Ja + 36] = za
        a[n] = J
        c = C ^ 127
        b = va ^ 39
        bb = a[0]
        if b < c:
            J ^= 186
            a[n] = J
            b = a[0]
            c = a[b + 44]
            c ^= 186
            a[b + 44] = c
        Za = a[0]
        z = a[Za + 16]
        Oa = C
        if z < Ba:
            a[A] = Y
            a[v + 52] = C
            Oa = Y
            Y = C
        k = Za + 16
        u = a[0]
        b = a[u + 76]
        a[u + 76] = H
        D = Y ^ 4
        a[v + 52] = D
        K = a[0]
        Ca = a[K + 40]
        c = Ca ^ 4
        a[K + 40] = c
        Aa = a[0]
        ya = a[Aa + 72]
        a[Aa + 72] = z
        a[k] = ya
        Da = Oa ^ 188
        a[A] = Da
        Ua = b ^ 188
        a[r + 4] = Ua
        w = a[0]
        U = a[w + 12]
        a[w + 12] = N
        a[l + 56] = U
        Na = a[0]
        ra = a[Na + 28]
        ia = da
        if ra < da:
            a[B + 48] = G
            a[ha + 64] = da
            ia = G
            G = da
        O = N
        if q < N:
            a[w + 12] = H
            a[u + 76] = N
            O = H
            H = N
        b = U ^ 41
        c = H ^ 253
        if c < b:
            c = a[0]
            b = a[c + 32]
            a[c + 32] = D
            D = a[v + 52] = b
        ma = J
        if z < Da:
            a[x] = J
            ma = a[n] = q
            q = J
        Ya = a[0]
        b = G ^ 193
        na = a[Ya + 44]
        c = na ^ 54
        if c < b:
            U ^= 51
            a[l + 56] = U
            O ^= 51
            a[w + 12] = O
        e = Ja + 36
        V = Aa + 72
        ba = Na + 28
        a[x] = D
        a[e] = q
        a[v + 52] = za
        b = O ^ 15
        a[w + 12] = b
        b = ra ^ 15
        a[ba] = b
        a[V] = ya
        a[k] = z
        c = G ^ 89
        qa = a[0]
        ua = a[qa + 60]
        b = ua ^ 204
        ds = D
        if b < c:
            a[x] = q
            a[e] = D
            ds = q
            q = D
        ea = bb + 8
        ga = Ya + 44
        b = ma ^ 9
        a[n] = b
        b = 59 * Ua
        b += 8555
        Ha = b % 255
        a[r + 4] = Ha
        b = 220 * va
        b += 53020
        ja = b % 255
        a[ea] = ja
        b = O ^ 184
        b *= 141
        P = b % 255
        a[w + 12] = P
        Ra = z ^ 25
        a[k] = Ra
        b = 153 * Ba
        b %= 255
        ca = b ^ 37
        a[h] = ca
        b = 214 * Da
        b += 15622
        Ma = b % 255
        a[A] = Ma
        b = ra ^ 162
        a[ba] = b
        Qa = a[0]
        a[Qa + 32] = 0
        b = 149 * q
        b %= 255
        ka = b ^ 138
        a[e] = ka
        b = Ca ^ 114
        a[K + 40] = b
        b = U ^ 223
        W = b % 255
        a[ga] = W
        Xa = ia ^ 191
        a[B + 48] = Xa
        S = na ^ 166
        a[v + 52] = S
        b = za ^ 84
        b *= 25
        sa = b % 255
        a[l + 56] = sa
        b = ua ^ 216
        a[qa + 60] = b
        b = 65 * G
        b += 12675
        Q = b % 255
        a[ha + 64] = Q
        b = 151 * ds
        b += 20234
        m = b % 255
        a[x] = m
        b = 49 * ya
        xa = b % 255
        g = xa ^ 103
        a[V] = g
        b = 198 * H
        Ta = b % 255
        Sa = Ta ^ 84
        a[u + 76] = Sa
        c = P ^ 208
        b = sa ^ 192
        Ga = ka
        if b < c:
            a[h] = ka
            Ga = a[e] = ca
            ca = ka
        R = Ga ^ 74
        a[e] = R
        a[u + 76] = Xa
        a[B + 48] = Sa
        d = ca ^ 38
        a[h] = d
        b = ma ^ 101
        a[n] = b
        a[x] = Ra
        a[k] = m
        b = P ^ 199
        c = xa ^ 206
        if c < b:
            m ^= 89
            a[k] = m
            R = Ga ^ 19
            a[e] = R
        Ia = ra ^ 128
        a[ba] = Ia
        La = ma ^ 71
        a[n] = La
        T = P
        if ja < g:
            a[e] = P
            T = a[w + 12] = R
            R = P
        F = ia ^ 26
        a[u + 76] = F
        f = Ha ^ 165
        a[r + 4] = f
        if F < m:
            f = Ha ^ 98
            a[r + 4] = f
            d = ca ^ 225
            a[h] = d
        b = W ^ 230
        a[ga] = b
        oa = Ca ^ 148
        a[K + 40] = oa
        b = ja ^ 52
        c = W ^ 215
        E = oa
        if c < b:
            a[K + 40] = f
            a[r + 4] = oa
            E = f
            f = oa
        pa = Qa + 32
        a[pa] = 130
        fa = ua ^ 90
        a[qa + 60] = fa
        p = sa ^ 92
        a[l + 56] = p
        Wa = z ^ 69
        a[x] = Wa
        c = d ^ 247
        b = d ^ 79
        if b < c:
            g = xa ^ 114
            a[V] = g
            m ^= 21
            a[k] = m
        la = R ^ 227
        a[e] = la
        Ka = ja ^ 227
        a[ea] = Ka
        c = g ^ 104
        b = T ^ 107
        t = la
        if b < c:
            a[e] = d
            a[h] = la
            t = d
            d = la
        b = 115 * La
        Fa = b % 255
        b = Fa ^ 11
        a[n] = b
        b = Q ^ 35
        c = na ^ 6
        if c < b:
            b = 35 * f
            b %= 255
            f = b ^ 219
            a[r + 4] = f
        b = 74 * Ka
        Ea = b % 255
        aa = Ea ^ 234
        a[ea] = aa
        if E < Ia:
            b = 150 * T
            b += 4650
            T = b % 255
            a[w + 12] = T
        b = m << 4
        Va = b % 255
        I = Va ^ 201
        a[k] = I
        if F < aa:
            b = d ^ 39
            b *= 91
            d = b % 255
            a[h] = d
        b = 247 * Ma
        Pa = b % 255
        M = Pa ^ 211
        a[A] = M
        b = 147 * Ia
        b += 6468
        c = b % 255
        a[ba] = c
        a[pa] = 201
        b = na ^ 43
        c ^= 248
        if c < b:
            b = 30 * t
            b += 6180
            t = b % 255
            a[e] = t
        c = z ^ 161
        b = Ea ^ 121
        if b < c:
            b = E ^ 73
            b *= 14
            E = b % 255
            a[K + 40] = E
        b = W ^ 128
        a[ga] = b
        b = Ta ^ 160
        b *= 155
        y = b % 255
        a[B + 48] = y
        b = g ^ 172
        c = y ^ 230
        if c < b:
            b = 59 * S
            b %= 255
            S = b ^ 150
            a[v + 52] = S
        if Wa < g:
            p = sa ^ 185
            a[l + 56] = p
        if F < S:
            fa = ua ^ 130
            a[qa + 60] = fa
        b = f ^ 93
        c = Ea ^ 28
        if c < b:
            b = Q ^ 158
            b *= 98
            Q = b % 255
            a[ha + 64] = Q
        if y < aa:
            t ^= 157
            a[e] = t
            g ^= 157
            a[V] = g
        if t < y:
            I = Va ^ 103
            a[k] = I
            p ^= 174
            a[l + 56] = p
        if F < f:
            I ^= 17
            a[k] = I
            p ^= 17
            a[l + 56] = p
        ta = f ^ 221
        a[r + 4] = ta
        X = Fa ^ 104
        a[n] = X
        Z = d ^ 190
        a[h] = Z
        a[A] = F
        a[u + 76] = M
        a[l + 56] = E
        a[K + 40] = p
        if aa < E:
            Z = d ^ 149
            a[h] = Z
            ta = f ^ 246
            a[r + 4] = ta
        b = fa ^ 21
        c = fa ^ 164
        if c < b:
            y ^= 168
            a[B + 48] = y
            a[pa] = 97
        a[n] = t
        a[e] = Z
        a[h] = X
        b = ia ^ 131
        if b < Z:
            X = Fa ^ 147
            a[h] = X
            M = Pa ^ 40
            a[u + 76] = M
        a[k] = M
        a[u + 76] = I
        b = M ^ 118
        c = Q ^ 207
        if c < b:
            a[V] = aa
            a[ea] = g
        a[A] = y
        a[B + 48] = F
        b = z ^ 37
        a[x] = b
        b = T ^ 96
        a[w + 12] = b
        c = ta ^ 103
        b = X ^ 10
        if b < c:
            b = S ^ 80
            a[v + 52] = b
            b = W ^ 208
            a[ga] = b

        pong = ' '.join([str(a[ga]), str(a[k]), str(a[ea]), str(a[ba]), str(a[A]), str(a[x]), str(a[V]), str(a[h]), str(a[pa]), str(a[e])])

        log.debug('received ping %s, sending pong: %s' % (ping, pong))

        return self.send('sp/pong_flash2', pong)