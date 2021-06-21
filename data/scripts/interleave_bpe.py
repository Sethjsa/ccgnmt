with open("train_interleaved.en", "r") as f, open("train_inter_bpe.en", "w") as g:
    for line in f:
        interleaved = []
        for c, word in enumerate(line.split()):
            if "@@" in line.split()[c-1]:
                pass
            else:
                interleaved.append(word)
        g.write(" ".join(interleaved))
        g.write("\n")
