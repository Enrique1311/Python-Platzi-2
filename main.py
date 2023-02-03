def message_creator(text):
   # Escribe tu solución 👇
   options = {
      "computadora" : "Con mi computadora puedo programar usando Python",
      "celular" : "En mi celular puedo aprender usando la app de Platzi",
      "cable" : "¡Hay un cable en mi bota!"
   }
   if text in options.keys():
      return options.values()
   else:
      return"Artículo no encontrado"

text = 'computadora'
response = message_creator(text)
print(response)