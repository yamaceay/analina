from PIL import Image
import streamlit as st
import os
import math
import numpy as np

wochen_int = list(range(0, 15))
wochen = ["-", *[f"{woche:02d}" for woche in wochen_int]]

keys = ['000.png', '001.png', '010.png', '011.png', '012.png', '020.png', '021.png', '022.png', '023.png', '024.png', '030.png', '031.png', '032.png', '033.png', '040.png',
 '041.png', '042.png', '050.png', '051.png', '052.png', '060.png', '061.png', '062.png', '070.png', '071.png', '072.png', '073.png', '080.png', '081.png', '082.png',
 '090.png', '091.png', '092.png', '093.png', '100.png', '101.png', '102.png', '110.png', '111.png', '112.png', '120.png', '121.png', '122.png', '130.png', '131.png',
 '132.png', '140.png', '141.png', '142.png']

vals = ["Rechenregeln", "Rechenregeln für Bruchrechnung", "Ungleichungen", "Summen- und Produktzeichen", "Rechenregeln für Potenzrechnung",
        "Komplexe Zahlen", "Eigenschaften reeller Funktionen", "Eigenschaften reeller Funktionen", "Exponentialfunktion und Logarithmus",
        "Sinus und Cosinus", "Eulerdarstellung", "Polynomdivision", "Nullstellen von Polynomen", "Partialbruchzerlegung", "Linearkombination",
        "Lineare Unabhängigkeit", "Rechnen mit Matrizen", "Lineare Gleichungssysteme lösen", "Rang und Invertierbarkeit", "Lineare Abbildungen",
        "Matrixdarstellung", "Konvergenz", "Monotonie und Konvergenz", "Grenzwerte von Funktionen", "Stetigkeit", "Zwischenwertsatz und Bisektionsverfahren",
        "Rechenregeln für die Ableitung", "Die Regel von L-Hospital", "Mittelwertsatz", "Satz von Taylor", "Extremwerte",
        "Satz von Taylor", "Allgemeine Potenz und Logarithmen", "Hyperbolische Funktionen", "Integration", "Partielle Integration",
        "Die Substitutionsregel", "Uneigentliche Integrale", "Determinante", "Eigenwerte und Eigenvektoren", "Diagonalisierbarkeit",
        "Orthogonalität und Orthogonalprojektion", "Das Gram-Schmidt-Verfahren", "Fourierapproximation", "Fourierapproximation",
        "Fourieranalysis", "Reihen", "Absolut konvergente Reihen", "Potenzreihen"]

map_dict = {k:v for k,v in zip(keys, vals)}

def get_image(path):
    return Image.open(path)

def open_images(woche):
    images = []
    for filename in os.listdir("imgs"):
        if filename.startswith(woche):
            images.append(get_image("imgs/"+filename))
    return images

def remove_all(alist):
    if alist != []:
        for img in alist:
            img.empty()
        alist = []
    return alist


st.title("AnaLinA - Cheatsheet API")
img_list = []

nb = st.empty()
ar = st.empty()

opt = nb.radio("Suche nach: ", ["Woche", "Thema"], index = 1)
if opt == "Woche":
    ar.empty()
    woche = ar.selectbox("Woche: ", wochen, index=0)

    if woche != "-":
        img_list = remove_all(img_list)
        images = open_images(woche)
        for img in images:
            a = st.empty()
            a.image(img)
            img_list.append(a)

if opt == "Thema":
    ar.empty()
    name = ar.selectbox("Thema: ", ["-", *list(set(map_dict.values()))], index=0)
    if name != "-":
        img_list = remove_all(img_list)
        found_imgs = []
        for key, val in map_dict.items():
            if val == name:
                found_imgs.append(get_image("imgs/" + key))
        for img in found_imgs:
            a = st.empty()
            a.image(img)
            img_list.append(a)
