import pandas as pd
import numpy as np
from sklearn import metrics

def popularity_based_recommender(dataframe, bookid_column, rate_column, userid_column, reference_dataframe, quantile_num):
    """Recommend books based on IMDB weighted rating. Input dataframes with bookid, rating and userid.
    Reference dataframe of bookid and author/title/first_author_title of books. 
    Quantile_num is the percentage of the books to be listed on the chart. It can take from 0 to 1.0. Output is
    the dataframe."""
    popular_books = dataframe.groupby(bookid_column)[rate_column].mean().reset_index().rename({rate_column: "average_rating"}, axis = 1)
    num_votes = dataframe.groupby(bookid_column)[userid_column].size().reset_index().rename({userid_column: "num_votes"}, axis = 1)
    popular_books = pd.merge(popular_books, num_votes, on = bookid_column, how = 'left')
    min_votes = popular_books.num_votes.quantile(quantile_num)
    mean_votes = popular_books.average_rating.mean()
    popular_books["weighted_average"] = ((popular_books["average_rating"] * popular_books["num_votes"]) + (mean_votes*min_votes))/ (popular_books["num_votes"] + min_votes)
    popular_books = pd.merge(popular_books, reference_dataframe, on = bookid_column, how = "left")
    popular_books = popular_books.sort_values(by="weighted_average", ascending = False).reset_index(drop=True)
    return popular_books

def user_collaborative_filtering_cosine(pivot_dataframe, cosine_dataframe, userid_query, workid_query):
    """Predict the rating based on user-user based collaborative filtering with cosine similarity. Output is the predicted rating of an interested book of a user."""
    # Similar users
    userquery_users = cosine_dataframe[userid_query].drop(userid_query)
    userquery_users = userquery_users[userquery_users > 0]
    # Similar users that read the book
    # Ratings
    sim_user = pivot_dataframe[workid_query].loc[userquery_users.index]
    sim_user = sim_user[sim_user.notnull()]
    # Weightage
    userquery_users_sim = userquery_users.loc[sim_user.index]
    userid_query_weights = userquery_users_sim.values/np.sum(userquery_users_sim.values)
    result = np.dot(sim_user.values, userid_query_weights)
    return result

def item_collaborative_filtering_cosine(pivot_dataframe, cosine_dataframe, userid_query, workid_query):
    """Predict the rating based on user-item based collaborative filtering with cosine similarity. Output is the predicted rating of an interested book of a user."""
    user_ratings = pivot_dataframe.T[userid_query]
    user_ratings = user_ratings[user_ratings.notnull()]
    sim_books = cosine_dataframe[workid_query].loc[user_ratings.index]
    sim_books = sim_books[sim_books > 0]
    sim_books_weights = sim_books.values/np.sum(sim_books.values)
    user_simbook = user_ratings.loc[sim_books.index]
    result = np.dot(user_simbook.values, sim_books_weights)
    return result

def coverage(test, predicted_rating):
    result_zero = test[test[predicted_rating] == 0]
    result_nonzero = test[test[predicted_rating] != 0]
    print(f"The total observations: {test.shape[0]}")
    print(f"Unable to predict:{result_zero.shape}")
    print(f"Able to predict:{result_nonzero.shape}")
    coverage = round((result_nonzero.shape[0])/(test.shape[0])*100, 2)
    print()
    print(f"The coverage for the recommender system is")
    return coverage

def ratings_rmse(test, actual_rating, predicted_rating):
    predictions = test[test[predicted_rating] != 0]
    rmse = np.sqrt(metrics.mean_squared_error(predictions[actual_rating], predictions[predicted_rating]))
    return rmse