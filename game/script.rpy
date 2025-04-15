# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define y = Character('Yasmine', color="#000000")
define l = Character('Lena', color="#000000")
define h = Character('Harceleur', color="#000000")


#backgrounds
#school
image bg_classroom_day = "classroom_day.jpg"
image bg_classroom_evening = "classroom_evening.jpg"
image bg_classroom_night_lightOff = "classroom_night_lightOff.jpg"
image bg_classroom_night_lightOn = "classroom_night_lightOn.jpg"
image bg_frontGate_day = "frontGate_day.jpg"
image bg_frontGate_evening = "frontGate_evening.jpg"
image bg_frontGate_night = "frontGate_night.jpg"
image bg_courtyard_day = "courtyard_day.jpg"

#roadToSchool
image bg_roadToSchool_day = "roadToSchool_day.jpg"
image bg_roadToSchool_evening = "roadToSchool_evening.jpg"
image bg_roadToSchool_night = "roadToSchool_night.jpg"

#backstreets
image bg_backstreets_day = "backstreets_day.jpg"
image bg_backstreets_evening = "backstreets_evening.jpg"
image bg_backstreets_night = "backstreets_night.jpg"

#bedroom
image bg_bedroom_day = "bedroom_day.jpg"
image bg_bedroom_night_lightOff = "bedroom_night_lightOff.jpg"
image bg_bedroom_night_lightOn = "bedroom_night_lightOn.jpg"
image bg_bedroom_afterSchool = "bedroom_afterSchool.jpg"


#living room
image bg_livingRoom_day = "livingRoom_day.jpg"
image bg_livingRoom_evening = "livingRoom_evening.jpg"
image bg_livingRoom_night_lightOff = "livingRoom_night_lightOff.jpg"
image bg_livingRoom_night_lightOn = "livingRoom_night_lightOn.jpg"

#ruins
image bg_ruins_start = "ruins_start.jpg"
image bg_ruins_corridor = "ruins_corridor.jpg"
image bg_ruins_end = "ruins_end.jpg"
image bg_ruins_outside = "ruins_outside.jpg"


#park
image bg_park_day = "park_day.jpg"
image bg_park_evening = "park_evening.jpg"
image bg_park_night = "park_night.jpg"
#ending
image bg_black_screen = "black.jpg"


#screenshake
transform shake_bg:
    linear 0.05 xoffset -10  # Déplace légèrement à gauche
    linear 0.05 xoffset 10   # Déplace légèrement à droite
    linear 0.05 xoffset -5   # Retourne légèrement à gauche
    linear 0.05 xoffset 5    # Retourne légèrement à droite
    linear 0.05 xoffset 0    # Revient à la position initiale




#resize character
transform size_normal:
    ysize 600
    fit "contain"


#character positions 
transform left: 
    xalign 0.0
    yalign 0.3
    zoom (0.5)

transform right: 
    xalign 1.0
    yalign 0.3
    zoom (0.5)

transform center: 
    zoom (0.5)
    yalign 0.3
    xalign 0.5


# Le jeu commence ici
label start:

    "Cette oeuvre est un travail de fiction. Toute ressemblance à des personnes ou des événements est totalement fortuite."
    "Si vous êtes témoin de toute forme d'harcèlement ou de cyberharcèlement, ne laissez pas faire ces actions et contactez les autorités compétentes."

    scene bg_bedroom_afterSchool with fade
    
    return
