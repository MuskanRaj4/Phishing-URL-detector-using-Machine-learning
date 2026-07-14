import pandas as pd

# Dataset load
data = pd.read_csv("phishing_url_dataset.csv")

# Features aur Target alag karein
X = data.drop("target", axis=1)
y = data["target"]

# Train Test Split
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Random Forest Model
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Model Train
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Accuracy
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Model Save
import joblib
joblib.dump(model, "phishing_model.pkl")

print("Model saved successfully!")
