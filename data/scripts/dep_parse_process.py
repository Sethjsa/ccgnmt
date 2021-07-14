import ast

with open("train_trgparse.tags", "r") as stanza_result, open("train_trgparse.deptags", "w") as tag_file:


# word_head-head_word tag
    for c, tree in enumerate(stanza_result):
        tree = ast.literal_eval(tree)
        word_head = {d['word_id'] : d['head'] for d in tree}
        tags = [] # this is tags for each sentence
        for d in tree:
            if word_head[d['word_id']] == 0:
                tags.append('SYN_root')
            else:
                tags.append("SYN_%s|%s"%(d['deprel'], tree[word_head[d['word_id']]-1]['deprel']))
        #print(" ".join(tags))
        tag_file.write(" ".join(tags))
        tag_file.write("\n")

# word_head-dependency direction
    # for c, tree in enumerate(stanza_result):
    #     tree = ast.literal_eval(tree)
    #     word_head = {d['word_id'] : d['head'] for d in tree}
    #     head_word = {d['head'] : d['word_id'] for d in tree}

    #     tags = [] # this is tags for each sentence
        
    #     root_id = head_word[0]
    #     #print(root_id)
    #     root_L, root_R = [], []

    #     for word in word_head.keys():
    #             if word_head[word] == root_id:
    #                 if word < root_id:
    #                     root_L.append(word)
    #                 if word > root_id:
    #                     root_R.append(word)
        

        
    #     for a, d in enumerate(tree):
    #         #print(d)
    #         # if word_head[d['word_id']] == 0:
    #         #     tags.append('SYN_root+L_R')
    #         head_id = word_head[d['word_id']]
    #         word_id = d['word_id']
    #         #print(f"{word_id}, {head_id}")
    #         # if parent is to right of current word = |R
    #         if word_id < head_id and head_id != 0:
    #             # tags.append(f"SYN_{d['deprel']}|R")
                
    #             dep_L, dep_R = [], []
    #             for word in word_head.keys():
    #                  if word_head[word] == d['word_id']:
    #                     if word < d['word_id']:
    #                         dep_L.append(word)
    #                     if word > d['word_id']:
    #                         dep_R.append(word)

    #             if dep_L and not dep_R:
    #                 tags.append(f"SYN_{d['deprel']}|R|L")
    #             elif dep_R and not dep_L:
    #                 tags.append(f"SYN_{d['deprel']}|R|R")
    #             elif dep_L and dep_R:
    #                 tags.append(f"SYN_{d['deprel']}|R|L+R")
    #             else:
    #                 tags.append(f"SYN_{d['deprel']}|R")

    #             # if d['word_id'] in word_head.values():
    #             #     if head_word[d['word_id']] < word_head[d['word_id']]:
    #             #         print(head_word[d['word_id']], word_head[d['word_id']], d['word_id'])

    #         # if parent is to left of current word = |L
    #         if word_id > head_id and head_id != 0:
    #             # tags.append(f"SYN_{d['deprel']}|L")

    #             dep_L, dep_R = [], []
    #             for word in word_head.keys():
    #                 if word_head[word] == d['word_id']:
    #                     if word < d['word_id']:
    #                         dep_L.append(word)
    #                     if word > d['word_id']:
    #                         dep_R.append(word)

    #             if dep_L and not dep_R:
    #                 tags.append(f"SYN_{d['deprel']}|L|L")
    #             elif dep_R and not dep_L:
    #                 tags.append(f"SYN_{d['deprel']}|L|R")
    #             elif dep_L and dep_R:
    #                 tags.append(f"SYN_{d['deprel']}|L|L+R")
    #             else:
    #                 tags.append(f"SYN_{d['deprel']}|L")

    #         elif word_head[d['word_id']] == 0 and root_L and not root_R:
    #             tags.append('SYN_root|L|L')
    #         elif word_head[d['word_id']] == 0 and root_R and not root_L:
    #             tags.append('SYN_root|L|R')
    #         elif word_head[d['word_id']] == 0 and root_R and root_L:
    #             tags.append('SYN_root|L|L+R')
    #         elif word_head[d['word_id']] == 0 and not root_R and not root_L:
    #             tags.append('SYN_root|L')
            
    #         # else:
    #         #     tags.append(f"SYN_{d['deprel']}")
            
    #         # print(a+1, len(tags))
    #     #print(" ".join(tags))
    #     #print(len(tree), len(tags)

    #     tag_file.write(" ".join(tags))
    #     tag_file.write("\n")
