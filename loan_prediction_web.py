# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 00:25:33 2024

@author: ranja
"""

import numpy as np
import pickle
import streamlit as st


loaded_model= pickle.load(open('C:\ARAHUL COLLEGE\sahil project\Model_Prediction_loan.sav','rb'))


         
         
def main():
    st.title('Bank Loan Prediction Model ')

    account_no=st.text_input('Account Number')
    fn=st.text_input('Full Name')
    
    gen_display=('Female','Male')
    gen_options =list(range(len(gen_display)))
    gen=st.selectbox("Gender",gen_options,format_func=lambda x:gen_display[x])
    
    mar_display=('No','Yes')
    mar_options =list(range(len(mar_display)))
    mar=st.selectbox("Marital Status",gen_options,format_func=lambda x:mar_display[x])
    
    
    dep_display=('no','one','two','more than two')
    dep_options =list(range(len(dep_display)))
    dep=st.selectbox("Dependents",gen_options,format_func=lambda x:dep_display[x])
    
    edu_display=('Not Graduate','Graduate')
    edu_options =list(range(len(edu_display)))
    edu=st.selectbox("Education",gen_options,format_func=lambda x:edu_display[x])
    
    
    emp_display=('job','Buissness')
    emp_options =list(range(len(emp_display)))
    emp=st.selectbox("Employment Status",gen_options,format_func=lambda x:emp_display[x])
    
    
    
    prop_display=('Rular','Semi-urban','urban')
    prop_options =list(range(len(prop_display)))
    prop=st.selectbox("property area",gen_options,format_func=lambda x:prop_display[x])
    
   
    cred_display=('Between 300 to 500','Above 500')
    cred_options =list(range(len(cred_display)))
    cred=st.selectbox("Credit Score",gen_options,format_func=lambda x:cred_display[x])
    
    mon_income = st.number_input("Applicant monthly income($)",value=0)
    
    
    co_mon_income = st.number_input("co-Applicant monthly income($)",value=0)
    
   
    loan_amt = st.number_input("Loan Amount",value=0)
    
    
    dur_display=('2 Month','6 Month','8 Month','1 Year','16 Month')
    dur_options =list(range(len(dur_display)))
    dur=st.selectbox("loan Duration ",gen_options,format_func=lambda x:dur_display[x])
    
    
    if st.button("Submit"):
        duration =0
        if dur==0:
            duration=60
        if dur==1:
            duration==180
        if dur==2:
            duration==240
        if dur ==3:
            duration=360
        if dur==4:
            duration=480
            
        features=[[gen,mar,dep,edu,emp,mon_income,co_mon_income,loan_amt]]
        print(features)
        prediction=model.predict(features)
        lc=[str(i) for i in prediction]
        ans=int("".join(lc))
        if ans ==0:
            st.error(
                "hello: "+fn+ ' ||'
                'According to our calculation , you will not get the loan')
     
        else:
           st.success( "hello: "+fn+ " ||"
            "Account Number:" "+account_no +"'||'
           'Conguralation , you will  get the loan'
               )
           
           
   
  
if __name__=='__main__':
    main()
    