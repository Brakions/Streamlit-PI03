import datetime
from unicodedata import decimal
import requests
import pandas as pd
import matplotlib.pyplot as plt

api_url = "https://ftx.com/api"
api= "/markets"
url = api_url + api

#Convertimos a df markets
markets= requests.get(url).json()
data = markets["result"]
df=pd.DataFrame(data)

#Creamos un dataframe con el registrol de nuestras divisasy nombres de crypomonedas

df["name"]=df["name"].str.replace("-",",")
df["name"]=df["name"].str.replace("/",",")
new2 =df["name"].str.split(",",n=1,expand=True)
df["Nombre"]= new2[0]
df["Divisa"]= new2[1]
df.drop(columns=["name"],inplace=True)

#Precio de Bitcoin a USD
mask1 =df["Nombre"] =="BTC" 
onlybtc=df[mask1]
mask2 =onlybtc["Divisa"] =="USD"
BTCUSD=onlybtc[mask2]
BA=BTCUSD["price"].values

#Volumen de Bitcoin a USD
mask1 =df["Nombre"] =="BTC" 
onlybtc=df[mask1]
mask2 =onlybtc["Divisa"] =="USD"
BTCUSD=onlybtc[mask2]
volumeA=BTCUSD["volumeUsd24h"].values

#Precio de Bitcoin a EUR
mask1 =df["Nombre"] =="BTC" 
onlybtc=df[mask1]
mask2 =onlybtc["Divisa"] =="EUR"
BTCEUR=onlybtc[mask2]
BB=BTCEUR["price"].values

#Precio de Bitcoin a YEN
mask1 =df["Nombre"] =="BTC" 
onlybtc=df[mask1]
mask2 =onlybtc["Divisa"] =="JPY"
BTCYEN=onlybtc[mask2]
BC=BTCYEN["price"].values

#Precio de Bitcoin a Dolar Australiano
mask1 =df["Nombre"] =="BTC" 
onlybtc=df[mask1]
mask2 =onlybtc["Divisa"] =="AUD"
BTCAUD=onlybtc[mask2]
BD=BTCAUD["price"].values

#Precio de Bitcoin a Perpetual Protocol
mask1 =df["Nombre"] =="BTC" 
onlybtc=df[mask1]
mask2 =onlybtc["Divisa"] =="PERP"
BTCPERP=onlybtc[mask2]
BE=BTCPERP["price"].values

#Precio de Bitcoin a Brazilian Digital Token
mask1 =df["Nombre"] =="BTC" 
onlybtc=df[mask1]
mask2 =onlybtc["Divisa"] =="BRZ"
BTCBRZ=onlybtc[mask2]
BF=BTCBRZ["price"].values

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Precio de Etherium a USD
mask1e =df["Nombre"] =="ETH" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="USD"
ETHUSD=onlyeth[mask2e]
EA=ETHUSD["price"].values

#Volumen de Etherium a USD
mask1 =df["Nombre"] =="ETH" 
onlybtc=df[mask1]
mask2 =onlybtc["Divisa"] =="USD"
BTCUSD=onlybtc[mask2]
volumeB=BTCUSD["volumeUsd24h"].values

#Precio de Etherium a EUR
mask1e =df["Nombre"] =="ETH" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="EUR"
ETHUSD=onlyeth[mask2e]
EB=ETHUSD["price"].values

#Precio de Etherium a YEN
mask1e =df["Nombre"] =="ETH" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="JPY"
ETHUSD=onlyeth[mask2e]
EC=ETHUSD["price"].values

#Precio de Etherium a Dolar Australiano
mask1e =df["Nombre"] =="ETH" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="AUD"
ETHUSD=onlyeth[mask2e]
ED=ETHUSD["price"].values

#Precio de Etherium a Perpetual Protocol
mask1e =df["Nombre"] =="ETH" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="PERP"
ETHUSD=onlyeth[mask2e]
EE=ETHUSD["price"].values

