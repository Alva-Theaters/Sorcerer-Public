# SPDX-FileCopyrightText: 2025 Alva Theaters
#
# SPDX-License-Identifier: GPL-3.0-or-later

from bpy import spy


class COMMON_LG_american_english(spy.types.Language):
    as_idname = 'american_english'
    as_label = "American English"
    as_description = "American English"

    from ..assets.tooltips import default_tooltips
    tooltips = default_tooltips


class COMMON_LG_spanish(spy.types.Language):
    as_idname = 'spanish'
    as_label = "Spanish"
    as_description = "The Spanish language"

    tooltips = { # Translation provided by ChatGPT (GPT-4o) last on 12/15/2024.
        # Object Only
        "mute": "Silenciar la salida OSC de este objeto",
        "summon_movers": "Texto de línea de comando para enfocar luminarias móviles en el objeto del escenario",
        "erase": "Borrar en lugar de añadir",
        "speaker_number": (
            '''Número del altavoz en Qlab o en el mezclador de sonido. Estás viendo esto aquí porque seleccionaste un objeto Altavoz, '''
            '''y los objetos altavoz representan altavoces físicos reales en tu teatro para el propósito de audio espacial. Para '''
            '''mover micrófonos a la izquierda o derecha, no se usa un codificador; simplemente mueve el micrófono u objeto de sonido '''
            '''más cerca a la izquierda o derecha en la vista 3D'''
        ),
        "sound_source": "Selecciona una pista de sonido en el secuenciador o un micrófono en el Patch de Audio",

        # Lighting Parameters
        "intensity": "Valor de intensidad",
        "strobe": "Valor de estroboscopio",
        "color": (
            "Valor de color. Si tu luminaria no es RGB, sino CMY, RGBA o algo similar, "
            "Sorcerer traducirá automáticamente RGB al perfil de color correcto. La mejor manera de indicar "
            "a Sorcerer qué perfil de color usar es aquí en el controlador del objeto, a la derecha de este campo. "
            "Para realizar cambios masivos, usa la función mágica 'Perfil a Aplicar' en la esquina superior izquierda de este cuadro "
            "o el botón 'Aplicar Parche a Objetos en la Escena' al final del parche del grupo debajo de este panel."
        ),
        "color_restore": (
            "¿Por qué hay 2 colores para esto? Porque hacer cambios relativos remotamente al color no funciona bien. "
            "Los influenciadores usan cambios relativos para todo excepto para el color por esta razón. Este segundo selector de color "
            "elige el color al que el influenciador restaurará los canales después de pasar por encima."
        ),
        "pan": "Valor de paneo",
        "tilt": "Valor de inclinación",
        "zoom": "Valor de zoom",
        "iris": "Valor de iris",
        "edge": "Valor de borde",
        "diffusion": "Valor de difusión",
        "gobo": "Valor de ID de gobo",
        "speed": "Valor de velocidad de rotación del gobo",
        "prism": "Valor de prisma",

        # Audio Parameters
        "volume": "Intensidad/valor del micrófono del objeto del escenario",

        # Common Header
        "manual_fixture_selection": (
            "En lugar del selector de grupo a la izquierda, simplemente escribe lo que deseas controlar aquí. Escribe los "
            "canales que quieres o no quieres en lenguaje sencillo."
        ),
        "selected_group_enum": (
            '''Elige una luminaria para controlar. Usa ya sea los Grupos de Iluminación estáticos o la ubicación de la malla '''
            '''en relación con otras mallas para una selección espacial dinámica (Dinámico).'''
        ),
        "selected_profile_enum": (
            '''Elige un perfil de luminaria para aplicar a esta luminaria y a cualquier otra luminaria seleccionada. Para copiar '''
            '''configuraciones directamente de otra luz, selecciona las luces a las que quieres copiar, luego selecciona la luz '''
            '''de la que quieres copiar y luego selecciona la opción Dinámico aquí.'''
        ),
        "color_profile_enum": "Elige un perfil de color para la malla basado en el parche en la consola de iluminación",
        "freezing_mode_enum": "Elige si renderizar en todos los fotogramas, cada dos fotogramas o cada tres fotogramas",
        "solo": (
            "Silencia todos los controladores excepto este y cualquier otro con solo también activado. Borra todos los solos con el "
            "botón en el menú de Reproducción en el encabezado de la Línea de Tiempo."
        ),

        # Object Only
        "absolute": (
            "Habilita el modo absoluto. En modo absoluto, el objeto puede animar los canales dentro de él mientras están dentro. " 
            "Con esto desactivado, los canales solo serán cambiados por el influenciador cuando este entre y salga, no solo "
            "porque haya datos de curvas de animación. Con esto desactivado, el influenciador está en modo relativo y puede trabajar "
            "encima de otros efectos."
        ),
        "strength": (
            "Si disminuyes la fuerza, actuará como un pincel. Si mantienes esto al máximo, actuará más como un objeto que pasa a través "
            "de las luces y las reinicia al salir."
        ),
        "sem": (
            '''Si esto no es cero, se comportará como un canal "SEM" en ETC Eos. Úsalo para animar la traslación '''
            '''de objetos en Augment3D. Esto incluye parcheo remoto también. Para conectar un objeto 3D en Augment3D a este '''
            '''canal, ve a la pestaña derecha en el editor de A3D y arrastra el modelo sobre el canal SEM para vincularlo. '''
            '''Eos no los posicionará automáticamente juntos.'''
        ),

        # Mins and maxes
        "strobe_min": "Valor mínimo para el estroboscopio en la luminaria",
        "strobe_max": "Valor máximo para el estroboscopio en la luminaria",
        "white_balance": (
            '''Si el blanco natural no es realmente blanco, ajusta aquí para que el blanco en el selector de color de Blender '''
            '''sea realmente blanco.'''
        ),
        "pan_min": "Valor mínimo para el paneo en la luminaria",
        "pan_max": "Valor máximo para el paneo en la luminaria",
        "tilt_min": "Valor mínimo para la inclinación en la luminaria",
        "tilt_max": "Valor máximo para la inclinación en la luminaria",
        "zoom_min": "Valor mínimo para el zoom en la luminaria",
        "zoom_max": "Valor máximo para el zoom en la luminaria",
        "speed_min": "Valor mínimo para la velocidad de rotación del gobo en la luminaria",
        "speed_max": "Valor máximo para la velocidad de rotación del gobo en la luminaria",

        # Toggles
        "enable_audio": "El audio está habilitado cuando está marcado",
        "enable_microphone": "El volumen del micrófono está vinculado a la Intensidad cuando está en rojo",
        "enable_pan_tilt": "El paneo/inclinación está habilitado cuando está marcado",
        "enable_color": "El color está habilitado cuando está marcado",
        "enable_diffusion": "La difusión está habilitada cuando está marcada",
        "enable_strobe": "El estroboscopio está habilitado cuando está marcado",
        "enable_zoom": "El zoom está habilitado cuando está marcado",
        "enable_iris": "El iris está habilitado cuando está marcado",
        "enable_edge": "El borde está habilitado cuando está marcado",
        "enable_gobo": "El gobo está habilitado cuando está marcado",
        "enable_prism": "El prisma está habilitado cuando está marcado",

        # Enable/Disable Arguments
        "simple_enable_disable_argument": "Añade # para el ID del grupo",
        "gobo_argument": "Añade # para el ID del grupo y $ para los datos de animación",

        # Orb Executors
        "event_list": "Debe ser el número de la lista de eventos que has creado en la consola para esta canción",
        "cue_list": "Debe ser el número de la lista de cues que has creado en la consola para esta canción",
        "start_cue": (
            '''Especifica qué cue iniciará (o habilitará) el reloj de código de tiempo. No puede ser el mismo que el primer cue '''
            '''en la secuencia de Blender, ya que eso creará un bucle.'''
        ),
        "end_cue": "Especifica qué cue detendrá (o deshabilitará) el reloj de código de tiempo",
        "start_macro": "Macro universal usada para varias actividades iniciales",
        "end_macro": "Macro universal usada para varias actividades finales",
        "start_preset": "Preset universal usado para varias actividades iniciales",
        "end_preset": "Preset universal usado para varias actividades finales",

        # View3D Operators
        "alva_object.duplicate_object": "Duplicar y Deslizar",
        "duplicate_columns": "(untranslated)",
        'duplicate_rows': "(untranslated)",

        # Scene Properties
        "is_parameter_bar_expanded": "Expande la barra de herramientas para ver más parámetros."
    }


