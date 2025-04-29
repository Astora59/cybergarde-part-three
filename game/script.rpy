# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
# ex: image eileen heureuse = "eileen_heureuse.png"

# Déclarez les personnages utilisés dans le jeu.
define y = Character('Yasmine', color="#000000")
define l = Character('Lena', color="#000000")
define h1 = Character('Harceleur 1', color="#000000")
define h2 = Character('Harceleur 2', color="#000000")
define h3 = Character('Harceleur 3', color="#000000")
define cpe = Character('CPE', color="#000000")


#characters
image Lena_afraid = "Lena_afraid.png"
image Lena_angry = "Lena_angry.png"
image Lena_annoyed = "Lena_annoyed.png"
image Lena_anxious = "Lena_anxious.png"
image Lena_default = "Lena_default.png"
image Lena_explaining = "Lena_explaining.png"
image Lena_sad = "Lena_sad.png"
image Lena_happy = "Lena_happy.png"

image Lena_angry_sleeves = "Lena_angry_sleeves.png"
image Lena_sad_sleeves = "Lena_sad_sleeves.png"


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
image bg_cpe_day = "bg_cpe_day.jpg"

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

default lena_trust = 0
default harcelement = False
default harceleur = False
default ignorer = False
default indice = 0

# Le jeu commence ici
label start:

    "Cette oeuvre est un travail de fiction. Toute ressemblance à des personnes ou des événements est totalement fortuite."
    "Si vous êtes témoin de toute forme d'harcèlement ou de cyberharcèlement, ne laissez pas faire ces actions et contactez les autorités compétentes."

    scene bg_bedroom_afterSchool with fade
    play music "audio/Evening.mp3" loop fadeout 1.0
    "La chambre de Yasmine respire la douceur et la personnalité : des murs tapissés de posters de groupes de musique, des illustrations colorées, des étoiles phosphorescentes collées au plafond. Un léger parfum de vanille flotte dans l’air."
    "Lena est affalée sur le lit, le dos contre les coussins. Ses épaules sont affaissées, son regard un peu perdu. Elle tient son téléphone entre les doigts, mais ne le regarde pas vraiment."
    y "Mhhhh... Est-ce que je devrais me débarasser de ce haut..."
    "Yasmine était tellement absorbée par le tri de ses vêtements qu'elle en oublia son amie."
    y "Lena ma belle ! Tu viens choisir une tenue pour la rentrée avec moi ?"
    show Lena_anxious at center
    l "Ouais... Si tu veux."
    y "T'as l'air fatiguée, est-ce que ça va ?"
    "Lena semblait absente, le regard vide tournait vers l'écran de son téléphone."
    l "Ouais, ouais… juste un peu crevée."
    play music "audio/Brady.mp3"
    "On aurait dit que le monde s'écroulait sur Lena. Ce n'est pas normal. Elle est si enjouée d'habitude."

    menu :
        "Insister gentiment":
            $ lena_trust += 1
            jump insister
        "Changer de sujet":
            jump changerSujet
    
label insister:
    "Yasmine pose les vêtements sur son lit et s’assoit doucement à côté de Lena. Elle fronce légèrement les sourcils, visiblement préoccupée, mais garde une voix douce."
    y "Tu es sûre ? T’es pas comme d’habitude… Tu veux en parler ?"
    "Lena hausse les épaules, le regard toujours fuyant. Elle serre un peu plus son téléphone, comme pour s’y accrocher."
    l "C’est rien, vraiment."
    "Yasmine pose une main légère sur l’avant-bras de son amie."
    y "Tu sais que je suis là, hein ?"
    "Un léger silence suit, mais cette fois Lena tourne la tête vers elle. Son visage se détend, juste un peu."
    hide Lena_anxious
    show Lena_default at center
    "Ouais, je sais… Merci."

    jump chapter2

label changerSujet:
    "Yasmine hésite un instant, puis attrape son ordinateur portable posé sur le bureau."
    y "Bon, et si on regardait les nouvelles collections en ligne ? Peut-être qu’on trouvera nos tenues parfaites pour la rentrée."
    "Lena relève enfin la tête, visiblement soulagée par ce changement de ton."
    hide Lena_anxious
    show Lena_default at center
    l "Ouais, bonne idée."
    "Elles se rapprochent autour de l’écran, commentant les vêtements avec entrain."
    "Pourtant, un petit voile de tristesse reste accroché au regard de Lena. Elle rit, mais son esprit semble ailleurs."

    jump chapter2



