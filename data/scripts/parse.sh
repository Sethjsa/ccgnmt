#!/bin/bash

#java -jar ~/easyccg/easyccg.jar -m ~/model_rebank -f ~/data/split_corpus02 -o supertags > ~/data/output_corpus02.en

#java -jar ~/easyccg/easyccg.jar -m ~/model_rebank -f ~/data/split_corpus03 -o supertags > ~/data/output_corpus03.en

java -jar ~/ccgnmt/easyccg/easyccg.jar -m ~/ccgnmt/model_rebank -f ~/ccgnmt/data/tren/mono.en -o supertags > ~/ccgnmt/data/tren/mono_output.en


