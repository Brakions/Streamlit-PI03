from secrets import choice
import streamlit as st
import requests
##TEST
from client import df
from client import BA,BB,BC,BD,BE,BF,EA,EB,EC,ED,EE,EF,EG,bA,bB,bC,bD,bE,bF,bG,DA,DB,DC,DD,DE,DF,DG

##TEST
#MAIN

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
        if st.checkbox("Bitcoin"):
        
            with st.form(key="f"):
                nab1,nab2,nab3 = st.columns([3,2,1])
                meses=["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiempre","Octubre","Noviembre","Diciembre"]
                numeros=["USD","GBP","EUR","JPY","AUD","PERP","BRZ","BTC","ARS","CLP"]
                with nab2:
                    divisd=st.select_slider("Select",numeros)
                submit_searchd = st.form_submit_button()
                with nab1:
                    search_term1 =st.select_slider("Select Date :",meses)
                    if search_term1 =="Enero" and divisd =="USD":
                        return st.write("nonde")
                    if search_term1 =="Febrero"and divisd =="JPY":
                        return st.write("none")
                
                with nab3:
                
                    submit_searchd = st.form_submit_button()
                    
                
                    
        if st.checkbox("Dogecoin"):
            dforder=df.sort_values(by=["price"],ascending=False)
            st.dataframe(dforder)
        
        if st.checkbox("Ethereum"):
            dforder=df.sort_values(by=["price"],ascending=False)
            st.dataframe(dforder)
        
        if st.checkbox("Binance Coin"):
            dforder=df.sort_values(by=["price"],ascending=False)
            st.dataframe(dforder)
        

        if st.checkbox("Estadisticas crypto"):
            dforder=df.sort_values(by=["price"],ascending=False)
            st.dataframe(dforder)




if __name__ =="__main__":
    main()