label chapter2:
    scene bg_courtyard_day with fade
    play music "audio/Morning.mp3" fadeout 1.0 loop
    "La cour est animée de rires, de cris et de pas précipités. Pourtant, au milieu de cette agitation, Lena est seule, dos contre un mur, les bras croisés."
    "Son sac repose à ses pieds. Elle garde la tête baissée, son visage à moitié dissimulé par ses mèches."
    "Un groupe de trois élèves plus âgés s’approche de Lena."
    "Ils se placent en arc de cercle autour d’elle, comme des vautours."
    play music "audio/Symmetry.mp3" fadeout 1.0 loop
    h1 "Alors Lena, c’était bien les vacances ? T’as bien profité des garçons ?"
    h2 "Tout le monde a vu tes talents, en tout cas..."
    h3 "T’es qu’une pute, franchement."
    show Lena_sad at center
    "Lena serre les poings. Son corps se crispe. Elle ne répond pas, les dents serrées, les yeux fixés au sol."
    "Yasmine est témoin de la scène. Pourquoi tout un groupe semble mettre mal à l'aise Lena ?"
    "Que doit faire Yasmine ?"

    menu:
        "Défendre Lena":
            $ lena_trust += 1
            $ harcelement = True
            jump defendreLena

        "Ignorer la scène":
            $ lena_trust -= 1
            $ harcelement = False
            $ ignorer = True

            jump ignorerLena

        "Se moquer avec les harceleurs":
            $ lena_trust -= 3
            $ harcelement = False
            $ harceleur = True

            jump harcelerLena

label defendreLena:
    play music "audio/Hot Pursuit.mp3" fadeout 1.0 loop
    "Yasmine, témoin de la scène à quelques mètres, serre les dents."
    "Son cœur bat plus vite. Elle se fraye un chemin entre les élèves et s’interpose, regard brûlant d’indignation."
    y "Vous êtes sérieux ? Vous avez que ça à faire ?!"
    h1 "Oh, la petite héroïne veut sauver sa copine ?"
    "Yasmine prend la main de Lena."
    y "Viens, on s’en va."
    "Lena hésite, comme si ses jambes refusaient de bouger… puis elle se redresse et suit Yasmine en silence."
    l "Merci..."

    jump chapter3

label ignorerLena:
    play music "audio/Echoes_of_Time.mp3" fadeout 1.0 loop
    "Yasmine détourne le regard, faisant mine de consulter son téléphone."
    "Elle fait quelques pas en arrière, laissant la scène se poursuivre."
    "Le regard de Yasmine croise brièvement celui de Lena, avant que Yasmine ne décide de détourner les yeux et de partir."
    "Le groupe rit de plus en plus fort. Lena reste figée, plus seule que jamais."

    jump chapter3

label harcelerLena:
    play music "audio/Echoes_of_Time.mp3" fadeout 1.0 loop
    "Yasmine s’approche avec un sourire malaisant. Elle tente de se fondre dans le groupe, le ton moqueur."
    y "Bah alors Lena on essaie de draguer trois gars en même temps ?"
    "Les éclats de rire des trois jeunes hommes rassurent Yasmine."
    "Elle se sent acceptée, validée. Peut-être cherche-t-elle à se protéger socialement, au prix de sa propre humanité."
    hide Lena_sad
    show Lena_afraid at center
    "Lena semble avoir le souffle coupée. Son regard est livide, complètement abattue par le fait que sa propre amie la trahisse."
    "Lena ramasse son sac, les mains tremblantes. Elle s'éloigne du groupe, seule."
    "Une fois le silence retombé, Le regard de Lena était encore gravé dans la rétine de Yasmine. Qu'avait-elle donc fait ?"
    h1 "Yasmine je savais pas que t'étais aussi drôle... Faut qu'on y aille, mais ravi d'avoir pu rigoler un bon coup avec toi !"
    "La tumulte se dissipe avec la fin de la récréation, et chaque élève retourne vers sa classe."

    jump chapter3

