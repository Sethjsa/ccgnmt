import re
import sys

pp = []
qs = []
cc = []
relsub = []
cont = []

with open("test_split.tags", "r") as f, open("test_bpe.en", "r") as test_en, \
    open("test_bpe.tr", "r") as test_tr, open("test_bpe_relsub.en", "w") as test_en_wr, open("test_bpe_relsub.tr", "w") as test_tr_wr:
    for i, line in enumerate(f):
        if line.find("S[q]") != -1 or line.find("S[wq]") != -1 \
        or line.find("S[qem]") != -1:
            qs.append(i)

        if line.find("conj") != -1:
            cc.append(i)

        if re.search("\ \(N[P]?[\\\/]N[P]?\)[\\\/]\(S(\[[a-z]?[a-z]?[a-z]?\])?[\\\/]N[P]?\)", line) \
        or re.search("\ S(\[[a-z]?[a-z]?[a-z]?\])?[\\\/]S(\[[a-z]?[a-z]?[a-z]?\])? ", line):
            relsub.append(i)

        if line.find("PP") != -1 or line.find("((S\\NP)/(S\\NP))/NP") != -1 \
        or line.find("(NP\\NP)/NP") != -1:
            pp.append(i)
        

        if re.search("\(S(\[[a-z]+\])?[\\\/]N[P]?\)\/\(S(\[to\])[\\\/]N[P]?\)", line):
            cont.append(i)

    print(len(pp), len(qs), len(cc), len(relsub), len(cont))

    t_en = test_en.readlines()
    t_tr = test_tr.readlines()

    for i in relsub:
        line_en = t_en[i]
        test_en_wr.write(line_en)

        line_tr = t_tr[i]
        test_tr_wr.write(line_tr)

