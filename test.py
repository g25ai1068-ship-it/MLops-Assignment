import joblib
from sklearn.datasets import fetch_olivetti_faces

# Load model
model = joblib.load("savedmodel.pth")

# Load SAME dataset
data = fetch_olivetti_faces()
X = data.data

# Take one sample
sample = X[0].reshape(1, -1)

# Prediction
prediction = model.predict(sample)

print("Prediction:", prediction)