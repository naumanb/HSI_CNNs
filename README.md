# Comparison of CNN Architectures for Brain Cancer Hyperspectral Image Classification

This project aims to compare various Convolutional Neural Network (CNN) architectures for classifying brain cancer in Hyperspectral Images (HSI). The implemented architectures include 2D CNN, 3D CNN, U-Net, and ResNet50. The models are trained and evaluated using the leave-one-out cross-validation method on a dataset of hyperspectral brain cancer images.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- TensorFlow 2.6 or higher
- Keras 2.6 or higher
- Scikit-learn 0.24 or higher
- Numpy 1.19 or higher
- Matplotlib 3.4 or higher

### Installation

1. Clone the repository:
```
git clone https://github.com/naumanb/HSI_CNNs.git
cd brain-cancer-hsi-classification
```

2. Install the required dependencies using pip:
```
pip install -r requirements.txt
```

## Usage

1. Place your hyperspectral image data in the `data` folder. The files should be in `.mat` format.

2. Execute the `main.py` script to train and evaluate the CNN architectures on the dataset:

```python
python main.py
```

The script will preprocess the hyperspectral image data, split it using leave-one-out cross-validation, and train each architecture on the dataset. The models' performance metrics will be displayed in the terminal, and the classification reports will be saved in the `results` folder.

## Results

The performance metrics for each architecture, such as precision, recall, and F1-score, will be saved in a text file in the `results` folder. You can compare these metrics to analyze the performance of each architecture for the given task.

## Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your proposed changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.


