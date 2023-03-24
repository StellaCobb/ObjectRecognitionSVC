# ObjectRecognitionSVC

This code is for image classification using machine learning. It processes images using the PIL library and converts them into arrays using the numpy library. It then extracts features from the images and uses them to train a support vector machine (SVM) classifier using the sklearn library. The train_test_split function is used to split the data into training and testing sets. The SVM model is optimized using grid search to find the best hyperparameters for the model. The GridSearchCV function is used to perform a grid search over different combinations of hyperparameters. Finally, the model is used to predict the class of test images and the accuracy of the model is calculated. Overall, this code is a basic implementation of image classification using machine learning, where the model is trained on a set of labeled images and used to predict the class of new, unseen images. 

I have tested the image classification model on a dataset consisting of 7200 files and achieved a 100% accuracy rate. This suggests that the model was able to accurately classify all of the images in the test set.

To access the data set, visit https://www.kaggle.com/datasets/jessicali9530/coil100.