label chapter3 :
    scene bg_classroom_day with fade
    play music "audio/Covert_Affair.mp3" fadeout 1.0 loop
    "Les élèves écrivent, la craie crisse au tableau. Le soleil tape fort à travers les vitres. Pourtant, Lena porte un large pull en col roulé."
    "Yasmine, assise à côté, l’observe du coin de l’œil."
    "Lorsque Lena soulève la manche pour écrire, une série de fines cicatrices pâles se dévoile un instant sur son avant-bras. Yasmine retient sa respiration."
    "Que doit-elle faire ?"
    menu:
        "En parler directement avec Lena":
            $ lena_trust += 1
            jump enParler
        "Espionner son téléphone":
            $ indice += 1
            jump espionner

        "Ne rien faire":
            $ lena_trust -= 1
            jump rienFaire

            
label enParler:
    scene bg_classroom_evening with dissolve
    play music "audio/Evening.mp3"
    "À la sortie du cours, Yasmine attrape doucement le bras de Lena."
    y "Lena… c’est quoi sur ton bras ?"
    "Lena tire brutalement sa manche, évitant le regard de Yasmine."

    if harceleur == True:
        show Lena_angry_sleeves at center
        l "Qu'est-ce que ça peut bien te faire ? Ca t'a bien fait rire de te moquer de moi non ?"
        "Yasmine ne peut pas rétorquer. Elle sait qu'elle a tort."
    else:
        show Lena_sad_sleeves at center
        l "C'est rien."
        y "Lena, s’il te plaît… c’est à cause d’eux ?"
        "Un long silence. Puis Lena hoche lentement la tête."
        y "Tu sais que je serai toujours là pour toi peu importe ce qu'il se passe, je veux être ton rocher."
        if ignorer == True:
            l "Euh ouais c'est ça..."
            "Lena n'est pas convaincue."
        else:
            l "T'es une personne en or. Merci Yasmine, vraiment."

    "Lena s'enfonce dans les couloirs, rejoignant la masse d'élèves se dirigeant vers la sortie."

    jump chapter4


label espionner:
    "Pendant que Lena va aux toilettes, Yasmine jette un oeil dans le sac de Lena."
    "Elle cherche un indice, n'importe lequel, qui pourrait l'aider à comprendre la situation."
    "Son regard se pose sur le téléphone de Lena, l'écran d'accueil contient plusieurs notifications."
    "\"T'es une traînée, meurs.\""
    "\"On a tous vu tes photos tchoin.\""
    "Yasmine pâlit. L'ampleur du harcèlement dépasse ce qu'elle imaginait."
    "Avant que Lena ne revienne, Yasmine se remet tranquillement à sa place."



    jump chapter4
label rienFaire:
    scene bg_classroom_evening with dissolve
    play music "audio/Evening.mp3"

    "Yasmine reste figée. Elle ne dit rien, détourne le regard."
    if harceleur == True:
        "Comment pouvait-elle faire quoi que ce soit après ce qu'elle avait dit ?"
        "Entrer en opposition avec Lena était la pire idée."
        "Elle n'aurait pas dû se moquer."
    else: 
        "Aucun mot ne lui vient en tête, aucune action, rien."
        "Son amie allait mal et Yasmine était figée."
        "Peut-être qu'elle ne la considère pas tant que ça comme une amie, se dit-elle."
        "Si ça avait été le cas, elle se donnerait plus pour l'aider."

    "Lena, quant à elle, s'enfonce encore un peu plus dans le silence et l'isolement."

    jump chapter4


label chapter4:
    scene bg_bedroom_night_lightOn with fade
    play music "audio/Late Night Radio.mp3" fadeout 1.0 loop
    "Assise à son bureau, lumière tamisée, Yasmine tape frénétiquement sur son clavier."
    "La pluie claque contre la vitre. Elle veut comprendre. Elle veut agir."
    "Elle réfléchit à un moyen de mener l'enquête..."

    menu:
        "Demander à Lena directement":
            $ lena_trust += 1
            jump demanderDirect
        "Chercher sur les réseaux sociaux":
            $ indice += 1
            jump rechercheReseaux
        "Ne pas chercher à comprendre":
            $ lena_trust -= 1
            jump nePasComprendre


