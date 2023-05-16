# LSSP-crypto-communities


## Cypherpunk mailing list

Cypherpunk mailing list after pre processing (pre process + timedate fixed (to UTC), removed duplicates).

(Merged dataset with cypherpunks mailing list (From, Date, Subject and Body)

https://zenodo.org/record/7765080#.ZBzhmOzMKcs (initial + timedate fixed)

## Bitcointalk.org scrape

Bitcoin scrape (April-may 2023) or board 1 (https://bitcointalk.org/index.php?board=1.0) with within this board/list 

"PostID": post_id, "Username": username_element.text, "PostDate": post_date_element.text, "PostContent": post_content_element.text,

"PostTitle": post_title_element.text, "PostURL": post_url for all pages per post/topic

File name : output_file_name = output_folder + url.split('=')[1].replace('.', '_') + ".csv" (from the list of url's per topic)

https://zenodo.org/record/7924639#.ZFzcxuzMKzk
