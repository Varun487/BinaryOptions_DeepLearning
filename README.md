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

* A 60% return in case of a successful trade
* A 100% loss in case of a unsuccessful trade

* Profit calculations based on assumptions -

| % of successful trades | Return % on initial investment|  
| ---   | --- |  
|  70   | 5  |  
|  80   | 20 |  
|  90   | 35 |  
|  100  | 50 |  

###### READ AS: Need to win at least 70% of trades to make 5% profit on initial investment

## Jupyter notebooks

* A jupyter notebook to interact with the model and perform back tests.

* Notebooks to create, test, train and tweak the model.

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
1. Collection of data ![DONE]
2. Preprocessing ![DONE]
	- Remove NaN values ![DONE]
	- Add company name ![DONE]
	- Put prices 1, 2, 3, 5, 10, 15, 30, 60 mins ahead columns ![DONE]
	- Put indicators values as columns ![DONE]
		- SMA ![DONE]
		- EMA ![DONE]
		- MACD ![DONE]
		- RSI ![DONE]
		- BB ![DONE]
3. Models ![DONE]
	- LSTMs `Varun` ![DONE]
	- Transformers `Shashwath` ![DONE]
4. Back testing ![DONE]
	- Load all models, calculate accuracy, precision and recall for all companies and datasets ![DONE]
	- Show best models with returns ![DONE]
	- Visualizations of datasets, indicators and predictions ![DONE]
	- Add tranformer predictions to backtesting `Shashwath` ![DONE]
5. Mock Session 1 ![INCOMPLETE]
6. Mock Session 2 ![INCOMPLETE]

[DONE]: https://img.shields.io/badge/DONE-brightgreen
[INCOMPLETE]: https://img.shields.io/badge/INCOMPLETE-red
[BUG]: https://img.shields.io/badge/BUG-red
[BUGFIXED]: https://img.shields.io/badge/BUG-FIXED-brightgreen
[FEATUREINCOMPLETE]: https://img.shields.io/badge/FEATURE-INCOMPLETE-red
[FEATURECOMPLETE]: https://img.shields.io/badge/FEATURE-COMPLETE-brightgreen
[MEETINGINCOMPLETE]: https://img.shields.io/badge/MEETING-INCOMPLETE-red
[DOCINCOMPLETE]: https://img.shields.io/badge/DOC-INCOMPLETE-red
[DOCCOMPLETE]: https://img.shields.io/badge/DOC-COMPLETE-brightgreen
