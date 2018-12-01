# Machine Learning Engineer Nanodegree
## Capstone Proposal
Matthias Buehl
December 1st, 2018


## Proposal
Create original music via machine learning


### Domain Background
Music has been composed since the dawn of time.  Music composition requires creativity and is deemed to be a uniquely  human capability.  At its core, music is rhythm and pitch.  Music composition is the creation of a sequence of pitches over time.  It will be interesting to explore how machine learning can be used to mimic a human composer.

### Problem Statement
As stated above, composing music is exclusively a human activity.  Composers are highly trained individuals and the craft takes decades to master.  Nevertheless, composers tend to be strongly inspired by past works.  This fact suggest the possibility that an algorithm could learn from existing works and could create an original piece.


### Datasets and Inputs
I believe that the most appropriate input data will be midi files.  Midi files contain information about notes and not the notes themselves. Midi notes contain information about pitch, velocity, note-on, note-off, etc.   Since these parameters are numerical, they can be easily fed to a machine learning algorithm.

There are lots of public repositories of midi files e.g.
https://newzik.com/project/online-public-domain-libraries-musicxml-midi-scores/


### Solution Statement
A music composition consists of a sequence of pitches.  In order for a note to sound pleasing, it needs to work within the context provided by the notes that precede it.  I plan on using a recurrent neural network to predict the next note from a sequence of notes.  The newly predicted note will be part of the sequence that gets run through the network next.  This process continues indefinitly in order to produce a continuous stream of notes.


### Benchmark Model
The current standard in algorithmic music composition appears to be https://magenta.tensorflow.org/.  I could try to compare a magenta composition to one created by my algorithm.

The true benchmark for composition is a human composer.  I could train the model on the works of just one composer and compare the algorithmic composition with one of the composers works.


### Evaluation Metrics
I plan on using a recurrent neural network and use categorical crossentropy as a loss function.  The ultimate choice will depend on the performance of the model.


### Project Design
The exact design is unclear at the moment.  I am still in the process of learning about recurrent networks.
The hight level design is a follows.
As stated above the input to the model will be a sequence of midi notes.  To keep things simple I will only keep the pitch information of the notes which lies between the values of 21 and 108.  If the midi event is a chord, I will only keep the root note.

For example, an input sequence may look like this: [55, 75, 74, 20, 25].
I will decide on how may pitches to use for the input sequence.  In this example I will use 3.

In this case pitch with value 20 follows a the sequence [55, 75, 74].
[55, 75, 74] -> [20]

And the pitch with value 25 follows the sequence [75, 74, 20]
[75, 74, 20] -> [25]

The above illustrates how I will use the input midi files to train the network.

Once the model is trained, I should be able to predict an ‘original’ pitch from an sequence of three existing pitches.
