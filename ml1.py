
# Uber Fare Price Prediction

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load Dataset
data = pd.read_csv("uber.csv")

# 2. Select Columns and Remove Missing Values
data = data[[
    "fare_amount", "pickup_longitude",
    "pickup_latitude", "dropoff_longitude",
    "dropoff_latitude", "passenger_count"
]].dropna()

# 3. Remove Invalid Data
data = data[
    (data["fare_amount"] > 0) &
    (data["fare_amount"] <= 100) &
    (data["passenger_count"].between(1, 6)) &
    (data["pickup_latitude"].between(40, 42)) &
    (data["dropoff_latitude"].between(40, 42)) &
    (data["pickup_longitude"].between(-75, -72)) &
    (data["dropoff_longitude"].between(-75, -72))
].copy()

# 4. Calculate Distance
def haversine(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = map(
        np.radians, [lat1, lon1, lat2, lon2]
    )

    a = (np.sin((lat2-lat1)/2)**2 +
         np.cos(lat1) * np.cos(lat2) *
         np.sin((lon2-lon1)/2)**2)

    return 6371 * 2 * np.arcsin(np.sqrt(a))

data["distance"] = haversine(
    data["pickup_latitude"], data["pickup_longitude"],
    data["dropoff_latitude"], data["dropoff_longitude"]
)

data = data[data["distance"].between(0.1, 50)].copy()

# 5. Identify and Remove Outliers
Q1 = data["fare_amount"].quantile(0.25)
Q3 = data["fare_amount"].quantile(0.75)
IQR = Q3 - Q1

data = data[
    data["fare_amount"].between(
        Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
    )
].copy()

# 6. Check Correlation
print("Correlation Matrix:")
print(data[["fare_amount", "distance",
            "passenger_count"]].corr())

sns.heatmap(
    data[["fare_amount", "distance",
          "passenger_count"]].corr(),
    annot=True, cmap="coolwarm"
)
plt.title("Correlation Heatmap")
plt.show()

# 7. Input and Output
X = data[["distance", "passenger_count"]]
y = data["fare_amount"]

# 8. Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 9. Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

# 10. Random Forest Regression
rf = RandomForestRegressor(
    n_estimators=100, random_state=42
)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

# 11. Evaluate Models
print("\nLinear Regression Results")
print("MAE:", mean_absolute_error(y_test, lr_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, lr_pred)))
print("R2 Score:", r2_score(y_test, lr_pred))

print("\nRandom Forest Results")
print("MAE:", mean_absolute_error(y_test, rf_pred))
print("RMSE:", np.sqrt(mean_squared_error(y_test, rf_pred)))
print("R2 Score:", r2_score(y_test, rf_pred))

# 12. Compare Models
print("\nModel Comparison")
print("Linear Regression R2:", r2_score(y_test, lr_pred))
print("Random Forest R2:", r2_score(y_test, rf_pred))

# 13. Predict New Uber Fare
print("\nEnter Ride Details")

p_lat = float(input("Pickup Latitude: "))
p_lon = float(input("Pickup Longitude: "))
d_lat = float(input("Drop Latitude: "))
d_lon = float(input("Drop Longitude: "))
passengers = int(input("Passenger Count: "))

if (40 <= p_lat <= 42 and 40 <= d_lat <= 42 and
    -75 <= p_lon <= -72 and -75 <= d_lon <= -72 and
    1 <= passengers <= 6):

    distance = haversine(p_lat, p_lon, d_lat, d_lon)

    ride = pd.DataFrame(
        [[distance, passengers]],
        columns=["distance", "passenger_count"]
    )

    fare = rf.predict(ride)[0]

    print("Distance:", round(float(distance), 2), "km")
    print("Predicted Uber Fare: $", round(max(0, fare), 2))

else:
    print("Invalid Input")