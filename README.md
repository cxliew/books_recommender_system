## Capstone Project : Books Recommender System

### Problem Statement

There is always a need for book recommendation when one would like to start picking a new book to read. With the vast availability of book choices we have currently, readers always faced with the difficulty of choosing a book to read and on average take a huge amount of time, effort and energy to select and choose a book to read. This include social media, online browsing and book referrals, which is time-consuming [[1]](https://www.nlb.gov.sg/Portals/0/Docs/AboutUs/2018%20NATIONAL%20READING%20HABITS%20STUDY%20ON%20ADULTS%20-%20REPORT.pdf). With the current lacking of a book recommendation system in libraries, as a data scientist in the national library, we aim to help reader to save time to decide for which books to read, by developing book recommendations system which matches their  preferences. The team will explore the use of popularity-based system, content-based system and collaborative filtering-based system for predicting the books that the readers would rate. The model's success will be evaluated based on the root mean square error that will evaluate the differences between the actual rating and the predicted ratings a reader will rate for a book. The closer the predicted rating to the actual rating, the better the book can be selected for recommendation,which will enhance the reader experience.


---
### Data Dictionary

As goodreads has one of the world's largest site for readers and book recommendations, we will be using the goodreads datasets obtained from [University of California San Diego Book Graph](https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home?authuser=0) to aid in the development of book recommendation system [1]. 
The assumption is goodread readers are random and come from all around the world, in which the data is symbolic of readers in national libraries.
The dataset contains meta-data of books and user-book interactions.

The datasets obtained are as followed:-

Meta-data of books:-
* goodreads_books
* goodreads_book_works
* goodreads_book_authors
* goodreads_book_series
* goodreads_book_genres_initial

User-book interactions:-
* goodreads_interactions
* book_id_map

For more details, please refer to the data_dictionary.ipynb.

---
### Data Cleaning

The datasets are cleaned as followed:-

* Columns are selected for futher analysis
* Data values:- Change to integers/floats, remove spaces and rename values for consistency
* Generate new dataframes for easier references
* Remove books that have majority of the information missing
* Map the author name to the booklist and generate a new column for author-title of a book for easier reference
* Fill in missing values in title in goodreads_book_works
* Map work_id into goodreads_interactions and average the rating score.

---
### References

[1] M. Wan, and J. McAuley, "Item Recommendation on Monotonic Behvaior Chains," *Proceedings of the 12th ACM conference on Recommender Systems, RecSys 2018*, September 2018, pp. 86-94. doi: 10.1145/3240323.3240369 [Online]. Available:https://dl.acm.org/doi/10.1145/3240323.3240369 [Accessed: May 10, 2021].