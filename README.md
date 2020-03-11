## Day to Night Unsupervised Domain Adaptation usingImage-to-Image Translation for Object Detection





![Method Overview](https://github.com/abderrazzak555/Day-to-Night-Unsupervised-Domain-Adaptation/blob/master/images/methodoverview.png)

#### Abstract

In order to have a well performed detector, it needto  be  trained  on  data  which  resemble  to  the  target  task  alsoa well annotated dataset, this last is very expensive and needsa lot of manual work. In Autonomous vehicles we have a lotof driving scenarios with different domains and that’s requiresannotated data. In our Work, we present a method for a specificdomain (Day images) with labels but without any labels from thetarget domain (Night Images) to train an object detection. Forthat, a model based on Generative Adversarial Networks (GANs)is explored to enable the generation of an artificial dataset withits respective annotations. The artificial dataset (fake dataset) iscreated translating images from day-time domain to night-timedomain. The fake dataset, which comprises annotated imagesof only the target domain (night images), is then used to trainthe  car  detector  model.  Experimental  results  showed  that  theproposed method has improve the detector performance in thetarget domain.

---

### Source-code
#### Disentangled (High resolution)

The source code used for the DRIT(Disentangled) model was made publicly available by [Hsin-Ying Lee, Hung-Yu Tseng](https://github.com/hytseng0509/DRIT_hr).

#### Object detection API

The source code used for the Object detection API model was made publicly available (https://github.com/tensorflow/models/tree/master/research/object_detection).

#### Faster R-CNN

The source code used for the Faster R-CNN model was made publicly available by [Xinlei Chen](https://github.com/endernewton/tf-faster-rcnn).

For training the Faster R-CNN, a pre-trained resnet-101 model was used to initializate the process an can be downloaded [here](http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz).

---

### Trained Models

#### DRIT

The trained model used in this paper is available [here](https://drive.google.com/drive/folders/1jrb2GIHOAKY0SlW9tZc1JhumQdloKgkg?usp=sharing).

#### Faster R-CNN

The trained models used in this paper are available [here](https://drive.google.com/drive/folders/1BgP55i3wixBcTmQTV8UDsgAEE53_t4qo?usp=sharing).

---

### Dataset

#### Berkeley Deep Drive Dataset

##### Dataset Acquisition

Download the Berkeley Deep Drive dataset [here](https://bdd-data.berkeley.edu/).
It is only necessary to download the Images and Labels files.

##### Dataset Filtering

After downloading the BDD dataset, the Images and Labels will be placed into the zipped files `bdd100k_images.zip` and `bdd100k_labels.zip` respectively. In the same directory, place the provided source code `filter_dataset.py` from this repository with the folder `BDD_lists`.

On the terminal, run: `python filter_dataset.py`.
It will take a few minutes, and at the end, the folder `images` and `labels` will contain the images and bounding boxes of the images respectively. 

#### Generated (Fake) Dataset

Available [here](https://drive.google.com/drive/folders/1rCVj2sMc9oxxqADAYLocwITzU5Sq6V6E?usp=sharing).






     
