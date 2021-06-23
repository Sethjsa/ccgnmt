# import spacy

# nlp = spacy.load("en_core_web_sm")

# with open("train.en", "r") as f, open("train_upos.tags", "w") as g, open("train_pos.tags", "w") as h, open("train_dep.tags", "w") as i:
#     for line in f:
#         doc = nlp(line)
#         upos_line = []
#         pos_line = []
#         dep_line = []
#         for token in doc:
#             upos_line.append(token.pos_)
#             pos_line.append(token.tag_)
#             dep_line.append(token.dep_)
#         g.write(" ".join(upos_line[:-1]))
#         g.write("\n")

#         h.write(" ".join(pos_line[:-1]))
#         h.write("\n")

#         i.write(" ".join(dep_line[:-1]))
#         i.write("\n")