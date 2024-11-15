# 24HS-ETSP_Detecting-Depressive-Tendencies-in-Social-Media-Posts
UZH 24HS 521-900a Essentials in Text and Speech Processing


## Project Description

In this project, the goal is to assess the performance of various NLP models in the context
of sentiment analysis and depression detection. The task involves categorizing text data
into different classes, either representing sentiment (healthy vs. depressed) or levels of
depression (severe, moderate, and not depressed). These problems are critical as they
contribute to mental health monitoring, where NLP models can help identify distress
signals in textual data.
The models evaluated in this study are based on transformer architectures, specifically
RoBERTa, which has become one of the most effective models for text classification tasks.
By comparing base and fine-tuned versions of these models, we aim to determine how well
each performs in these domains and whether fine-tuning can enhance performance.


## Dataset

The dataset consists of social media posts annotated with binary labels indicating whether the post shows signs of depression (`1`) or not (`0`).

### Original datasets:
- **Reddit Depression Dataset**: [Kaggle Dataset Link](https://www.kaggle.com/datasets/infamouscoder/depression-reddit-cleaned/data)
- **Detecting Signs of Depression from Social Media Posting**: [Dataset Link](https://github.com/Kayal-Sampath/detecting-signs-of-depression-from-social-media-postings)

### Preprocessed datasets:
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

## Model

For the aimed task, we used two main transformer-based models, all based on RoBERTa,
a well-established model known for its high performance on NLP tasks. 

The models are:

• cardiffnlp/twitter-roberta-base-sentiment: Pretrained on a sentiment analysis task
and designed for text classification.

• Fine-tuned cardiffnlp/twitter-roberta-base-sentiment: Fine-tuned by us from
cardiffnlp/twitter-roberta-base-sentiment.

• FacebookAI/roberta-base: A general-purpose RoBERTa model trained on diverse
text data.

• Fine-tuned Facebookai/roberta-base: Fine-tuned by us from Facebookai/roberta-
base.

These models were chosen because of their proven capabilities in text classification tasks.
Pretrained models like RoBERTa (A Robustly Optimized BERT Pretraining Approach)
is a variant of the BERT (Bidirectional Encoder Representations from Transformers) are
known for their strong performance out-of-the-box, but fine-tuning allows them to better
adapt to specific domains, which we hypothesize will improve their performance on tasks
like sentiment and depression detection.
For training, we used transfer learning, leveraging pre-trained models and fine-tuning them
on our datasets. This approach allows for faster training times, as the models already have
general knowledge about language.
Additionally, comparing the base model with the fine-tuned version provides insights into
the significance of task-specific pretraining and whether leveraging data from similar do-
mains enhances the model’s ability to understand context in mental health-related texts.
