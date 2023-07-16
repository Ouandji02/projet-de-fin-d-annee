import tensorflow as tf
import time
import cv2
import numpy as np
import os

# from tensorflow.python.keras import load_model


def bilderladen():
    Pfad = "./"
    for Datei in os.listdir(Pfad):
        img = os.path.join(Pfad, Datei)
        img = cv2.imread(img)
        img = cv2.resize(img, (450, 450))
        img = img / 255
        Bilder.append(img)


Bilder = []

vk = [
    "Limite de vitesse à 20 km/h",
    "Limitation de vitesse à 30 km/h",
    "Limite de vitesse à 50 km/h",
    "Limitation de vitesse à 60 km/h",
    "Vitesse limitée à 70 km/h",
    "Limite de vitesse à 80 km/h",
    "Fin de la limitation de vitesse à 80 km/h",
    "Limite de vitesse à 100 km/h",
    "Limitation de vitesse à 120 km/h",
    "interdiction générale de dépasser",
    "Interdiction de dépasser pour les camions",
    "Droit de passage unique",
    "droit de passage",
    "Céder",
    "Panneau stop",
    "Disque de blocage",
    "Pas de passage pour les camions",
    "Pas de passage",
    "Danger",
    "Attention : virage serré à gauche",
    "Attention : virage serré à droite",
    "Attention double courbe pointue",
    "Bouts d'attention",
    "Attention, risque de glissade",
    "Attention, voie qui se rétrécit à droite",
    "Attention chantier",
    "Attention feu tricolore",
    "Attention piétons",
    "Attention les enfants",
    "Attention vélos",
    "Attention chute de neige",
    "Attention passage des cerfs",
    "Suppression de la limitation de vitesse",
    "Flèche forcée à droite",
    "Flèche obligatoire à gauche",
    "Flèche droite obligatoire",
    "Flèche obligatoire droite ou droite",
    "Flèche obligatoire droite ou gauche",
    "Passez ici sur la droite",
    "Passez ici à gauche",
    "Rond point",
    "Suppression de l'interdiction de dépasser",
    "Suppression de l'interdiction de dépasser pour les camions",
]
bilderladen()


c = 111
d = 0
model = tf.keras.saving.load_model("./models/traffic_classifier.h5")
url = "http://192.168.144.54:8080/video"

vid = cv2.VideoCapture(url)

while True:
    ret, frame = vid.read()
    cv2.imshow("Bild", frame)
    frame = cv2.resize(frame, (30, 30))
    frame = frame / 255
    frame = frame.reshape(1, 30, 30, 3)
    # classes = model.predict(frame)
    pred = np.argmax(model.predict([frame]), axis=-1)
    # print("La prediction est : ", pred)
    # a = np.argmax(classes[0])
    # b = np.amax(classes[0])
    a = np.argmax(pred[0])
    b = np.amax(pred[0])
    print("A ==>", a, " B ====> ", b)
    if a != c or round(b, 2) != round(d, 2):
        c = a
        bild_text = np.zeros((150, 650, 3), np.uint8)
        cv2.putText(
            bild_text,
            str(vk[a]),
            (60, 30),
            cv2.FONT_HERSHEY_TRIPLEX,
            1,
            (255, 255, 255),
            2,
        )
        cv2.putText(
            bild_text,
            str((round(b * 100, 2))) + "%",
            (60, 90),
            cv2.FONT_HERSHEY_TRIPLEX,
            1,
            (255, 255, 255),
            2,
        )
        cv2.imshow("Image predit", bild_text)
        #     # cv2.imshow("erkanntes Verkehrsschild", Bilder[a])
        d = b
    if cv2.waitKey(20) & 0xFF == ord("q"):  # mit q könnt ihr das Programm beenden
        break
vid.release()

# while True:
#     ret, frame = vid.read()
#     if frame is not None:
#         cv2.imshow("frame", frame)
#     q = cv2.waitKey(1)
#     if q == ord("q"):
#         break
# cv2.destroyAllWindows()
