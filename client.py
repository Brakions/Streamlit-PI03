import datetime
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

