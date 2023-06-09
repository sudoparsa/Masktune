#!/bin/bash
cd /home/user01/masktune/Masktune

python3 -m src.main --dataset waterbirds \
                    --train \
                    --arch resnet50 \
                    --base_dir /home/user01/masktune/Masktune \
                    --lr 0.001 \
                    --use_cuda \
                    --optimizer sgd \
                    --train_batch 256 \
                    --test_batch 256 \
                    --masking_batch 256 \
                    --epochs 100 \
                    --masktune \
                    --dataset_dir /home/user01/hosseini/waterbird_complete95_forest2water2

