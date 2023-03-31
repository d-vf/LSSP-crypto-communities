# LSSP-crypto-communities

## Bitacointalk.org scraper:

- 1. Scrapper bitcointalk.org selenium getd all links of each board (gets a list of all post within a given board) 
   * bitcointalk.py
   * for "board" 1 (https://bitcointalk.org/index.php?board=1.0')
   * outpur: bitcointalk_data.csv
- 2. Gets all replies for each post (author, date, content, title, ID and url)
   * get_post_from_list.py
   * uses the list from 1 and gets all post (+ all nav pages) and store id, post, title, date and url
   * output folder: output_data/ (each topic)
 

To do:
approx 60000, that with 1  422.78 seconds per request would need more than 1 week to get all.

E.g 

Processed 7794 posts from https://bitcointalk.org/index.php?topic=20333.0 in 422.78 seconds.
Processed 10 posts from https://bitcointalk.org/index.php?topic=1649348.0 in 1.84 seconds.

* breaking list and running in // 

## Cypherpunk mailing list

Cypherpunk mailing list after pre processing (initial pre process).

(Merged dataset with cypherpunks mailing list (From, Date, Subject and Body)

https://zenodo.org/record/7765080#.ZBzhmOzMKcs

To do:

- fixing timedares (different TZ); almost all (0.1%)
- Checking duplicates
- regular expression
- spam filter
