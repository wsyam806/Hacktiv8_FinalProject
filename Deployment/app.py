import streamlit as st
import pandas as pd 
import joblib
import numpy as np
from sklearn.cluster import KMeans
import time

page_bg_img = """
<style>[data-testid="stAppViewContainer"]{
background-color: #d1d1e6;
opacity: 0.2;
background-image:  repeating-radial-gradient( circle at 0 0, transparent 0, #d1d1e6 10px ), repeating-linear-gradient( #444cf755, #444cf7 );
}

[data-testid="stHeader"]{
background-color: rgba(0,0,0,0);
}
</style>


"""

Home, App = st.tabs(['Home','App'])

with Home:
  st.title("Final Project - Uncover potential insights 1999 Czech Bank Financial Dataset ")
  st.subheader("Abstract")
  st.write('This study presents an exploratory analysis of banking data to uncover potential insights and patterns related to customer behavior, credit risk assessment, geographic influences, customer segmentations, and time series trends. The analysis is conducted by integrating multiple tables containing transaction records, customer demographics, and district characteristics. The study employs various analytical techniques to extract valuable information from the data.')
  st.image('bank-building.jpg')
  st.subheader("Objective")
  st.write('In the realm of Customer Behavior Analysis, the study investigates transaction frequency patterns among different account types, distinguishing between owners and users. Additionally, the research delves into the average transaction amounts and account balances across distinct demographic regions. The analysis further dissects transaction types, such as credit and debit, based on customer attributes, uncovering trends and correlations between demographics and transaction behaviors.')  
  st.write('Credit Risk Assessment is another focal point, wherein the study evaluates the intricate connection between client demographics and their credit activities. Notably, the study scrutinizes credit utilization ratios among diverse demographic groups and explores the relationship between unemployment rates and loan default rates. By employing these insights, the study contributes to the enhancement of credit risk assessment strategies.')  
  st.write('Geographic Analysis explores the interplay between district characteristics and banking activities. The study investigates how features like district population and urban ratio influence banking behaviors, yielding valuable insights into regional banking dynamics.')
  st.write('Time Series Analysis forms an essential component of this study, unraveling transaction trends and patterns over time. The study identifies peak transaction periods and explores any seasonality in transaction frequencies or amounts. By uncovering temporal trends, the research contributes to proactive decision-making for resource allocation and customer service enhancements.')
  st.write('Furthermore, the study employs advanced techniques such as Customer Segmentations, wherein clustering algorithms are utilized to group customers based on transaction behaviors and demographic attributes. These segments provide a deeper understanding of customer profiles and enable tailored services. The identification of high-value customers based on criteria such as average salary, transaction volume, and account types is an integral part of this analysis.')
  

