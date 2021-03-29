# Oxymètre de flux

Tous les fichiers utilisés lors de notre projet de création d'un oxymètre de flux (dans le cadre du cours travaux pratiques d'optique photonique I) se trouvent dans ce répertoire.

**Attention**, les *paths* utilisés sont absolus puisque je ne sais pas utiliser des *relative paths...*, je vais l'apprendre un jour, promis.

## CSV

Les fichiers csv correspondent aux données enregistrées à l'oscilloscope. Nous avons réalisé 10 essais numérotés de 0 à 9.

## C++

Deux fichiers en C++ sont présents dans le répertoires. "oximetre.ino" est notre premier essai, où nous essayons d'analyser les données en temps réel. 
"oximetre_LED.ino" est le script qui permet seulement d'allumer les LED en alternance, puisqu'il était trop difficile de faire l'analyse en temps réel.

## python

4 scripts python sont présents dans le répoertoire:
- analyse_data.py analyse de façon automatisée les données enregistrées sur l'oscilloscope et imprime dans le terminal le pouls et le taux d'oxygénation de chaque essai.
- echelle_bad.py a été utilisé pour générer une figure qui montre la mauvaise échelle choisie à l'oscilloscope (pour le rapport)
- figure.py génère des figures pour le pouls et le taux d'oxygénation en fonction de l'essai et compare les résultats expérimentaux aux mesures de l'oxymètre comemrcial (données de référence)
- incertitude.py calcule l'incertitude sur le taux d'osygénation

Le répertoire contient aussi diverses figures et des pdf.
