pintas = ["picas", "treboles", "diamantes", "corazones"]
<<<<<<< HEAD
valores = ["A", "J", "Q", "K" ] + [str (i)for i in range (2,11)]
=======
valores = ["A", "J", "Q", "K" ] + [str(i) for i in range (2,11)]
>>>>>>> 02fb14b79b98c698e0fe6619acddb6e717199766
mazo = [(v,p) for v in valores for p in pintas]
for c in mazo:
    print (c)