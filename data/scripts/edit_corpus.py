"""
with open("train_18.de", "r+") as g:
    lines = g.readlines()

with open("train_18.en", "r+") as h:
    lines2 = h.readlines()
"""

remove = []

with open("train_corpus.en", "r") as f:
    for count, line in enumerate(f):
        if line == "\n":    
            remove.append(count)

with open("train_corpus.de", "r") as g:
    with open("train_corpus_proc.de", "w") as h:
        for count, line in enumerate(g):
            if not count in remove:
                h.write(line)

with open("train_corpus.en", "r") as j:
    with open("train_corpus_proc.en", "w") as k:
        for count, line in enumerate(j):
            if not count in remove:
                k.write(line)

with open("tags_corpus.en", "r") as j:
    with open("train_corpus_proc.tags", "w") as k:
        for count, line in enumerate(j):
            if not count in remove:
                k.write(line)

"""
with open("train_18.de", "w") as g:
    for count, line in enumerate(lines):
        if not count in remove:
            g.write(line)

with open("train_18.en", "w") as h:
    for count, line in enumerate(lines2):
        if not count in remove:
            h.write(line)
"""
