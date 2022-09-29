from secrets import choice
from unicodedata import decimal
import streamlit as st
import requests
import pandas as pd
##Calculador
from client import df,fbtc,feth,fdoge,fbn,Vbtc,Veth,Vdoge,Vbnb,volbtc,volbnb,voldoge,voleth,volumeA,volumeB,volumeC,volumeD
from client import BA,BB,BC,BD,BE,BF,EA,EB,EC,ED,EE,EF,EG,bA,bB,bC,bD,bE,bF,bG,DA,DB,DC,DD,DE,DF,DG
from client import varianzabnb,varianzabtc,varianzadoge,varianzaeth,desviacionbtc,desviaciondoge,desviacioneth,desviacionbnbn
from client import rollh
##Calculador

#Grafico
#from client import fige,figd,figbn
#from datetime import datetime
#import json
import plotly.graph_objects as go

##Grafico
#MAINn

def main():
    menu = ["Home","Calculador"]
    choice = st.sidebar.selectbox("Menu",menu)

    st.title("Proyecto Individual III")



#CALCULADOR
    if choice== "Calculador":
        st.subheader("Calculador")

        # Nav Search Form
        with st.form(key="searchform"):
            nav1,nav2,nav3 = st.columns([3,2,1])
            criptos=["Bitcoin","Ethereum","Dogecoin","Binance Coin"]
            divisas=["USD","GBP","EUR","JPY","AUD","PERP","BRZ","BTC","ARS","CLP"]
            with nav1:
                search_term =st.selectbox("Select Cripto :",criptos)
                #BITCOIN
                def result():
                    if search_term =="Bitcoin" and moneda == "USD":
                        return f"{float(BA):,.2f}"
                    if search_term =="Bitcoin" and moneda == "GBP":
                        return f"{(float(BA))*0.93:,.2f}"
                    if search_term =="Bitcoin" and moneda == "EUR":
                        return f"{float(BB):,.2f}"
                    if search_term =="Bitcoin" and moneda == "JPY":
                        return f"{float(BC):,.2f}"
                    if search_term =="Bitcoin" and moneda == "AUD":
                        return f"{float(BD):,.2f}"
                    if search_term =="Bitcoin" and moneda == "PERP":
                        return f"{float(BE):,.2f}"
                    if search_term =="Bitcoin" and moneda == "BRZ":
                        return f"{float(BF):,.2f}"
                    if search_term =="Bitcoin" and moneda == "BTC":
                        return "1"
                    if search_term =="Bitcoin" and moneda == "ARS":
                        return f"{(float(BA))*146.28:,.2f}"
                    if search_term =="Bitcoin" and moneda == "CLP":
                        return f"{(float(BA))*994.01:,.2f}"
                #DODGECOIN
                
                    if search_term =="Dogecoin" and moneda == "USD":
                        return f"{float(DA):,.2f}"
                    if search_term =="Dogecoin" and moneda == "GBP":
                        return float(f"{float(DA):,.2f}")*0.93
                    if search_term =="Dogecoin" and moneda == "EUR":
                        return float(f"{float(DA):,.2f}")*1.04
                    if search_term =="Dogecoin" and moneda == "JPY":
                        return float(f"{float(DA):,.2f}")*144.48
                    if search_term =="Dogecoin" and moneda == "AUD":
                        return float(f"{float(DA):,.2f}")*1.54
                    if search_term =="Dogecoin" and moneda == "PERP":
                        return float(f"{float(DE):,.2f}")*1.7039316518935792
                    if search_term =="Dogecoin" and moneda == "BRZ":
                        return float(f"{float(DA):,.2f}")*5.417499607231279
                    if search_term =="Dogecoin" and moneda == "BTC":
                        return float(f"{float(DA):,.2f}")*0.000050
                    if search_term =="Dogecoin" and moneda == "ARS":
                        return f"{(float(DA))*146.28:,.2f}"
                    if search_term =="Dogecoin" and moneda == "CLP":
                        return f"{(float(DA))*994.01:,.2f}"
                #ETHEREUM
                
                    if search_term =="Ethereum" and moneda == "USD":
                        return f"{float(EA):,.2f}"
                    if search_term =="Ethereum" and moneda == "GBP":
                        return f"{(float(EA))*0.93:,.2f}"
                    if search_term =="Ethereum" and moneda == "EUR":
                        return f"{float(EB):,.2f}"
                    if search_term =="Ethereum" and moneda == "JPY":
                        return f"{(float(EA))*144.48:,.2f}"
                    if search_term =="Ethereum" and moneda == "AUD":
                        return f"{float(ED):,.2f}"
                    if search_term =="Ethereum" and moneda == "PERP":
                        return f"{float(EE):,.2f}"
                    if search_term =="Ethereum" and moneda == "BRZ":
                        return f"{float(EF):,.2f}"
                    if search_term =="Ethereum" and moneda == "BTC":
                        return f"{float(EG):,.2f}"
                    if search_term =="Ethereum" and moneda == "ARS":
                        return f"{(float(EA))*146.28:,.2f}"
                    if search_term =="Ethereum" and moneda == "CLP":
                        return f"{(float(EA))*994.01:,.2f}"
                #Binance Coin 

                    if search_term =="Binance Coin" and moneda == "USD":
                        return f"{float(bA):,.2f}"
                    if search_term =="Binance Coin" and moneda == "GBP":
                        return f"{(float(bA))*0.93:,.2f}"
                    if search_term =="Binance Coin" and moneda == "EUR":
                        return float(f"{float(bA):,.2f}")*1.04
                    if search_term =="Binance Coin" and moneda == "JPY":
                        return f"{(float(bA))*144.48:,.2f}"
                    if search_term =="Binance Coin" and moneda == "AUD":
                        return f"{(float(bA))*1.54:,.2f}"
                    if search_term =="Binance Coin" and moneda == "PERP":
                        return f"{float(bE):,.2f}"
                    if search_term =="Binance Coin" and moneda == "BRZ":
                        return f"{(float(bA))*5.417499607231279:,.2f}"
                    if search_term =="Binance Coin" and moneda == "BTC":
                        return f"{float(bG):,.2f}"
                    if search_term =="Binance Coin" and moneda == "ARS":
                        return f"{(float(bA))*146.28:,.2f}"
                    if search_term =="Binance Coin" and moneda == "CLP":
                        return f"{(float(bA))*994.01:,.2f}"
                    

            with nav2:
                moneda = st.selectbox("Divisa :",divisas)
            with nav3:
                def simb():
                    if moneda == "USD":
                        return "$"
                    if moneda == "GBP":
                        return "£"
                    if moneda == "EUR":
                        return "€"
                    if moneda == "JPY":
                        return "¥"
                    if moneda == "AUD":
                        return "$"
                    if moneda == "PERP":
                        return "PERP"
                    if moneda == "BRZ":
                        return "BRZ"
                    if moneda == "BTC":
                        return "BTC"
                    if moneda == "ARS":
                        return "ARS"
                    if moneda == "CLP":
                        return "CLP"
                submit_search = st.form_submit_button()
            
                     
                
                
        st.success("Convertir {} a {}".format(search_term,moneda))
        st.write(f"  {result()} {simb()} ")
    else :
        
        st.subheader("Cryptomonedas")
        

        with st.form(key="my_form"):
            nab1,nab2,nab3 = st.columns([3,2,1])
            criptosbtc=["Bitcoin","Ethereum","Dogecoin","Binance Coin"]
        
            with nab1:
                search_term =st.selectbox("Select Cripto :",criptosbtc)
                    #BITCOIN               
                if search_term =="Bitcoin":
                        hola="USD"
                        d=f"{float(BA):,.2f}"  
                        m=Vbtc
                        v="Vol. 24h(USD)"
                        st.write(fbtc())
                        Vol=f"{float(volumeA):,.2f}"
                if search_term =="Dogecoin":  
                        hola="USD"
                        d=f"{float(DA):,.2f}"
                        m=Vdoge
                        v="Vol. 24h(USD)"
                        Vol=f"{float(volumeD):,.2f}"
                        st.write(fdoge())
                if search_term =="Ethereum":  
                        hola="USD"
                        d=f"{float(EA):,.2f}"
                        m=Veth
                        v="Vol. 24h(USD)"
                        st.write(feth())
                        Vol=f"{float(volumeB):,.2f}"
                if search_term =="Binance Coin": 
                        st.write(fbn())
                        d=f"{float(bA):,.2f}"
                        hola="USD"
                        m=Vbnb 
                        v="Vol. 24h(USD)"
                        Vol=f"{float(volumeC):,.2f}"
                        
                
            with nab2:
                st.metric(hola,d,m)
                
                
            with nab3:
                st.metric(v,Vol)
            submit_search = st.form_submit_button()
        if search_term=="Bitcoin":    
            a1,a2,a3=st.columns(3)
            a1.metric("Varianza",f"{float(varianzabtc):,.2f}")
            a2.metric("Desviacion Tipica",f"{float(desviacionbtc):,.2f}")
            #a3.metric("Media movil",st.write(rollh),"-8")
        if search_term=="Ethereum":    
            a1,a2,a3=st.columns(3)
            a1.metric("Varianza",f"{float(varianzaeth):,.2f}")
            a2.metric("Desviacion Tipica",f"{float(desviacioneth):,.2f}")
            #a3.metric("Media movil","9","-8")
        if search_term=="Dogecoin":    
            a1,a2,a3=st.columns(3)
            a1.metric("Varianza",f"{float(varianzadoge):,.2f}")
            a2.metric("Desviacion Tipica",f"{float(desviaciondoge):,.2f}")
            #a3.metric("Media movil","9","-8")
        if search_term=="Binance Coin":    
            a1,a2,a3=st.columns(3)
            a1.metric("Varianza",f"{float(varianzabnb):,.2f}")
            a2.metric("Desviacion Tipica",f"{float(desviacionbnbn):,.2f}")
           # a3.metric("Media movil","9","-8")
              
               
        #if st.checkbox("Dogecoin"):
                #st.write(fdoge())
            
        #if st.checkbox("Ethereum"):
                #st.write(feth())
            
        #if st.checkbox("Binance Coin"):
                #st.write(fbn())

        #rowa
        


        if st.checkbox("Estadisticas crypto"):
                #dforder=df.sort_values(by=["price"],ascending=False)
                st.dataframe(df)




if __name__ =="__main__":
    main()