#Precio de Etherium a Brazilian Digital Token
mask1e =df["Nombre"] =="ETH" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="BRZ"
ETHUSD=onlyeth[mask2e]
EF=ETHUSD["price"].values

#Precio de Etherium a Bitcoin
mask1e =df["Nombre"] =="ETH" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="BTC"
ETHUSD=onlyeth[mask2e]
EG=ETHUSD["price"].values

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Precio de Binance Coin a USD
mask1e =df["Nombre"] =="BNB" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="USD"
ETHUSD=onlyeth[mask2e]
bA=ETHUSD["price"].values

#Volumen de Binance Coin a USD
mask1 =df["Nombre"] =="BNB" 
onlybtc=df[mask1]
mask2 =onlybtc["Divisa"] =="USD"
BTCUSD=onlybtc[mask2]
volumeC=BTCUSD["volumeUsd24h"].values

#Precio de Binance Coin a EUR
mask1e =df["Nombre"] =="BNB" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="EUR"
ETHUSD=onlyeth[mask2e]
bB=ETHUSD["price"].values

#Precio de Binance Coin a YEN
mask1e =df["Nombre"] =="BNB" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="JPY"
ETHUSD=onlyeth[mask2e]
bC=ETHUSD["price"].values

#Precio de Binance Coin a Dolar Australiano
mask1e =df["Nombre"] =="BNB" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="AUD"
ETHUSD=onlyeth[mask2e]
bD=ETHUSD["price"].values

#Precio de Binance Coin a Perpetual Protocol
mask1e =df["Nombre"] =="BNB" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="PERP"
ETHUSD=onlyeth[mask2e]
bE=ETHUSD["price"].values

#Precio de Binance Coin a Brazilian Digital Token
mask1e =df["Nombre"] =="BNB" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="BRZ"
ETHUSD=onlyeth[mask2e]
bF=ETHUSD["price"].values

#Precio de Binance Coin a Bitcoin
mask1e =df["Nombre"] =="BNB" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="BTC"
ETHUSD=onlyeth[mask2e]
bG=ETHUSD["price"].values

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Precio de DOGECOIN a USD
mask1e =df["Nombre"] =="DOGE" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="USD"
ETHUSD=onlyeth[mask2e]
DA=ETHUSD["price"].values

#Volumen de DOGECOIN a USD
mask1 =df["Nombre"] =="DOGE" 
onlybtc=df[mask1]
mask2 =onlybtc["Divisa"] =="USD"
BTCUSD=onlybtc[mask2]
volumeD=BTCUSD["volumeUsd24h"].values

#Precio de DOGECOIN a EUR
mask1e =df["Nombre"] =="DOGE" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="EUR"
ETHUSD=onlyeth[mask2e]
DB=ETHUSD["price"].values

#Precio de DOGECOIN a YEN
mask1e =df["Nombre"] =="DOGE" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="JPY"
ETHUSD=onlyeth[mask2e]
DC=ETHUSD["price"].values

#Precio de DOGECOIN a Dolar Australiano
mask1e =df["Nombre"] =="DOGE" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="AUD"
ETHUSD=onlyeth[mask2e]
DD=ETHUSD["price"].values

#Precio de DOGECOIN a Perpetual Protocol
mask1e =df["Nombre"] =="DOGE" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="PERP"
ETHUSD=onlyeth[mask2e]
DE=ETHUSD["price"].values

#Precio de DOGECOIN a Brazilian Digital Token
mask1e =df["Nombre"] =="DOGE" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="BRZ"
ETHUSD=onlyeth[mask2e]
DF=ETHUSD["price"].values

#Precio de DOGECOIN a Bitcoin
mask1e =df["Nombre"] =="DOGE" 
onlyeth=df[mask1e]
mask2e =onlyeth["Divisa"] =="BTC"
ETHUSD=onlyeth[mask2e]
DG=ETHUSD["price"].values

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Dataframe de BTC  USD
import time
import requests
from datetime import datetime
import json
import plotly.graph_objects as go

