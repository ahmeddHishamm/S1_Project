def search2(inp, needed):
    for word in needed:
        if substring_search(inp, word):
            return True
    return False


def substring_search(subs, s):
    sub_length = len(subs)
    s_length = len(s)
    for index in range(0, s_length - sub_length + 1):
        if subs[0] == s[index]:
            # check if the rest are the same or not
            if subs[1:] == s[index + 1:index + sub_length]:
                return True
    return False
