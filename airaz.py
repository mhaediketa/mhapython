# Mu fara AI
import numpy as np
import sklearn.preprocessing
from sklearn import preprocessing

mha_data = np.array([[2.1, -1.9, 5.5], [-1.5, 2.4, 3.5], [0.5, -7.9, 5.6], [5.9, 2.3, -5.8]])
data_binarized = preprocessing.Binarizer(threshold=0.5).transform(mha_data)
print("\nBinarized data:\n", data_binarized)
print("Mean = ", mha_data.mean(axis=0))
print("Std deviation = ", mha_data.std(axis=0))

data_scaled = preprocessing.scale(mha_data)
print("Mean = ", data_scaled.mean(axis=0))
print("Std deviation = ", data_scaled.std(axis=0))

data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0, 1))
data_scaled_minmax = data_scaler_minmax.fit_transform(mha_data)
print("\nMin max scaled data:\n", data_scaled_minmax)
# Normalization
data_normalized = preprocessing.normalize(mha_data, norm='l1')
print("\nL1 normalized data:\n", data_normalized)
# L2 Normalized data
data_normalized_l2 = preprocessing.normalize(mha_data, norm='l2')
print("\nL2 normalized data:\n", data_normalized_l2)

# Labeling Data
# Sample input labels
mha_labels = ['red', 'black', 'red', 'green', 'black', 'yellow', 'white']
# Label encoder
encoder = preprocessing.LabelEncoder()
encoder.fit(mha_labels)

# encoding a set of labels
test_labels = ['green','red','black']
encoded_values = encoder.transform(test_labels)
print("\nLabels =", test_labels)

print("Encoded values =", list(encoded_values))

# decoding a set of values
encoded_values = [3, 0, 4, 1]
decoded_list = encoder.inverse_transform(encoded_values)
print("\nEncoded values =", encoded_values)

print("\nDecoded labels =", list(decoded_list))

# Classification
import sklearn
import sklearn.datasets
from sklearn.datasets import load_breast_cancer
mhadata = load_breast_cancer()
label_names = mhadata['target_names']
labels = mhadata['target']
feature_names = mhadata['feature_names']
features = mhadata['data']

print(label_names)
print(label_names[0])
print(feature_names)