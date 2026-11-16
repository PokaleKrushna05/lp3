
# 1. Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 2. Load dataset
data = pd.read_csv("Churn_Modelling.csv")

# 3. Remove unnecessary columns
data = data.drop(
    ["RowNumber", "CustomerId", "Surname"], axis=1
)

# 4. Separate input and output
X = data.drop("Exited", axis=1)
y = data["Exited"]

# 5. Convert categorical data into numbers
X = pd.get_dummies(
    X, columns=["Geography", "Gender"], dtype=int
)

# 6. Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 7. Normalize the data
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 8. Create Neural Network model
model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    max_iter=500,
    early_stopping=True,
    random_state=42
)

# 9. Train the model
model.fit(X_train, y_train)

# 10. Predict results
predictions = model.predict(X_test)

# 11. Evaluate the model
print("Accuracy:", accuracy_score(y_test, predictions))

print("Confusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("Classification Report:")
print(classification_report(y_test, predictions, zero_division=0))

# 12. Predict one customer
result = model.predict(X_test[[0]])[0]

if result == 1:
    print("Customer will leave the bank")
else:
    print("Customer will stay in the bank")
