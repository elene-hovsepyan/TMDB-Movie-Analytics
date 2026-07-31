import pandas as pd

# Read the dataset from CSV file
movie_data = pd.read_csv('TMDB_movie_dataset_v11.csv')

# Define columns to be dropped from the DataFrame
ToDrop = ['id','backdrop_path', 'original_title']

# Drop specified columns from the DataFrame
movie_data.drop(ToDrop, axis=1, inplace=True)

# Drop rows where 'title' and 'imdb_id' are missing
movie_data = movie_data[movie_data['title'] != '']
movie_data = movie_data[movie_data['imdb_id'] != '']

# Drop duplicate rows based on 'title' and 'release_date' columns
movie_data = movie_data.drop_duplicates(subset=['title', 'release_date'])

# Choose the most frequent data type among columns
common_type = movie_data.dtypes.value_counts().sort_values(ascending=False).index[0]

# Check each column and convert its data type to the common_type if needed
for column in movie_data.columns:
    if movie_data[column].dtype != common_type:
        movie_data[column] = movie_data[column].astype(common_type)

# Save the final DataFrame to a CSV file
movie_data.to_csv('cleaned_movies.csv', index=False)