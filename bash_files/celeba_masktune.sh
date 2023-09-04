#!/bin/bash
cd /home/user01/masktune/Masktune

python3 -m src.main --dataset celeba \
                    --arch resnet50 \
                    --base_dir /content/Masktune \
                    --lr 0.0001 \
                    --use_cuda \
                    --optimizer sgd \
                    --train_batch 256 \
                    --test_batch 256 \
                    --masking_batch 128 \
                    --epochs 20 \
                    --gamma 1.0 \
                    --weight_decay 0.0001 \
                    --masktune \
                    --use_pretrained_weights \
                    --dataset_dir /content/drive/MyDrive/Meta_ood/data/celeba/celeba \
                    --masktune_iterations 1
