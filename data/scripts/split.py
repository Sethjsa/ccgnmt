with open("mono_output.en", "r") as f, open("train_mono.tags", "w") as g, open("train_mono.en", "w") as h:
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
