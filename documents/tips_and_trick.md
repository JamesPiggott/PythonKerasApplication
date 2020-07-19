# Tips and tricks setting up a Deep Learning Network

Below is a description of the values for parameters you can define when setting up a Deep Learning Network

## Setting values for Epoch, 

epochs: sets the number of times the model is trained over the entire dataset. Hard-coding this value is considered bad form. Training should stop when performance metric such as accuracy reaches a set threshold. However, initial testing of the model with a fixed epoch size is acceptable.

steps_per_epoch: the number of batch iterations thta should be performed before an epoch is considered finished. If you have a fixed size training set then this value can be omitted. However, if you have a large data set and are creating data augmentations on the fly then settign this value can be useful to define the end of an epoch.

validation_per: similar to steps_per_epoch but instead used for the validation data set. If you have time to go through the entire validation set then skip this parameter