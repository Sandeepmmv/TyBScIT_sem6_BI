# Import required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Load dataset (Replace 'data.csv' with actual dataset file)
df = pd.read_csv('data.csv')

# Display first few rows
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Fill or drop missing values (modify as needed)
df = df.dropna()

# Encode categorical variables if necessary
# df['Category'] = df['Category'].map({'Yes': 1, 'No': 0})  # Example

# Define independent (X) and dependent (y) variables
X = df.iloc[:, :-1]  # Features (all columns except last)
y = df.iloc[:, -1]   # Target variable (last column)

# Split data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Standardize the data (important for Logistic Regression)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Initialize and train the Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Get predictions
y_pred = model.predict(X_test)

# Model performance metrics
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Classification report
print("Classification Report:\n", classification_report(y_test, y_pred))

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
sns.heatmap(conf_matrix, annot=True, cmap="Blues", fmt="d")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()
