import streamlit as st # type: ignore
from streamlit_option_menu import option_menu # type: ignore
import psycopg2
import pandas as pd
import plotly.express as px
#DataFrame Creation
mydb = psycopg2.connect(host="localhost",
                        user="postgres",
                        port="5432",
                        database="phonepe_data",
                        password="0501")
cursor = mydb.cursor()


#aggregated_transaction_df
cursor.execute("SELECT * FROM aggregated_transaction")
mydb.commit()
table2= cursor.fetchall()

Aggre_transaction= pd.DataFrame(table2,columns=("States", "Years", "Quarter", "Transaction_type ", "Transaction_count", "Transaction_amount"))



#aggregated_user_df
cursor.execute("SELECT * FROM aggregated_user")
mydb.commit()
table3= cursor.fetchall()

Aggre_user= pd.DataFrame(table3,columns=("States", "Years", "Quarter", "Brands ", "Transaction_count", "Percentage"))

#map_insurance_
cursor.execute("SELECT * FROM map_insurance")
mydb.commit()
table4= cursor.fetchall()

Aggre_insurance= pd.DataFrame(table4,columns=("States", "Years", "Quarter", "District ", "Transaction_count", "Transaction_amount"))


#map_transaction
cursor.execute("SELECT * FROM map_transaction")
mydb.commit()
table5= cursor.fetchall()

map_transaction= pd.DataFrame(table5,columns=("States", "Years", "Quarter", "District ", "Transaction_count", "Transaction_amount"))


#map_user
cursor.execute("SELECT * FROM map_user")
mydb.commit()
table6= cursor.fetchall()

map_user= pd.DataFrame(table6,columns=("States", "Years", "Quarter", "District ", "RegisteredUser", "AppOpens"))


#top_insurance
cursor.execute("SELECT * FROM top_insurance")
mydb.commit()
table7= cursor.fetchall()

top_insurance= pd.DataFrame(table7,columns=("States", "Years", "Quarter", "Pincodes ", "Transaction_count", "Transaction_amount"))


#top_transaction
cursor.execute("SELECT * FROM top_transaction")
mydb.commit()
table8= cursor.fetchall()

top_transaction= pd.DataFrame(table8,columns=("States", "Years", "Quarter", "Pincodes ", "Transaction_count", "Transaction_amount"))


#top_user
cursor.execute("SELECT * FROM top_user")
mydb.commit()
table9= cursor.fetchall()

top_user= pd.DataFrame(table9,columns=("States", "Years", "Quarter", "Pincodes ", "RegisteredUsers"))


def Transaction_amount_count_Y(df, year):



    tacy= df[df["Years"]== year]
    tacy.reset_index(drop = True, inplace= True)

    tacyg=tacy.groupby("States")[["transaction_count","transaction_amount", ]].sum()
    tacyg.reset_index(inplace=True)

    col1,col2=st.columns(2)
    with col1:


        fig_amount= px.bar(tacy, x="States", y="transaction_amount", title="TRANSACTION AMOUNT", title=f"{year} TRANSACTION AMOUNT ",
                        color_discrete_sequence=px.colors.sequential.Aggrnyl,height= 650,width=600)
        st.plotly_chart(fig_amount)

    with col2:    
    
        fig_count = px.bar(tacyg, x="States", y="Transaction_count", tittle=f"{year} TRANSACTION COUNT" ,
                        color_discrete_sequence=px.colors.sequential.Bluered_r, height=650, width = 600)
        st.plotly_chart(fig_count)




#Streamlit Part

#st.set_page_config(layouts= "wide")
st.tittle("PHONEPE DATA VISUALIZATION AND EXPLORATION")

with st.sidebar:
    
    select=option_menu("Main Menu",["HOME", "DATA EXPLORATION", "TOP CHARTS"])

if select=="HOME" :
    pass
elif select =="DATA EXPLORATION":

    tab1, tab2, tab3 = st.tabs(["Aggregated Analysis", "Map Analysis","Top Analysis"])

    with tab1:

        method = st.radio("select The Method",["Insurance Analysis", "Transaction Analysis","User Analysis"])

        if method == "Insurance Analysis":

            col1,col2= st.columns(2)

            with col1:



                years=st.slider("Select The Year", Aggre_insurance["Years"].min(),Aggre_insurance["Years"].max(), Aggre_insurance["Years"].min())
                Transaction_amount_count_Y(Aggre_insurance,years)

        elif method == "Transaction Analysis":
            pass
        elif method == "User Analysis":
            pass

    with tab2:

        method_2= st.radio("SELECT The Mehtod", ["Map Insurance", "Map Transaction", "Map User"])

        if method_2 == "Map Insurance":
            pass
        elif method_2 =="Map Transaction":
            pass
        elif method_2== "Map User":
            pass    


    with tab3:

        method_3= st.radio("SELECT The Mehtod", ["Top Insurance", "Top Transaction", "Top User"])

        if method_2 == "Top Insurance":
            pass
        elif method_2 =="Top Transaction":
            pass
        elif method_2== "Top User":
            pass       

elif select =="TOP CHARTS": 
    pass       