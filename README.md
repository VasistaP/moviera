# Moviera - Movie Recommendation System

## Description

Moviera is an online movie recommendation system designed to suggest 5 movies based on a chosen movie of interest. It utilizes the Porter stemming algorithm to identify similar movies based on attributes such as title, genre, and more. With a dataset comprising 5000 movies, Moviera offers a diverse selection for users to explore.

## Packages Used

- **nltk:** Utilized for building the Porter stemming model.
- **sklearn:** Employed for data vectorization.
- **pickle:** Utilized for saving the trained models.
- **streamlit:** Used for hosting with an interactive web UI.
- **pandas:** Utilized for dataset processing.

## Setup

To set up Moviera, follow these steps:

1. **Add Python Executable to PATH:**

   - **For Windows:**

     ```cmd
     set PATH=%PATH%;C:\path\to\Python\Scripts
     ```

   - **For Linux:**

     ```bash
     export PATH=$PATH:/path/to/python/bin
     ```

2. Install the required packages by running the following command in your terminal:

   ```bash
   pip install -r requirements.txt
   ```

3. Extract `data.zip` to `data` directory.

4. Run the code in `trainer/model.ipynb`.

## Usage

To use Moviera, follow these steps:

1. Run the following command in your terminal:

   ```bash
   streamlit run deb.py
   ```

This will start the Moviera web application, allowing you to input a movie of interest and receive recommendations based on it.
