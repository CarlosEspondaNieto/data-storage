# -*- coding: utf-8 -*-

# Data Graduates: Analysis and Other Examples
# Author: Jorge Raze

#Carlos' note: In line 185 begins my code

# First import urllib for downloading and uncompress the file
import urllib.request
import zipfile
import os
from collections import Counter
import pandas as pd
from statistics import mean
from matplotlib import pyplot as plt
import numpy as np
import seaborn 
seaborn.set() 

DEBUG = False

# # This is the URL for the public data
url = "http://files.grouplens.org/datasets/movielens/ml-latest-small.zip"
# This is the working directory
working_dir = "data/movies/"
# Destination filename
file_name = working_dir + "movies.zip"
# We already know the expected files so:
expected_files = [
    'links.csv',
    'movies.csv',
    'ratings.csv',
    'README.txt',
    'tags.csv']
# movie.ID mv.ID MV.ID MV_ID
movie_names = ['movie_id', 'title', 'genres']
rating_names = ['user_id', 'movie_id', 'rating', 'timestamp']
# Helper arrays for generating the final files
filenames_array = [
    working_dir + 'top20.csv',
    working_dir + 'top5.csv',
    working_dir + 'final.csv']


# Download the file from `url` and save it locally under `file_name`:
if os.path.isfile(file_name):
    if DEBUG:
        print('Data is already downloaded')
else:
    if DEBUG:
        print("Downloading file")
    urllib.request.urlretrieve(url, file_name)

# There's an extra dir level in thwe extracted files
inner_dir = "ml-latest-small/"
# I want to know the names of the extracted files
file_names = os.listdir(working_dir + inner_dir)

if file_names == expected_files:
    if DEBUG:
        print("You already have the data files, check it!")
else:
    # This is the code for uncompress hte zipfile
    path_to_zip_file = working_dir + "movies.zip"
    # Reference to zipfile
    zip_ref = zipfile.ZipFile(path_to_zip_file, 'r')
    print("Extracting files")
    zip_ref.extractall(working_dir)
    # Is important to use .close()
    zip_ref.close()


# Reading the files needed for this analysis
movies = pd.read_csv(
    working_dir +
    inner_dir +
    expected_files[1],
    sep=',',
    names=movie_names)
ratings = pd.read_csv(
    working_dir +
    inner_dir +
    expected_files[2],
    sep=',',
    names=rating_names)


# Let's print the first lines of each dataframe
if DEBUG:
    print(movies.head())
    print(ratings.head())

    print("The names of our new data frames are:")
    print(list(movies.columns.values))
    print(list(ratings.columns.values))

    print("The dimension of the dataframes are:")
    print(movies.count())
    print(ratings.count())

rated_movies = pd.merge(movies, ratings, on='movie_id')
rated_movies = rated_movies.sort_values('rating', ascending=False)

rated_movies.to_csv(working_dir + 'rated_movies.csv')

# Number of movies: 9126
# Number of evaluations: 100005

# Rated movies names:
# ['movie_id', 'title', 'genres', 'user_id', 'rating', 'timestamp']

# Shortcut for names
rated_movies.dtypes

# Get summary of your data
rated_movies.describe()

# Getting the Transpose
transposed_movies = rated_movies.T

# Sorting by an index
rated_movies.sort_index(axis=1, ascending=False)

# You can get the first two rows with
rated_movies[0:3]

# You can select data based in value of a column
rated_movies['rating'] = pd.to_numeric(rated_movies['rating'][1:100005])
rated_movies[rated_movies['rating'] > 4]
rated_movies[rated_movies['title'] == 'Shawshank Redemption, The (1994)']

# rated_movies = rated_movies.pop(0)

# You can aggregate data like this
grouped = rated_movies.groupby('title')
group_by_sum = grouped.aggregate(sum)
group_by_mean = grouped.aggregate(mean)
#group_by_count = Counter(grouped).most_common(20)

