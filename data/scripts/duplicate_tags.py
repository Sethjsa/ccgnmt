with open("train_trgparse_bpe.en", "r") as f, open("train_trgparse_proc.deptags", "r") as g, open("train_trgparse_bpe.tags", "w") as h:
    f0 = f.readlines()
    g0 = g.readlines()
    for count, line in enumerate(f0):
        tag_line = g0[count].split()
        skip = 0
        
        for c, word in enumerate(line.split()):

            h.write(f"{tag_line[c-skip]} ")

            if "@@" in word:
                skip += 1

        h.write("\n")

        

