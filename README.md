# 24HS-ETSP_Detecting-Depressive-Tendencies-in-Social-Media-Posts
UZH 24HS 521-900a Essentials in Text and Speech Processing


## Project Description

This is a binary text classification using sentiment analysis, aiming to determine
whether a social media post shows signs of depressive tendencies. The input is text, and the
output is a prediction of whether the content indicates depressive symptoms.
What makes this project both interesting and meaningful is leveraging NLP techniques to
identify early warning signs of depression, potentially enabling timely interventions and support, thereby applying technology for social good.

Based on existing solutions, we aim to introduce more advanced pre-trained models such as
BERT and fine-tune them to improve the effectiveness of detecting tendencies of depression.
Our experiments will be conducted using both traditional classification models, such as logistic regression 
and support vector machines (as baselines), and advanced large language models like BERT.

Additionally, we plan to utilize data augmentation techniques like SMOTE to address data
imbalance, enabling the model to better identify minority depression-related texts. T
he performance of these models will be evaluated using metrics such as precision, recall, and F1 score.

In this project, our primary goal is to analyze social media posts and assess the likelihood of
depressive tendencies. It could potentially be expanded into a web-based application where
users or mental health professionals can input text for analysis.


## Dataset

The dataset consists of social media posts annotated with binary labels indicating whether the post shows signs of depression (`1`) or not (`0`).

### Sources:
- **Reddit Depression Dataset**: [Kaggle Dataset Link](https://www.kaggle.com/datasets/infamouscoder/depression-reddit-cleaned/data)

### Files:
- `depression_dataset_reddit_cleaned.csv`: Contains the Reddit posts with the `is_depression` label.
- Preprocessed datasets:
  - `train.csv`: Training data after preprocessing.
  - `dev.csv`: Validation data after preprocessing.
  - `test.csv`: Test data after preprocessing.


## Data Preprocessing

The data preprocessing involves the following steps:
1. **Text Cleaning**: 
   - Lowercasing all text.
   - Removing URLs, HTML tags, punctuation, and numbers.
   - Removing stopwords to reduce noise in the data.

2. **Dataset Splitting**: 
   - The data is split into training (80%), validation (10%), and test (10%) sets.

