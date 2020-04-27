#!/usr/bin/env python2
#
# rail fence cipher implementation with optional offset feature
#
# for educational use only! (rail fence cipher is a very weak cipher.)
#
# https://en.wikipedia.org/wiki/Rail_fence_cipher
#


def printFence(fence):
    for rail in range(len(fence)):
        print(''.join(fence[rail]))
    
def encryptFence(plain, rails, offset=0, debug=False):
    cipher = ''

    # offset
    plain = '#'*offset + plain

    length = len(plain)
    fence = [['#']*length for _ in range(rails)]

    # build fence
    rail = 0
    for x in range(length):
        fence[rail][x] = plain[x]
        if rail >= rails-1:
            dr = -1
        elif rail <= 0:
            dr = 1
        rail += dr


    # read fence
    for rail in range(rails):
        for x in range(length):
            if fence[rail][x] != '#':
                cipher += fence[rail][x]
    return cipher


def decryptFence(cipher, rails, offset=0, debug=False):
    plain = ''

    # offset
    if offset:
        t = encryptFence('o'*offset + 'x'*len(cipher), rails)
        for i in range(len(t)):
            if(t[i] == 'o'):
                cipher = cipher[:i] + '#' + cipher[i:]
    
    length = len(cipher)
    fence = [['#']*length for _ in range(rails)]

    # build fence
    i = 0
    for rail in range(rails):
        p = (rail != (rails-1))
        x = rail
        while (x < length and i < length):
            fence[rail][x] = cipher[i]
            if p:
                x += 2*(rails - rail - 1)
            else:
                x += 2*rail
            if (rail != 0) and (rail != (rails-1)):
                p = not p
            i += 1


    # read fence
    for i in range(length):
        for rail in range(rails):
            if fence[rail][i] != '#':
                plain += fence[rail][i]
    return plain


if __name__ == "__main__":
    cipher = "tat_uiwirc{s_iaaotrc_ahn}pkdb_esg" 
    for i in range(2,20):
        for j in range(0, 20):
            plain2 = decryptFence(cipher, i, offset=j, debug=False)
            if "rtcp" in plain2:
                print(plain2)
