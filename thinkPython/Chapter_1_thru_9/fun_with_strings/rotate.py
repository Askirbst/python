def rotate_word(s, n):
    word = s.lower()
    cypher = ''
    i = 0
    for c in word:
        if c in (' ', "'", '.', ',', '!', '-') or c.isnumeric():
            c2 = c
        elif (ord(c) + n) > 122:
            c2 = chr((ord(c) + n) - 26)
        else:
            c2 = chr(ord(c) + n)
        cypher += c2
        i += 1
    return cypher

print(rotate_word("Uv gurer. Guvf vf abg ernyyl wbxr. Whfg univat fbzr sha jvgu gubfr jub pna'g ebg13 na negvpyr.", 13))
print(rotate_word("Gb or ernyyl zrna, sbyybj-hc gb guvf negvpyr jvgu fbzrguvat yvxr 'Obl, gung jnf gur shaavrfg wbxr V rire urneq!'", 13))