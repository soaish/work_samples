import gradio as gr
import os
import requests
import google.generativeai as genai
import openai

def generate_text_chatgpt(key, prompt, temperature, top_p):

    openai.api_key = key

    response = openai.chat.completions.create(
      model="gpt-4-0613",
      messages=[{"role": "system", "content": "Suppose that you are a talented diagnostician"},
                {"role": "user", "content": prompt}],
      temperature=temperature,
      max_tokens=50,
      top_p=top_p,
      frequency_penalty=0
    )

    return response.choices[0].message.content


def generate_text_gemini(key, prompt, temperature, top_p):
    genai.configure(api_key=key)

    generation_config = genai.GenerationConfig(
        max_output_tokens=len(prompt)+50,
        temperature=temperature,
        top_p=top_p,
    )
    model = genai.GenerativeModel("gemini-1.5-flash", generation_config=generation_config)
    response = model.generate_content(prompt)
    return response.text


def generate_text_llama(key, prompt, temperature, top_p):
    model_name = "meta-llama/Llama-3.1-8B-Instruct"

    API_URL = f"https://api-inference.huggingface.co/models/{model_name}"
    headers = {"Authorization": f"Bearer {key}"}
    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": temperature,
            "max_new_tokens": 50,
            "top_p": top_p,
        }
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    resp_obj = response.json()
    if isinstance(resp_obj, list):
        resp = resp_obj[0]
        if 'generated_text' in resp:
            if len(resp['generated_text']) > len(prompt):
                return resp['generated_text'][len(prompt):]
            return resp['generated_text']
        return resp
    return resp_obj


def diagnose(key, model, top_k, temperature, symptom_prompt):

    if symptom_prompt:
        if "GPT" in model:
            message = generate_text_chatgpt(key, symptom_prompt, temperature, top_k)
        elif "Llama" in model:
            message = generate_text_llama(key, symptom_prompt, temperature, top_k)
        elif "Gemini" in model:
            message = generate_text_gemini(key, symptom_prompt, temperature, top_k)
        else:
            message = "Incorrect model, please try again."
    else:
        message = "Please add the symptoms data"
    
    return message



with gr.Blocks() as ui:
    message = "Hello, Welcome to the GUI by Team #9."

    with gr.Row(equal_height=500):
        with gr.Column(scale=1, min_width=300):
            model = gr.Radio(label="LLM Selection", value="GPT-3.5-Turbo",  
                             choices=["GPT-3.5-Turbo", "Llama-3.1", "Gemini-1.5"])
            key = gr.Textbox(label="Please input your LLM key", type="password")
            gr.Button(value="Don't have an LLM key? Get one through the below links.")
            gr.Button(value="OpenAi Key", link="https://platform.openai.com/account/api-keys")
            gr.Button(value="Meta Llama Key", link="https://platform.openai.com/account/api-keys")
            gr.Button(value="Gemini Key", link="https://platform.openai.com/account/api-keys")
            gr.ClearButton(key, message, variant="primary")
            
        with gr.Column(scale=2, min_width=600):
            message = gr.Textbox(label="", value=message, interactive=False, visible=True)
            output = gr.Textbox(label="Model output status", value="Model hasn't run yet.")
            temperature = gr.Slider(0.0, 1.0, value=0.7, step = 0.01, label="Temperature", info="Set the Temperature")
            top_k = gr.Slider(1, 10, value=3, step = 1, label="top-k value", info="Set the 'k' for top-k LLM responses")
            symptoms = gr.Textbox(label="Add the symptom data in the input to receive diagnosis")
            llm_btn = gr.Button(value="Diagnose Disease", variant="primary", elem_id="diagnose")
            llm_btn.click(fn=diagnose, inputs=[key, model, top_k, temperature, symptoms], outputs=output, api_name="auditor")
            output = gr.Textbox(label="LLM output status", value=output.value)



ui.launch(share=True)