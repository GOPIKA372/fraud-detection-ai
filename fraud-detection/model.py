import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv("creditcard.csv")

print("Dataset Loaded Successfully")
print(data.head())

# Separate features and target
X = data.drop(columns='Class')
Y = data['Class']

# Split the dataset
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=2
)

# Create model
model = LogisticRegression(max_iter=1000)

# Train model
model.fit(X_train, Y_train)

# Predictions
train_pred = model.predict(X_train)
test_pred = model.predict(X_test)

# Accuracy
train_accuracy = accuracy_score(Y_train, train_pred)
test_accuracy = accuracy_score(Y_test, test_pred)

print("Training Accuracy:", train_accuracy)
print("Testing Accuracy:", test_accuracy)

# Save model
joblib.dump(model, "fraud_model.pkl")

print("Model saved successfully!")