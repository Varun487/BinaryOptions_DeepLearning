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

"API_KEY = <Enter your api key here>" > secret_key.py

python3 collection.py

```

# Project members
###### All members are from Semester 6 Pes University EC Campus
1. Varun Seshu - PES2201800074
2. Hritik Shanbhag - PES2201800082
3. Shashwath S Kumar - PES2201800623
