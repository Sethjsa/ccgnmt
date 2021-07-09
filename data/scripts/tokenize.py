import re 

# tokenizer idiom
# scripts/tokenizer/tokenizer.perl -l fr < ~/corpus/training/news-commentary-v8.fr-en.fr > ~/corpus/news-commentary-v8.fr-en.tok.fr

# # change - to @-@
# p = re.compile(r'(?P<g1>[A-z]+)-(?P<g2>[A-z]+)')
# line = p.sub(r'\g<g1> @-@ \g<g2>', line)