import numpy as np
from sklearn.model_selection import LeaveOneOut
from sklearn.preprocessing import LabelEncoder

def get_leave_one_out_splits(X, y):
    # Assuming X has a shape of (num_images, height, width, num_spectra)

    # Initialize the leave-one-out cross-validator
    loo = LeaveOneOut()

    # Split the data into training and testing sets using leave-one-out cross-validation
    splits = list(loo.split(X, y))

    return splits