label demanderDirect:
    "Yasmine décide d'inviter Lena chez elle."
    "Après un moment d'hésitation, elle ose poser la question."
    y "Je veux comprendre. Tu peux me dire ce qu'il s'est passé ? Je promets de ne pas te juger, je suis là pour toi."
    "Lena éclate aux sanglots. Yasmine accourt à ses côtés afin de la soutenir."
    "Après un moment dans ses bras, Lena se calme enfin."
    show Lena_sad_sleeves at center
    play music "audio/Brady.mp3" fadeout 1.0 loop
    l "Il y a un garçon que j'aimais beaucoup pendant les vacances, un peu plus vieux que moi..."
    "Yasmine écoute avec attention."
    l "Il était très gentil avec moi, et on se parlait beaucoup. Quand les vacances se sont terminés, on a échangé nos réseaux sociaux."
    l "Tout se passait bien, puis il a demandé des photos intimes de moi..."
    "Le choc s'empare de Yasmine, comment ose-t-il ?"
    l "J'étais naïve, alors je lui ai envoyé. Après ça tout a changé : il était horrible avec moi, me faisait du chantage. Sa gentillesse était une facade."
    l "Après ça, il m'a ordonné de prendre plus de photos, sinon il allait les diffuser sur internet. Et par peur, j'ai obéi à ses ordres."
    l "Il y a eu un moment où il ne me parlait plus et je pensais être tranquille. Sauf que d'un coup, il m'envoie un lien vers un groupe Echord."
    l "En rejoignant le groupe, je me rends compte qu'il a déjà diffusé les photos à des centaines de personnes sur le groupe. Tous rigolaient, me sexualisaient, m'harcelaient..."
    l "Maintenant, ils ont mon adresse, là où j'étudie, et me menacent... Je ne sais pas quoi faire. L'harcèlement va jusque dans l'école, comme tu as pu voir."
    "Yasmine est bouche bée. Elle ne se rendait pas compte de la gravité de la situation."
    "Avoir à souffrir silencieusement, seule... Yasmine était admirative du courage de Lena."

    jump chapter5

label rechercheReseaux:
    play music "audio/Covert_affair.mp3"
    "Yasmine décide de mener son enquête sur les réseaux sociaux"
    "Elle se rend sur le compte de Lena, des indices doivent forcément s'y trouver."
    "Yasmine parcourt les profils, fouille les commentaires."
    "C'est là qu'elle aperçoit des commentaires suspects."
    "Plusieurs comptes qui harcèlent Lena dans les commentaires. Sur certaines photos de profil, elle peut reconnaître les harceleurs de son collège."
    "D'autres comptes quant à eux, reprennent des photos de Lena en les modifiant dans des situations compromettantes. Des scènes dénudées mais pas que."
    "Les commentaires sont remplis de haine et de moqueries. Certains sont si violents que l'estomac de Yasmine se retourne."
    "Elle pouvait voir une fraction de la souffrance de Lena. Ce qu'elle doit vivre au quotidien est horrible."

    jump chapter5

label nePasComprendre:
    "Si elle y réfléchit bien, qu'est-ce qu'elle pouvait bien faire dans cette situation ?"
    if indice == 1:
        "Lena est seule, face à plusieurs d'harceleurs."
    "Yasmine ne peut pas aider son amie. C'est ce qu'elle s'était convaincue."
    "Elle éteint son ordinateur. La pluie continue de tomber. Plus forte, presque en colère."
    "La jeune fille ne pense pas pouvoir faire quoi que ce soit pour Lena. Comment pouvait-elle ? Elle sait qu'elle est lâche."
    "Elle pourrait en parler à un adulte de confiance, mais elle a peur."
    "Peur de quoi ? Des représailles ? De sortir du moule ? D'aider son amie ?"
    "Yasmine se pose 1001 questions, avec pour seule réponse le silence de sa chambre."
    scene bg_bedroom_night_lightOff
    "Yasmine part se coucher pour affronter une nouvelle journée demain."
    jump chapter5
    
