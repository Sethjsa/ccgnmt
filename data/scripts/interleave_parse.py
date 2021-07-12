with open("test_parse.lrdeptags", "r") as f, open("test_bpe.tr", "r") as g, open("test_parselr_bpe.tr", "w") as h:
    g = g.readlines()
    for c, line in enumerate (f):
        l = g[c].split()
        l2 = line.split()

        #inter = [l0 for pair in zip(l2, l) for l0 in pair if pair]
        apos_skip = 0
        bpe_skip = 0
        out = []
        #print(l, l2)
        # print(c, l, l2)
        for c, word in enumerate(l):
            if word == "&apos;" or word == "&quot;":
                apos_skip += 1
            if "@@" in l[c-1]:
                out.append(l[c])
                bpe_skip += 1
                pass
            else:
                out.append(l2[c+apos_skip - bpe_skip])
                out.append(l[c])
        h.write(" ".join(out))
        h.write("\n")

# with open("train_bpe.en", "r") as f, open("train_bpe.tags", "r") as g, open("train_interleaved.en", "w") as h:
#     #f = f.read()
#     g = g.readlines()
#     for c, line in enumerate(f):
#         l = line.split()
#         l2 = g[c].split()
#         l2 = [f"TAG_{l}" for l in l2]
#         inter = [l0 for pair in zip(l2, l) for l0 in pair]
#         h.write(" ".join(inter))
#         h.write("\n")

#     for line in f:
#         interleaved = []
#         #for c, word in enumerate(line.split()):
#         #    if "@@" in line.split()[c-1]:
#         #        pass
#         #    else:
#         #        interleaved.append(word)
#         for c, word in enumerate(line.split()):
#             if "@@" in line.split()[c-1]:
#                 pass
#             else:
#                 interleaved.append(word)
#         g.write(" ".join(interleaved))
#         g.write("\n")
