pintas = ["picas", "treboles", "diamantes", "corazones"]
valores = ["A", "J", "Q", "K" ]
mazo = [(v,p) for v in valores for p in pintas]
for c in mazo:
    print (c)