---
title: "WCCI 2018 Tutorial : Prediction, Interaction, and User Behaviour"
layout: post
---

### Tutorial Description
The goal of this tutorial is to apply predictive machine learning models to human behaviour through a human computer interface. We will introduce participants to the key stages for developing predictive interaction in user-facing technologies: collecting and identifying data, applying machine learning models, and developing predictive interactions. Many of us are aware of recent advances in deep neural networks (DNNs) and other machine learning (ML) techniques; however, it is not always clear how we can apply these techniques in interactive and real time applications. Apart from well known examples such as image classification and speech recognition, what else can predictive ML models be used for? How can these computational intelligence techniques be deployed to help users?

![]({{ site.baseurl }}/assets/predictive-interaction.png)

In this tutorial, we will show that ML models can be applied to many interactive applications to enhance users’ experience and engagement. We will demonstrate how sensor and user interaction data can be collected and investigated, modelled using classical ML and DNNs, and where predictions of these models can feed back into an interface. We will walk through these processes using live-coded demonstrations with Python code in Jupyter Notebooks so participants will be able to see our investigations live and take the example code home to apply in their own projects.

### Our Prediction Systems

Our demonstrations will be motivated from examples from our own research in creativity support tools, robotics, and modelling user behaviour. In creativity, we will show how streams of interaction data from a creative musical interface can be modelled with deep recurrent neural networks (RNNs). From this data, we can predict users' future interactions, or the potential interactions of other users. This enables us to "fill in" parts of a tablet-based musical ensemble when other users are not available, or to continue a user's composition with potential musical parts. In user behavior, we will show how smartphone sensor data can be used to infer user contextual information such as physical activities. This contextual information can be used to trigger interactions in  smart home or internet of things (IoT) environments, to help tune interactive applications to user’s needs, or to help track health data.


### Session Plan:
This 1.5 hour session will consist of live code demonstrations using a series of Jupyter Notebooks. These documents contain both Python code and rich text elements allowing the tutorial descriptions to go alongside code examples, and the results of visualisations. The code examples can be executed inside the notebooks allowing participants to investigate data sets and interact with trained models during the tutorial. The organisers will execute and explain the notebooks on a projector screen, and participants can follow along on their own systems if they wish.

The session schedule will be as follows:

**Introduction to Predictive Interaction (20 minutes)**
- Overview of applications: creativity, user behavior, robotics.
- What is a prediction?
- Forecasting, classification, and sequence learning.
- Temporal and non-temporal models.
- Forward models and bio-inspired prediction.

**Data Collection and Investigation (10 minutes)**
- Collecting data from smartphone sensors.
- Exploratory data analysis.

**Classifying Activity Data (20 minutes)**
- Using a classical ML model (e.g., Random Forests).
- Training a classifier.
- Evaluating a classifier.

**Continuing Creative Sequences (40 minutes)**
- Recurrent Neural Networks (RNNs) and Long Short-Term Memory (LSTM) with Keras.
- Generating Text with a CharRNN; inventing Star Trek episode titles.
- Continuing musical sequences.

The session material (iPython notebooks), data, and system requirements will be published on a tutorial website prior to the conference so that attendees can set up their systems if they wish. 

### Outline of Covered Material
This tutorial will focus on applications of predictive ML techniques to user interaction data. Prediction could be said to be the generation of unknown data from current and previous sensor data. In user interaction, we generally deal with sequences of data, but the predictions can relate to future elements of the sequence (forecasting) or a present, but unknown sequence (classification or segmentation). Models for making these predictions can operate using just the present sample (non-temporal models) or using a history of previous knowledge (temporal models).

![]({{ site.baseurl }}/assets/predictive-models-overview.png)


To choose which model to apply, we will briefly demonstrate exploratory data analysis. This involves collecting and examining data in an interactive programming environment such as Python. We will demonstrate how Python’s numerical computation library Numpy and data analysis library Pandas can be used to apply descriptive statistical analysis to user behaviour data and how visualisation can reveal patterns in data and targets for ML prediction.

Our first application area will be prediction of activity states, such as walking, running or sitting, from activity data, such as accelerometer readings from a smartphone. This can be accomplished with a classical ML classifier such as Random Forests, one of the simplest models in ML. We will use Python’s Scikit-Learn library to train a classifier (e.g., Random Forests) and do an evaluation of our results. We will show how such a classifier might be integrated into an IoT or smart home environment.

Our second application will be in interactive music and creative ML systems. RNNs, a popular temporal DNN model, have been very successfully applied to sequences of musical notes. In this configuration, they predict the next note in a sequence in order to compose new music. These models can easily be applied to any corpus of categorical sequential data, and in particular, strings of text using a simple character-level RNN architecture. This system can be applied to many creative and fun problems, for instance, generating Star Trek episode titles.  We will demonstrate RNNs using Keras, a high-level library for specifying and training deep learning models. We will show how a model of musical sequences can be used in a smartphone app to generate potential responses from other participants in a musical ensemble.


### Required Software

In order to succesfully run the code examples from this tutorial, please install the following software:

* [Jupyter Notebooks](http://jupyter.org/install) and [Python 3](https://www.python.org/downloads/)
* The latest versions of [Keras](https://keras.io/#installation), including one of Keras' backends, such as [TensorFlow](https://www.tensorflow.org/install/).
* The python packages [numpy, matplotlib and pandas](https://scipy.org/install.html).

To test if your setup is working, you can try running our code samples at [TODO: Insert link]