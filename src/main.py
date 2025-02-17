import os

from src.arguments import init_train_argparse
from src.methods import (
    MnistTrain,
    IN9lTrain,
    CatsVsDogsTrain,
    CelebATrain,
    CIFAR10Train,
    SVHNTrain,
    WaterbirdsTrain
)


def main(args):
    if len(args.gpu_ids) == 1:
        os.environ["CUDA_VISIBLE_DEVICES"] = str(args.gpu_ids[0])
    if args.dataset == "mnist":
        method = MnistTrain(args)
    elif args.dataset == "in9l":
        method = IN9lTrain(args)
    elif args.dataset == "svhn":
        method = SVHNTrain(args)
    elif args.dataset == "catsvsdogs":
        method = CatsVsDogsTrain(args)
    elif args.dataset == "cifar10":
        method = CIFAR10Train(args)
    elif args.dataset == "celeba":
        method = CelebATrain(args)
    elif args.dataset == "waterbirds":
        method = WaterbirdsTrain(args)
    else:
        raise NotImplementedError
    if args.train:
        if args.masktune:
            method.masktune()
            if args.selective_classification:
                method.test_selective_classification(erm_model_checkpoint_path=method.best_erm_model_checkpoint_path, finetuned_model_checkpoint_path=method.finetuned_model_checkpoint_path)
            else:
                method.test(method.finetuned_model_checkpoint_path)
        else:
            method.train_erm()
            method.test(method.best_erm_model_checkpoint_path)
    else:
        if args.masktune:
            # Changed for loading pretrained ERM
            
            # Waterbirds
            # method.best_erm_model_checkpoint_path = '/home/user01/models/waterbirds/100resnet50_erm_ll.model'
            # method.last_erm_model_checkpoint_path = '/home/user01/models/waterbirds/100resnet50_erm_ll.model'
            
            # CelebA
            method.best_erm_model_checkpoint_path = '/content/drive/MyDrive/Meta_ood/image_rationalization/resnet50_celeba.model'
            method.last_erm_model_checkpoint_path = '/content/drive/MyDrive/Meta_ood/image_rationalization/resnet50_celeba.model'
            
            method.masktune()
            if args.selective_classification:
                method.test_selective_classification(erm_model_checkpoint_path=args.best_erm_model_checkpoint_path, finetuned_model_checkpoint_path=args.finetuned_model_checkpoint_path)
            else:
                method.test(method.finetuned_model_checkpoint_path)
        else:
            if args.selective_classification:
                method.test_selective_classification(erm_model_checkpoint_path=args.best_erm_model_checkpoint_path, finetuned_model_checkpoint_path=args.finetuned_model_checkpoint_path)
            else:
                method.test(args.best_erm_model_checkpoint_path)


if __name__ == "__main__":
    parser = init_train_argparse()
    args = parser.parse_args()
    main(args)
