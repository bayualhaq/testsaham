# import
import streamlit as st
import yfinance as yf
import cufflinks as cf

# import pandas as pd
# import numpy as np

# Menampilkan teks header pada slidebar
st.sidebar.header("Analisa Pasar Saham \n Masukkan Data Saham")


# Membuat fungsi untuk mengambil informasi dari symbol saham
def get_ticker(ticker):
    company = yf.Ticker(ticker)
    return company


# Membuat fungsi untuk mengambil informasi period dan interval
def get_history(period, interval):
    df = ticker_data.history(period=period, interval=interval)
    if len(df) == 0:
        st.write('Data saham tidak ditemukan, silahkan atur kembali sampai data tersedia')
    else:
        df.index = df.index.strftime("%d-%m-%Y %H:%M")
        return df


# Input Data
ticker_symbol = st.sidebar.text_input("Symbol Saham", "ANTM.JK")  # Input Symbol Saham, default ANTM.JK

ticker_data = get_ticker(ticker_symbol)  # Untuk mengambil informasi dari symbol saham
period = st.sidebar.selectbox("Period",
                              ['1d', '5d', '1mo', '3mo', '6mo', '1y', '2y', '5y', '10y', 'ytd', 'max'])  # Input Periode
interval = st.sidebar.selectbox("Interval",
                                ['1m', '2m', '5m', '15m', '30m', '60m', '90m', '1h', '1d', '5d', '1wk', '1mo',
                                 '3mo'])  # Input Periode

# Informasi saham
# Menampilkan nama lengkap saham
string_name = ticker_data.info['longName']
st.markdown("<h1 style='text-align: center; color: white;'>%s</h1>" % string_name, unsafe_allow_html=True)

# Menampilkan logo saham
string_logo = '<center><img src=%s ></center></br>' % ticker_data.info['logo_url']
st.markdown(string_logo, unsafe_allow_html=True)

# Menampilkan informasi ringkas dari saham
string_summary = ticker_data.info['longBusinessSummary']
st.info(string_summary)

# Data saham
# Menampikan teks Header
st.header('**Data Saham**')

# Memasukkan input data ke Fungsi get_history
ticker_df = get_history(period, interval)
st.write(ticker_df)

# Menampilkan Candlestick
# Bollinger bands
st.header('**Bollinger Bands**')
qf = cf.QuantFig(ticker_df, title='First Quant Figure', legend='top', name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)

st.header('**Smooth Moving Average**')
qf = cf.QuantFig(ticker_df, title='Smooth Moving Average', legend='top', name='GS')
qf.add_sma(5)
qf.add_sma(10)
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)

# add_bollinger_bands() - It adds Bollinger Bands (BOLL) study to the figure.
# add_volume() - It adds volume bar charts to the figure.
# add_sma() - It adds Simple Moving Average (SMA) study to the figure.
# add_rsi() - It adds Relative Strength Indicator (RSI) study to the figure.
# add_adx() - It adds Average Directional Index (ADX) study to the figure.
# add_cci() - It adds Commodity Channel Indicator study to the figure.
# add_dmi() - It adds Directional Movement Index (DMI) study to the figure.
# add_ema() - It adds Exponential Moving Average (EMA) to the figure.
# add_atr() - It adds Average True Range (ATR) study to the figure.
# add_macd() - It adds Moving Average Convergence Divergence (MACD) to the figure.
# add_ptps() - It adds Parabolic SAR (PTPS) study to the figure.
# add_resistance() - It adds resistance line to the figure.
# add_trendline() - It adds trend line to the figure.
# add_support() - It adds support line to the figure.
