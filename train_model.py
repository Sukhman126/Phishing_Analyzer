import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. Load the dataset
try:
    print("Loading dataset...")
    data = pd.read_csv('Phishing_data.csv')
    
    # 2. Separate features (X) and the answer key (y)
    # Using the 'CLASS_LABEL' column we found earlier
    X = data.drop('CLASS_LABEL', axis=1) 
    y = data['CLASS_LABEL']

    # 3. Split into Training (80%) and Testing (20%)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 4. Train the Random Forest Model
    print("Training the AI model... this might take a few seconds.")
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)

    # 5. Save the "Brain"
    joblib.dump(model, 'phishing_model.pkl')
    
    # 6. Show the result
    accuracy = model.score(X_test, y_test)
    print("--- Training Complete! ---")
    print(f"Accuracy Score: {accuracy * 100:.2f}%")
    print("The file 'phishing_model.pkl' has been created.")

except Exception as e:
    print(f"An error occurred: {e}")