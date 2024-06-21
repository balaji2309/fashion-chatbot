import gradio as gr
import openai

# Set up OpenAI GPT-3.5 credentials
openai.api_key = "OPENAI_KEY"

def generate_fashion_outfit(gender, weather, place, age, style, time, colors, accessories):
    prompt = f"Generate a fashion outfit for {gender} with the following parameters:\nWeather: {weather}\nPlace to Visit: {place}\nAge: {age}\nStyle: {style}\nTime of Day: {time}\nColors: {colors}\nAccessories: {accessories}\nOutfit:"
    response = openai.Completion.create(
        engine="text-davinci-003", 
        prompt=prompt,
        max_tokens=500
    )
    outfit = response.choices[0].text.strip()
    return outfit

def generate_with_button(gender, weather, place, age, style, time, colors, accessories):
    outfit = generate_fashion_outfit(gender, weather, place, age, style, time, colors, accessories)
    return outfit

gender_options = ["Male", "Female"]
style_options = [
    "Traditional", "Modern", "Classic", "Vintage", "Bohemian", 
    "Casual", "Streetwear", "Retro", "Chic", "Avant-garde"
]

inputs = [
    gr.inputs.Radio(gender_options, label="Gender"),
    gr.inputs.Textbox(label="Weather"),
    gr.inputs.Textbox(label="Place you will Visit"),
    gr.inputs.Number(label="Age"),
    gr.inputs.Radio(style_options, label="Style Preference"),
    gr.inputs.Radio(["Day", "Night"], label="Time of Day"),
    gr.inputs.Textbox(label="Color Preferences"),
    gr.inputs.Textbox(label="Accessories")
]

fashion_bot = gr.Interface(
    fn=generate_with_button,
    inputs=inputs,
    outputs=gr.outputs.Textbox(),
    live=False,
    title="Fashion Recommendation Chatbot",
    description="Get personalized fashion recommendations based on your preferences."
)

fashion_bot.launch()