class COMMON_LG_french(spy.types.Language):
    as_idname = 'french'
    as_label = "French"
    as_description = "The French language"

    tooltips = {  # Translation provided by ChatGPT (GPT-4o) last on 03/30/2025.
        # Object Only
        "mute": "Couper la sortie OSC de cet objet",
        "summon_movers": "Texte en ligne de commande pour orienter les projecteurs motorisés vers l'objet de la scène",
        "erase": "Effacer au lieu d’ajouter",
        "speaker_number": (
            "Numéro du haut-parleur dans Qlab ou sur la console audio. Vous voyez cela ici parce que vous avez sélectionné un objet Haut-parleur, "
            "et les objets haut-parleurs représentent les haut-parleurs physiques réels dans votre théâtre pour l'audio spatial. "
            "Pour faire un panoramique gauche/droite avec des micros, vous ne touchez pas à un encodeur, vous déplacez simplement le micro ou l'objet son "
            "vers la gauche ou la droite dans la vue 3D."
        ),
        "sound_source": "Sélectionnez soit une piste audio dans le séquenceur, soit un micro dans Audio Patch",

        # Lighting Parameters
        "intensity": "Valeur d’intensité",
        "strobe": "Valeur de stroboscope",
        "color": (
            "Valeur de couleur. Si votre projecteur n’est pas RGB mais CMY, RGBA ou autre, "
            "Sorcerer traduira automatiquement le RGB vers le bon profil de couleur. "
            "Le meilleur moyen d’indiquer à Sorcerer quel profil utiliser est ici, à droite de ce champ. "
            "Pour modifier plusieurs objets à la fois, utilisez la fonction magique 'Profil à appliquer' en haut à gauche de cette boîte, "
            "ou le bouton 'Appliquer le patch aux objets de la scène' en bas du groupe de patch."
        ),
        "color_restore": (
            "Pourquoi y a-t-il deux couleurs ici ? Parce que les modifications relatives de couleur à distance fonctionnent mal. "
            "Les influenceurs utilisent des modifications relatives pour tout sauf la couleur pour cette raison. "
            "Ce second sélecteur de couleur définit la couleur que l’influenceur appliquera à la fin de son passage."
        ),
        "pan": "Valeur de panoramique",
        "tilt": "Valeur d'inclinaison",
        "zoom": "Valeur de zoom",
        "iris": "Valeur d’iris",
        "edge": "Valeur de bord",
        "diffusion": "Valeur de diffusion",
        "gobo": "Identifiant du gobo",
        "speed": "Vitesse de rotation du gobo",
        "prism": "Valeur de prisme",

        # Audio Parameters
        "volume": "Intensité/valeur du micro de l’objet de scène",

        # Common Header
        "manual_fixture_selection": (
            "Au lieu du sélecteur de groupe à gauche, tapez simplement ce que vous voulez contrôler ici. "
            "Écrivez les canaux à inclure ou exclure en langage simple."
        ),
        "selected_group_enum": (
            "Choisissez les projecteurs à contrôler. Utilisez les Groupes d’éclairage statiques ou la position du mesh "
            "par rapport aux autres pour une sélection spatiale dynamique (Dynamique)."
        ),
        "selected_profile_enum": (
            "Choisissez un profil de projecteur à appliquer à ce projecteur et à tous les autres sélectionnés. "
            "Pour copier les paramètres d’un autre projecteur, sélectionnez ceux à copier, puis celui à copier depuis, "
            "puis sélectionnez l’option Dynamique ici."
        ),
        "color_profile_enum": "Choisissez un profil de couleur pour le mesh en fonction du patch dans la console d’éclairage",
        "freezing_mode_enum": "Choisissez de rendre à chaque frame, une frame sur deux, ou une frame sur trois",
        "solo": (
            "Coupe tous les contrôleurs sauf celui-ci et les autres avec le solo activé. "
            "Réinitialisez tous les solos avec le bouton dans le menu Lecture de l'en-tête Timeline."
        ),

        # Object Only
        "absolute": (
            "Activer le mode absolu. En mode absolu, l’objet peut animer les canaux à l’intérieur tant qu’ils y sont. "
            "Sinon, les canaux ne changent que lorsque l’influenceur entre ou sort. "
            "Ce mode relatif permet à l’influenceur de s'empiler sur d'autres effets."
        ),
        "strength": (
            "Réduire la force le fait agir comme un pinceau. À fond, il agit comme un objet traversant les lumières "
            "et les réinitialisant en partant."
        ),
        "sem": (
            "Si ce champ n'est pas zéro, il se comporte comme un canal « SEM » sur une console ETC Eos. "
            "Utilisez-le pour animer la translation d’objets dans Augment3D, y compris le patch à distance. "
            "Pour connecter un objet 3D dans Augment3D à ce canal, allez dans l’onglet de droite dans l’éditeur A3D "
            "et glissez le modèle sur le canal SEM. Eos ne les superposera pas automatiquement."
        ),

        # Mins and maxes
        "strobe_min": "Valeur minimale du stroboscope sur le projecteur",
        "strobe_max": "Valeur maximale du stroboscope sur le projecteur",
        "white_balance": (
            "Si le blanc naturel n’est pas vraiment blanc, corrigez-le ici pour que le blanc dans le sélecteur Blender "
            "soit un vrai blanc"
        ),
        "pan_min": "Valeur minimale du panoramique sur le projecteur",
        "pan_max": "Valeur maximale du panoramique sur le projecteur",
        "tilt_min": "Valeur minimale de l’inclinaison sur le projecteur",
        "tilt_max": "Valeur maximale de l’inclinaison sur le projecteur",
        "zoom_min": "Valeur minimale du zoom sur le projecteur",
        "zoom_max": "Valeur maximale du zoom sur le projecteur",
        "speed_min": "Vitesse minimale de rotation du gobo sur le projecteur",
        "speed_max": "Vitesse maximale de rotation du gobo sur le projecteur",

        # Toggles
        "enable_audio": "L’audio est activé si cette case est cochée",
        "enable_microphone": "Le volume du micro est lié à l’intensité si ce champ est rouge",
        "enable_pan_tilt": "Panoramique/Inclinaison activés si cette case est cochée",
        "enable_color": "Couleur activée si cette case est cochée",
        "enable_diffusion": "Diffusion activée si cette case est cochée",
        "enable_strobe": "Stroboscope activé si cette case est cochée",
        "enable_zoom": "Zoom activé si cette case est cochée",
        "enable_iris": "Iris activé si cette case est cochée",
        "enable_edge": "Bord activé si cette case est cochée",
        "enable_gobo": "Gobo activé si cette case est cochée",
        "enable_prism": "Prisme activé si cette case est cochée",

        # Enable/Disable Arguments
        "simple_enable_disable_argument": "Ajoutez # pour l’identifiant du groupe",
        "gobo_argument": "Ajoutez # pour l’ID de groupe et $ pour les données d’animation",

        # Orb Executors
        "event_list": "Numéro de la liste d’événements que vous avez créée sur la console pour cette chanson",
        "cue_list": "Numéro de la liste de cues que vous avez créée sur la console pour cette chanson",
        "start_cue": (
            "Spécifie quel cue démarre (ou active) l’horloge de timecode. "
            "Ne peut pas être le même que le premier cue dans Blender sinon cela créera une boucle"
        ),
        "end_cue": "Spécifie quel cue arrête (ou désactive) l’horloge de timecode",
        "start_macro": "Macro universelle utilisée pour les actions de démarrage",
        "end_macro": "Macro universelle utilisée pour les actions de fin",
        "start_preset": "Preset universel utilisé pour les actions de démarrage",
        "end_preset": "Preset universel utilisé pour les actions de fin",

        # View3D Operators
        "alva_object.duplicate_object": "Dupliquer et glisser. Facultatif : sélectionnez une courbe ou un cercle pour contraindre.",
        "duplicate_columns": "Nombre de colonnes supplémentaires à créer",
        "duplicate_rows": "Nombre de rangées supplémentaires à créer",

        # Scene Properties
        "is_parameter_bar_expanded": "Développer la barre d'outils pour voir plus de paramètres"
    }


