# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 13:20:38 2024

@author: USER
"""

import numpy as np


# Fonction pour déterminer la mention
def obtenir_note(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    else:
        return 'F'


# Demande le nombre d'étudiants et de matières
nombre_etudiants = int(input("Entrez le nombre d'étudiants: "))
nombre_matiere = int(input("Entrez le nombre de matières: "))

# Initialisation d'un tableau NumPy pour les notes
grades = np.zeros((nombre_etudiants, nombre_matiere))

# Saisie des notes pour chaque étudiant
for i in range(nombre_etudiants):
    print(f"Saisissez les notes pour l'étudiant {i + 1}:")
    for j in range(nombre_matiere):
        grades[i, j] = float(input(f"  Matière {j + 1}: "))

# Calcul des totaux, pourcentages et mentions
totals = np.sum(grades, axis=1)
percentages = (totals / (nombre_matiere * 100)) * 100  # Supposant que chaque matière est sur 100
grades_letters = np.array([obtenir_note(p) for p in percentages])

# Affichage des résultats
print("\n    Le résultat des étudiants:")
print(f"{'Étudiant':<10} {'Total':<10} {'Pourcentage':<10} {'Mention':<10}")
print("=" * 60)
for i in range(nombre_etudiants):
    print(f"{i + 1:<10} {totals[i]:<10} {percentages[i]:<15.2f} {grades_letters[i]:<10}")
