import pyautogui
import time
import ctypes
import random
#RESOLUÇÃO 1024X768 EU ACHO
# Defina a semente inicial para geração de números aleatórios (opcional)
random.seed()

def alterar_titulo_janela(progresso):
    ctypes.windll.kernel32.SetConsoleTitleW(f"@IURIRUSSO7 Progresso: {progresso}")

dados_coluna_d = []

# Função para copiar e colar URLs
def trampos(urls):
    total_urls = len(urls)
    for i, valor in enumerate(urls, 1):
        # Seleciona o valor atual da lista
        valor_atual = str(valor)
        numero_aleatorio = random.randint(0, 15)  # Gere um novo número aleatório para cada iteração
        time.sleep(numero_aleatorio)

        pyautogui.moveTo(305, 53)
        time.sleep(numero_aleatorio)
        pyautogui.click()
        time.sleep(numero_aleatorio)

        pyautogui.write(valor_atual)
        time.sleep(numero_aleatorio)
        pyautogui.press("enter")
        time.sleep(numero_aleatorio)

        seguir = 'C:\\Users\\vboxuser\\Desktop\\PROGRAMASVM\\Screenshot_1.png'
        try:
            img = pyautogui.locateCenterOnScreen(seguir, confidence=0.7)
            pyautogui.click(img.x, img.y)
        except:
            pass
        time.sleep(numero_aleatorio)

# Função para ler as URLs a partir do console
def ler_urls():
    while True:
        url = input("Digite a URL do Instagram (ou 'sair' para encerrar): ")
        if url.lower() == 'sair':
            break
        dados_coluna_d.append(url)

# Defina o nome da janela do prompt de comando
def definir_nome_janela(nome):
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(nome)

# Executar a função para ler as URLs
print("Digite as URLs do Instagram. Digite 'sair' quando terminar.")
ler_urls()

# Definir o nome da janela do prompt de comando
definir_nome_janela("#UNIAO SUL && NORDESTE INTENSA -- @IURIRUSSO7 E @GOTTI.ADS")

# Definir o número de URLs a serem seguidas em cada lote
porvez = int(input("Quantas URLs por Lote??"))
urls_per_batch = porvez
horas2 = int(input("Quantas horas de intervalo entre lotes?:"))
# Calcular o número total de lotes
total_batches = (len(dados_coluna_d) + urls_per_batch - 1) // urls_per_batch

def ler_progresso():
    try:
        with open('progresso.txt', 'r') as arquivo:
            return int(arquivo.read())
    except FileNotFoundError:
        return 0

# Função para salvar o progresso em um arquivo
def salvar_progresso(progresso):
    with open('progresso.txt', 'w') as arquivo:
        arquivo.write(str(progresso))

# Inicialize o índice atual do lote lendo o progresso anterior
indice_atual = ler_progresso()

for batch_num in range(indice_atual, total_batches):
    start_index = batch_num * urls_per_batch
    end_index = (batch_num + 1) * urls_per_batch
    batch_urls = dados_coluna_d[start_index:end_index]

    try:
        # Execute trampos com o lote atual de URLs
        trampos(batch_urls)
    except Exception as e:
        print(f"Erro encontrado no lote {batch_num + 1}: {e}")
        # Armazene o índice atual para retomar a partir do lote onde parou
        indice_atual = batch_num
        salvar_progresso(indice_atual)
        # Você também pode adicionar um tempo de espera aqui antes de continuar

    if batch_num < total_batches - 1:
        print(f"Esperando por {horas2} horas... (Lote {batch_num + 1}/{total_batches})")
        time.sleep(3600 * horas2)  # Pausar por horas definidas
