# Streamlit - Stock Search Web App

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html) 
---

![Demo](assets/web_app_demo.gif)

## Introduction

This web app allows you to search for and retrieve information on any stock from Yahoo! Finance using its ticker and display a line chart of the closing prices, the last closing price, and the daily volume. The web app also allows you to view the following additional information for every stock searched:

* Stock Actions (i.e. dividends payments and stock splits)
* Quarterly Financials
* List of Institutional Shareholders
* Quarterly Balance Sheet
* Quarterly Cashflow
* Quarterly Earnings
* List of Analysts Recommendations (i.e. buy, sell, hold)

For each searched ticker, the web app will query the yfinance API, which will retrieve the related market data from Yahoo! Finance and save it into a dataframe that streamlit will use as input to display the data.


## Let’s get started

### The prerequisites

To run the web app, you will first need to install streamlit and yfinance. To do so, I recommend using a virtual python environment so as not to pollute your global python environment.

To install streamlit run:

~~~
pip install streamlit
~~~

To install yfinance run:

~~~
pip install yfinance
~~~

You will also need the datetime library which comes with the default python installation, hence no need to install it separately.

### The CSS Sheet

By using the style sheet, you can customize the background and text colour of the web app, the colour and size of the “GO” button, as well as the colour of the default text of the search box in the sidebar (i.e. “Enter a valid stock ticker…” — see line 16 of Part 1 of the code).


## Let’s run it

Open a terminal session, navigate to the folder where the files are stored, and run:

~~~
streamlit run web_app_v3.py
~~~

If all is proceeding well, you should see a terminal message saying that you can view your streamlit app in your browser. At this point, a new window of your default web browser will open and display your web app at the address **http://localhost:8501**.

Note that if you run the app on a Monday or the day after a public holiday, you might get this message as well:

~~~
- GOOG: No data found for this date range, symbol may be delisted
~~~

Nothing to worry about! The web app has queried yfinance to retrieve the closing price for the ticker “GOOG” when the market was closed, and hence it could not find any information. In this case, the app will conveniently display that **“No data is available at the moment”**.
