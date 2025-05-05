Documentação do Projeto FURIABot
🖤 Visão Geral
O FURIABot é um chatbot interativo criado com Python, utilizando a biblioteca Gradio para criar uma interface web e a API da OpenAI para gerar respostas em tempo real. O bot é temático, focado no time de CS2 da FURIA Esports e visa proporcionar aos fãs do time uma experiência de bate-papo divertida, com simulações de partidas e uma linguagem repleta de gírias gamers, emojis e muita energia positiva!

🔧 Tecnologias Utilizadas
Python 3.10+

Gradio: Biblioteca para criar interfaces web interativas de forma rápida.

OpenAI API: Utilizada para gerar respostas com o modelo GPT-3.5, baseado em um prompt customizado.

GitHub: Para versionamento e controle de código-fonte.

📁 Estrutura do Projeto
O projeto é organizado da seguinte maneira:

bash
Copiar código
furiabot/
├── app.py                # Arquivo principal do bot (onde o código do chatbot e Gradio ficam)
├── requirements.txt      # Lista de dependências do projeto
├── .gitignore            # Arquivo para ignorar arquivos que não devem ser versionados
└── README.md             # Documentação do projeto (este arquivo)
⚙️ Instalação e Execução
1. Clone o Repositório
Primeiro, clone o repositório para a sua máquina local:

bash
Copiar código
git clone https://github.com/seunome/furiabot.git
cd furiabot
2. Crie um Ambiente Virtual (opcional, mas recomendado)
Se você deseja usar um ambiente isolado para o projeto:

bash
Copiar código
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
3. Instale as Dependências
Execute o comando abaixo para instalar todas as dependências necessárias para o projeto:

bash
Copiar código
pip install -r requirements.txt
4. Configure a Chave da API da OpenAI
Para que o bot funcione corretamente, você precisa de uma chave da OpenAI API. Obtenha sua chave em OpenAI.

Crie um arquivo .env na raiz do projeto e adicione sua chave:

ini
Copiar código
OPENAI_API_KEY="sua-chave-aqui"
Ou, defina diretamente no código Python (não recomendado para produção).

5. Execute o Projeto
Com tudo configurado, você pode executar o bot com o seguinte comando:

bash
Copiar código
python app.py
O Gradio iniciará a aplicação localmente. Abra o navegador e acesse http://127.0.0.1:7860 para interagir com o bot.

🚀 Funcionalidades
Login Simples: O bot exige um login básico com usuário e senha (hardcoded). Usuários válidos podem acessar o chat.

Chat Interativo: O usuário interage com o bot em tempo real através de um campo de texto.

Simulação de Partidas: O bot pode simular partidas do time FURIA, gerando resultados aleatórios com base em um adversário e mapa escolhidos aleatoriamente.

Histórico de Conversa: O histórico de mensagens é mantido, permitindo uma conversa contínua com o bot.

🔒 Segurança e Limitações
O login é não seguro: Apenas uma simulação simples usando credenciais hardcoded.

A chave da OpenAI API não deve ser hardcoded em ambientes de produção. Utilize variáveis de ambiente ou outras práticas recomendadas para segurança.

Limitação de uso da API: O bot depende da API da OpenAI, que possui limites de uso, de acordo com o plano escolhido.

🤖 Prompt do Assistente (FURIABot)
O comportamento do FURIABot é determinado por um prompt base passado para a API da OpenAI. Aqui está o conteúdo do prompt:

text
Copiar código
Você é o FURIABot, o assistente oficial dos fãs da FURIA Esports.
Fale como um torcedor apaixonado pelo time de CS da FURIA.
Sempre responda como se estivesse dentro da comunidade FURIA.
Use emojis, gírias gamers e energia positiva.
Foque sempre no time de CS2: jogadores, partidas, treinos e bastidores.
Se não souber algo, responda como um torcedor criativo, inventando com bom humor.
⚡ Fluxo de Uso
O usuário acessa o bot via navegador.

Ele faz login com um usuário e senha (exemplo: furiafan/1234).

O usuário pode então interagir com o bot digitando mensagens no campo de texto.

Se desejar, pode digitar o comando /simular partida para gerar uma simulação de partida aleatória do time FURIA.
