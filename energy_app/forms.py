from django import forms
class EnergyForm(forms.Form):
 Global_active_power = forms.FloatField(label='Global active power', min_value=0)
 Global_reactive_power= forms.FloatField(label='Global reactive power', min_value=0)
 Voltage = forms.FloatField(label='Voltage', min_value=0)
 Global_intensity = forms.FloatField(label='Global intensity', min_value=0)
