#remove blank lines
#sed '/^$/d' input > output

#python3 remove_hashtags.py

#parse tags 
#python3 parse.py
#java ...

#split output into train.en and train.tags
#python3 split.py

#remove unparsed lines from en, de and tag files, rewrite
#python3 edit_corpus.py

#bpe vocabulary merging, apply to all files (manually, see joey colab)
#python3 bpe.py

#duplicate tags for bpe'd words
#python3 duplicate_tags.py

#get normal dev and test data
#strip_sgml.py

#apply bpe to test and dev

#

