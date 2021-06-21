with open("train_bpe.en", "r") as f, open("train_bpe.tags", "r") as g, open("train_interleaved.en", "w") as h:
    #f = f.read()
    g = g.readlines()
    for c, line in enumerate(f):
        l = line.split()
        l2 = g[c].split()
        inter = [l0 for pair in zip(l, l2) for l0 in pair]
        h.write(" ".join(inter))
        h.write("\n")
    #line = " ".join(i for j in zip(f, g) for i in j)
    #print(line)
    
