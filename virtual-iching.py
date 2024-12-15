import os
import random
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
import threading

# Diccionario para asociar hexagramas con los archivos de audio
hexagrama_audios = {
    1: "1-lo-creativo.wav",
    2: "2-lo-receptivo.wav",
    3: "3-la-dificultad-inicial.wav",
    4: "4-necedad-juvenil.wav",
    5: "5-la-espera.wav",
    6: "6-el-conflicto.wav",
    7: "7-el-ejercito.wav",
    8: "8-la-solidaridad.wav",
    9: "9-la-fuerza-domesticadora-de-lo-pequeño.wav",
    10: "10-el-porte.wav",
    11: "11-la-paz.wav",
    12: "12-el-estancamiento.wav",
    13: "13-comunidad-con-los-hombres.wav",
    14: "14-la-posesion-de-lo-grande.wav",
    15: "15-la-modestia.wav",
    16: "16-el-entusiasmo.wav",
    18: "18-el-trabajo-en-lo-echado-a-perder.wav",
    17: "17-el-seguimiento.wav",
    19: "19-el-acercamiento.wav",
    20: "20-la-contemplacion.wav",
    21: "21-la-mordedura-tajante.wav",
    22: "22-la-gracia.wav",
    23: "23-la-desintegracion.wav",
    24: "24-el-retorno.wav",
    25: "25-la-inocencia.wav",
    26: "26-la-fuerza-domesticadora-de-lo grande.wav",
    27: "27-las-comisuras-de-la-boca.wav",
    28: "28-la-preponderancia-de-lo-grande.wav", 
    29: "29-abismal.wav",
    31: "31-el-influjo.wav",
    32: "32-la-duracion.wav",
    33: "33-la-retirada.wav"


    # Agrega aquí las asociaciones para todos los hexagramas...
}