class COMMON_LG_german(spy.types.Language):
    as_idname = 'german'
    as_label = "German"
    as_description = "The German language"

    tooltips = {
        # Object Only
        "mute": "Dieses Objekt stumm schalten (OSC-Ausgabe deaktivieren)",
        "summon_movers": "Kommandozeilentext, um bewegliche Scheinwerfer auf das Bühnenobjekt zu fokussieren",
        "erase": "Löschen statt hinzufügen",
        "speaker_number": (
            "Nummer des Lautsprechers in QLab oder auf dem Audio-Mischpult. Diese Einstellung erscheint, weil du ein "
            "Lautsprecher-Objekt ausgewählt hast. Lautsprecher-Objekte repräsentieren reale Lautsprecher im Theater "
            "für räumliches Audio. Um Mikrofone nach links oder rechts zu verschieben, nutzt du keinen Encoder – "
            "verschiebe einfach das Mikrofon oder Sound-Objekt im 3D-View nach links oder rechts."
        ),
        "sound_source": "Wähle entweder einen Sound-Streifen im Sequencer oder ein Mikrofon im Audio Patch",

        # Lighting Parameters
        "intensity": "Intensitätswert",
        "strobe": "Stroboskop-Wert",
        "color": (
            "Farbwert. Wenn dein Scheinwerfer kein RGB-Gerät ist, sondern z. B. CMY, RGBA oder ein anderes, "
            "übersetzt Sorcerer automatisch RGB in das korrekte Farbprofil. Das Farbprofil gibst du rechts neben "
            "diesem Feld an. Um viele gleichzeitig zu ändern, verwende 'Profil anwenden' oben links oder den Button "
            "'Patch auf Objekte in Szene anwenden' weiter unten im Gruppen-Patch."
        ),
        "color_restore": (
            "Warum gibt es hier zwei Farbfelder? Weil relative Änderungen bei Farbe problematisch sind. "
            "Influencer verwenden relative Änderungen für alles außer Farbe. Dieses zweite Feld bestimmt, auf "
            "welche Farbe der Influencer die Kanäle zurücksetzt, nachdem er vorbei ist."
        ),
        "pan": "Pan-Wert",
        "tilt": "Tilt-Wert",
        "zoom": "Zoom-Wert",
        "iris": "Iris-Wert",
        "edge": "Kantenwert",
        "diffusion": "Diffusionswert",
        "gobo": "Gobo-ID-Wert",
        "speed": "Rotationsgeschwindigkeit des Gobos",
        "prism": "Prismenwert",

        # Audio Parameters
        "volume": "Lautstärke/Mikrofonpegel des Bühnenobjekts",

        # Common Header
        "manual_fixture_selection": (
            "Statt der Gruppenauswahl links kannst du hier direkt eingeben, was du steuern möchtest – einfach in "
            "natürlicher Sprache die gewünschten oder auszuschließenden Kanäle angeben."
        ),
        "selected_group_enum": (
            "Wähle die zu steuernden Fixtures. Entweder statische Lichtgruppen oder dynamisch anhand ihrer Position "
            "im Verhältnis zu anderen Objekten."
        ),
        "selected_profile_enum": (
            "Wähle ein Scheinwerferprofil, das auf dieses und andere ausgewählte Fixtures angewendet wird. "
            "Zum Kopieren von Einstellungen: Zuerst Ziel-Scheinwerfer wählen, dann den Quell-Scheinwerfer, und "
            "dann hier 'Dynamisch' auswählen."
        ),
        "color_profile_enum": "Wähle ein Farbprofil für das Mesh basierend auf dem Lichtpult-Patch",
        "freezing_mode_enum": "Wähle, ob jedes Bild, jedes zweite oder jedes dritte Bild gerendert wird",
        "solo": (
            "Alle Controller stummschalten außer diesem (und anderen, bei denen Solo aktiviert ist). "
            "Alle Solos aufheben über den Button im Wiedergabemenü der Timeline."
        ),

        # Object Only
        "absolute": (
            "Absoluten Modus aktivieren. In diesem Modus können die Kanäle im Objekt animiert werden, solange sie "
            "drin sind. Im relativen Modus (wenn deaktiviert) ändern sich Kanäle nur, wenn der Influencer kommt oder "
            "geht – ideal für sich überlagernde Effekte."
        ),
        "strength": (
            "Bei geringerer Stärke verhält es sich wie ein Pinsel. Bei voller Stärke wie ein Objekt, das "
            "Lichtwerte beim Durchqueren zurücksetzt."
        ),
        "sem": (
            "Wenn dieser Wert ungleich null ist, funktioniert er wie ein 'SEM'-Kanal in ETC Eos. "
            "Verwende dies, um Objektpositionen in Augment3D zu animieren, einschließlich Remote-Patching. "
            "Verknüpfe ein 3D-Objekt, indem du es im A3D-Editor auf den SEM-Kanal ziehst. "
            "Eos positioniert es nicht automatisch korrekt."
        ),

        # Mins and maxes
        "strobe_min": "Minimaler Stroboskopwert am Gerät",
        "strobe_max": "Maximaler Stroboskopwert am Gerät",
        "white_balance": (
            "Wenn Weiß nicht wirklich weiß erscheint, kannst du hier einen Weißabgleich vornehmen, "
            "damit Weiß im Blender-Farbwähler auch als Weiß dargestellt wird."
        ),
        "pan_min": "Minimaler Pan-Wert am Gerät",
        "pan_max": "Maximaler Pan-Wert am Gerät",
        "tilt_min": "Minimaler Tilt-Wert am Gerät",
        "tilt_max": "Maximaler Tilt-Wert am Gerät",
        "zoom_min": "Minimaler Zoom-Wert am Gerät",
        "zoom_max": "Maximaler Zoom-Wert am Gerät",
        "speed_min": "Minimale Goborotationsgeschwindigkeit am Gerät",
        "speed_max": "Maximale Goborotationsgeschwindigkeit am Gerät",

        # Toggles
        "enable_audio": "Audio ist aktiviert, wenn ausgewählt",
        "enable_microphone": "Mikrofonlautstärke ist mit Intensität verknüpft, wenn rot",
        "enable_pan_tilt": "Pan/Tilt ist aktiviert, wenn ausgewählt",
        "enable_color": "Farbe ist aktiviert, wenn ausgewählt",
        "enable_diffusion": "Diffusion ist aktiviert, wenn ausgewählt",
        "enable_strobe": "Stroboskop ist aktiviert, wenn ausgewählt",
        "enable_zoom": "Zoom ist aktiviert, wenn ausgewählt",
        "enable_iris": "Iris ist aktiviert, wenn ausgewählt",
        "enable_edge": "Kante ist aktiviert, wenn ausgewählt",
        "enable_gobo": "Gobo ist aktiviert, wenn ausgewählt",
        "enable_prism": "Prisma ist aktiviert, wenn ausgewählt",

        # Enable/Disable Arguments
        "simple_enable_disable_argument": "Füge # für Gruppen-ID hinzu",
        "gobo_argument": "Füge # für Gruppen-ID und $ für Animationsdaten hinzu",

        # Orb Executors
        "event_list": "Nummer der Event-Liste auf dem Pult für diesen Song",
        "cue_list": "Nummer der Cue-Liste auf dem Pult für diesen Song",
        "start_cue": (
            "Gibt an, welcher Cue den Timecode startet (oder aktiviert). "
            "Darf nicht identisch mit dem ersten Cue in der Blender-Sequenz sein, sonst entsteht eine Schleife."
        ),
        "end_cue": "Gibt an, welcher Cue den Timecode stoppt (oder deaktiviert)",
        "start_macro": "Universelles Makro für Startaktionen",
        "end_macro": "Universelles Makro für Endaktionen",
        "start_preset": "Universelles Preset für Startaktionen",
        "end_preset": "Universelles Preset für Endaktionen",

        # View3D Operators
        "alva_object.duplicate_object": "Duplizieren und Verschieben. Optional zuerst eine Kurve oder einen Kreis auswählen zur Begrenzung.",
        "duplicate_columns": "Anzahl zusätzlicher Spalten",
        "duplicate_rows": "Anzahl zusätzlicher Zeilen",

        # Scene Properties
        "is_parameter_bar_expanded": "Werkzeugleiste erweitern, um mehr Parameter zu sehen"
    }


