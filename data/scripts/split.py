with open("output_corpus.en", "r") as f, open("train_corpus.tags", "w") as g, open("train_corpus.en", "w") as h:
    for line in f:
        #splitted = line.split("||")
        line = line.replace("||", " ")
        #print(splitted)
        tag_list = line.split()
        #print(tag_list[1::2])
        tags = " ".join(tag_list[1::2])
        #print(tags)
        g.write(tags)
        g.write("\n")

        words = " ".join(tag_list[0::2])
        h.write(words)
        h.write("\n")
