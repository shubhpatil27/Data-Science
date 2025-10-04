🧩 Basic Keras Operations (Before LSTM)

This project also introduces some fundamental Keras operations before moving into advanced time-series modeling. These include:
1)Importing Keras Layers and Models
2)Building a Simple Sequential Model
3)Compiling the Model
4)Key Concepts



📈 Google Stock Price Prediction using LSTM
This project demonstrates how to build and train a Long Short-Term Memory (LSTM) model using Keras/TensorFlow to predict Google stock prices based on historical data.
The notebook preprocesses stock market data, trains an LSTM model, evaluates prediction accuracy, and visualizes the results.

🚀 Project Overview

Dataset: ggl_stock_exg.csv containing 4431 rows and 7 columns (Date, Open, High, Low, Close, Adj Close, Volume).
Target Variable: Adjusted Closing Price (Adj Close).
Model: LSTM neural network with stacked layers.
Objective: Predict the stock price for the next day using the previous 60 days of data.

📂 Project Workflow

1)Data Preprocessing
Loaded Google stock dataset using Pandas.
Selected Adj Close as target column.
Normalized data using MinMaxScaler.
Split into training (80%) and testing (20%) sets.
Created sequences of past 60 days → next day prediction.

2)Model Architecture
model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mean_squared_error')

3)Training
Batch size: 32
Epochs: 10

4)Evaluation
Predictions compared against actual values.
Root Mean Squared Error (RMSE) used as metric.
Multiple visualization methods:
i)Line plot (Train vs Actual vs Predicted).
ii))Scatter plot (Actual vs Predicted).
iii)Interactive Plotly chart.

5)Next Day Forecast
Predicts the stock price for the next trading day using the most recent 60 days of data.

📊 Results
The model learns stock price patterns reasonably well.
Predictions follow the actual price trend closely, but some deviations occur (as expected with stock data).
Achieved a low RMSE, showing good performance for a baseline LSTM.
Achieved a low RMSE, showing good performance for a baseline LSTM.

🔧 Requirements
Python 3.x
TensorFlow / Keras
Pandas, NumPy
Scikit-learn
Matplotlib, Plotly


▶️ How to Run
Clone the repository:
#bash
git clone https://github.com/yourusername/stock-price-prediction.git
cd stock-price-prediction

Place the dataset ggl_stock_exg.csv in the project folder.
Open the notebook:
jupyter notebook Keras&LSTM.ipynb
Run all cells to train the model and visualize predictions.


📌 Key Findings

LSTM networks are effective for time-series forecasting like stock prices.
Using 60-day windows improves the model’s ability to capture temporal dependencies.
Visualizations help clearly compare actual vs predicted values.

📜 Future Improvements

Hyperparameter tuning (epochs, batch size, LSTM units).
Adding more features (Open, High, Low, Volume).
Experiment with GRU or Transformer-based models.
Deploy as a web app for real-time predictions.

🙌 Acknowledgments
Data sourced from Google stock historical data.
Built using TensorFlow/Keras.






