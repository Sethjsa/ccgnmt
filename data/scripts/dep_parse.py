import stanza 

nlp = stanza.Pipeline(lang='en', processors='tokenize,mwt,pos,lemma,depparse')

# line = "polisler evde"
#l = " ".join(line.split())

# parse train, dev and test
with open("train.en", "r") as f, open("train_trgparse.tags", "w") as g:
   for c, line in enumerate(f):

        doc = nlp(line)
        sent = [{"word":word.text, "word_id":word.id, "deprel": word.deprel, "head_word": sent.words[word.head-1].text if word.head > 0 else "root", "head": word.head} for sent in doc.sentences for word in sent.words]
        #print(str(sent))
        g.write(str(sent))
        g.write("\n")
        if c % 100 == 0:
            print(c)
        
        # for sent in doc.sentences:
        #     for word in sent.words:
        #         d["word"] =  
        # print([f'{word.text}, {word.head}, {word.deprel}, {sent.words[word.head-1].text if word.head > 0 else "root"}' for sent in doc.sentences for word in sent.words])
#pprint.pprint(doc)
        #print(*[f'id: {word.id}\tword: {word.text}\thead id: {word.head}\thead: {sent.words[word.head-1].text if word.head > 0 else "root"}\tdeprel: {word.deprel}' for sent in doc.sentences for word in sent.words], sep='\n')
