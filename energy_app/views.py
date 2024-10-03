from django.shortcuts import render
from .forms import EnergyForm
import pandas as pd
from xgboost import XGBRegressor
import numpy as np
import pickle
# Load the iris dataset and train a simple classifier
energy = pd.read_csv('dataset/cleaned_household_power_consumption.csv')
#load model
xgb = pickle.load(open('model/xgboost_model.pkl', 'rb'))

def energy_predict(request):
    result = None
    
    # คำนวณค่าเฉลี่ยของ Sub_metering
    mean_sub_metering_1 = energy['Sub_metering_1'].mean()
    mean_sub_metering_2 = energy['Sub_metering_2'].mean()
    
    if request.method == 'POST':
        form = EnergyForm(request.POST)
        if form.is_valid():
            Global_active_power = form.cleaned_data['Global_active_power']
            Global_reactive_power = form.cleaned_data['Global_reactive_power']
            Voltage = form.cleaned_data['Voltage']
            Global_intensity = form.cleaned_data['Global_intensity']

            # Predict based on the input
            input_data = np.array([[Global_active_power, Global_reactive_power, Voltage, Global_intensity, mean_sub_metering_1, mean_sub_metering_2]])
            prediction = xgb.predict(input_data)[0]

            result = prediction
    else:
        form = EnergyForm()
    
    return render(request, 'energy_app/index.html', {'form': form, 'result': result})

