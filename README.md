# Binary Options Predictions - A Deep Learning Approach

## What is the project ?

A ```Neural Network``` for the classification of ```Binary options``` as a call or put option within a given timeframe.

## What are binary options ?

* A binary option is a financial instrument where traders bet on a binary outcome - whether the value of a stock/commodity/instrument rises above a set ```strike price``` within the expiry time of the option.

* At the time of expiry, the price of the underlying asset must be on the correct side of the strike price (above or below based on the trade taken) for the trader to make a profit.

* The risk in the trade is always the amount bet on the binary option, while the profit is always a fixed amount.

## What does our model do ?

* The deep learning model can predict whether the closing price of a stock, commodity or other financial instrument would be above or below a particular ```strike price``` in a given time period.

* The model classifies whether the closing price would be above/below the strike price before the expiry of our time period allowing us to purchase the appropriate binary option, thus beating the market and turning a profit.

## Baseline to outperform

* Investment in stock for the same period of time we are conducting binary options trading (long and short term)

## Assumptions

* A 50% return in case of a successful trade
* A 100% loss in case of a unsuccessful trade

* Profit calculations based on assumptions -

| % of successful trades | Return % on initial investment|  
| ---   | --- |  
|  70   | 5  |  
|  80   | 20 |  
|  90   | 35 |  
|  100  | 50 |  

## Jupyter notebook

* We provide a jupyter notebook to interact with the model and perform back tests.

* We also provide notebooks to create, test, train and tweak the model.

## Webapp

* We also provide a website to interact with the model and perform back tests on custom data.

* Click here to go to the website.

# To replicate this project on your computer

1. Make a virtual environment and activate it.
2. Run these commands to initialize the project: 
```
git clone git@github.com:Varun487/BinaryOptions_DeepLearning.git

cd BinaryOptions_DeepLearning

pip3 install -r requirements.txt
```
2. We are sourcing data from Alpha Vantage. You can get your ```secret Api key``` [here](https://www.alphavantage.co/support/#api-key).
3. After getting your ```Api key```, make a file in the BinaryOptions_DeepLearning folder called ```secret_key.py```.
4. Add the line ```API_KEY = <Enter your api key here>``` in ```secret_key.py```
5. Finally, to download the dataset, run:
```
python3 collection.py
```

# Project members
###### All members are from Semester 6 Pes University EC Campus
1. Varun Seshu - PES2201800074
2. Hritik Shanbhag - PES2201800082
3. Shashwath S Kumar - PES2201800623

# TODO
1. Preprocessing
    - Assume 50% return per trade
        - Win 70% of trades -> 5% ROI -> Least needed to be profitable
        - Win 80% of trades -> 20% ROI
        - Win 90% of trades -> 35% ROI
        - Win 100% of trades -> 50% ROI
2. Models
    - Input
        - Open
        - High
        - Low
        - Close
        - Volume
        - Time stamp
        - Technical Indicators to compute (for different time periods)
            - SMA
            - EMA
            - MACD
            - ROC
            - Momentum
            - RSI
            - BB
            - CCI
    - Build multiple models 
        - Classification
            - Classes for prediction
                - Up and Down + Threshold for no action after predictions
                - Up, Down and No_Action
        - Regression
            - Predict prices and apply rules to decide when to skip trades
        - Choose either the best model, or an ensemble which gives the highest accuracy
        - If no model provides an accuracy above 70%, show that binary options trading is not worth the investment
3. Back testing report
    - Create a back testing report showing performance of model, taking into account
        - risk
        - account size
    