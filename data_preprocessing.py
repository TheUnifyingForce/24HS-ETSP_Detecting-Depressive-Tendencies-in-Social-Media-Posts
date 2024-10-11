import pandas as pd
from sklearn.model_selection import train_test_split
import re
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS


# load the dataset
reddit_data_path = 'Original_Dataset/depression_dataset_reddit_cleaned.csv'
reddit_df = pd.read_csv(reddit_data_path)
reddit_df = reddit_df[['clean_text', 'is_depression']]

def clean_text(text):
    text = text.lower()  # Lowercase

    text = re.sub(r'https?://\S+|www\.\S+', '', text)  # Remove the URL
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)  # Remove the numbers
    text = ' '.join([word for word in text.split() if word not in ENGLISH_STOP_WORDS])  # 去除停用词
    return text

reddit_df['clean_text'] = reddit_df['clean_text'].apply(clean_text)
X = reddit_df['clean_text']
y = reddit_df['is_depression']

# 80% training set, 10% validation set, 10% test set
X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.2, random_state=42)
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=42)

# Save to the Preprocessed_Dataset folder
train_df = pd.DataFrame({'text': X_train, 'label': y_train})
val_df = pd.DataFrame({'text': X_val, 'label': y_val})
test_df = pd.DataFrame({'text': X_test, 'label': y_test})

train_df.to_csv('Preprocessed_Dataset/train.csv', index=False)
val_df.to_csv('Preprocessed_Dataset/dev.csv', index=False)
test_df.to_csv('Preprocessed_Dataset/test.csv', index=False)

print("The data preprocessing is complete and saved to the Preprocessed_Dataset folder.")

# Preview the dataset
train_df = pd.read_csv('Preprocessed_Dataset/train.csv')
print("Preview of the training set:")
print(train_df.head())

val_df = pd.read_csv('Preprocessed_Dataset/dev.csv')
print("\nPreview of the validation set:")
print(val_df.head())

test_df = pd.read_csv('Preprocessed_Dataset/test.csv')
print("\nPreview of the test set:")
print(test_df.head())
