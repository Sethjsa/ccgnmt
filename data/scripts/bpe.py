import os


src_lang = 'de'
trg_lang = 'en'
bpe_size = 85000
datadir = '~/data/full/'
name = f'{src_lang}_{trg_lang}_bpe{bpe_size}'


train_src_file = os.path.join(datadir, f'train.{src_lang}')
train_trg_file = os.path.join(datadir, f'train.{trg_lang}')
train_joint_file = os.path.join(datadir, f'train.{src_lang}-{trg_lang}')
dev_src_file = os.path.join(datadir, f'dev.{src_lang}')
dev_trg_file = os.path.join(datadir, f'dev.{trg_lang}')
test_src_file = os.path.join(datadir, f'test.{src_lang}')
test_trg_file = os.path.join(datadir, f'test.{trg_lang}')
src_files = {'train': train_src_file, 'dev': dev_src_file, 'test': test_src_file}
trg_files = {'train': train_trg_file, 'dev': dev_trg_file, 'test': test_trg_file}


vocab_src_file = os.path.join(datadir, f'vocab.{bpe_size}.{src_lang}')
vocab_trg_file = os.path.join(datadir, f'vocab.{bpe_size}.{trg_lang}')
bpe_file = os.path.join(datadir, f'bpe.codes.{bpe_size}')

!cat $train_src_file $train_trg_file > $train_joint_file

!subword-nmt learn-bpe \
  --input $train_joint_file \
  -s $bpe_size \
  -o $bpe_file



src_bpe_files = {}
trg_bpe_files = {}
for split in ['train', 'dev', 'test']:
  src_input_file = src_files[split]
  trg_input_file = trg_files[split]
  src_output_file = src_input_file.replace(split, f'{split}.{bpe_size}.bpe')
  trg_output_file = trg_input_file.replace(split, f'{split}.{bpe_size}.bpe')
  src_bpe_files[split] = src_output_file
  trg_bpe_files[split] = trg_output_file

  ! subword-nmt apply-bpe \
    -c $bpe_file \
    < $src_input_file > $src_output_file

  ! subword-nmt apply-bpe \
    -c $bpe_file \
    < $trg_input_file > $trg_output_file


