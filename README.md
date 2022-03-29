# Emoti-ON: music data for feelings
This is the final project of Ironhack Bootcamp in Data Analytics. The algorithm predicts the emotions from the facial expressions and generates music according to them.

# Part I: Facial Emotion Recognition (FER)

## Emotion Detection Using Yolo-V5 and RepVGG
This repository uses [Yolo-V5](https://github.com/ultralytics/yolov5) and [RepVGG](https://github.com/DingXiaoH/RepVGG) to detect facial expressions and classify emotions (see the [architecture](#Architecture) for more info on how it works). To see how to use the code, check out the [usage](#usage) section for more information.

## Emotions
This model detects 8 basic facial expressions:
- anger
- contempt
- disgust
- fear
- happy
- neutral
- sad
- surprise<br>
and then attempts to assign them appropriate colours. It classifies every face, even if it is not that confident about the result!
## Usage
```
usage: main.py [-h] [--source SOURCE] [--img-size IMG_SIZE] [--conf-thres CONF_THRES] [--iou-thres IOU_THRES]
               [--device DEVICE] [--hide-img] [--output-path OUTPUT_PATH | --no-save] [--agnostic-nms] [--augment]
               [--line-thickness LINE_THICKNESS] [--hide-conf] [--show-fps]

optional arguments:
  -h, --help            show this help message and exit
  --source SOURCE       source
  --img-size IMG_SIZE   inference size (pixels)
  --conf-thres CONF_THRES
                        face confidence threshold
  --iou-thres IOU_THRES
                        IOU threshold for NMS
  --device DEVICE       cuda device, i.e. 0 or 0,1,2,3 or cpu
  --hide-img            hide results
  --output-path OUTPUT_PATH
                        save location
  --no-save             do not save images/videos
  --agnostic-nms        class-agnostic NMS
  --augment             augmented inference
  --line-thickness LINE_THICKNESS
                        bounding box thickness (pixels)
  --hide-conf           hide confidences
  --show-fps            print fps to console
```
## Architecture
There are two parts to this code: facial detection and emotion classification.
### Face Detection
This repository is a fork of [ultralytics/Yolo-V5](https://github.com/ultralytics/yolov5) because this is the code for classifying faces. Read [here](https://ultralytics.com/yolov5) for more information on Yolo-V5. To detect faces, the model was trained on the [WIDER FACE](http://shuoyang1213.me/WIDERFACE/) dataset which has 393,703 faces. For more information, check out the paper [here](https://arxiv.org/pdf/1511.06523.pdf).
### Facial Expression Classification
This repository uses code directly from the [DingXiaoH/RepVGG](https://github.com/DingXiaoH/RepVGG) repository. You can read the RepVGG paper [here](https://arxiv.org/pdf/2101.03697.pdf) to find out more. Even though this is the main model, it made more sense to fork the Yolo-V5 repository because it was more complicated. The model was trained on the [AffectNet dataset](http://mohammadmahoor.com/affectnet/), which has 420,299 facial expressions. For more information, you can read the paper [here](http://mohammadmahoor.com/wp-content/uploads/2017/08/AffectNet_oneColumn-2.pdf).


# Part II: Music Generation 
This repository is a fork of https://github.com/kiecodes/generate-music.git 

## Melody creation using Genetic Algorithm
<p align="center">
  <a href="https://youtu.be/aOsET8KapQQ" target="_blank">
    <img src="http://i3.ytimg.com/vi/aOsET8KapQQ/hqdefault.jpg" alt="Can AI make music?">
  </a>
</p>

## Content

The following files are included:
|File| Description |
|--|--|
| algorithms/genetic.py | The genetic algorithm library. You can find more about it here: https://github.com/kiecodes/genetic-algorithms |
| mgen.py | The actual implementation of the music generation using a genetic algorithm. 
| requirements.txt | Python library requirements to use with pip.

## How to use this script

First you need to install the requirements you need to run everything. This repository contains a requirements.txt file.

To install the needed requirements:

```
$ pip install -r requirements.txt 
```

To start the script call:

```
$ python mgen.py
```

The script will ask you to define couple parameters:

| Name | Description |
| --| -- |
| Number of bars | Length of the generated melody in bars
| Notes per bar | Number of notes inside of a bar
| Number of steps | Number of pitches per note
| Introduce pauses | Should the algorithm introduce pauses betwen notes or do you want a constant stream of notes?
| Key | Key of the scale the melody should fit in
| Scale | Type of scale the melody shoud fit in
| Scale Root | Pitch of the scale (ex.: 4 means C4 is the root note of a scale in C)
| Population Size | Number of melodies per generation to rate and recombine
| Number of mutations | Max number of mutations that should be possible per child generated
| Mutation probability | Probability for a mutation to occur

After you defined all parameters above the genetic algorithm will generate a population of melodies and play each one back to you. After each playback you can rate the melody. 

Each generation all melodies are saved in midi format to disk using the following system:
```
<timestamp>/<generation>/<rating>.mid

```

## Music 
GarageBand was used to add voices, instruments and effects to the melodies generated.

