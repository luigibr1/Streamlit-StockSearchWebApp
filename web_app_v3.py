#import required libraries
import streamlit as st
import yfinance as yf
from datetime import datetime

#function calling local css sheet
def local_css(file_name):
    with open(file_name) as f:
        st.sidebar.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

#local css sheet
local_css("style.css")

#ticker search feature in sidebar
st.sidebar.subheader("""Stock Search Web App""")
selected_stock = st.sidebar.text_input("Enter a valid stock ticker...", "GOOG")
button_clicked = st.sidebar.button("GO")
if button_clicked == "GO":
    main()

#main function
def main():
    st.subheader("""Daily **closing price** for """ + selected_stock)
    #get data on searched ticker
    stock_data = yf.Ticker(selected_stock)
    #get historical data for searched ticker
    stock_df = stock_data.history(period='1d', start='2020-01-01', end=None)
    #print line chart with daily closing prices for searched ticker
    st.line_chart(stock_df.Close)

    st.subheader("""Last **closing price** for """ + selected_stock)
    #define variable today 
    today = datetime.today().strftime('%Y-%m-%d')
    #get current date data for searched ticker
    stock_lastprice = stock_data.history(period='1d', start=today, end=today)
    #get current date closing price for searched ticker
    last_price = (stock_lastprice.Close)
    #if market is closed on current date print that there is no data available
    if last_price.empty == True:
        st.write("No data available at the moment")
    else:
        st.write(last_price)
    
    #get daily volume for searched ticker
    st.subheader("""Daily **volume** for """ + selected_stock)
    st.line_chart(stock_df.Volume)

    #additional information feature in sidebar
    st.sidebar.subheader("""Display Additional Information""")
    #checkbox to display stock actions for the searched ticker
    actions = st.sidebar.checkbox("Stock Actions")
    if actions:
        st.subheader("""Stock **actions** for """ + selected_stock)
        display_action = (stock_data.actions)
        if display_action.empty == True:
            st.write("No data available at the moment")
        else:
            st.write(display_action)
    
    #checkbox to display quarterly financials for the searched ticker
    financials = st.sidebar.checkbox("Quarterly Financials")
    if financials:
        st.subheader("""**Quarterly financials** for """ + selected_stock)
        display_financials = (stock_data.quarterly_financials)
        if display_financials.empty == True:
            st.write("No data available at the moment")
        else:
            st.write(display_financials)

    #checkbox to display list of institutional shareholders for searched ticker
    major_shareholders = st.sidebar.checkbox("Institutional Shareholders")
    if major_shareholders:
        st.subheader("""**Institutional investors** for """ + selected_stock)
        display_shareholders = (stock_data.institutional_holders)
        if display_shareholders.empty == True:
            st.write("No data available at the moment")
        else:
            st.write(display_shareholders)

    #checkbox to display quarterly balance sheet for searched ticker
    balance_sheet = st.sidebar.checkbox("Quarterly Balance Sheet")
    if balance_sheet:
        st.subheader("""**Quarterly balance sheet** for """ + selected_stock)
        display_balancesheet = (stock_data.quarterly_balance_sheet)
        if display_balancesheet.empty == True:
            st.write("No data available at the moment")
        else:
            st.write(display_balancesheet)

    #checkbox to display quarterly cashflow for searched ticker
    cashflow = st.sidebar.checkbox("Quarterly Cashflow")
    if cashflow:
        st.subheader("""**Quarterly cashflow** for """ + selected_stock)
        display_cashflow = (stock_data.quarterly_cashflow)
        if display_cashflow.empty == True:
            st.write("No data available at the moment")
        else:
            st.write(display_cashflow)

    #checkbox to display quarterly earnings for searched ticker
    earnings = st.sidebar.checkbox("Quarterly Earnings")
    if earnings:
        st.subheader("""**Quarterly earnings** for """ + selected_stock)
        display_earnings = (stock_data.quarterly_earnings)
        if display_earnings.empty == True:
            st.write("No data available at the moment")
        else:
            st.write(display_earnings)

    #checkbox to display list of analysts recommendation for searched ticker
    analyst_recommendation = st.sidebar.checkbox("Analysts Recommendation")
    if analyst_recommendation:
        st.subheader("""**Analysts recommendation** for """ + selected_stock)
        display_analyst_rec = (stock_data.recommendations)
        if display_analyst_rec.empty == True:
            st.write("No data available at the moment")
        else:
            st.write(display_analyst_rec)

if __name__ == "__main__":
    main()