# Or the short way
grouped = rated_movies.groupby('title').sum()

# Subsetting for our results
top20 = grouped.sort_values('rating', ascending=False)[0:20]
top5 = top20[0:5]
# Wee need to transform it to a dict
# so we can get the movies' titles
top5_dict = top5.to_dict()
# We need to get the items (Movies titles)
top5_items = top5_dict['rating'].items()

# A helper array for stacking the results per movie
frames = []

# A for loop for getting all the results matching a movie
for name, value in top5_items:
    frames.append(rated_movies[rated_movies['title'] == name])

# Concatenate into a single data frame
result = pd.concat(frames)

# Helper array for generating target files
final_variables_array = [top20, top5, result]

# We can get the observations as well
ratings_by_title = rated_movies.groupby('title').size()
#sorting the reviews in order desc
reviews_count = ratings_by_title.sort_values(ascending=False)[0:20]

# Do we need to subset?
hottest_titles = ratings_by_title.index[ratings_by_title >= 213]
hottest_titles2 = [x.replace("'",'') for x in hottest_titles]
#hottest_titles3 = [str(x) for x in hottest_titles2]
# Getting the mean of rated movies
mean_ratings = rated_movies.pivot_table(
    'rating',
    index='title',
    aggfunc='mean')



# The mean of the hottest movies
mean_ratings = mean_ratings.ix[hottest_titles]
mean_ratings = mean_ratings.sort_values(ascending=False) 

print(mean_ratings)


#-------LINEAR AND BAR CHARTS CODE OF MOVIES---------------------------------

#Here we are storing the names of the top 20 with the same order into a list:rating_names
rating_names=[x for x in top20.index[:]]

#Here  we put a range to x-axis, which lenght is 20
x_axis= np.arange(0.0,20.0,1.0)
#Setting the rating_names as x-labels
plt.xticks(x_axis, rating_names, rotation=-90)
#x and y values
plt.plot(x_axis,top20, 'go-')
plt.title("Top 20 of ratings")
plt.ylabel("# of ratings ")
plt.show()


#Storing the names of the reviews_count into titles with the same order of reviews_count
titles = [x for x in reviews_count.index[:]]

xs = [i + 0.1 for i, _ in enumerate(titles)]
plt.bar(xs,reviews_count)
plt.xticks([i + 0.0 for i, _ in enumerate(titles)], titles, rotation=90)
plt.ylabel("# of reviews", )
plt.title("Top 20 of the most viewed movies")
plt.show()

#---
rate_by_point_redemption = result[result['title']== 'Shawshank Redemption, The (1994)'].groupby('rating').size()
#transforming the serie result into a dictionary with th e data I need
rate_by_point_redemption_dict= rate_by_point_redemption.to_dict()
#Generating a new dictionary sorted by key
o_rate_by_point_redemption_dict = collections.OrderedDict(sorted(rate_by_point_redemption_dict.items()))
#Here I'm taking apart the keys and the values, storing each one in lists
keys_redemption = list(o_rate_by_point_redemption_dict.keys())
values_redemption = list(o_rate_by_point_redemption_dict.values())

width=0.3
plt.bar(keys_redemption, values_redemption, width, color='green', align='center')
plt.ylabel("# of reviews")

plt.title('reviews by each rating of Shawshank Redemption')
plt.xticks(keys_redemption)

plt.show()

#y_axis= np.arange(0.0,20.0,1.0)
#plt.yticks(y_axis, titles2)
#plt.plot(reviews_count, y_axis, 'o-')
#plt.title("Top 20 of the most viewed movies")
#plt.xlabel("# of reviews")
#plt.show()

#top20_dict = top20._dict_()


# For loop for generating the files
for i in range(3):
    if os.path.isfile(filenames_array[i]):
        if DEBUG:
            print("File %s already exists!" % i)
    else:
        # Export to CSV
        print("Exporting file to CSV")
        final_variables_array[i].to_csv(filenames_array[i])


