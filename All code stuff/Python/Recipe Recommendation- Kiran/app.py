from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors

app = Flask(__name__)

# Load the dataset
recipe_df = pd.read_csv("recipe_final.csv")

# Fill NaNs in ingredients_list
recipe_df['ingredients_list'] = recipe_df['ingredients_list'].fillna('')

# Vectorize ingredients using TF-IDF
tfidf = TfidfVectorizer()
ingredient_vectors = tfidf.fit_transform(recipe_df['ingredients_list']).toarray()

# Scale nutritional features
nutritional_features = recipe_df[['calories', 'fat', 'protein']]
scaler = StandardScaler()
scaled_df = scaler.fit_transform(nutritional_features)

# Combine scaled nutrition + ingredient vectors
combined_features = np.hstack([scaled_df, ingredient_vectors])

# Fit KNN model
knn = NearestNeighbors(n_neighbors=5)
knn.fit(combined_features)

@app.route('/')
def home():
    return render_template('index.html', recipes=None, warning=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get inputs from form
        calories = float(request.form['calories'])
        protein = float(request.form['protein'])
        fat = float(request.form['fat'])
        ingredients = request.form['ingredients'].lower().strip()

        # Process ingredient input
        user_ingredients = [ing.strip() for ing in ingredients.split(',') if ing.strip()]
        
        # Filter recipes that include ALL the input ingredients
        filtered_df = recipe_df[recipe_df['ingredients_list'].apply(
            lambda x: all(ing in x.lower() for ing in user_ingredients)
        )]

        # Fallback to full dataset if no matches found
        if filtered_df.empty:
            filtered_df = recipe_df.copy()
            ingredient_warning = "No perfect ingredient match found. Showing closest nutritional matches."
        else:
            ingredient_warning = ""

        # Prepare input nutrition vector
        input_features = pd.DataFrame([[calories, fat, protein]], columns=['calories', 'fat', 'protein'])
        scaled_input = scaler.transform(input_features)

        # Use only filtered ingredient vectors
        filtered_indices = filtered_df.index.tolist()
        ingredient_vectors_filtered = ingredient_vectors[filtered_indices]

        # Input vector = nutrition + zeroed ingredients (only nutrition is used for input matching)
        input_vector = np.hstack([scaled_input, np.zeros((1, ingredient_vectors.shape[1]))])

        # Combine filtered recipes’ nutrition + ingredient vectors
        combined_filtered = np.hstack([scaled_df[filtered_indices], ingredient_vectors_filtered])

        # Fit temporary KNN for filtered data
        temp_knn = NearestNeighbors(n_neighbors=5)
        temp_knn.fit(combined_filtered)

        # Get recommendations
        distances, indices = temp_knn.kneighbors(input_vector)

        recommended_recipes = filtered_df.iloc[indices[0]]
        recipes = recommended_recipes.to_dict('records')

        return render_template('index.html', recipes=recipes, warning=ingredient_warning)

    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
