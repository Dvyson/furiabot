import openai
import gradio as gr
import random

# Configuração do cliente OpenAI no novo estilo
client = openai.OpenAI(api_key="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")


system_prompt = {
    "role": "system",
    "content": (
        "Você é o FURIABot, o assistente oficial dos fãs da FURIA Esports.\n"
        "Fale como um torcedor apaixonado pelo time de CS da FURIA.\n"
        "Use emojis, gírias gamers e energia positiva.\n"
        "Foque sempre no time de CS2: jogadores, partidas, treinos e bastidores.\n"
        "Se não souber algo, invente com bom humor como um torcedor fanático."
    )
}

USUARIOS = {"furiafan": "1234", "torcedor": "furia"}

def furia_bot(user_input, history):
    if user_input.strip().lower() == "/simular partida":
        adversario = random.choice(["NAVI", "G2", "Faze", "MIBR", "Liquid"])
        mapa = random.choice(["Overpass", "Mirage", "Inferno", "Nuke", "Ancient"])
        destaque = random.choice(["arT", "KSCERATO", "yuurih", "chelo", "fallen"])
        score_furia = random.randint(14, 16)
        score_adv = random.randint(10, 14)
        resposta = f"🎯 Partida simulada: FURIA {score_furia} x {score_adv} {adversario} em {mapa}!\n{destaque} destruiu tudo hoje! VAMO FURIA! 🖤🔥"
        history.append((user_input, resposta))
        return history

    # Monta a conversa
    messages = [system_prompt]
    for user, bot in history:
        messages.append({"role": "user", "content": user})
        messages.append({"role": "assistant", "content": bot})
    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        bot_reply = response.choices[0].message.content
    except Exception as e:
        bot_reply = f"Erro ao falar com o servidor da FURIA 😓:\n\n{e}"

    history.append((user_input, bot_reply))
    return history

with gr.Blocks() as app:
    gr.Markdown("# 🖤🔥 FURIABot - Torcida da FURIA")
    gr.Markdown("Entre para bater um papo com o bot mais fanático da FURIA! 😎")

    with gr.Row():
        usuario = gr.Textbox(label="Usuário")
        senha = gr.Textbox(label="Senha", type="password")
        login_btn = gr.Button("Entrar")
        login_msg = gr.Markdown(visible=False)

    chatbot = gr.Chatbot()
    msg = gr.Textbox(placeholder="Digite sua mensagem ou /simular partida", visible=False)
    state = gr.State([])

    def autenticar(u, s):
        if u in USUARIOS and USUARIOS[u] == s:
            return gr.update(visible=True), [], gr.update(visible=False)
        return gr.update(visible=False), [], gr.update(value="Usuário ou senha inválidos", visible=True)

    login_btn.click(autenticar, inputs=[usuario, senha], outputs=[msg, state, login_msg])
    msg.submit(furia_bot, inputs=[msg, state], outputs=[chatbot], queue=False)

if __name__ == "__main__":
    app.launch()
