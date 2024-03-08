def inverter_string(texto):
  """
  Função que inverte os caracteres de uma string.

  Argumentos:
    texto: String que deseja inverter.

  Retorno:
    String com os caracteres invertidos.
  """
  texto_invertido = ""
  for i in range(len(texto)-1, -1, -1):
    texto_invertido += texto[i]
  return texto_invertido

texto = "Olá, mundo!"
texto_invertido = inverter_string(texto)

print(f"Texto original: {texto}")
print(f"Texto invertido: {texto_invertido}")
