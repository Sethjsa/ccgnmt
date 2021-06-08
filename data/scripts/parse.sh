#!/bin/bash

java -jar ~/easyccg/easyccg.jar -m ~/model_rebank -f ~/data/split_corpus02 -o supertags > ~/data/output_corpus02.en

java -jar ~/easyccg/easyccg.jar -m ~/model_rebank -f ~/data/split_corpus03 -o supertags > ~/data/output_corpus03.en

java -jar ~/easyccg/easyccg.jar -m ~/model_rebank -f ~/data/split_corpus04 -o supertags > ~/data/output_corpus04.en

