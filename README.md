## Capstone Project : Books Recommender System

### Problem Statement

There is always a need for book recommendation when one would like to start picking a new book to read. With the vast availability of book choices we have currently, readers are always faced with the situation to decide which books to select next and on average, the process of selecting a suitable book for the reader may take up a huge amount of time, effort and energy. With the rising trend of online platform preference, as a data scientist in the online bookstore, we aim to build a book recommendation system in our online bookstore website to help readers save up time to search for the books that they are interested in and match the books to their preference. Our team will explore the use of non-personalized recommendation system (popularity-based and content-based recommender system) and personalized recommendation system (collaborative filtering and model-based recommender systems) for predicting books ratings that the readers may rate. For personalized recommendation system, the recommender system's success will be evaluated based on the root mean square error (RMSE) between the actual and the predicted rating. This prediction will allow our bookstore website to recommend books that are more personalized to the readers, leading to an enhanced reader's experience and higher subscription rate, which may lead to an increase in business profitability.

---
### Background

Reading is a superfood for our brains and many of us read books throughout our journey of life. With the vast amount of books available (estimated 130 million books in 2010), readers often faced with the situation to decide which books to read next [[1]](https://mashable.com/2010/08/05/number-of-books-in-the-world/). As it is estimated that a person read about 12-120 books per year with some exceptional readers reading 200-300 books per year, they will be able to finish with a maximum of about 1 - 23 thousand books in their lifetime (with an estimated lifespan of a person having 80 years and subtracting the first 5 years of age) [[2]](https://lostinbook.com/how-many-books-should-i-read-a-year/)[[3]](https://bookriot.com/what-i-learned-from-reading-300-books-in-2017/). With the current available books and the rate of new books published about 2.2 million a year, a reader will not be able to read all the books available and would want to select the books that matches their choice of preference [[4]](https://ebookfriendly.com/countries-publish-most-books-infographic/). As a result, a book recommendation system becomes essential and very useful for readers who are undecided on which books to pick up next.

On average, the process of selecting a suitable book for the reader may take up a huge amount of time, effort and energy. This process of selection may include through social media, online browsing or book referrals from friends. [[5]](https://www.nlb.gov.sg/Portals/0/Docs/AboutUs/2018%20NATIONAL%20READING%20HABITS%20STUDY%20ON%20ADULTS%20-%20REPORT.pdf). As a data scientist in the online bookstore, we aim to design and create a book recommender system in our online bookstore website to help readers save up time to search for the books that they are interested in and match to their preference. Our team will explore the use of non-personalized recommendation system (popularity-based and content-based recommender system) and personalized recommendation system (collaborative filtering and model-based recommender systems) for predicting the books that the readers would rate. For personalized recommendation system, the model's success will be evaluated based on the root mean square error (RMSE) between the actual and the predicted rating. This prediction will allow our online bookstore website to recommend books that are more personalized and customized to the readers' preference, provide a better and seamless reading experience for readers, which will lead to a higher sastisfaction and overall help to improve business and sales. 

---
### Data Dictionary

As goodreads has one of the world's largest site for readers and book recommendations, we will be using the goodreads datasets obtained from [University of California San Diego Book Graph](https://sites.google.com/eng.ucsd.edu/ucsdbookgraph/home?authuser=0) to aid in the development of book recommendation system [6]. 
The assumption is goodread readers are random and come from everywhere around the world, in which the data is symbolic and representative of book buyers on online platform.
The dataset contains meta-data of books and user-book interactions.

The datasets of user-book interactions will be used for modeling.
For more details, please refer to the data_dictionary_model.ipynb

---
### Data Cleaning

The datasets are cleaned as followed:-

* Selected columns for the datasets
* Handled data values including changing to integers/floats, remove spaces and rename values for consistency
* Generate new dataframes for easy references
* Remove books with majority of the information are missing.
* Generate new columns of first_author_name, first_author_title in meta-data of books dataset
* Fill in missing values such as title in meta-data of books dataset
* Map work_id into user-book interactions dataset and average the rating score.
* For user-book interactions dataset, remove books that are not read and without rating, remove books with no information in the meta-data of books dataset, map work_id and average the rating score
* Create a new dataframe of a cleaned user-book interactions dataset with work_id and genres map to it

---
### Exploratory Data Analysis

The majority of the books present in this dataset are as followed:-

* **Genre** - fiction
* **The number of books in a series** - approximately 3 books (Range: 0 to 738 books) (excluding book editions)
* **Book editions** - less than 10 book editions (Range: 1-3676 book editions)
* **Number of pages** - 150-350 pages (Range: 0-300 thousand pages)
* **Year of book published** - an increasing trend in the books published from 1950 to recent years(21st century)
* **Book language type** - undefined and english
* **Book format types** - paperback, undefined, hardcover and ebook.
* **Book publisher** - undefined. The publisher having more than 10 thousand books in goodreads are smashwords edition, harlequin and createspace.


In goodreads website, the majority of the books present in this dataset have the following characteristics:-

* **Books average rating** - 4.0 (Range: 1.0 to 5.0)
* **Book authors average rating** - 4.0 (Range: 1.0 to 5.0)


For the user book interactions, the books have the following characteristics:-
* A significant proportion of the books rated are not reviewed by the users
* Outlier are removed in the number of books rated per user
* Majority of the users rated the books less than 150 books with some users rated more than 7500 to 17000 books.
* Majority of user have rated the book with an average rating of 4.0 (Range: 1.0 to 5.0)
* Majority of the books are being rated by less than 20 users (Range: 1-307136 users)

Due to computational limitation, threshold for ratings of a book required and number of books rated by a user are applied prior to obtain a subset fraction of the full dataset for further analysis. This subset fraction is then further filtered to ensure sufficient user book interactions when performing train-test-split.


----
### Data Preprocessing and Modeling & Analysis Summary

**For non-personalized recommendation** 
* popularity-based recommender system - able to recommend the top 10 popular books, which coincide with the exploratory data analysis result.
* content-based recommender system, - able to recommend based on similar genre. 

As non-personalized recommendation does not provide predicted ratings, we will be evaluating the collaborative filtering and model-based recommender system for our subsequent analysis before choosing a final model.

**For personalized recommendation** 
* All 7 models has a root mean square error (RMSE) higher than the null model, which is based on random rating prediction. 
* For user-based and item-based collaborative filtering, both have very low coverage (the percentage of the test set that can be predicted from the train set) and the prediction model fair slightly better than the null model with an improvement of 34% improvement.
* K-means clustering with collaborative filtering of user-based and item-based has led to an increase of coverage to 55-58% and an improvement of RMSE of 43% compared to the null model. However, it is to note that the clustering has limit the books and users to their genres, which limits the user's preference according to a particular genre.
* Model-based recommender system is able to increase the coverage to 100% with an improvement of 47-53% compared to the null model. The singular value decomposition algorithms perform better than non-negative matrix factorization. 

As there is minimal difference between singular value decomposition and singular value decomposition ++, we will be selecting the singular value decomposition as our final model as it has the lowest RMSE out of all, which translates to the lowest error of the predicted rating against the true rating. This will allow us to predict the ratings more accurately and recommend books that are more targeted to the readers and better reader's experience.

---

### Conclusion

In conclusion, we have gathered and collected our datasets, performed data cleaning and analyzed the data with visualization methods. In our exploratory data analysis, we discovered majority of the books characteristics in the dataset. We also found that the user book interactions illustrates the long tail scenario in which a small fraction of the books are highly rated by the users while a large proportion of the books have low number of ratings by the users. Due to the large dataset and computational limitation, we have set a threshold for ratings of a book required and number of books rated by a user prior to obtain a subset fraction for further analysis.

With the dataset and analysis, we have built two models for non-personalized recommendation and seven models for personalized recommendation. For non-personalized recommendation systems, the popularity-based recommender systems is able to recommend the top 10 popular books while the content-based recommender system is able to recommend based on similarity in genre. For the personalized recommendation, all models have RMSE lower than the null model. The singular value decomposition was chosen as our final model as it has the best performance with the lowest RMSE and 100% coverage as compared to the other models studied. With this singular value decomposition model, we are able to predict the ratings more accurately and recommend books that are more customized to the readers's preference, and this can provide a seamless reading experience for user which leads to a higher satisfaction, which in turns may drive more traffic to our online bookstore and increase sales.

---

### Recommendations

Out of the 7 models built for personalized recommendation, the singular value decomposition has the lowest RMSE with a full coverage (100%) compare to the other models such as collaborative filtering and k-means clustering with collaborative filtering. We are also able to improve the accuracy of the prediction by 53% compared to the null model, which is a random prediction of ratings. With this model, we are able to have the full coverage and able to predict the unknown ratings of the user with an RMSE of 0.9086, thus allowing us to recommend books that are more suited to the readers through the website.

As such, we will recommend this singular value decomposition model recommender system to be employed as our book recommender system as a solution to our challenges identified in our problem statement.

---
### Future Improvement

Future work that could be done is to explore more algorithms that may further improve the RMSE score.

Furthermore, one could also explore algorithms that can handle greater user-book-interactions with good scalability and faster processing speed so that full datasets maybe use for analysis in future.

Implicit data such as user purchased history and more details on the users such age, geographical location can also be explored to enhance the user's experience.

---
### References

[1] B. Parr, "Google: There are 129,864,880 Books in the Entire World," *Mashable, Inc.*, August 06, 2010. [Online]. Available:https://mashable.com/2010/08/05/number-of-books-in-the-world/ [Accessed: June 06, 2021].

[2] E. Yilmaz, "How Many Books Should I Read in a Year?," *Lost In Book*, August 05, 2020. [Online]. Available:https://lostinbook.com/how-many-books-should-i-read-a-year/ [Accessed: June 06, 2021].

[3] L. Sackton, "What I learned from reading 300+ books in 2017," *Book Riot*, January 08, 2018 [Online]. Available:https://bookriot.com/what-i-learned-from-reading-300-books-in-2017/ [Accessed: June 06, 2021].

[4] P. Kowalczyk, "Which countries publish the most books? (Infographic)," *Ebook Friendly*, April 06, 2017 [Online]. Available:https://ebookfriendly.com/countries-publish-most-books-infographic/ [Accessed: June 06, 2021].

[5] "2018 National Reading Habits Study on Adults," *National Library Board Singapore*, 2019. [Online]. Available:https://www.nlb.gov.sg/Portals/0/Docs/AboutUs/2018%20NATIONAL%20READING%20HABITS%20STUDY%20ON%20ADULTS%20-%20REPORT.pdf [Accessed: May 10, 2021].

[6] M. Wan, and J. McAuley, "Item Recommendation on Monotonic Behavior Chains," *Proceedings of the 12th ACM conference on Recommender Systems, RecSys 2018*, September 2018, pp. 86-94. doi: 10.1145/3240323.3240369 [Online]. Available:https://dl.acm.org/doi/10.1145/3240323.3240369 [Accessed: May 10, 2021].