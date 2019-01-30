# Loan Default Predictions

This repository entails the classification process of predicting where a Credit One Bank customer will default or honor their loan.  The dataset used for analysis was found on the Kaggle public datasets page.  The goal for this project was to minimize the false positive errors, which would be the most detrimental for the bank.  In the case of this error, the bank would predict that a customer would honor their loan, but in reality they defaulted.

First, I had to decide which features were the most important towards making predictions.  This dataset contained many categorical variables which were all converted into dummy variables to ease the process.  Exploratory data analysis was performed to understand the distribution of data and view the intial descrepancies among the features.

Next, I utilized several classification models to accurately predict loan defaults.  These algorithms include logistic regression, K nearest neighbors, and random forest.  All the models made fairly smooth predictions, but one still performed better than others.  I also did some hyperparameter tuning to find optimal parameters without overfitting the model.

Lastly, I analyzed coefficients of the results to establish default likelihood changes for each unit increase/decrease of a specific feature.  The process of the modeling can be found in the Final Project (.ipynb) notebook.

I constructed a basic flask web application that lets you input a few features and predicts whether you will default or honor your loan!  The code for this app can be found in the flask_default (.py) notebook.