label chapter5:
    scene bg_frontGate_day with fade
    play music "audio/Morning.mp3"
    "Yasmine se tient devant le portail de son école. Les événements de ces derniers jours la hantent encore."
    "Aujourd'hui il fallait prendre une décision. Elle ne peut pas continuer comme ça plus longtemps."

    menu:
        "Soutenir Lena et prévenir un adulte":
            $ lena_trust += 1
            jump soutenirLena
        
        "Se venger en attaquant le garçon sur les réseaux" if indice == 2:
            jump seVenger
        
        "Abandonner Lena":
            $ lena_trust -= 1
            jump trahirLena

label soutenirLena:
    "Il lui était impossible de rester éternellement dans le silence. Yasmine doit agir."
    if harceleur == True:
        "C'est vrai, elle a rejoint les harceleurs pour se moquer de Lena. Mais elle ne veut pas que cette erreur définisse la personne qu'elle est."
        "Elle sait qu'elle a un bon fond et qu'elle aime Lena. C'était une erreur de sa part."
    "Son amie avait besoin d'aide. Et elle ferait tout pour l'aider."
    "Il est temps d'arrêter de garder tout ça entre eux. Les adultes pourraient les aider à résoudre la situation."
    "Lena s'approche du portail de l'école. Ses yeux sont absents de toute étincelle de vie. Un sombre mélange d'émotions semble écrasé la jeune fille."
    y "Lena ! Suis-moi s'il te plait, je ne peux plus te voir comme ça."
    show Lena_sad_sleeves at center
    l "..."
    "Lena ne prononce aucun mot."
    "Yasmine prend la main de Lena, elle compte se diriger au bureau du CPE."

    scene bg_cpe_day with dissolve
    "Dans la salle des bureaux du corps éducatif, Yasmine et Lena se tiennent devant le bureau de leur CPE."
    cpe "Merci d’être venues me parler. Vous avez bien fait."
    show Lena_sad_sleeves at center
    l "Je… je voulais pas causer de problèmes."
    y "Tu n’en causes pas. Ceux qui t’ont fait ça sont les seuls responsables."
    cpe "Nous allons agir immédiatement. La police sera informée, et les élèves responsables seront sanctionnés."

    scene bg_courtyard_day with fade
    "Dans la cour du collège, Lena et Yasmine sont à nouveau ensemble."

    l "Merci, Yasmine. Sans toi… je sais pas où j’en serais."
    if harceleur == True:
        y "Je tiens vraiment à m'excuser pour le comportement que j'ai eu il y a quelques temps. Je ne savais vraiment pas comment agir dans la situation et j'ai pris la pire décision."
        if lena_trust == 1:
            l "C'est pas grave vraiment. Je t'ai déjà pardonné. Peu de gens auraient su quoi faire dans la situation."
        else:
            l "Ne refais plus jamais ça. Je ne comptais plus te parler."
    "Enfin les deux collégiennes peuvent aller de l'avant. Dans ce genre de situations, il est important de parler à un adulte de confiance."
    "L'harcelement qu'a subi Lena ne disparaitra pas du jour au lendemain. Cependant, c'est un premier pas vers l'arrêt de l'harcelement et vers la guérison de Lena."
    l "Tu crois que tout se passera bien."
    y "J'en suis persuadée. Et je serai toujours là pour toi."

    scene bg_black_screen with fade:
        xalign 0.5
        yalign 0.2
        zoom 2.0
    centered "Parler, c’est briser le silence.\nUn simple soutien peut sauver une vie."
    centered "{size=+75}{cps=8}{color=#ffffff}CRÉDITS{/color}{/cps}{/size}{p=5.0}{nw}"
    centered "{size=+75}{cps=8}{color=#ffffff}Scénario: Étudiants de Louise Michel{/color}{/cps}{/size}{p=5.0}{nw}"
    centered "{size=+75}{cps=8}{color=#ffffff}programmation: Vegacy{/color}{/cps}{/size}{p=5.0}{nw}"

    return

