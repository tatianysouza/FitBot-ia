import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk
from ttkbootstrap import Style
import google.generativeai as genai

# Configuração da API do Google
GOOGLE_API_KEY = "SUA_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)

# Configuração do modelo generativo
generation_config = {
  "candidate_count": 1,
  "temperature": 0.5,
}
safety_settings = {
    'HATE': 'BLOCK_NONE',
    'HARASSMENT': 'BLOCK_NONE',
    'SEXUAL' : 'BLOCK_NONE',
    'DANGEROUS' : 'BLOCK_NONE'
}

model = genai.GenerativeModel(model_name='gemini-1.0-pro',
                              generation_config=generation_config,
                              safety_settings=safety_settings,)

chat = model.start_chat(history=[])

root = tk.Tk()
style = Style('superhero')
root.style = style
root.geometry('500x400')
root.title('FitBot')

# Área de texto para a resposta do chatbot
response_area = scrolledtext.ScrolledText(root, width=60, height=20, font=('Helvetica', 10))
response_area.pack(padx=10, pady=10)
response_area.tag_config('user', foreground='black')
response_area.tag_config('bot', foreground='white')

# Frame para o campo de entrada e o botão
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

# Campo de texto para a entrada do usuário
user_input = ttk.Entry(input_frame, width=50, font=('Helvetica', 10))
user_input.pack(side=tk.LEFT, padx=(10, 5))

# Função para lidar com o envio de mensagens
def send_message():
    prompt = user_input.get()
    response = chat.send_message(prompt)
    response_area.insert(tk.END, "Você: " + prompt + '\n', 'user')
    response_area.insert(tk.END, "FitBot: " + response.text + '\n', 'bot')
    user_input.delete(0, tk.END)

# Botão para enviar a mensagem
send_button = ttk.Button(input_frame, text='Enviar', command=send_message)
send_button.pack(side=tk.RIGHT, padx=(5, 10))

# Mensagem inicial do chatbot
initial_prompt = "se apresente como um FitBot(um personal trainer que vai ajudar as pessoas a se exercitarem), voce vai perguntar que dias a pessoa pretende se exercitar, qual é o imc da pessoa, se ela tem algum problema fisico,(até essa parte crie um texto curto e simples de apresentação com perguntas) e depois disso vai criar um cronograma para essa pessoa de acordo com suas nescessidades e depois se a pessoa quiser você vai explicar cada exercicio deixe claro isso, mas não passe nenhum exercico agora"
initial_response = chat.send_message(initial_prompt)
response_area.insert(tk.END, "FitBot: " + initial_response.text + '\n', 'bot')

root.mainloop()