class COMMON_LG_chinese(spy.types.Language):
    as_idname = 'chinese'
    as_label = "Chinese"
    as_description = "The Chinese language"

    tooltips = {
        # Object Only
        "mute": "静音此对象的 OSC 输出",
        "summon_movers": "命令行文本，用于将移动灯具聚焦到舞台对象上",
        "erase": "删除而不是添加",
        "speaker_number": (
            "QLab 中或调音台上的扬声器编号。你看到此设置，是因为你选择了一个扬声器对象，"
            "扬声器对象用于表示剧院中实际的物理扬声器，用于空间音频。"
            "要将麦克风向左或右移动，不使用编码器，而是直接在 3D 视图中移动麦克风或声音对象的位置。"
        ),
        "sound_source": "选择序列中的音频条或音频补丁中的麦克风",

        # Lighting Parameters
        "intensity": "强度值",
        "strobe": "频闪值",
        "color": (
            "颜色值。如果你的灯具不是 RGB 类型，而是 CMY、RGBA 或其他，"
            "Sorcerer 会自动将 RGB 转换为正确的色彩模式。"
            "你可以在此字段右侧的对象控制面板中指定颜色模式。"
            "若要批量更改多个对象，请使用左上角的“应用配置文件”功能，"
            "或点击该面板下方组补丁中的“将补丁应用于场景中的对象”按钮。"
        ),
        "color_restore": (
            "为什么有两个颜色选择器？因为相对方式修改颜色效果不佳。"
            "因此 Influencer 通常对颜色使用绝对方式。"
            "这个第二个颜色选择器指定了 Influencer 离开后将颜色还原为哪种值。"
        ),
        "pan": "水平移动（Pan）值",
        "tilt": "垂直移动（Tilt）值",
        "zoom": "变焦值",
        "iris": "光圈值",
        "edge": "边缘值",
        "diffusion": "柔光值",
        "gobo": "图案盘 ID 值",
        "speed": "图案盘旋转速度",
        "prism": "棱镜值",

        # Audio Parameters
        "volume": "舞台对象麦克风的音量值",

        # Common Header
        "manual_fixture_selection": (
            "可在此手动输入要控制的灯具或通道。"
            "使用自然语言输入要包含或排除的通道，而不是使用左侧的组选择器。"
        ),
        "selected_group_enum": (
            "选择要控制的灯具。可选择静态分组（Lighting Groups）或基于位置的动态选择（Dynamic）。"
        ),
        "selected_profile_enum": (
            "选择要应用的灯具配置文件，可应用于当前灯具及其他所选灯具。"
            "如需从另一灯具复制设置，先选择目标灯具，再选择源灯具，然后选择“动态”选项。"
        ),
        "color_profile_enum": "根据灯控台中的补丁为模型选择颜色配置文件",
        "freezing_mode_enum": "选择每帧、隔帧或每第三帧进行渲染",
        "solo": (
            "仅保留此控制器（及其他处于 Solo 状态的控制器）启用，"
            "其它全部静音。可在时间轴菜单的播放菜单中清除所有 Solo 设置。"
        ),

        # Object Only
        "absolute": (
            "启用绝对模式。在此模式下，只要通道在对象内，就会根据动画进行控制。"
            "关闭此选项后，只有当 Influencer 进入或离开时才会修改通道值，"
            "即使用相对模式，可叠加其它效果。"
        ),
        "strength": (
            "降低强度会使其行为像画笔；提高到最大时会像一个穿过灯光的对象，"
            "在离开时重置灯光。"
        ),
        "sem": (
            "如果该值不为 0，则表现为 ETC Eos 中的 SEM 通道。"
            "用于在 Augment3D 中动画对象的位置，也适用于远程补丁。"
            "要将 Augment3D 中的 3D 模型连接至此通道，请在 A3D 编辑器右侧标签中，"
            "将模型拖动至 SEM 通道。Eos 不会自动对齐它们的位置。"
        ),

        # Mins and maxes
        "strobe_min": "灯具的最小频闪值",
        "strobe_max": "灯具的最大频闪值",
        "white_balance": (
            "若白色看起来不是真正的白色，可在此调整白平衡，使 Blender 颜色选择器中的白色实际为白色"
        ),
        "pan_min": "灯具的最小 Pan 值",
        "pan_max": "灯具的最大 Pan 值",
        "tilt_min": "灯具的最小 Tilt 值",
        "tilt_max": "灯具的最大 Tilt 值",
        "zoom_min": "灯具的最小 Zoom 值",
        "zoom_max": "灯具的最大 Zoom 值",
        "speed_min": "灯具的最小图案旋转速度",
        "speed_max": "灯具的最大图案旋转速度",

        # Toggles
        "enable_audio": "勾选后启用音频",
        "enable_microphone": "红色状态表示麦克风音量受强度控制",
        "enable_pan_tilt": "勾选后启用 Pan/Tilt",
        "enable_color": "勾选后启用颜色",
        "enable_diffusion": "勾选后启用柔光",
        "enable_strobe": "勾选后启用频闪",
        "enable_zoom": "勾选后启用变焦",
        "enable_iris": "勾选后启用光圈",
        "enable_edge": "勾选后启用边缘控制",
        "enable_gobo": "勾选后启用图案盘",
        "enable_prism": "勾选后启用棱镜",

        # Enable/Disable Arguments
        "simple_enable_disable_argument": "使用 # 表示组 ID",
        "gobo_argument": "使用 # 表示组 ID，使用 $ 表示动画数据",

        # Orb Executors
        "event_list": "为该歌曲设置的控台事件列表编号",
        "cue_list": "为该歌曲设置的控台提示列表编号",
        "start_cue": (
            "指定哪个提示（Cue）启动或激活时间码。"
            "不能与 Blender 序列中的第一个提示相同，否则会造成循环。"
        ),
        "end_cue": "指定哪个提示停止或禁用时间码",
        "start_macro": "用于各种启动操作的通用宏",
        "end_macro": "用于各种结束操作的通用宏",
        "start_preset": "用于各种启动操作的通用预设",
        "end_preset": "用于各种结束操作的通用预设",

        # View3D Operators
        "alva_object.duplicate_object": "复制并滑动。如选择曲线或圆形，则可沿其约束方向复制。",
        "duplicate_columns": "创建的额外列数",
        "duplicate_rows": "创建的额外行数",

        # Scene Properties
        "is_parameter_bar_expanded": "展开工具栏以查看更多参数"
    }