label seVenger:
    "Yasmine ne supporte pas l’injustice. Elle décide de rendre coup pour coup."
    "Elle fait demi-tour, finalement pour se rendre chez elle."
    
    scene bg_bedroom_day with fade
    play music "audio/Symmetry.mp3" fadeout 1.0 loop
    "Une fois arrivée chez elle, Yasmine allume son ordinateur."
    "Si personne ne peut aider Lena, elle le fera. Et à sa manière."
    "Elle utilise ses réseaux pour exposer les harceleurs, publier leur nom, des captures de leurs commentaires..."
    "Yasmine reprend les techniques des harceleurs : des montages de leur visage, des commentaires les insultant. Elle veut combattre le feu par le feu."

    scene bg_bedroom_night_lightOn with fade
    "Cela fait plusieurs jours que Yasmine rend justice à Lena."
    "Le fait-elle vraiment pour Lena ? Au fond d'elle, elle sait qu'elle aime les messages qu'elle envoie."
    "Chaque menace et chaque insulte qu'elle vocifère lui procure le plus grand bien. Chaque montage ou deepfake qu'elle crée la fait rire aux éclats."
    "Les réactions sont partagées. Certains la soutiennent, d'autres l’accusent de cyberharcèlement."
    "Mais ils ne peuvent pas comprendre. Comment pouvait-il ? Ce n'était pas leur amie qui se faisait harceler."
    "Les réactions sont partagées. Certains la soutiennent, d'autres l’accusent de cyberharcèlement."
    "Lena quant à elle, n'a pas réagi à ce que faisait Yasmine."
    "Dans sa chasse aux sorcières, Yasmine n'a pas pensé à contacter Lena."
    if harceleur == True:
        "Peut-être qu'elle se jettait corps et âme dans le cyberharcèlement des harceleurs pour se racheter."
        "Yasmine sait que ce qu'elle a fait est mal. La culpabilité l'étouffe."
    "Ce n'est qu'une question de temps avant que Yasmine ne se fasse convoquer pour son cybeharcèlement..."

    scene bg_black_screen with fade:
        xalign 0.5
        yalign 0.2
        zoom 2.0
    centered "Se venger par le cyberharcèlement, c’est choisir de blesser au lieu de guérir — tu ne répares rien, tu reproduis ce qui a détruit."
    centered "{size=+75}{cps=8}{color=#ffffff}CRÉDITS{/color}{/cps}{/size}{p=5.0}{nw}"
    centered "{size=+75}{cps=8}{color=#ffffff}Scénario: Étudiants de Louise Michel{/color}{/cps}{/size}{p=5.0}{nw}"
    centered "{size=+75}{cps=8}{color=#ffffff}programmation: Vegacy{/color}{/cps}{/size}{p=5.0}{nw}"

label trahirLena:
    stop music
    scene bg_classroom_day with fade
    "Yasmine évite le regard de Lena toute la journée."
    "Elle fait comme si de rien n'était. Comme si tout ce qu'elle sait n'exister pas."
    "Elle ne veut pas s'impliquer. Trop lourd. Trop dangereux."
    "Elle se convainc que ce n'est pas son rôle. Que quelqu’un d’autre finira bien par faire quelque chose."
    "Petit à petit, Yasmine s'éloigne de Lena, la laissant plus seule que jamais."

    scene bg_bedroom_night_lightOff with dissolve
    "Le soir venu, Yasmine est allongée sur son lit. Le silence est pesant."
    "La pluie recommence à tomber, mais cette fois, elle ne trouve aucun apaisement dans son bruit."
    "Elle se sent vide. Et lâche."

    scene bg_black_screen with fade:
        xalign 0.5
        yalign 0.2
        zoom 2.0
    centered "Se taire, c’est laisser la peur gagner — face au cyberharcèlement, chaque silence est une complicité de trop."
    centered "{size=+75}{cps=8}{color=#ffffff}CRÉDITS{/color}{/cps}{/size}{p=5.0}{nw}"
    centered "{size=+75}{cps=8}{color=#ffffff}Scénario: Étudiants de Louise Michel{/color}{/cps}{/size}{p=5.0}{nw}"
    centered "{size=+75}{cps=8}{color=#ffffff}programmation: Vegacy{/color}{/cps}{/size}{p=5.0}{nw}"


    return
