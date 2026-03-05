import pyautogui
import time

pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

# Abrir o navegador
pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")
# Fazer uma pausa maior para o site carregar
time.sleep(4)


# Fazer login
# Email
pyautogui.click(x=721, y=371)
pyautogui.write("pythonimpressionador@gmail.com")
# Senha
pyautogui.press("tab") # Passar para o próximo campo
pyautogui.write("senha secreta")
# Logar
pyautogui.press("tab") # clique no botao de login
pyautogui.press("enter")
# Fazer uma pausa maior para o site carregar
time.sleep(3)

# Abrir a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Cadastrar produtos
for linha in tabela.index:
  # código
  pyautogui.click(x=718, y=253)
  codigo = str(tabela.loc[linha, "codigo"])
  pyautogui.write(codigo)
  pyautogui.press("tab")

  # marca
  marca = str(tabela.loc[linha, "marca"])
  pyautogui.write(marca)
  pyautogui.press("tab")

  # tipo
  tipo = str(tabela.loc[linha, "tipo"])
  pyautogui.write(tipo)
  pyautogui.press("tab")

  # categoria
  categoria = str(tabela.loc[linha, "categoria"])
  pyautogui.write(categoria)
  pyautogui.press("tab")

  # preco_unitario
  preco = str(tabela.loc[linha, "preco_unitario"])
  pyautogui.write(preco)
  pyautogui.press("tab")

  # custo
  custo = str(tabela.loc[linha, "custo"])
  pyautogui.write(custo)
  pyautogui.press("tab")

  # obs
  obs = str(tabela.loc[linha, "obs"])
  if obs != "nan":
    pyautogui.write(obs)
  pyautogui.press("tab")

  pyautogui.press("enter")
  
  # Voltar ao início da tela 
  pyautogui.scroll(5000)