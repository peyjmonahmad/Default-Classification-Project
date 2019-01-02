# Loan Default Predictions

This repository entails the classification process of predicting where a Credit One Bank customer will default or honor their loan.  The dataset used for analysis was found on the Kaggle public datasets page.

First, I had to decide which features were the most important towards making predictions.  This dataset contained many categorical variables which were all converted into dummy variables the ease the process.  Exploratory data analysis was performed to understand the distribution of data and view the intial descrepancies among the features.

Next, I utilized several classification models to accurately predict loan defaults.  These algorithms include logistic regression, K nearest neighbors, and random forest.  All the models made fairly smooth predictions, but one still performed better than others.  I also did some hyperparameter tuning to find optimal parameters with overfitting the model.

Lastly, I analyzed coefficients of the results to establish default likelihood changes for each unit increase/decrease of a specific feature.  The process of the modeling can be found in the Final Project (.ipynb) notebook.
