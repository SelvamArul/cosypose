from pathlib import Path
import shutil

def move_split(train_split, test_split):
    for i in range(60):
        print (str(train_split / f'{i + 240:06d}'), '-->'  ,str(test_split / f'{i:06d}'))
        shutil.move(train_split / f'{i + 240:06d}', test_split / f'{i:06d}')


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('dataset_path', type=str, help='an integer for the accumulator')
    args = parser.parse_args()
    DATASET_PATH = Path(args.dataset_path)
    sets = ['pick_bad']

    for s in sets:
        move_split(DATASET_PATH / f'train_{s}',  DATASET_PATH / f'test_{s}')