# Concatenar cadenas de caracteres.
# Supongamos que queremos crear una caena que diga:
# Aprende a programar con _____________.

empresa = 'Coderhouse'

print('Aprende a programar en: ' + empresa )

# Mad Libs 

adj = input("Adjetivo: ")
verbo1 = input("Verbo: ")
verbo2 = input("Verbo: ")
sustantivo_plural = input("Sustantivo (plural): ")

madlib = f"Programar es tan {adj} siempre me emociona porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con Coderhouse y alcanza tus {sustantivo_plural}!" 

print(madlib)