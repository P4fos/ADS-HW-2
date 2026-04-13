def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    d1 = {}
    d2 = {}

    for i in range(len(s)):
        a = s[i]
        b = t[i]

        if a in d1:
            if d1[a] != b:
                return False
        else:
            d1[a] = b

        if b in d2:
            if d2[b] != a:
                return False
        else:
            d2[b] = a

    return True