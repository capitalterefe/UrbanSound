import os
import glob
import shutil
from pathlib import Path
data_path = Path('UrbanSound8K/data/')
spectrogram_path = Path('UrbanSound8K/spectrogram/')

labels = ['air_conditioner', 'car_horn', 'children_playing',
          'dog_bark', 'drilling', 'engine_idling', 'gun_shot', 'jackhammer', 'siren', 'street_music']


def create_fold_directory(fold):
    png_files = list(Path(spectrogram_path/fold).glob('*.png'))
    os.mkdir(data_path/fold)
    os.mkdir(data_path/fold/'train')
    os.mkdir(data_path/fold/'valid')
    for label in labels:
        os.mkdir(data_path/fold/'train'/label)
        os.mkdir(data_path/fold/'valid'/label)

    for file in png_files:
        label = file.as_posix().split('-')[1]
        shutil.copyfile(file, data_path/fold/'valid' /
                        labels[int(label)]/file.name)
    for i in range(1, 11):
        if str(i) == fold:
            continue
        png_files = list(Path(spectrogram_path/str(i)).glob('*.png'))
        for file in png_files:
            label = file.as_posix().split('-')[1]
            shutil.copyfile(file, data_path/fold/'train' /
                            labels[int(label)]/file.name)


for i in range(1, 11):
    create_fold_directory(str(i))
