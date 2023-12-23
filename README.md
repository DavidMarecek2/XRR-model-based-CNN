# XRR-model-based-CNN


## X-ray reflectivity curves co-refinement based on the growth model implementation 

This repository provides tools for analyzing dependent XRR (X-ray reflectivity) curves, specifically those obtained from thin film growth experiments. The tools allow for accurate analysis of XRR data, even in cases where the data is sparsely sampled or noisy. The methodology employed is detailed in the following publication: https://journals.iucr.org/j/issues/2022/05/00/yr5088/yr5088.pdf.

The repository contains a few Jupyter notebooks and some data files. For the first time is useful to through the repository in the following steps:

### step 0 - Data generation for the CNN
**This step can be skipped**, but all the folder is just for the data generation. However, the repository contains a "Training data" folder with 50 *R(q,t)* (*training_data.npy*) and corresponding labels (*label_Theta.npy*).

### step 1 - Training of the CNN
Training data normalization, CNN architecture and training.

### step 2 - Implementation of sparse sampling 
Script loads normalized synthetic data and apply the drop-out function to create sparsely sampled data. The script saves the sparsely sampled data for the next step.

### step 3 - Training of the CNN on sparsely sampled data 
Load the sparsely sampled data and retrain the CNN with them.

### step 4 -  Implementation of the noise
Script loads normalized synthetic data and added Poisson noise distribution to create noisy data. The script saves the noisy data for the next step.

### step 5 - Training of the CNN on noisy data 
Script loads the noisy data and retrains the CNN with them.

### step 6 - CNN prediction
The script loads experimental data and the CNN model from the *conv_models* folder and makes predictions of parameters. New *R(q,t)* is generated based on the predicted parameters. The new and the experimental *R(q,t)* are plotted.

### step 7 - CNN prediction from sparsely sampled data 
The script loads experimental data and introduces the dropout function to create sparsely sampled experimental data. The script loads CNN (dropout) model from the *conv_models* folder and predicts parameters based on the sparsely sampled experimental data. New *R(q,t)* is generated based on the predicted parameters. The new and the experimental *R(q,t)* are plotted.

### step 8 - CNN prediction from noisy data
The script loads experimental data and applies Poisson noise distribution to create noisy experimental data. The script loads CNN (noise) model from the *conv_models* folder and predicts parameters based on the noisy experimental data. New *R(q,t)* is generated based on the predicted parameters. The new and the experimental *R(q,t)* are plotted.

