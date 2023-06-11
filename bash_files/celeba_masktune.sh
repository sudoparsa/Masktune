#!/bin/bash
cd /home/user01/masktune/Masktune

python3 -m src.main --dataset celeba \
                    --arch resnet50 \
                    --base_dir /home/user01/masktune/Masktune \
                    --lr 0.0001 \
                    --use_cuda \
                    --optimizer sgd \
                    --train_batch 512 \
                    --test_batch 512 \
                    --masking_batch 256 \
                    --epochs 20 \
                    --gamma 1.0 \
                    --weight_decay 0.0001 \
                    --masktune \
                    --use_pretrained_weights \
                    --dataset_dir /home/user01/hosseini/celebA \
                    --masktune_iterations 3
