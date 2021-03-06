

from fastai import *
from fastai.vision import *
from fastai.vision import *
from selenium.webdriver import *
from fastai.vision.data import imagenet_stats
from pathlib import Path


data_directory = Path('UrbanSound8K/data')
# don't use any transformations because it doesn't make sense in the case of a spectrogram
# i.e. flipping a spectrogram changes the meaning
data = ImageDataLoaders.from_folder(data_directory/'1', ds_tfms=[], size=224)
data.normalize(imagenet_stats)