# Definición de los hexagramas y sus detalles
hexagramas = {
    1: {
        "nombre": "乾",
        "pinyin": "Ch´ien",
        "significado": "Lo Creativo", 
        "variaciones": ["El Cielo", "El Principio Activo", "El Movimiento", "Dios"],
        "trigrama_superior": "☰",
        "trigrama_superior_nombre": "ch'ien -el cielo-",
        "trigrama_inferior": "☰",
        "trigrama_inferior_nombre": "ch'ien -el cielo-",
        "dictamen": "Lo Creativo obra elevado logro, propiciando por la perseverancia."
    },
    2: {
        "nombre": "坤",
        "pinyin": "K'un",
        "significado": "Lo Receptivo",
        "variaciones": ["La Tierra", "La Protección", "El Flujo"],
        "trigrama_superior": "☷",
        "trigrama_superior_nombre": "坤 k'un -la tierra-",
        "trigrama_inferior": "☷",
        "trigrama_inferior_nombre": "坤 k'un -la tierra-",
        "dictamen": (
            "Lo Receptivo obra elevado éxito, propiciante por la perseverancia de una yegua. "
            "Cuando el noble ha de emprender algo y quiere avanzar, se extravía; más si va en seguimiento "
            "encuentra conducción. Es propicio encontrar amigos al Oeste y al Sur; evitar los amigos al Este "
            "y al Norte. Una tranquila perseverancia trae ventura."
        )
    },
    3: {
        
        "nombre": "屯",
        "pinyin": "Chūn",
        "significado": "La Dificultad Inicial",
        "variaciones": ["Brotar", "Empezar Algo Nuevo" , "Acumular"],
        "trigrama_superior": "☵",
        "trigrama_superior_nombre": "坎 k'an -el agua-",
        "trigrama_inferior": "☳",
        "trigrama_inferior_nombre": "震 chen -el trueno-",
        "dictamen": (
                 "La Dificultad Inicial obra elevado éxito." 
                  "Propicio en virtud de la perseverancia. "
                  "No debe emprenderse nada." 
                   "Es propicio designar ayudantes."
        )
    },
    4: {
        
        "nombre": "蒙",
        "pinyin": "meng",
        "significado":  "La Necedad Juvenil",
        "variaciones": ["El Aprendiz", "La Inexperiencia Juvenil",  "Descubrir"],
        "trigrama_superior": "☶",
        "trigrama_superior_nombre": "艮 ken -la montaña-",
        "trigrama_inferior": "☵",
        "trigrama_inferior_nombre": "坎 k'an -el agua-",
        "dictamen": (
                      "La Necedad Juvenil tiene éxito."
                       "No soy yo quien busca al joven necio,el joven necio me busca a mí."
                        "Al primer oráculo doy razón."
                        "Si pregunta dos, tres veces, es molestia."
                        " Cuando mole sta no doy información."
                        "Es propicia la perseverancia"
                        )
                    },
    5: {
        
        "nombre": "需",
        "pinyin": "hsü",
        "significado":  "La Espera",
        "variaciones": ["La Paciencia", "La Resistencia a las Fuerzas Perjudiciales" , "La Inactividad"],
        "trigrama_superior": "☵ ",
        "trigrama_superior_nombre": "(坎 k'an -el agua-)",
        "trigrama_inferior": "☰",
        "trigrama_inferior_nombre": "乾 ch'ien -el cielo-",
        "dictamen": (
                    "La Espera."
                     "Si eres veraz, tendrás luz y éxito."
                     "La perseverancia trae ventura."
                      "Es propicio atravesar las grandes aguas"      
                        )
                    },
    6: {
        
        "nombre": "訟",
        "pinyin": "sung",
        "significado":   "El Conflicto",
        "variaciones": ["El Desacuerdo" , "El Pleito"],
        "trigrama_superior": "☰",
        "trigrama_superior_nombre": "乾 ch'ien -el cielo-)",
        "trigrama_inferior": "☵",
        "trigrama_inferior_nombre": "坎 k'an -el agua-" ,
        "dictamen": (
                    "El Conflicto: eres veraz y te frenan."
                     "Detenerse con cautela a mitad del camino trae ventura."
                     "Ir hasta el fin trae desventura."
                      "Es propicio ver al Gran Hombre." 
                     "No es propicio atravesar las grandes aguas."
                        )
                    },
    7: {
        
        "nombre": "師",
        "pinyin": "shih",
        "significado":   "El Ejército",
        "variaciones": ["El Líder" , "Las Masas"],
        "trigrama_superior": "☷ ",
        "trigrama_superior_nombre": "坤 k'un -la tierra-)",
        "trigrama_inferior": "☵",
        "trigrama_inferior_nombre": "坎 k'an -el agua-" ,
        "dictamen": (
                    "El Ejército requiere perseverancia y un hombre fuerte."
                     "Ventura sin falla."
                     
                        )
                    },
     8: {
        
        "nombre": " 比 ",
        "pinyin": "pi",
        "significado":    "La Solidaridad",
        "variaciones": ["La Reunión" , "La Alianza"],
        "trigrama_superior": " ☵ ",
        "trigrama_superior_nombre": "坎 k'an -el agua-",
        "trigrama_inferior": "☷ ",
        "trigrama_inferior_nombre": "坤 k'un -la tierra-" ,
        "dictamen": (
                    "La Solidaridad trae ventura."
                     "Indaga el oráculo una vez más, ve si tienes elevación, duración y perseverancia;"
                     "Si es así no habría defecto."
                     "Los inseguros se allegan poco a poco."
                     "El que llega tarde tiene desventura."
                        )
                    },
      9: {
        
        "nombre": " 小畜 ",
        "pinyin": "ch'u",
        "significado":    "La Fuerza Domesticadora de lo Pequeño",
        "variaciones": ["Débil Influencia" , "Suave Progreso"],
        "trigrama_superior": " ☴ ",
        "trigrama_superior_nombre": "巽 sun -el viento-",
        "trigrama_inferior": "☰ ",
        "trigrama_inferior_nombre": "乾 ch'ien -el cielo-" ,
        "dictamen": (
                    "La Fuerza Domesticadora de lo Pequeño tiene éxito."
                     "Indaga el oráculo una vez más, ve si tienes elevación, duración y perseverancia;"
                     "Densas nubes, ninguna lluvia de nuestra región del Oeste."
                        )
                    },
    10: {
        
        "nombre": "履",
        "pinyin": "lü",
        "significado": "El Porte",
        "variaciones": ["Débil Influencia" , "Suave Progreso"],
        "trigrama_superior": " ☰ ",
        "trigrama_superior_nombre": "☰ 乾 ch'ien -el cielo-",
        "trigrama_inferior": " ☱  ",
        "trigrama_inferior_nombre": "兌 tui -el lago-" ,
        "dictamen": (
                    "Pisar la cola al tigre."
                     "Éste no muerde al hombre. Éxito."
                     
                        )
                    },
      11: {
        
        "nombre": "泰",
        "pinyin": "t'ai",
        "significado": "La Paz",
        "variaciones": [ "La Abundancia", "La Prosperidad"],
        "trigrama_superior": "☷",
        "trigrama_superior_nombre": "☰ 乾 ch'ien -el cielo-",
        "trigrama_inferior": "☰",
        "trigrama_inferior_nombre": "坤 k'un -la tierra-" ,
        "dictamen": (
                    "La Paz. Lo pequeño se va, llega lo grande."
                     "¡Ventura! ¡Éxito!"
                     
                        )
                    },

     12: {
        
        "nombre": "否",
        "pinyin": "p'i",
        "significado": "El Estancamiento",
        "variaciones": [ "La Desunión" , "La Separación"],
        "trigrama_superior": "☰",
        "trigrama_superior_nombre": " 乾 ch'ien -el cielo-",
        "trigrama_inferior": "☷ ",
        "trigrama_inferior_nombre": "坤 k'un -la tierra-" ,
        "dictamen": (
                    "El Estancamiento."
                     "Hombres vulgares no favorecen la perseverancia del noble."
                     "Lo grande se va, llega lo pequeño."
                        )
                    },
      13: {
        
        "nombre": "同人 ",
        "pinyin": "t'ung jen",
        "significado": "Comunidad con los Hombres",
        "variaciones": [ "La Comunidad" , "La Amistad"],
        "trigrama_superior": "☰",
        "trigrama_superior_nombre": " 乾 ch'ien -el cielo-",
        "trigrama_inferior": "☲ ",
        "trigrama_inferior_nombre": "離 Lí -el fuego-" ,
        "dictamen": (
                    "Comunidad con los hombres en lo libre: éxito."
                     "Es propicio atravesar las grandes aguas."
                     "Propicia es la perseverancia del noble."
                        )
                    },
     14: {
        
        "nombre": "大有 ",
        "pinyin": "ta yu",
        "significado": "La Posesión de lo Grande",
        "variaciones": [ "El Dominio" , "La Gran Posesión"],
        "trigrama_superior": "☲",
        "trigrama_superior_nombre": "  離 Lí -el fuego-",
        "trigrama_inferior": "☰ ",
        "trigrama_inferior_nombre": "乾 ch'ien -el cielo- " ,
        "dictamen": (
                    "La Posesión de lo Grande. Elevado logro."
                     
                        )
                    },
    15: {
        
        "nombre": "謙  ",
        "pinyin": "ch'ien",
        "significado": "La Modestia",
        "variaciones": [ "El Recato" , "El Respeto"],
        "trigrama_superior": "☷",
        "trigrama_superior_nombre": "坤 k'un -la tierra-",
        "trigrama_inferior": " ☶",
        "trigrama_inferior_nombre": "艮 ken -la montaña- " ,
        "dictamen": (
                    "La Modestia va creando el éxito."
                     "El noble lleva a buen término."
                        )
                    },
    16: {
        
        "nombre": "豫",
        "pinyin": "yü",
        "significado": "El Entusiasmo",
        "variaciones": [ "La Felicidad" , "El Fervor"],
        "trigrama_superior": "☳",
        "trigrama_superior_nombre":  "震 chen -el trueno-",
        "trigrama_inferior": "☷",
        "trigrama_inferior_nombre": "坤 k'un -la tierra- " ,
        "dictamen": (
                    "El Entusiasmo. Es propicio."
                     "designar ayudantes y hacer marchar ejércitos."
                        )
                    },
    17: {
        
        "nombre": "隨",
        "pinyin": "sui",
        "significado": "El Seguimiento",
        "variaciones": ["La Huella"],
        "trigrama_superior": "☱",
        "trigrama_superior_nombre":  "兌 tui -el lago-",
        "trigrama_inferior": "☳",
        "trigrama_inferior_nombre": "震 chen -el trueno- " ,
        "dictamen": (
                    "El seguimiento tiene elevado éxito."
                     "Es propicia la perseverancia."
                     "No hay defecto"
                        )
                    },
     18: {
        
        "nombre": "蠱",
        "pinyin": "ku",
        "significado": "El Trabajo en lo Echado a Perder",
        "variaciones": [ "La Decadencia", "La Descomposición" , "La Restauración"],
        "trigrama_superior": " ☶ ",
        "trigrama_superior_nombre":  "艮 ken -la montaña-",
        "trigrama_inferior": "☴ ",
        "trigrama_inferior_nombre": "巽 sun -el viento- " ,
        "dictamen": (
                    "El Trabajo en lo Echado a Perder tiene elevado éxito."
                     "Es propicio atravesar las grandes aguas."
                     "Antes del punto inicial tres días, después del punto inicial tres días."
                        )
                    },
    19: {
        
        "nombre": "臨",
        "pinyin": "lin",
        "significado": "El acercamiento",
        "variaciones": [ "Vigilar" , "Incentivar"],
        "trigrama_superior": "☷",
        "trigrama_superior_nombre":  "坤 k'un -la tierra-",
        "trigrama_inferior": "☱ ",
        "trigrama_inferior_nombre": "兌 tui -el lago-" ,
        "dictamen": (
                    "El Acercamiento tiene elevado éxito."
                     "Es propicia la perseverancia."
                     "Al llegar el octavo mes habrá desventura."
                        )
                    },
     20: {
        
        "nombre": " 觀",
        "pinyin": "kuan",
        "significado": "El acercamiento",
        "variaciones": [ "Vigilar" , "Incentivar"],
        "trigrama_superior": "☴",
        "trigrama_superior_nombre":  "巽 sun -el viento-",
        "trigrama_inferior": "☷ ",
        "trigrama_inferior_nombre": "坤 k'un -la tierra-" ,
        "dictamen": (
                    "La Contemplación."
                     "Se ha cumplido la ablución, pero aún no la ofrenda."
                     "Plenos de confianza levantan la mirada hacia él."
                        )
                    },
      21: {
        
        "nombre": "噬嗑",
        "pinyin": "shìh ho",
        "significado": "La Mordedura Tajante",
        "variaciones": [ "Eliminar Obstáculos" , "Quebrar Drásticamente"],
        "trigrama_superior": "☲",
        "trigrama_superior_nombre":  "離 Lí -el fuego-",
        "trigrama_inferior": "☳ ",
        "trigrama_inferior_nombre": "震 chen -el trueno-" ,
        "dictamen": (
                    "La Mordedura Tajante tiene éxito."
                    "Es propicio administrar justicia."
                        )
                    },
     22: {
        
        "nombre": "賁",
        "pinyin": "pi",
        "significado":  "La Gracia",
        "variaciones": [  "La Apariencia" , "La Elegancia"],
        "trigrama_superior": "☶",
        "trigrama_superior_nombre":  "艮 ken -la montaña-",
        "trigrama_inferior": "☲ ",
        "trigrama_inferior_nombre": "離 Lí -el fuego-" ,
        "dictamen": (
                    "La Gracia tiene éxito."
                    "En lo pequeño es propicio emprender algo."
                        )
                    },
     23: {
        
        "nombre": "剝",
        "pinyin": "po",
        "significado":  "La Desintegración",
        "variaciones": [  "La Apariencia" , "La Elegancia"],
        "trigrama_superior": "☶",
        "trigrama_superior_nombre":  "艮 ken -la montaña-",
        "trigrama_inferior": "☷ ",
        "trigrama_inferior_nombre":  "坤 k'un -la tierra- " ,
        "dictamen": (
                    "La Desintegración."
                    "No es propicio ir a parte alguna."
                        )
                    },
     24: {
        
        "nombre": "復",
        "pinyin":   "fu",
        "significado":  "El Retorno",
        "variaciones": [  "La Apariencia" , "La Elegancia"],
        "trigrama_superior": "☷",
        "trigrama_superior_nombre":  "坤 k'un -la tierra-",
        "trigrama_inferior": "☳  ",
        "trigrama_inferior_nombre":  "震 chen -el trueno- " ,
        "dictamen": (
                    "El Retorno. éxito."
                   " Salida y entrada sin falla."
                    "Llegan amigos sin tacha."
                    "Va y viene el camino."
                    "Al séptimo día llega el retorno."

                    "Es propicio tener adonde ir."
                        )
                    },
    25: {
        
        "nombre": "無妄",
        "pinyin": "wu wang",
        "significado":  "La Inocencia",
        "variaciones": [  "Inexperiencia" , "La Espontaneidad"],
        "trigrama_superior": "☰",
        "trigrama_superior_nombre":  " 乾 ch'ien -el cielo-",
        "trigrama_inferior": "☳  ",
        "trigrama_inferior_nombre":  " 震 chen -el trueno- " ,
        "dictamen": (
                    "La Inocencia. Elevado éxito."
                   "Es propicia la perseverancia"
                    "Si alguien no es recto tendrá desdicha,"
                    "y no será propicio emprender algo"
                    
                        )
                    },
      26: {
        
        "nombre": "大畜 ",
        "pinyin": "ta ch'u",
        "significado":  "La Fuerza Domesticadora de lo Grande",
        "variaciones": [  "Gran Dedicación", "El Desarrollo de la Personalidad" , "Energía Potencial"],
        "trigrama_superior": "☶ ",
        "trigrama_superior_nombre":  " 艮 ken -la montaña-",
        "trigrama_inferior": "☰  ",
        "trigrama_inferior_nombre":  " 乾 ch'ien -el cielo- " ,
        "dictamen": (
                   " La Fuerza Domesticadora de lo Grande."
                   " Es propicia la perseverancia."
                    "Trae ventura no comer en casa."

                    "Es propicio atravesar las grandes aguas."
                    
                        )
                    },
     27: {
        
        "nombre": "頤 ",
        "pinyin": "I",
        "significado":  "Las Comisuras de la Boca",
        "variaciones": [ "Tragar", "La Salud" , "Actitudes Moderadas"],
        "trigrama_superior": "☶ ",
        "trigrama_superior_nombre":  " 艮 ken -la montaña-",
        "trigrama_inferior": " ☳ ",
        "trigrama_inferior_nombre":  " 震 chen -el trueno-" ,
        "dictamen": (
                  " Las Comisuras de la Boca."
                    "Perseverancia trae ventura."
                     "Presta atención a la nutrición, y a aquello con que trata de llenar su boca uno mismo."
                    
                        )
                    },
    # Agrega más hexagramas aquí...
}

