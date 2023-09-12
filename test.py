# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 00:57:45 2023

@author: Nitesh
"""

import numpy as np
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# loading the saved models
loaded_model = pickle.load(open('C:/Users/Nitesh/Desktop/GWL/trained_model.sav', 'rb'))
loaded_model2 = pickle.load(open('C:/Users/Nitesh/Desktop/GWL/trained_modelansh2.sav', 'rb'))
# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Ai Water well Predictor',
                          ['Current Water Level',
                           'Water Bearing Zone',
                           'Underground Water discharge'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
# Current Water Level Page
if (selected == 'Current Water Level'):
    
    # page title
    st.title('Current Water Level with NAQUIM data')
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        WLM_RPE = st.text_input('Reference Point Elevation')
        
    with col2:
        WLM_GSE = st.text_input('Ground Surface Elevation at site')
    
    with col3:
        RPE_WSE = st.text_input('Depth to the water surface in feet')
    
    with col1:
        GSE_WSE = st.text_input('Depth below ground surface')
    
    with col2:
        WSE2 = st.text_input('Ground Surface Elevation')
    
    diab_diagnosis = ''
    
    # creating a button for Prediction
    if st.button('GWL Test Result'):
        # Convert input data to numeric values
        try:
            WLM_RPE = float(WLM_RPE)
            WLM_GSE = float(WLM_GSE)
            RPE_WSE = float(RPE_WSE)
            GSE_WSE = float(GSE_WSE)
            WSE2 = float(WSE2)
            
            # Make the prediction with numeric input data
            diab_prediction = loaded_model.predict([[WLM_RPE, WLM_GSE, RPE_WSE, GSE_WSE, WSE2]])
            st.write("Prediction:", diab_prediction)
        except ValueError as e:
            st.error("Please enter valid numeric values for all input fields.")
        
    st.success(diab_diagnosis)


if (selected == 'Water Bearing Zone'):
    
    # page title
    st.title('AI-Enabled Water Well Predictor')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        name_of_state = st.text_input('Name of State')
        
    with col2:
        name_of_district = st.text_input('Name of District')
        
    with col3:
        recharge_monsoon = st.text_input('Recharge from rainfall During Monsoon Season')
        
    with col1:
        recharge_other_monsoon = st.text_input('Recharge from other sources During Monsoon Season')
        
    with col2:
        recharge_non_monsoon = st.text_input('Recharge from rainfall During Non Monsoon Season')
        
    with col3:
        recharge_other_non_monsoon = st.text_input('Recharge from other sources During Non Monsoon Season')
        
    with col1:
        total_natural_discharges = st.text_input('Total Natural Discharges ')
        
    with col2:
        Annual_Extractable_Ground= st.text_input('Annual Extractable Ground')
    with col3:
        water_resource = st.text_input('Water Resource')
        
    with col1:
        annual_groundwater_extraction_irrigation = st.text_input('Current Annual Ground Water Extraction For Irrigation')
        
    with col2:
        annual_groundwater_extraction_domestic_industrial = st.text_input('Current Annual Ground Water Extraction For Domestic & Industrial Use')
        
    with col3:
        total_current_annual_groundwater_extraction = st.text_input('Total Current Annual Ground Water Extraction')
        
    with col1:
        annual_gw_allocation = st.text_input('Annual GW Allocation')
        
    with col2:
        net_groundwater_availability_future_use = st.text_input('Net Ground Water Availability for future use')
    
    
    
    # Code for Prediction
    GWL_diagnosis = ''
    
    # Creating a button for Prediction
    if st.button('AI-Enabled Predictor'):
        # Convert input data to numeric values
        try:
            recharge_monsoon = float(recharge_monsoon)
            recharge_other_monsoon = float(recharge_other_monsoon)
            recharge_non_monsoon = float(recharge_non_monsoon)
            recharge_other_non_monsoon = float(recharge_other_non_monsoon)
            total_natural_discharges = float(total_natural_discharges)
            Annual_Extractable_Ground=float(total_natural_discharges)
            water_resource = float(water_resource)
            annual_groundwater_extraction_irrigation = float(annual_groundwater_extraction_irrigation)
            annual_groundwater_extraction_domestic_industrial = float(annual_groundwater_extraction_domestic_industrial)
            total_current_annual_groundwater_extraction = float(total_current_annual_groundwater_extraction)
            annual_gw_allocation = float(annual_gw_allocation)
            net_groundwater_availability_future_use = float(net_groundwater_availability_future_use)
            
            # Make the prediction with numeric input data
            GWL_prediction = loaded_model2.predict([[
                name_of_state, name_of_district, recharge_monsoon, recharge_other_monsoon,
                recharge_non_monsoon, recharge_other_non_monsoon, total_natural_discharges,
                water_resource, annual_groundwater_extraction_irrigation,
                annual_groundwater_extraction_domestic_industrial,
                total_current_annual_groundwater_extraction, annual_gw_allocation,
                net_groundwater_availability_future_use
            ]])
            st.write("Prediction:", GWL_prediction)  # Display the prediction
        except ValueError as e:
            st.error("Please enter valid numeric values for all input fields.")
        
    st.success(GWL_diagnosis)
