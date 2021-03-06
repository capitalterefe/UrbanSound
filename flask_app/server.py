from flask import Flask
import fastai.vision as fastai
import matplotlib.pyplot as plt
from matplotlib.pyplot import specgram
#import librosa
import numpy as np
from pathlib import Path
#import librosa.display

app = Flask(__name__)
CLASSIFIER = fastai.load_learner('./models/soundclassifierModel.pkl')
SOUND_TYPE = "siren"
SPECTOGRAMS = "./sample_spectograms/"


@app.route("/classify")
def classify():
    convert_sound_to_spectogram(SOUND_TYPE)
    sound = fastai.image.open_image(SPECTOGRAMS+SOUND_TYPE+'.png')
    prediction = CLASSIFIER.predict(sound)
    return {
        "SoundPrediction": sorted(
            list(
                zip(
                    CLASSIFIER.data.classes, [
                        round(x, 4) for x in map(float, prediction[2])]
                )
            ),
            key=lambda p: p[1],
            reverse=True
        )
    }


def convert_sound_to_spectogram(file_name):
    print(file_name)
    sound_file = './sample_sounds/'+file_name+'.wav'
    spectogram_file = './sample_spectograms/'+file_name+'.png'
#    samples, sample_rate = librosa.load(sound_file)
    fig = plt.figure(figsize=[0.72, 0.72])
    ax = fig.add_subplot(111)
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_frame_on(False)
  #  S = librosa.feature.melspectrogram(y=samples, sr=sample_rate)
 #   librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    plt.savefig(spectogram_file, dpi=400, bbox_inches='tight', pad_inches=0)
    plt.close('all')


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8000, debug=True)
