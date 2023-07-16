#!/usr/bin/env python
# coding: utf-8

# In[2]:

import tkinter as tk
from tkinter import filedialog
from tkinter import *

# from PIL import Image, ImageTk
import PIL
from PIL import ImageTk
from PIL import Image

import numpy
import tensorflow as tf

from keras.models import load_model

model = tf.keras.saving.load_model("./models/traffic_classifier.h5")

classes = {
    1: "Limite de vitesse (20km/h)",
    2: "Limite de vitesse (30km/h)",
    3: "Limite de vitesse (50km/h)",
    4: "Limite de vitesse (60km/h)",
    5: "Limite de vitesse (70km/h)",
    6: "Limite de vitesse (80km/h)",
    7: "Fin limitation de vitesse (80km/h)",
    8: "Limite de vitesse (100km/h)",
    9: "Limite de vitesse (120km/h)",
    10: "Pas de dépassement",
    11: "Pas de dépassement de véh de plus de 3,5 tonnes",
    12: "Emprise de passage à l'intersection",
    13: "Route prioritaire",
    14: "Cédez",
    15: "Arrête",
    16: "Pas de véhicules",
    17: "Véh > 3,5 tonnes interdits",
    18: "Pas d'entrée",
    19: "Précaution générale",
    20: "Courbe dangereuse à gauche",
    21: "Courbe dangereuse à droite",
    22: "Double courbe",
    23: "Route cahoteuse",
    24: "Route glissante",
    25: "La route se rétrécit à droite",
    26: "Travaux routiers",
    27: "Feux de circulation",
    28: "Piétons",
    29: "Enfants traversant",
    30: "Traversée des vélos",
    31: "Attention à la glace/neige",
    32: "Animaux sauvages traversant",
    33: "Vitesse finale + limites de dépassement",
    34: "Tourner à droite",
    35: "Tourner à gauche devant",
    36: "Avant uniquement",
    37: "Allez tout droit ou à droite",
    38: "Aller tout droit ou à gauche",
    39: "Tenir à droite",
    40: "Tenir à gauche",
    41: "Rond-point obligatoire",
    42: "Fin du non-passage",
    43: "Fin pas de passage véh > 3,5 tonnes",
}

top = tk.Tk()
top.geometry("1200x700")
top.title("Reconnaissance des panneaux de signalisations. ")
top.configure(background="#2F4F4F")
label = Label(top, background="#2F4F4F", font=("georgia", 20, "bold"))
sign_image = Label(top)


def classify(file_path):
    global label_packed
    image = Image.open(file_path)
    image = image.resize((30, 30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    # pred = model.predict([image])[0]
    pred = numpy.argmax(model.predict([image]), axis=-1)
    # pred = model.predict([image])[0]
    print("La prediction est : ", pred)
    print("La classe est :", classes[pred[0] + 1])
    sign = classes[pred[0] + 1]
    print(sign)
    label.configure(foreground="#FFC0CB", text=sign)


def show_classify_button(file_path):
    classify_b = Button(
        top,
        text="Reconnaitre ",
        command=lambda: classify(file_path),
        padx=10,
        pady=10,
    )
    classify_b.configure(
        background="#FEBD07", foreground="#2F4F4F", font=("georgia", 15, "bold")
    )
    classify_b.place(relx=0.40, rely=0.38)


def upload_image():
    try:
        file_path = filedialog.askopenfilename()
        uploaded = Image.open(file_path)
        uploaded.thumbnail(((top.winfo_width() / 2.25), (top.winfo_height() / 2.25)))
        im = ImageTk.PhotoImage(uploaded)
        sign_image.configure(image=im)
        sign_image.image = im
        label.configure(text="")
        show_classify_button(file_path)
    except:
        pass


upload = Button(
    top, text="Selectionnez un panneaux", command=upload_image, padx=10, pady=10
)
upload.configure(
    background="#FEBD07", foreground="#2F4F4F", font=("georgia", 15, "bold")
)
upload.pack(side=BOTTOM, pady=50)
sign_image.pack(side=BOTTOM, expand=True)
label.pack(side=BOTTOM, expand=True)
heading = Label(
    top,
    text="Reconnaissance des panneaux de signalisation. ",
    pady=20,
    font=("georgia", 30, "bold"),
)
heading.configure(background="#2F4F4F", foreground="#FFD700")
heading.pack()

top.mainloop()


# In[ ]:
