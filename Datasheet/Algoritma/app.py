import gradio as gr 

title = "Machine learning klasifikasi berat badan dengan random forest"
description = """
klasifikasi status kesehatan berdasarkan tinggi badan, berat badan dan jenis kelamin.
"""

def make_prediction(Gender, Height, Weight):  
    rfc  = joblib.load('../Model development/API-BMI-Model-Using-Random-Forest.pkl')
    y_pred = rfc.predict([[Gender, Height, Weight]])
    if y_pred == 0:
        return 'Extremely Weak'
    elif y_pred == 1:
        return 'Weak'
    elif y_pred == 2:
        return 'Normal'
    elif y_pred == 3:
        return 'Overweight'
    elif y_pred == 4:
        return 'Obesity'
    elif y_pred == 5:
        return 'Extreme Obesity'

# Create the input component for Gradio since we are expecting 3 inputs
Gender_input = gr.Textbox(label = "Enter Gender Status {0:Female, 1:Male}")
Height_input = gr.Number(label  = "Enter Height")
Weight_input = gr.Number(label  = "Enter Weight")

# We create the output
output = gr.Textbox()


app = gr.Interface(title, description,, fn = make_prediction, inputs=[Gender_input, Height_input, Weight_input], outputs=output)
app.launch()