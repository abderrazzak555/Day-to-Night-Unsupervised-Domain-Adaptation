import argparse
import os

from tqdm import tqdm

from utils import load_json, save_json


def split_json(path, dataset_type):
    dirname = os.path.join(os.path.dirname(path), dataset_type)
    os.makedirs(dirname, exist_ok=True)

    labels = load_json(path)
    for label in tqdm(labels):
        name = label['name']
        f = os.path.join(dirname, name.replace('.jpg', '.json'))
        save_json(label, f, indent=4)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--root', type=str, default='data/bdd100k')
    args = parser.parse_args()

    root = args.root

    train_labels = os.path.join(root, '/home/abderrazzak/Desktop/filtern/publications-arruda-ijcnn-2019/bdd100k_labels/bdd100k/labels/bdd100k_labels_images_train.json')
    valid_labels = os.path.join(root, '/home/abderrazzak/Desktop/filtern/publications-arruda-ijcnn-2019/bdd100k_labels/bdd100k/labels/bdd100k_labels_images_val.json')

    split_json(train_labels, 'train')
    split_json(valid_labels, 'val')


if __name__ == '__main__':
    main()
