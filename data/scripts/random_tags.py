import random

tags = [f"tag_{i}" for i in range(507)]


with open("train.tags", "r") as f, open("train_random.tags", "w") as g:
    for c, line in enumerate(f):
        rand_line = []
        for tag in line.split():
            if tag == "." or tag == "," or tag == ":":
                rand_line.append(tag)
            else:
                rand_tag = random.choice(tags)
                rand_line.append(rand_tag)
        g.write(" ".join(rand_line))
        g.write("\n")
