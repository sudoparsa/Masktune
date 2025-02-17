#!/bin/bash
cd /home/user01/masktune/Masktune


#  --train
python3 -m src.main --dataset waterbirds \
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
                    --dataset_dir /home/user01/hosseini/waterbird_complete95_forest2water2 \
                    --best_erm_model_checkpoint_path /home/user01/models/waterbirds/100resnet50_erm_ll.model \
                    --masktune_iterations 1   

