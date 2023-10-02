def compareWords(w1, w2, alf='0123456789abcdefghijklmnopqrstuvwxyz',WHITESPACE=False):
    s1 = w1
    s2 = w2
    if not WHITESPACE:
        s1 = w1.replace(" ", "").replace("\n", "")
        s2 = w2.replace(" ", "").replace("\n", "")

    lmin = len(s1)
    if s1 == s2:
        return s1
    elif len(s1) < len(s2):
        lmin = len(s1)
        if s1 == s2[0:len(s1) - 1]: return w1
    elif len(s1) > len(s2):
        lmin = len(s2)
        if s2 == s1[0:len(s2) - 1]: return w2

    for i in range(0, lmin):
        if s1[i] not in alf:
            return False
        elif s2[i] not in alf:
            return False

        if alf.find(s1[i]) < alf.find(s2[i]):
            return w1
        elif alf.find(s1[i]) > alf.find(s2[i]):
            return w2

def sortWords(words, alf='0123456789abcdefghijklmnopqrstuvwxyz', WHITESPACE=False, reversed=False):
    if len(words) < 2: return words
    wlist = words[:]
    for w in range(0,len(wlist)):
        for k in range(0,len(wlist)):
            if wlist[w] != wlist[k]:
                if compareWords(wlist[w], wlist[k], alf, WHITESPACE) == False: return 'Invalid character'
                if compareWords(wlist[w], wlist[k], alf, WHITESPACE) == wlist[w]:
                    temp = wlist[w]
                    wlist[w] = wlist[k]
                    wlist[k] = temp

    if reversed: wlist = wlist[::-1]
    return wlist