class COMMON_LG_hindi(spy.types.Language):
    as_idname = 'hindi'
    as_label = "Hindi"
    as_description = "The Hindi language"

    tooltips = {
        # Object Only
        "mute": "इस ऑब्जेक्ट का OSC आउटपुट म्यूट करें",
        "summon_movers": "स्टेज ऑब्जेक्ट पर मूविंग फिक्स्चर फोकस करने के लिए कमांड लाइन टेक्स्ट",
        "erase": "जोड़ने के बजाय मिटाएं",
        "speaker_number": (
            "QLab या साउंड मिक्सर में स्पीकर का नंबर। यह इसलिए दिखाई दे रहा है क्योंकि आपने एक Speaker ऑब्जेक्ट चुना है। "
            "स्पीकर ऑब्जेक्ट थिएटर में वास्तविक, भौतिक स्पीकर्स का प्रतिनिधित्व करते हैं, जिनका उपयोग स्पैशियल ऑडियो के लिए होता है। "
            "माइक्रोफोन को बाएं या दाएं पैन करने के लिए आप एनकोडर का उपयोग नहीं करते, बल्कि माइक्रोफोन या साउंड ऑब्जेक्ट को "
            "3D व्यू में बाईं या दाईं ओर खिसका देते हैं।"
        ),
        "sound_source": "Sequencer में एक साउंड स्ट्रिप या Audio Patch में एक माइक्रोफोन चुनें",

        # Lighting Parameters
        "intensity": "प्रकाश तीव्रता का मान",
        "strobe": "स्ट्रोब का मान",
        "color": (
            "रंग का मान। यदि आपका फिक्स्चर RGB नहीं है, बल्कि CMY, RGBA आदि है, तो Sorcerer स्वतः ही RGB को "
            "सही कलर प्रोफाइल में कन्वर्ट कर देगा। सही प्रोफाइल बताने के लिए इस फील्ड के दाईं ओर उपलब्ध विकल्प का उपयोग करें। "
            "एक साथ कई फिक्स्चर बदलने के लिए ऊपर बाएं 'Profile to Apply' का प्रयोग करें या नीचे 'Apply Patch to Objects in Scene' बटन दबाएं।"
        ),
        "color_restore": (
            "यहाँ दो रंग क्यों हैं? क्योंकि रंग में सापेक्ष परिवर्तन अच्छे से काम नहीं करते। "
            "इसीलिए Influencer रंग को छोड़कर बाकी सभी चैनलों में रिलेटिव बदलाव करता है। "
            "यह दूसरा रंग Influencer द्वारा गुजरने के बाद ऑब्जेक्ट को वापस सेट करने के लिए उपयोग होता है।"
        ),
        "pan": "पैन का मान",
        "tilt": "टिल्ट का मान",
        "zoom": "ज़ूम का मान",
        "iris": "आईरिस का मान",
        "edge": "किनारे (एज) का मान",
        "diffusion": "डिफ्यूज़न का मान",
        "gobo": "गोबो ID का मान",
        "speed": "गोबो रोटेशन स्पीड का मान",
        "prism": "प्रिज़्म का मान",

        # Audio Parameters
        "volume": "स्टेज ऑब्जेक्ट के माइक्रोफोन की वॉल्यूम/तीव्रता",

        # Common Header
        "manual_fixture_selection": (
            "बाएं समूह चयनकर्ता की बजाय यहाँ पर टाइप करके चयन करें। आप जिन चैनलों को नियंत्रित करना या नहीं करना चाहते हैं, "
            "उन्हें सामान्य भाषा में लिखें।"
        ),
        "selected_group_enum": (
            "नियंत्रित करने के लिए फिक्स्चर चुनें। स्थिर Lighting Groups या अन्य ऑब्जेक्ट्स की तुलना में इनके स्थान के आधार पर "
            "डायनामिक चयन का उपयोग करें।"
        ),
        "selected_profile_enum": (
            "इस फिक्स्चर और अन्य चयनित फिक्स्चर पर लगाने के लिए एक फिक्स्चर प्रोफाइल चुनें। "
            "किसी और लाइट से सेटिंग्स कॉपी करने के लिए पहले सभी लक्षित लाइट्स चुनें, फिर स्रोत लाइट चुनें, और "
            "'Dynamic' विकल्प का चयन करें।"
        ),
        "color_profile_enum": "Lighting Console में दिए गए पैच के आधार पर रंग प्रोफाइल चुनें",
        "freezing_mode_enum": "हर फ्रेम, हर दूसरे फ्रेम, या हर तीसरे फ्रेम पर रेंडर करने का विकल्प चुनें",
        "solo": (
            "सिर्फ इस कंट्रोलर (और अन्य सक्रिय सोलो वाले) को चालू रखें; बाकी सभी म्यूट हो जाएंगे। "
            "Timeline हेडर के Playback मेन्यू में जाकर सभी Solo को हटाया जा सकता है।"
        ),

        # Object Only
        "absolute": (
            "एब्सोल्यूट मोड सक्षम करें। इस मोड में ऑब्जेक्ट में मौजूद चैनलों को एनिमेट किया जा सकता है। "
            "यदि यह बंद है, तो चैनल केवल तब बदलेंगे जब Influencer आए या जाए। "
            "इस मोड में Influencer रिलेटिव मोड में होता है और अन्य प्रभावों के ऊपर काम कर सकता है।"
        ),
        "strength": (
            "कम स्ट्रेंथ पर यह एक ब्रश जैसा बर्ताव करता है। अधिक स्ट्रेंथ पर यह एक वस्तु की तरह कार्य करता है "
            "जो लाइट्स के बीच से गुजरते समय उन्हें रीसेट करता है।"
        ),
        "sem": (
            "यदि यह शून्य से अलग है, तो यह ETC Eos के 'SEM' चैनल जैसा व्यवहार करेगा। "
            "Augment3D में ऑब्जेक्ट की पोजिशन को एनिमेट करने के लिए इसका उपयोग करें। "
            "A3D एडिटर के दाईं ओर टैब में जाकर मॉडल को SEM चैनल पर ड्रैग करें। "
            "Eos इन दोनों को खुद से एक ही जगह नहीं रखेगा।"
        ),

        # Mins and maxes
        "strobe_min": "फिक्स्चर पर न्यूनतम स्ट्रोब मान",
        "strobe_max": "फिक्स्चर पर अधिकतम स्ट्रोब मान",
        "white_balance": (
            "यदि नैचुरल व्हाइट वास्तव में सफेद नहीं दिखती, तो यहाँ उसे समायोजित करें, "
            "ताकि Blender में सफेद रंग वास्तव में सफेद दिखे।"
        ),
        "pan_min": "फिक्स्चर का न्यूनतम पैन मान",
        "pan_max": "फिक्स्चर का अधिकतम पैन मान",
        "tilt_min": "फिक्स्चर का न्यूनतम टिल्ट मान",
        "tilt_max": "फिक्स्चर का अधिकतम टिल्ट मान",
        "zoom_min": "फिक्स्चर का न्यूनतम ज़ूम मान",
        "zoom_max": "फिक्स्चर का अधिकतम ज़ूम मान",
        "speed_min": "फिक्स्चर की न्यूनतम गोबो रोटेशन स्पीड",
        "speed_max": "फिक्स्चर की अधिकतम गोबो रोटेशन स्पीड",

        # Toggles
        "enable_audio": "चयनित होने पर ऑडियो सक्षम होगा",
        "enable_microphone": "लाल होने पर माइक्रोफोन वॉल्यूम Intensity से लिंक होगा",
        "enable_pan_tilt": "चयनित होने पर Pan/Tilt सक्षम होंगे",
        "enable_color": "चयनित होने पर रंग सक्षम होगा",
        "enable_diffusion": "चयनित होने पर डिफ्यूज़न सक्षम होगा",
        "enable_strobe": "चयनित होने पर स्ट्रोब सक्षम होगा",
        "enable_zoom": "चयनित होने पर ज़ूम सक्षम होगा",
        "enable_iris": "चयनित होने पर आईरिस सक्षम होगा",
        "enable_edge": "चयनित होने पर एज सक्षम होगा",
        "enable_gobo": "चयनित होने पर गोबो सक्षम होगा",
        "enable_prism": "चयनित होने पर प्रिज़्म सक्षम होगा",

        # Enable/Disable Arguments
        "simple_enable_disable_argument": "ग्रुप ID के लिए # जोड़ें",
        "gobo_argument": "ग्रुप ID के लिए # और एनिमेशन डेटा के लिए $ जोड़ें",

        # Orb Executors
        "event_list": "इस गीत के लिए कंसोल में बनाए गए इवेंट लिस्ट की संख्या",
        "cue_list": "इस गीत के लिए बनाए गए क्यू लिस्ट की संख्या",
        "start_cue": (
            "वह क्यू जो टाइमकोड क्लॉक को शुरू या सक्रिय करेगा। "
            "यह Blender सीक्वेंस में पहले क्यू के समान नहीं होना चाहिए, वरना लूप बन जाएगा।"
        ),
        "end_cue": "वह क्यू जो टाइमकोड क्लॉक को बंद या निष्क्रिय करेगा",
        "start_macro": "विभिन्न स्टार्ट क्रियाओं के लिए सामान्य मैक्रो",
        "end_macro": "विभिन्न एंड क्रियाओं के लिए सामान्य मैक्रो",
        "start_preset": "विभिन्न स्टार्ट क्रियाओं के लिए सामान्य प्रीसेट",
        "end_preset": "विभिन्न एंड क्रियाओं के लिए सामान्य प्रीसेट",

        # View3D Operators
        "alva_object.duplicate_object": "डुप्लिकेट और स्लाइड करें। वैकल्पिक रूप से पहले कोई कर्व या सर्कल चुनें ताकि वह उसी दिशा में सीमित हो।",
        "duplicate_columns": "बनाने के लिए अतिरिक्त कॉलम की संख्या",
        "duplicate_rows": "बनाने के लिए अतिरिक्त पंक्तियों की संख्या",

        # Scene Properties
        "is_parameter_bar_expanded": "अधिक पैरामीटर देखने के लिए टूलबार विस्तार करें"
    }