# Carpeta donde se encuentran los audios
carpeta_audios = "/Users/sdcarr/Desktop/KAIROS-ICHING/python-ipynb/audios/"

def seleccionar_hexagrama():
    """Selecciona un hexagrama al azar."""
    return random.choice(list(hexagramas.keys()))

def crear_fondo_gradiante(width, height):
    """Crea un fondo con gradiente para la ventana."""
    base = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(base)
    for i in range(height):
        ratio = i / height
        r = int(255 * ratio)
        b = 255 - r
        draw.line([(0, i), (width, i)], fill=(r, 0, b))
    return ImageTk.PhotoImage(base)

def reproducir_audio(hexagrama_id):
    """Reproduce el audio asociado a un hexagrama."""
    archivo_audio = hexagrama_audios.get(hexagrama_id)
    if archivo_audio:
        archivo_completo = os.path.join(carpeta_audios, archivo_audio)
        print(f"Intentando reproducir: {archivo_completo}")  # Depuración
        if os.path.exists(archivo_completo):
            try:
                audio = AudioSegment.from_file(archivo_completo)
                play(audio)
            except Exception as e:
                print(f"Error al reproducir el audio: {e}")
        else:
            print(f"Archivo no encontrado: {archivo_completo}")
    else:
        print(f"No hay archivo de audio asociado al hexagrama {hexagrama_id}")