with App:
  st.subheader("Cluster Prediction and Product Recommendation")
  selected_features = ['Trans Withdrawal_x', 'Interest', 'Trans_Debit', 'total_amount',
       'Trans Withdrawal_y', 'total_balance', 'Payment of Statement',
       'Interest Credit', 'Standard Payment', 'transaction_count',
       'Trans_Credit']
  n_components = 2
  pipeline = joblib.load('pipeline.pkl')  
  
  df = pd.read_csv('df_trans.csv')
  pension = pd.read_csv("pension_package.csv")
  investment = pd.read_csv("investment_package.csv")
  mortgage = pd.read_csv("mortgage_package.csv")
  cluster_df = pipeline.fit(df)
  
    
  account_id = st.number_input('Account ID')
  total_amount = st.number_input('Accumulate Spending In Year')
  total_balance = st.number_input('Accumulate Balance After Spending In Year')
  transaction_count = st.number_input('Accumulate Transaction In Year')
  trans_Withdrawal_x = st.number_input('Accumulate Type Withdrawal Transaction In Year')
  trans_Credit = st.number_input('Accumulate Type Credit Card Transaction In Year')
  trans_Debit = st.number_input('Accumulate Type Debit Card Transaction In Year')
  collection_From_Other_Bank = st.number_input('Accumulate Collection From Other Bank In Year')
  credit_Card_Withdrawal = st.number_input('Accumulate Credit Card Withdrawal In Year')
  credit_in_Cash = st.number_input('Accumulate Credit in Cash In Year')
  interest = st.number_input('Accumulate Interest In Year')  
  remittance_From_Other_Bank = st.number_input('Accumulate Remittance From Other Bank In Year')
  trans_Withdrawal_y = st.number_input('Accumulate Trans Withdrawal Operation In Year')
  household_Payment = st.number_input('Accumulate Household Payment In Year')
  insurance_Payment = st.number_input('Accumulate Insurance Payment In Year')
  interest_Credit = st.number_input('Accumulate Interest Credit In Year')
  loan_Payment = st.number_input('Accumulate Loan Payment In Year')
  old_age_Pension_Payment = st.number_input('Accumulate Old age Pension Payment In Year')
  payment_of_Statement = st.number_input('Accumulate Payment of Statement In Year')  
  sanction_Negative_Bal= st.number_input('Accumulate Sanction Negative Bal. In Year')
  standard_Payment = st.number_input('Accumulate Standard Payment In Year')
  
  data = {
    'account_id': account_id,
    'total_amount': total_amount,
    'total_balance': total_balance,
    'transaction_count': transaction_count,
    'Trans Withdrawal_x': trans_Withdrawal_x,
    'Trans_Credit': trans_Credit,
    'Trans_Debit': trans_Debit,
    'Collection From Other Bank': collection_From_Other_Bank,
    'Credit Card Withdrawal': credit_Card_Withdrawal,
    'Credit in Cash': credit_in_Cash,
    'Interest': interest,
    'Remittance From Other Bank': remittance_From_Other_Bank,
    'Trans Withdrawal_y': trans_Withdrawal_y,
    'Household Payment': household_Payment,
    'Insurance Payment': insurance_Payment,
    'Interest Credit': interest_Credit,
    'Loan Payment': loan_Payment,
    'Old age Pension Payment': old_age_Pension_Payment,
    'Payment of Statement': payment_of_Statement,
    'Sanction Negative Bal.': sanction_Negative_Bal,
    'Standard Payment': standard_Payment,
  }
    
  input = pd.DataFrame(data, index=[0])
  st.subheader('User Input')
  st.write(input)
  if st.button('Predict'):
    progress_bar = st.progress(0)
    for perc_completed in range(100):
        time.sleep(0.10)
        progress_bar.progress(perc_completed+1)

    prediction = pipeline.predict(input)
    input['cluster'] = prediction
    st.write('Account Cluser Status : ', prediction)
    st.write("\n----------------\n")  
    for index, values in input.iterrows():
        for idx_ps, val_ps in pension.iterrows():
            if values['cluster'] == val_ps['Cluster']:
                st.write(f'For account : ', values['account_id'])
                st.write('Based on the client characteristic, here are the pension package product to offer :\n')
                st.write(f"Product Name: {val_ps['Product Name']} \n")
                val_ps_def = val_ps['Features'].split(',')
                st.write(f'Features :\n')
                for i in val_ps_def:
                    i = i.strip(" '\"[]")
                    st.write('*', i)
                st.write("\n----------------\n")
        for idx_iv, val_iv in investment.iterrows():
            if values['cluster'] == val_iv['Cluster']:
                st.write(f'For account : ', values['account_id'])
                st.write('Based on the client characteristic, here are the investment package product to offer :\n')
                st.write(f"Product Name: {val_iv['Product Name']} \n")
                val_iv_def = val_iv['Features'].split(',')
                st.write(f'Features :\n')
                for h in val_iv_def:
                    h = h.strip(" '\"[]")
                    st.write('*', h)
                st.write("\n----------------\n")
        for idx_mg, val_mg in mortgage.iterrows():
            if values['cluster'] == val_mg['Cluster']:
                st.write(f'For account : ', values['account_id'])
                st.write('Based on the client characteristic, here are the mortgage package product to offer :\n')
                st.write(f"Product Name: {val_mg['Product Name']} \n")
                val_mg_def = val_mg['Features'].split(',')
                st.write(f'Features :\n')
                for j in val_mg_def:
                    j = j.strip(" '\"[]")
                    st.write('*', j)
                st.write("\n----------------\n") 