class COMMON_LG_ukrainian(spy.types.Language):
    as_idname = 'ukrainian'
    as_label = "Ukrainian"
    as_description = "The Ukrainian language"

    tooltips = {
        # Object Only
        "mute": "Вимкнути OSC-вивід цього об'єкта",
        "summon_movers": "Текст команди для фокусування рухомих світильників на сценічному об'єкті",
        "erase": "Стерти замість додавання",
        "speaker_number": (
            "Номер динаміка у QLab або на звуковому пульті. Ви бачите це, тому що вибрали об'єкт-динамік. "
            "Об'єкти-динаміки представляють реальні фізичні динаміки у вашому театрі для просторового аудіо. "
            "Щоб панорамувати мікрофон ліворуч або праворуч, не використовуйте енкодер — просто перемістіть мікрофон "
            "або звуковий об'єкт уліво або управо у 3D-перегляді."
        ),
        "sound_source": "Оберіть звукову доріжку у секвенсері або мікрофон у аудіо-патчі",

        # Lighting Parameters
        "intensity": "Значення інтенсивності",
        "strobe": "Значення стробоскопу",
        "color": (
            "Значення кольору. Якщо ваш прилад не RGB, а CMY, RGBA або інший, Sorcerer автоматично "
            "перетворить RGB у правильний профіль. Вкажіть бажаний профіль кольору праворуч від цього поля. "
            "Щоб змінити багато об'єктів одночасно, скористайтеся функцією 'Профіль для застосування' вгорі ліворуч "
            "або кнопкою 'Застосувати патч до об'єктів у сцені' нижче."
        ),
        "color_restore": (
            "Чому тут два кольори? Тому що відносні зміни кольору часто не працюють коректно. "
            "Influencer'и використовують абсолютні значення для кольору. "
            "Другий вибір кольору визначає, до якого кольору буде повернено після впливу."
        ),
        "pan": "Значення панорами (Pan)",
        "tilt": "Значення нахилу (Tilt)",
        "zoom": "Значення зуму",
        "iris": "Значення ірису",
        "edge": "Значення країв (Edge)",
        "diffusion": "Значення розсіювання (Diffusion)",
        "gobo": "Значення ID гобо",
        "speed": "Швидкість обертання гобо",
        "prism": "Значення призми",

        # Audio Parameters
        "volume": "Гучність мікрофона сценічного об'єкта",

        # Common Header
        "manual_fixture_selection": (
            "Замість вибору груп ліворуч, введіть вручну, що саме ви хочете контролювати. "
            "Просто опишіть канали, які потрібно включити або виключити, звичайною мовою."
        ),
        "selected_group_enum": (
            "Оберіть прилади для керування. Можна використовувати статичні групи або динамічний вибір "
            "на основі просторового розміщення відносно інших об'єктів."
        ),
        "selected_profile_enum": (
            "Оберіть профіль світильника для цього та інших вибраних об'єктів. "
            "Щоб скопіювати налаштування з іншого світильника: спочатку оберіть цільові світильники, потім джерело, "
            "а після цього виберіть 'Динамічний' варіант."
        ),
        "color_profile_enum": "Оберіть профіль кольору на основі патчу у світловій консолі",
        "freezing_mode_enum": "Оберіть, чи рендерити кожен кадр, кожен другий або кожен третій кадр",
        "solo": (
            "Вимкнути всі контролери, крім цього та тих, де також увімкнено Solo. "
            "Очистити всі Solo можна в меню Відтворення у заголовку Таймлайну."
        ),

        # Object Only
        "absolute": (
            "Увімкнути абсолютний режим. У цьому режимі об'єкт може анімувати внутрішні канали. "
            "У вимкненому стані (відносному режимі), значення каналів змінюються лише при вході/виході Influencer'а, "
            "що дозволяє накладення ефектів."
        ),
        "strength": (
            "Зменшення сили робить об'єкт схожим на пензель. При максимальній силі об'єкт буде діяти як тіло, "
            "що проходить через світло і скидає його після себе."
        ),
        "sem": (
            "Якщо значення не нульове, буде діяти як SEM-канал в ETC Eos. "
            "Використовуйте для анімації переміщення об'єктів в Augment3D. "
            "Щоб з’єднати 3D-модель із цим каналом у редакторі A3D, перетягніть модель на SEM-канал з правої панелі. "
            "Eos не розміщує їх автоматично."
        ),

        # Mins and maxes
        "strobe_min": "Мінімальне значення стробоскопа на приладі",
        "strobe_max": "Максимальне значення стробоскопа на приладі",
        "white_balance": (
            "Якщо природній білий виглядає не зовсім білим — скорегуйте баланс білого тут. "
            "Тоді білий у виборі кольору Blender буде справді білим."
        ),
        "pan_min": "Мінімальне значення панорами на приладі",
        "pan_max": "Максимальне значення панорами на приладі",
        "tilt_min": "Мінімальне значення нахилу на приладі",
        "tilt_max": "Максимальне значення нахилу на приладі",
        "zoom_min": "Мінімальне значення зуму на приладі",
        "zoom_max": "Максимальне значення зуму на приладі",
        "speed_min": "Мінімальна швидкість обертання гобо на приладі",
        "speed_max": "Максимальна швидкість обертання гобо на приладі",

        # Toggles
        "enable_audio": "Аудіо увімкнено, якщо позначено",
        "enable_microphone": "Червоним позначено, якщо гучність мікрофона пов’язана з інтенсивністю",
        "enable_pan_tilt": "Пан/Тілт увімкнено, якщо позначено",
        "enable_color": "Кольори увімкнено, якщо позначено",
        "enable_diffusion": "Розсіювання увімкнено, якщо позначено",
        "enable_strobe": "Стробоскоп увімкнено, якщо позначено",
        "enable_zoom": "Зум увімкнено, якщо позначено",
        "enable_iris": "Ірис увімкнено, якщо позначено",
        "enable_edge": "Краї увімкнено, якщо позначено",
        "enable_gobo": "Гобо увімкнено, якщо позначено",
        "enable_prism": "Призму увімкнено, якщо позначено",

        # Enable/Disable Arguments
        "simple_enable_disable_argument": "Додайте # для ID групи",
        "gobo_argument": "Додайте # для ID групи та $ для анімаційних даних",

        # Orb Executors
        "event_list": "Номер списку подій, створеного на пульті для цієї пісні",
        "cue_list": "Номер списку cue, створеного на пульті для цієї пісні",
        "start_cue": (
            "Cue, який запускає або активує таймкод. "
            "Не повинен бути першим cue у Blender-послідовності, інакше виникне цикл."
        ),
        "end_cue": "Cue, який зупиняє або вимикає таймкод",
        "start_macro": "Універсальна макрокоманда для стартових дій",
        "end_macro": "Універсальна макрокоманда для завершальних дій",
        "start_preset": "Універсальний пресет для стартових дій",
        "end_preset": "Універсальний пресет для завершальних дій",

        # View3D Operators
        "alva_object.duplicate_object": "Дублювати з переміщенням. За бажанням — спочатку виберіть криву або коло для обмеження",
        "duplicate_columns": "Кількість додаткових стовпців",
        "duplicate_rows": "Кількість додаткових рядків",

        # Scene Properties
        "is_parameter_bar_expanded": "Розгорнути панель параметрів для перегляду додаткових налаштувань"
    }