endpoint_url = "https://ftx.com/api/markets"
base_currency= "BTC"
quote_currency = "USD"


request_url=f"{endpoint_url}/{base_currency}/{quote_currency}"
all_markets=requests.get(endpoint_url).json()

dh=pd.DataFrame(all_markets["result"])
dh.set_index("name",inplace=True)


#1 dia = 60 *60 *24 segundos



daily = str (60*60*24)
#Fecha inicial = 2022-01-01
start_date = datetime(2022,1,1).timestamp()
#Tomamos el historial del mercado en JSON
historical = requests.get(
    f"{request_url}/candles?resolution={daily}&start_time={start_date}"

).json()

#Convertimos de JSON a Pandas DataFrame
dh=pd.DataFrame(historical["result"])

#Convertimos de time a date
dh["date"] = pd.to_datetime(
    dh["time"]/1000,unit="s",origin="unix"

)
#Removemos columnas innecesarias 
dh.drop(["startTime","time"],axis=1, inplace=True)
#Volumen total de BTC en las ultimas 24hrs
volbtc=(dh["volume"].iloc[-1])
#cambio de % con respecto al dia anterior BTC 
Vbtc=round(((dh["close"].iloc[-1]-dh["open"].iloc[-1])*100)/dh["open"].iloc[-1],2)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Creamos el grafico
def fbtc():
   

        fig=go.Figure()

        #Configuramos el diseño
        fig.update_layout(
            title={
                "text":f"{base_currency}/{quote_currency}",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Fecha",
            yaxis_title = "Precio",
            xaxis_rangeslider_visible=False
        )

        #Adgregamos un grafico de velas
        fig.add_trace(
            go.Candlestick(
                x=dh["date"],
                open=dh["open"],
                high=dh["high"],
                low=dh["low"],
                close=dh["close"]
            )
        )
        return fig
        fig.show()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Dataframe de ETH  USD
endpoint_url = "https://ftx.com/api/markets"
base_currencye = "ETH"
quote_currencye = "USD"


request_url=f"{endpoint_url}/{base_currencye}/{quote_currencye}"
all_markets=requests.get(endpoint_url).json()

dhe=pd.DataFrame(all_markets["result"])
dhe.set_index("name",inplace=True)

#1 dia = 60 *60 *24 segundos



daily = str (60*60*24)
#Fecha inicial = 2022-01-01
start_datee = datetime(2021,12,31).timestamp()
#Tomamos el historial del mercado en JSON
historicale = requests.get(
    f"{request_url}/candles?resolution={daily}&start_time={start_date}"

).json()

#Convertimos de JSON a Pandas DataFrame
dhe=pd.DataFrame(historicale["result"])

#Convertimos de time a date
dhe["date"] = pd.to_datetime(
    dhe["time"]/1000,unit="s",origin="unix"

)
#Removemos columnas innecesarias 
dhe.drop(["startTime","time"],axis=1, inplace=True)
#Volumen total de BTC en las ultimas 24hrs
voleth=(dhe["volume"].iloc[-1])
#cambio de % con respecto al dia anterior ETH 
Veth=round(((dhe["close"].iloc[-1]-dhe["open"].iloc[-1])*100)/dhe["open"].iloc[-1],2)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Creamos el grafico
def feth():
        fige=go.Figure()
        #Configuramos el diseño
        fige.update_layout(
            title={
                "text":f"{base_currencye}/{quote_currencye}",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Fecha",
            yaxis_title = "Precio",
            xaxis_rangeslider_visible=False
        )

        #Adgregamos un grafico de velas
        fige.add_trace(
            go.Candlestick(
                x=dhe["date"],
                open=dhe["open"],
                high=dhe["high"],
                low=dhe["low"],
                close=dhe["close"]
            )
        )
        return fige
        fige.show()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Dataframe de DOGE  USD
endpoint_url = "https://ftx.com/api/markets"
base_currencyd = "DOGE"
quote_currencyd = "USD"


request_url=f"{endpoint_url}/{base_currencyd}/{quote_currencyd}"
all_markets=requests.get(endpoint_url).json()

dhd=pd.DataFrame(all_markets["result"])
dhd.set_index("name",inplace=True)

#1 dia = 60 *60 *24 segundos



daily = str (60*60*24)
#Fecha inicial = 2022-01-01
start_datee = datetime(2021,12,31).timestamp()
#Tomamos el historial del mercado en JSON
historicald = requests.get(
    f"{request_url}/candles?resolution={daily}&start_time={start_date}"

).json()

#Convertimos de JSON a Pandas DataFrame
dhd=pd.DataFrame(historicald["result"])

#Convertimos de time a date
dhd["date"] = pd.to_datetime(
    dhd["time"]/1000,unit="s",origin="unix"

)
#Removemos columnas innecesarias 
dhd.drop(["startTime","time"],axis=1, inplace=True)
#Volumen total de BTC en las ultimas 24hrs
voldoge=(dhd["volume"].iloc[-1])
#cambio de % con respecto al dia anterior DOGE 
Vdoge=round(((dhd["close"].iloc[-1]-dhd["open"].iloc[-1])*100)/dhd["open"].iloc[-1],2)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Creamos el grafico
def fdoge():
        figd=go.Figure()
        #Configuramos el diseño
        figd.update_layout(
            title={
                "text":f"{base_currencyd}/{quote_currencyd}",
                "x" : 0.5,
                "xanchor":"center"
            },
            xaxis_title ="Fecha",
            yaxis_title = "Precio",
            xaxis_rangeslider_visible=False
        )

        #Adgregamos un grafico de velas
        figd.add_trace(
            go.Candlestick(
                x=dhd["date"],
                open=dhd["open"],
                high=dhd["high"],
                low=dhd["low"],
                close=dhd["close"]
            )
        )
        return figd
        figd.show()

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#Dataframe de BNB  USD
endpoint_url = "https://ftx.com/api/markets"
base_currencybn = "BNB"
quote_currencybn = "USD"


request_url=f"{endpoint_url}/{base_currencybn}/{quote_currencybn}"
all_markets=requests.get(endpoint_url).json()

dhbn=pd.DataFrame(all_markets["result"])
dhbn.set_index("name",inplace=True)

#1 dia = 60 *60 *24 segundos



daily = str (60*60*24)
#Fecha inicial = 2022-01-01
start_datebn = datetime(2021,12,31).timestamp()
#Tomamos el historial del mercado en JSON
historicalbn = requests.get(
    f"{request_url}/candles?resolution={daily}&start_time={start_date}"

).json()

#Convertimos de JSON a Pandas DataFrame
dhbn=pd.DataFrame(historicalbn["result"])

#Convertimos de time a date
dhbn["date"] = pd.to_datetime(
    dhbn["time"]/1000,unit="s",origin="unix"

)
#Removemos columnas innecesarias 
dhbn.drop(["startTime","time"],axis=1, inplace=True)
#Volumen total de BTC en las ultimas 24hrs
volbnb=(dhbn["volume"].iloc[-1])
#cambio de % con respecto al dia anterior BNB 
Vbnb=round(((dhbn["close"].iloc[-1]-dhbn["open"].iloc[-1])*100)/dhbn["open"].iloc[-1],2)
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#Creamos el grafico
def fbn():
    figbn=go.Figure()
    #Configuramos el diseño
    figbn.update_layout(
        title={
            "text":f"{base_currencybn}/{quote_currencybn}",
            "x" : 0.5,
            "xanchor":"center"
        },
        xaxis_title ="Fecha",
        yaxis_title = "Precio",
        xaxis_rangeslider_visible=False
    )

    #Adgregamos un grafico de velas
    figbn.add_trace(
        go.Candlestick(
            x=dhbn["date"],
            open=dhbn["open"],
            high=dhbn["high"],
            low=dhbn["low"],
            close=dhbn["close"]
        )
    )
    return figbn
    figbn.show()



