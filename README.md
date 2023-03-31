# LSSP-crypto-communities

## Bitacointalk.org scrapper:

- 1. Scrapper bitcointalk.org selenium getd all links of each board (gets a list of all post within a given board) 
   * bitcointalk.py
   * for "board" 1 (https://bitcointalk.org/index.php?board=1.0')
   * outpur: bitcointalk_data.csv
- 2. Gets all replies for each post (author, date, content, title, ID and url)
   * bitcointalk_posts.py
   * uses the list from 1 and gets all post (+ all nav pages) and store id, post, title, date and url
   * output: bitcointalk_forum_data.csv

To do:
approx 60000, that with timeout=10 would need aprox 13,3 days to get all - breaking list and running in // 

## Cypherpunk mailing list

Cypherpunk mailing list after pre processing (initial pre process).

(Merged dataset with cypherpunks mailing list (From, Date, Subject and Body)

https://zenodo.org/record/7765080#.ZBzhmOzMKcs

To do:

- fixing timedares (different TZ); almost all (0.1%)
- Checking duplicates
- regular expression
- spam filter