class COMMON_LG_irish(spy.types.Language):
    as_idname = 'irish'
    as_label = "Irish (Gaeilge)"
    as_description = "The Irish language"

    tooltips = {
        # Object Only
        "mute": "Dún aschur OSC an réada seo",
        "summon_movers": "Téacs ordaithe chun spotsoilse gluaiseacha a dhíriú ar réad na stáitse",
        "erase": "Scrios in ionad cur leis",
        "speaker_number": (
            "Uimhir an chainteora i QLab nó ar an meascthóir fuaime. Tá tú á fheiceáil toisc gur roghnaigh tú réad 'Speaker'. "
            "Seasann na réada seo do chainteoirí fisiciúla i do théatar le haghaidh fuaime spásúla. "
            "Chun micreafón a phanáil ar chlé nó ar dheis, bog é sa radharc 3D — ní úsáidtear encoder chuige sin."
        ),
        "sound_source": "Roghnaigh stiall fuaime sa tseicheamh nó micreafón san Audio Patch",

        # Lighting Parameters
        "intensity": "Luach déine",
        "strobe": "Luach stroibe",
        "color": (
            "Luach datha. Má tá do sholas CMY, RGBA nó rud éigin eile seachas RGB, "
            "aistreoidh Sorcerer RGB go dtí an phróifíl chuí go huathoibríoch. "
            "Socraigh an phróifíl datha ar thaobh na láimhe deise den réimse seo. "
            "Chun iliomad réada a athrú ag an am céanna, úsáid 'Próifíl le Cuir i bhFeidhm' ag barr na láimhe clé, "
            "nó an cnaipe 'Cuir Patch i bhFeidhm ar Réada sa Radharc'."
        ),
        "color_restore": (
            "Cén fáth atá dhá rogha datha anseo? Ní oibríonn athruithe coibhneasta go maith le dath. "
            "Úsáideann Influencers athruithe coibhneasta i gcás gach rud eile seachas dath. "
            "Socraíonn an dara roghnóir an dath ar ais tar éis don Influencer imeacht."
        ),
        "pan": "Luach pan",
        "tilt": "Luach tilt",
        "zoom": "Luach súmála",
        "iris": "Luach iris",
        "edge": "Luach imill",
        "diffusion": "Luach scaipthe",
        "gobo": "ID gobo",
        "speed": "Luas rothlaithe gobo",
        "prism": "Luach priosma",

        # Audio Parameters
        "volume": "Luach déine micreafóin an réada stáitse",

        # Common Header
        "manual_fixture_selection": (
            "In áit an roghnóra ghrúpa ar chlé, clóscríobh na cainéil is mian leat a rialú nó a fhágáil amach anseo — "
            "úsáid Ghaeilge nádúrtha."
        ),
        "selected_group_enum": (
            "Roghnaigh soilse le rialú. Úsáid grúpaí statacha nó roghnú dinimiciúil bunaithe ar shuíomh na réada eile."
        ),
        "selected_profile_enum": (
            "Roghnaigh próifíl sholais le cur i bhfeidhm ar an bhfianaise seo agus ar na cinn roghnaithe eile. "
            "Chun socruithe a chóipeáil ó sholas eile: roghnaigh na cinn sprioc, ansin an fhoinse, agus ansin roghnaigh 'Dinimiciúil'."
        ),
        "color_profile_enum": "Roghnaigh próifíl datha bunaithe ar an bpaitinn ón chonsól soilsithe",
        "freezing_mode_enum": "Roghnaigh cé mhéad fráma a dtaispeánfar: gach ceann, gach dara ceann, nó gach tríú",
        "solo": (
            "Múch gach rialtóir seachas an ceann seo agus cinn eile ina bhfuil 'solo' gníomhach. "
            "Úsáid an cnaipe sa roghchlár Seinnte sa Timeline chun gach solo a ghlanadh."
        ),

        # Object Only
        "absolute": (
            "Cumasaigh mód iomlán. Sa mhód seo, is féidir leis an réad na cainéil istigh a bheochan. "
            "Má tá sé as feidhm, ní athraítear na cainéil ach nuair a thagann nó a imíonn an Influencer — "
            "oibríonn sé ar bharr éifeachtaí eile."
        ),
        "strength": (
            "Má laghdaíonn tú an neart, oibreoidh sé cosúil le scuab. Má mhéadaíonn tú é, oibreoidh sé cosúil le réad "
            "a thagann tríd na soilse agus a athshocraíonn iad agus é ag imeacht."
        ),
        "sem": (
            "Má tá luach seachas nialas ann, oibreoidh sé cosúil le cainéal 'SEM' ar ETC Eos. "
            "Úsáid é chun gluaiseacht réada i Augment3D a bheochan. "
            "Chun nascadh le cainéal SEM sa eagarthóir A3D, tarraing an tsamhail chuig an gcainéal ar an painéal ar dheis. "
            "Ní ailíníonn Eos iad go huathoibríoch."
        ),

        # Mins and maxes
        "strobe_min": "Luach íosta stroibe don fheiste féin",
        "strobe_max": "Luach uasta stroibe don fheiste féin",
        "white_balance": (
            "Má tá bán nádúrtha ag breathnú mícheart, socraigh an cothromaíocht bháin anseo "
            "ionas go mbeidh 'bán' i mBlender i ndáiríre bán."
        ),
        "pan_min": "Luach íosta pan don fheiste",
        "pan_max": "Luach uasta pan don fheiste",
        "tilt_min": "Luach íosta tilt don fheiste",
        "tilt_max": "Luach uasta tilt don fheiste",
        "zoom_min": "Luach íosta zoom don fheiste",
        "zoom_max": "Luach uasta zoom don fheiste",
        "speed_min": "Luas íosta rothlaithe gobo ar an fheiste",
        "speed_max": "Luas uasta rothlaithe gobo ar an fheiste",

        # Toggles
        "enable_audio": "Cuir fuaim ar siúl nuair atá sé ticáilte",
        "enable_microphone": "Tá micreafón nasctha le déine nuair atá sé dearg",
        "enable_pan_tilt": "Cumasaigh Pan/Tilt má tá sé ticáilte",
        "enable_color": "Cumasaigh dathanna má tá sé ticáilte",
        "enable_diffusion": "Cumasaigh scaipeadh má tá sé ticáilte",
        "enable_strobe": "Cumasaigh stroibe má tá sé ticáilte",
        "enable_zoom": "Cumasaigh zoom má tá sé ticáilte",
        "enable_iris": "Cumasaigh iris má tá sé ticáilte",
        "enable_edge": "Cumasaigh imill má tá sé ticáilte",
        "enable_gobo": "Cumasaigh gobo má tá sé ticáilte",
        "enable_prism": "Cumasaigh priosma má tá sé ticáilte",

        # Enable/Disable Arguments
        "simple_enable_disable_argument": "Cuir # leis don ghrúpa ID",
        "gobo_argument": "Cuir # leis don ghrúpa ID agus $ le haghaidh sonraí beochana",

        # Orb Executors
        "event_list": "Uimhir liosta imeachtaí ar an gconsól don amhrán seo",
        "cue_list": "Uimhir liosta cue ar an gconsól don amhrán seo",
        "start_cue": (
            "Sonraigh cén cue a thosóidh (nó a ghníomhóidh) an clog ama. "
            "Ní féidir leis a bheith mar an chéad cue sa seicheamh Blender — chruthóidh sé lúb."
        ),
        "end_cue": "Sonraigh cén cue a stopfaidh (nó a dhíghníomhóidh) an clog ama",
        "start_macro": "Macra uilíoch le haghaidh gníomhaíochtaí tosaigh éagsúla",
        "end_macro": "Macra uilíoch le haghaidh gníomhaíochtaí críochnaithe éagsúla",
        "start_preset": "Réamhshocrú uilíoch le haghaidh túsghníomhartha éagsúla",
        "end_preset": "Réamhshocrú uilíoch le haghaidh gníomhartha críochnaithe",

        # View3D Operators
        "alva_object.duplicate_object": "Cóipeáil agus bog. Roghnaigh cuar nó ciorcal ar dtús más mian leat sriantacht.",
        "duplicate_columns": "Líon breise colún le cruthú",
        "duplicate_rows": "Líon breise ró le cruthú",

        # Scene Properties
        "is_parameter_bar_expanded": "Leathnaigh an barra paraiméadair le níos mó roghanna a fheiceáil"
    }


languages = [
    COMMON_LG_american_english,
    COMMON_LG_spanish,
    COMMON_LG_french,
    COMMON_LG_german,
    COMMON_LG_chinese,
    COMMON_LG_hindi,
    COMMON_LG_ukrainian,
    COMMON_LG_irish
]


def register():
    for cls in languages:
        spy.utils.register_class(cls)


def unregister():
    for cls in reversed(languages):
        spy.utils.as_unregister_class(cls)