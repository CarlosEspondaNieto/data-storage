# -*- coding: utf-8 -*-

# Data Graduates: Analysis and Other Examples
# Author: Jorge Raze

# First import urllib for downloading and uncompress the file
import urllib.request
import zipfile
import os
import pandas as pd
from statistics import mean
from matplotlib import pyplot as plt

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
# group_by_count = grouped.aggregate(count)

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
# Do we need to subset?
hottest_titles = ratings_by_title.index[ratings_by_title >= 213]
print(hottest_titles)

# Getting the mean of rated movies
mean_ratings = rated_movies.pivot_table(
    'rating',
    index='title',
    aggfunc='mean')

# The mean of the hottest movies
mean_ratings = mean_ratings.ix[hottest_titles]

print(mean_ratings)


titles = [hottest_titles[0],hottest_titles[1],hottest_titles[2],hottest_titles[3],hottest_titles[4]]
mean = [mean_ratings[0], mean_ratings[1], mean_ratings[2], mean_ratings[3], mean_ratings[4]]
xs = [i + 0.1 for i, _ in enumerate(titles)]
plt.bar(xs,mean)
plt.xticks([i + 0.0 for i, _ in enumerate(titles)], titles)
plt.ylabel("mean of rated movies")
plt.title("the top 5")
plt.show()

#titles = [hottest_titles[0],hottest_titles[1],hottest_titles[2],hottest_titles[3],hottest_titles[4],hottest_titles[5],hottest_titles[6],hottest_titles[7],hottest_titles[8],hottest_titles[9],hottest_titles[10],hottest_titles[11],hottest_titles[12],hottest_titles[13],hottest_titles[14],hottest_titles[15],hottest_titles[16],hottest_titles[17],hottest_titles[18],hottest_titles[19]]
#mean = [mean_ratings[0], mean_ratings[1], mean_ratings[2], mean_ratings[3], mean_ratings[4], mean_ratings[5],mean_ratings[5],mean_ratings[7],mean_ratings[8],mean_ratings[9],mean_ratings[10],mean_ratings[11],mean_ratings[12],mean_ratings[13],mean_ratings[14],mean_ratings[15],mean_ratings[16],mean_ratings[17],mean_ratings[18],mean_ratings[19]]
#xs = [i + 0.1 for i, _ in enumerate(titles)]
##plt.bar(xs,mean)
#plt.xticks([i + 0.0 for i, _ in enumerate(titles)], titles)
#plt.ylabel("mean of rated movies")
#plt.title("the top 5")
#plt.show()

numbers=[]

mean=[]

titles=[]

for i in range(0,20):

  numbers.append(i)

  mean.append(mean_ratings[i])

  titles.append(hottest_titles[i])

plt.scatter(numbers,mean)

for titulo, numeros_count, promedios_count in zip(titles, numbers, mean):

  plt.annotate(titulo,xy=(numeros_count,promedios_count),

    xytext=(5,5),textcoords='offset points')

plt.title("Top 20")

plt.ylabel("mean of rated movies")

plt.show()



# For loop for generating the files
for i in range(3):
    if os.path.isfile(filenames_array[i]):
        if DEBUG:
            print("File %s already exists!" % i)
    else:
        # Export to CSV
        print("Exporting file to CSV")
        final_variables_array[i].to_csv(filenames_array[i])


