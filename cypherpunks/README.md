1. Data Processing:  LSSP_cypherpunks_dataprep_I .ipynb

1. Initial preprocessing namely:

- merging 3 data sources

- fixing dates and putting all dates back to UTC (final output: allmails_data_time_parsed_utc)

- removing duplicates

2. text treatment and LDA: cypherpunks_lda.ipynb

Functions in cypherpunks_lda.py

* `download_data()`: Downloads the Cypherpunks forum posts dataset from GitHub.
* `clean_data()`: Cleans the Cypherpunks forum posts dataset by removing stop words and punctuation.
* `train_lda()`: Trains the LDA model on the cleaned Cypherpunks forum posts dataset.
* `predict_topics()`: Predicts the topics for each Cypherpunks forum post.
* `visualize_topics()`: Visualizes the topics identified by the LDA model.
* `get_top_words()`: Gets the top words for each topic.
* `get_sentiment()`: Gets the sentiment of each topic.
* `get_influential_users()`: Gets the most influential users for each topic.
* `preprocess_text()`: Used to clean and preprocess text data.
* `get_wordnet_pos()`: Used to get the part-of-speech (POS) tag for a word.
* `lemmatize_text()`: Used to lemmatize a word.
* `tokenize_text()`: Used to tokenize a text.
* `sent_to_words()`: Used to convert sentences to words.
* `remove_stopwords()`: Used to remove stopwords from a list of words.

