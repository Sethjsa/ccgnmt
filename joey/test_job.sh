#!/bin/sh

# Job Name
#$ -N gpu_test

# Work in current working directory
#$ -cwd

# Time and memory requirements
#$ -l h_rt=01:00:00

#$ -l h_vmem=4G

# Request one GPU:
#$ -pe gpu 1

# Priority project queue
#$ -P "lel_hcrc_cstr_students"

#email address
#$ -M s1701869@ed.ac.uk

#reasons to have email sent: begin, end, abort, suspend
#$ -m beas

#initialise environment modules and load python
. /etc/profile.d/modules.sh

#load conda and activate env
module load anaconda/5.3.1
source activate nmt

#load cuda ver
module load cuda/10.1.105

# training run:
#command
python3 -m joeynmt train configs/ccg.yaml