def mostrar_hexagrama():
    """Muestra la información del hexagrama seleccionado y reproduce el audio correspondiente."""
    hexagrama = seleccionar_hexagrama()
    hexagrama_info = hexagramas[hexagrama]

    # Mostrar información en la interfaz gráfica
    significado.config(text=f"Significado: {hexagrama_info['significado']}")
    variaciones.config(text=f"Variaciones: {', '.join(hexagrama_info['variaciones'])}")
    trigramas.config(text=f"Trigrama Superior: {hexagrama_info['trigrama_superior']} ({hexagrama_info['trigrama_superior_nombre']})\n"
                          f"Trigrama Inferior: {hexagrama_info['trigrama_inferior']} ({hexagrama_info['trigrama_inferior_nombre']})")
    nombre_hexagrama.config(text=f"Hexagrama {hexagrama_info['nombre']} ({hexagrama_info['pinyin']})")
    dictamen.config(text=f"El Dictamen dice:\n{hexagrama_info['dictamen']}")

    # Reproducir audio asociado al hexagrama
    threading.Thread(target=reproducir_audio, args=(hexagrama,), daemon=True).start()

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Hexagrama I Ching")
ventana.attributes('-fullscreen', True)  # Pantalla completa
ventana.configure(bg='black')

# Fondo con gradiente
fondo_gradiante = crear_fondo_gradiante(1900, 1300)
etiqueta_fondo = tk.Label(ventana, image=fondo_gradiante)
etiqueta_fondo.place(x=0, y=0, relwidth=1, relheight=1)

# Marco para el contenido
frame_contenido = tk.Frame(ventana, bg='black')
frame_contenido.pack(expand=True, padx=20, pady=100)

significado = tk.Label(frame_contenido, text="", font=("Segoe UI Historic", 18), fg='yellow', bg='black')
significado.pack(pady=10)

variaciones = tk.Label(frame_contenido, text="", font=("Segoe UI Historic", 18), fg='yellow', bg='black')
variaciones.pack(pady=10)

trigramas = tk.Label(frame_contenido, text="", font=("Segoe UI Historic", 22, "bold"), fg='yellow', bg='black')
trigramas.pack(pady=10)

nombre_hexagrama = tk.Label(frame_contenido, text="", font=("Segoe UI Historic", 40, "bold"), fg='yellow', bg='black')
nombre_hexagrama.pack(pady=10)

dictamen = tk.Label(frame_contenido, text="", font=("Segoe UI Historic", 18), wraplength=550, justify="left", fg='yellow', bg='black')
dictamen.pack(pady=20)

# Botón para generar hexagramas
boton = ttk.Button(ventana, text="Generar Hexagrama", command=mostrar_hexagrama)
boton.pack(side=tk.BOTTOM, pady=50)

# Iniciar el bucle principal
ventana.mainloop()