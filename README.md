
![Logo](https://github.com/gajendrasharma-github/TMDB_Movie_Recommender_System/blob/master/Movie_Image.jpeg?raw=true)

# Movie Recommender System

Welcome to the **Movie Recommender System**! This project uses Streamlit to provide a simple and interactive way to recommend movies based on similarity of the content. Select a movie, and the system suggests five similar ones along with their posters.

## Features

- **Interactive Interface**: User-friendly interface built with Streamlit.
- **Movie Recommendations**: Suggests five movies similar to the selected movie.
- **Poster Display**: Displays movie posters using The Movie Database (TMDb) API.

## How It Works

1. **Load Data**: The application loads movie data and a similarity matrix from precomputed pickle files.
2. **User Selection**: Users select a movie from a dropdown menu.
3. **Recommendation Process**:
   - Finds the most similar movies based on the similarity matrix.
   - Fetches movie posters using the TMDb API.
4. **Display**: Shows recommended movies and their posters in a grid layout.

## Project Structure
- **app.py**: Main application script.
- **movies.pkl**: Pickle file containing movie data.
- **similarity.pkl**: Pickle file containing similarity matrix.
- **Data Preprocessing.ipynb**: Jupyter Notebook containing all the preprocessing.

## Data

The movie metadata used in this project is sourced from [Kaggle TMDb Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata). This dataset contains information on movies such as title, movie ID, and other metadata necessary for building the recommendation system.

## Skills and Technologies Used

- **Python**: The core language used for the project.
- **Streamlit**: For building the web application interface.
- **Pickle**: For loading and saving data files.
- **Requests**: For making HTTP requests to the TMDb API.
- **Data Processing**: Handling and processing data from pickle files.
- **Machine Learning**: Utilized similarity matrices for recommendations.
- **APIs**: Integration with The Movie Database (TMDb) API for fetching movie posters.

## Acknowledgements

 - The Movie Database (TMDb) for the movie data and posters.
 - Streamlit for the easy-to-use app framework.
 - Kaggle TMDb Movie Metadata for the movie dataset.

