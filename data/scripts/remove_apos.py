with open("train.en", "r") as f, open("train_trgparse.lrdeptags", "r") as g, open("train_trgparse_proc.lrdeptags", "w") as h:
    g = g.readlines()
    for co, line in enumerate(f):
        # print(c)
        tag_l = g[co].split()
        word_l = line.split()

        #inter = [l0 for pair in zip(l2, l) for l0 in pair if pair]
        apos_skip = 0
        bpe_skip = 0
        out = []
        #print(l, l2)
        # print(c, l, l2)
        for c, word in enumerate(word_l):
            if word == "&apos;" or word == "&apos;s" or "&quot;" in word:
                apos_skip += 1
            # if "@@" in tag_l[c-1]:
            #     out.append(tag_l[c])
            #     bpe_skip += 1
            #     pass
            
            # out.append(word_l[c])
            out.append(tag_l[c+apos_skip])
            # try:
            #     out.append(tag_l[c+apos_skip])
            # except IndexError as e:
            #     print(e,co)
        h.write(" ".join(out))
        h.write("\n")