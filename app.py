import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the dataset
@st.cache_data
def load_data():
    try:
        # Load data from the uploaded file
        data = pd.read_csv("data.csv")
        
        # Handle missing values for critical columns
        data['title'] = data['title'].fillna('Unknown')
        data['country'] = data['country'].fillna('Unknown')
        data['is_hourly'] = data['is_hourly'].fillna(False)
        
        # Fill missing values in salary columns (with a default value, like 0 or an appropriate fill)
        data['hourly_low'] = data['hourly_low'].fillna(0)
        data['hourly_high'] = data['hourly_high'].fillna(0)
        data['budget'] = data['budget'].fillna(0)
        
        # Create a combined column for TF-IDF model
        data['combined'] = data['title'] + ' ' + data['country'] + ' ' + data['is_hourly'].astype(str)
        
        return data
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()  # Return an empty dataframe if loading fails

# Load or train the TF-IDF model
def get_or_update_tfidf_model(data, update_model=False):
    if update_model or not st.session_state.get("model_loaded", False):
        try:
            # Train a new TF-IDF model
            vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
            job_vectors = vectorizer.fit_transform(data['combined'])
            
            # Save the updated model
            with open("model.pkl", "wb") as file:
                pickle.dump((vectorizer, job_vectors), file)
            
            # Mark the model as loaded in session
            st.session_state["model_loaded"] = True
            return vectorizer, job_vectors
        except Exception as e:
            st.error(f"Error training TF-IDF model: {e}")
            return None, None
    else:
        try:
            # Load the existing TF-IDF model
            with open("model.pkl", "rb") as file:
                vectorizer, job_vectors = pickle.load(file)
            return vectorizer, job_vectors
        except Exception as e:
            st.error(f"Error loading TF-IDF model: {e}")
            return None, None

# Streamlit UI
# Add a banner image with updated parameter
st.image("banner.jpg", use_container_width=True)  # Updated to use_container_width

st.title("Personalized Job Recommendation Engine")
st.sidebar.header("Input Your Preferences")

# Load data
data = load_data()

# Ensure the dataset is valid
if data.empty:
    st.write("No data available due to an error in loading the dataset.")
    st.stop()  # Stop execution if the data is invalid

# TF-IDF model with option to update
update_model = st.sidebar.checkbox("Update Model with Current Data", value=False)
vectorizer, job_vectors = get_or_update_tfidf_model(data, update_model=update_model)

# Ensure the model is loaded
if vectorizer is None or job_vectors is None:
    st.write("Unable to load or train TF-IDF model. Please check the error messages above.")
    st.stop()  # Stop execution if the model is not loaded properly

# User inputs
skills = st.sidebar.text_area("Enter your skills (comma-separated):", "Python, Data Analysis")
location = st.sidebar.text_input("Preferred Location:", "United States")

# Salary-related inputs (for filtering)
min_hourly_rate = st.sidebar.number_input("Minimum Hourly Rate:", min_value=0, step=1)
max_hourly_rate = st.sidebar.number_input("Maximum Hourly Rate:", min_value=0, step=1)
min_budget = st.sidebar.number_input("Minimum Budget:", min_value=0, step=1000)
max_budget = st.sidebar.number_input("Maximum Budget:", min_value=0, step=1000)

# Log the user inputs for debugging
st.write("User inputs:")
st.write(f"Skills: {skills}, Location: {location}")
st.write(f"Min Hourly Rate: {min_hourly_rate}, Max Hourly Rate: {max_hourly_rate}")
st.write(f"Min Budget: {min_budget}, Max Budget: {max_budget}")

# Combine user input for recommendation
user_input = skills + " " + location + " True"  # Assuming hourly jobs preferred
user_vector = vectorizer.transform([user_input])

# Find similar jobs
similarities = cosine_similarity(user_vector, job_vectors).flatten()
data['similarity'] = similarities

# Display the distribution of the salary columns (for debugging)
st.write("Salary Data Distribution (For Debugging):")
st.write(f"Hourly Low: {data['hourly_low'].describe()}")
st.write(f"Hourly High: {data['hourly_high'].describe()}")
st.write(f"Budget: {data['budget'].describe()}")

# Filter based on the user-defined salary range
filtered_data = data[
    (data['hourly_low'] >= min_hourly_rate) & 
    (data['hourly_high'] <= max_hourly_rate) & 
    (data['budget'] >= min_budget) & 
    (data['budget'] <= max_budget)
].sort_values(by='similarity', ascending=False)

# Display recommendations
st.subheader("Recommended Jobs for You")
if not filtered_data.empty:
    st.write(filtered_data[['title', 'country', 'hourly_low', 'hourly_high', 'budget', 'similarity']].head(10))
else:
    st.write("No matching jobs found based on your preferences. Try relaxing the filters.")

# Save user preferences (optional)
save_preferences = st.sidebar.button("Save Preferences")
if save_preferences:
    st.write("Preferences saved successfully!")

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("Developed by Minal Devikar")
