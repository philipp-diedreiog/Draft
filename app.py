import streamlit as st
import random

# Seite konfigurieren
st.set_page_config(page_title="Ö-Bundesliga Draft", layout="wide")

# 80 einzigartige Spieler aus deinen Quelldaten
@st.cache_data
def load_players():
    return [
        {"id": 1, "name": "Alexander Schlager", "club": "RB Salzburg", "pos": "TW", "rating": 82},
        {"id": 2, "name": "Samson Baidoo", "club": "RB Salzburg", "pos": "DEF", "rating": 79},
        {"id": 3, "name": "Amar Dedic", "club": "RB Salzburg", "pos": "DEF", "rating": 82},
        {"id": 4, "name": "Mads Bidstrup", "club": "RB Salzburg", "pos": "MID", "rating": 80},
        {"id": 5, "name": "Maurits Kjaergaard", "club": "RB Salzburg", "pos": "MID", "rating": 81},
        {"id": 6, "name": "Oscar Gloukh", "club": "RB Salzburg", "pos": "MID", "rating": 84},
        {"id": 7, "name": "Karim Konate", "club": "RB Salzburg", "pos": "FWD", "rating": 83},
        {"id": 8, "name": "Dorgeles Nene", "club": "RB Salzburg", "pos": "FWD", "rating": 79},
        {"id": 9, "name": "Petar Ratkov", "club": "RB Salzburg", "pos": "FWD", "rating": 77},
        {"id": 10, "name": "Joane Gadou", "club": "RB Salzburg", "pos": "DEF", "rating": 76},
        {"id": 11, "name": "Kjell Scherpen", "club": "Sturm Graz", "pos": "TW", "rating": 81},
        {"id": 12, "name": "Gregory Wüthrich", "club": "Sturm Graz", "pos": "DEF", "rating": 80},
        {"id": 13, "name": "Jusuf Gazibegovic", "club": "Sturm Graz", "pos": "DEF", "rating": 79},
        {"id": 14, "name": "Emanuel Aiwu", "club": "Sturm Graz", "pos": "DEF", "rating": 78},
        {"id": 15, "name": "Jon Gorenc Stankovic", "club": "Sturm Graz", "pos": "MID", "rating": 82},
        {"id": 16, "name": "Otar Kiteishvili", "club": "Sturm Graz", "pos": "MID", "rating": 83},
        {"id": 17, "name": "Tomi Horvat", "club": "Sturm Graz", "pos": "MID", "rating": 80},
        {"id": 18, "name": "Mika Biereth", "club": "Sturm Graz", "pos": "FWD", "rating": 81},
        {"id": 19, "name": "Seedy Jatta", "club": "Sturm Graz", "pos": "FWD", "rating": 76},
        {"id": 20, "name": "William Bøving", "club": "Sturm Graz", "pos": "FWD", "rating": 77},
        {"id": 21, "name": "Niklas Hedl", "club": "Rapid Wien", "pos": "TW", "rating": 80},
        {"id": 22, "name": "Serge-Philippe Raux-Yao", "club": "Rapid Wien", "pos": "DEF", "rating": 79},
        {"id": 23, "name": "Nenad Cvetkovic", "club": "Rapid Wien", "pos": "DEF", "rating": 78},
        {"id": 24, "name": "Bendegúz Bolla", "club": "Rapid Wien", "pos": "DEF", "rating": 77},
        {"id": 25, "name": "Lukas Grgic", "club": "Rapid Wien", "pos": "MID", "rating": 78},
        {"id": 26, "name": "Mamadou Sangare", "club": "Rapid Wien", "pos": "MID", "rating": 79},
        {"id": 27, "name": "Matthias Seidl", "club": "Rapid Wien", "pos": "MID", "rating": 81},
        {"id": 28, "name": "Guido Burgstaller", "club": "Rapid Wien", "pos": "FWD", "rating": 79},
        {"id": 29, "name": "Dion Drena Beljo", "club": "Rapid Wien", "pos": "FWD", "rating": 78},
        {"id": 30, "name": "Louis Schaub", "club": "Rapid Wien", "pos": "MID", "rating": 77},
        {"id": 31, "name": "Samuel Sahin-Radlinger", "club": "Austria Wien", "pos": "TW", "rating": 76},
        {"id": 32, "name": "Lucas Galvao", "club": "Austria Wien", "pos": "DEF", "rating": 76},
        {"id": 33, "name": "Reinhold Ranftl", "club": "Austria Wien", "pos": "DEF", "rating": 77},
        {"id": 34, "name": "Tin Plavotic", "club": "Austria Wien", "pos": "DEF", "rating": 74},
        {"id": 35, "name": "Manfred Fischer", "club": "Austria Wien", "pos": "MID", "rating": 77},
        {"id": 36, "name": "Abu Barry", "club": "Austria Wien", "pos": "MID", "rating": 75},
        {"id": 37, "name": "Dominik Fitz", "club": "Austria Wien", "pos": "MID", "rating": 80},
        {"id": 38, "name": "Maurice Malone", "club": "Austria Wien", "pos": "FWD", "rating": 76},
        {"id": 39, "name": "Nik Prelec", "club": "Austria Wien", "pos": "FWD", "rating": 75},
        {"id": 40, "name": "Hakim Guenouche", "club": "Austria Wien", "pos": "DEF", "rating": 73},
        {"id": 41, "name": "Jörg Siebenhandl", "club": "LASK", "pos": "TW", "rating": 75},
        {"id": 42, "name": "Philipp Ziereis", "club": "LASK", "pos": "DEF", "rating": 77},
        {"id": 43, "name": "Andrés Andrade", "club": "LASK", "pos": "DEF", "rating": 78},
        {"id": 44, "name": "George Bello", "club": "LASK", "pos": "DEF", "rating": 74},
        {"id": 45, "name": "Robert Zulj", "club": "LASK", "pos": "MID", "rating": 82},
        {"id": 46, "name": "Sascha Horvath", "club": "LASK", "pos": "MID", "rating": 78},
        {"id": 47, "name": "Valon Berisha", "club": "LASK", "pos": "MID", "rating": 77},
        {"id": 48, "name": "Marin Ljubicic", "club": "LASK", "pos": "FWD", "rating": 79},
        {"id": 49, "name": "Moses Usor", "club": "LASK", "pos": "FWD", "rating": 76},
        {"id": 50, "name": "Melayro Bogarde", "club": "LASK", "pos": "DEF", "rating": 74},
        {"id": 51, "name": "Andreas Leitner", "club": "SV Ried", "pos": "TW", "rating": 73},
        {"id": 52, "name": "Oliver Steurer", "club": "SV Ried", "pos": "DEF", "rating": 72},
        {"id": 53, "name": "Nikki Havenaar", "club": "SV Ried", "pos": "DEF", "rating": 71},
        {"id": 54, "name": "Fabian Wohlmuth", "club": "SV Ried", "pos": "DEF", "rating": 72},
        {"id": 55, "name": "Stefan Nutz", "club": "SV Ried", "pos": "MID", "rating": 75},
        {"id": 56, "name": "Mark Grosse", "club": "SV Ried", "pos": "MID", "rating": 73},
        {"id": 57, "name": "Philipp Pomer", "club": "SV Ried", "pos": "MID", "rating": 72},
        {"id": 58, "name": "Ante Bajic", "club": "SV Ried", "pos": "FWD", "rating": 74},
        {"id": 59, "name": "Wilfried Eza", "club": "SV Ried", "pos": "FWD", "rating": 73},
        {"id": 60, "name": "David Bumberger", "club": "SV Ried", "pos": "DEF", "rating": 70},
        {"id": 61, "name": "Dejan Stojanovic", "club": "SCR Altach", "pos": "TW", "rating": 74},
        {"id": 62, "name": "Constantin Reiner", "club": "SCR Altach", "pos": "DEF", "rating": 73},
        {"id": 63, "name": "Paul Koller", "club": "SCR Altach", "pos": "DEF", "rating": 74},
        {"id": 64, "name": "Sandro Ingolitsch", "club": "SCR Altach", "pos": "DEF", "rating": 72},
        {"id": 65, "name": "Vesel Demaku", "club": "SCR Altach", "pos": "MID", "rating": 73},
        {"id": 66, "name": "Mike-Steven Bähre", "club": "SCR Altach", "pos": "MID", "rating": 72},
        {"id": 67, "name": "Sofian Bahloul", "club": "SCR Altach", "pos": "MID", "rating": 73},
        {"id": 68, "name": "Lukas Fridrikas", "club": "SCR Altach", "pos": "FWD", "rating": 74},
        {"id": 69, "name": "Athe Nuhiu", "club": "SCR Altach", "pos": "FWD", "rating": 71},
        {"id": 70, "name": "Christian Gebauer", "club": "SCR Altach", "pos": "FWD", "rating": 72},
        {"id": 71, "name": "Nicolas Capaldo", "club": "RB Salzburg", "pos": "MID", "rating": 78},
        {"id": 72, "name": "Daouda Guindo", "club": "RB Salzburg", "pos": "DEF", "rating": 75},
        {"id": 73, "name": "Max Johnston", "club": "Sturm Graz", "pos": "DEF", "rating": 75},
        {"id": 74, "name": "Stefan Hierländer", "club": "Sturm Graz", "pos": "MID", "rating": 74},
        {"id": 75, "name": "Moritz Oswald", "club": "Rapid Wien", "pos": "MID", "rating": 73},
        {"id": 76, "name": "Isak Jansson", "club": "Rapid Wien", "pos": "FWD", "rating": 77},
        {"id": 77, "name": "Matteo Meisl", "club": "Austria Wien", "pos": "DEF", "rating": 72},
        {"id": 78, "name": "Sanel Saljic", "club": "Austria Wien", "pos": "MID", "rating": 70},
        {"id": 79, "name": "Branko Jovicic", "club": "LASK", "pos": "MID", "rating": 74},
        {"id": 80, "name": "Lenny Pintor", "club": "LASK", "pos": "FWD", "rating": 73}
    ]

# Session State Initialisierung
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
    st.session_state.teams = {0: [], 1: [], 2: [], 3: []}
    st.session_state.all_boosters = {1: {}, 2: {}, 3: {}, 4: {}}
    st.session_state.current_packs = {0: [], 1: [], 2: [], 3: []}
    st.session_state.picks_made = {0: None, 1: None, 2: None, 3: None}
    st.session_state.booster_num = 1
    st.session_state.pick_num = 1
    st.session_state.assigned_formations = {}

st.title("⚽ Ö-Bundesliga MTG Draft (80 Spieler / 4 Booster)")

# Sidebar Einstieg
st.sidebar.header("Lobby Einstieg")
player_id = st.sidebar.selectbox(
    "Wähle deinen Sitzplatz am Tisch:", 
    [0, 1, 2, 3], 
    format_func=lambda x: f"Spieler {x+1}"
)

if st.sidebar.button("Draft komplett zurücksetzen"):
    st.session_state.game_started = False
    st.session_state.teams = {0: [], 1: [], 2: [], 3: []}
    st.session_state.all_boosters = {1: {}, 2: {}, 3: {}, 4: {}}
    st.session_state.current_packs = {0: [], 1: [], 2: [], 3: []}
    st.session_state.picks_made = {0: None, 1: None, 2: None, 3: None}
    st.session_state.booster_num = 1
    st.session_state.pick_num = 1
    st.session_state.assigned_formations = {}
    st.rerun()

# Spielstart
if not st.session_state.game_started:
    st.info("Willkommen! Öffne diese Seite in 4 Browser-Tabs für Spieler 1 bis 4.")
    
    if st.button("🚀 Draft starten (4 Booster, 80 Spieler)", type="primary"):
        players = load_players()
        random.shuffle(players)  # Alle 80 Spieler einmalig mischen
        
        # 4 Booster à 20 Spieler aufteilen (4 Spieler x 5 Karten pro Booster)
        for b in range(1, 5):
            st.session_state.all_boosters[b] = {}
            for p in range(4):
                start_idx = (b - 1) * 20 + p * 5
                st.session_state.all_boosters[b][p] = players[start_idx : start_idx + 5]
        
        # Booster 1 laden
        st.session_state.current_packs = st.session_state.all_boosters[1].copy()
        st.session_state.game_started = True
        st.rerun()

# Aktiver Draft
elif st.session_state.booster_num <= 4:
    # MTG-Drehrichtung: Wechselt pro Booster
    direction_text = "➡️ Nach links" if st.session_state.booster_num % 2 != 0 else "⬅️ Nach rechts"
    st.header(f"📦 Booster {st.session_state.booster_num} / 4 — Pick {st.session_state.pick_num} / 5 ({direction_text})")
    st.subheader(f"Du spielst als: **Spieler {player_id + 1}**")
    
    my_pack = st.session_state.current_packs[player_id]
    
    st.markdown("**Status am Tisch:**")
    status_cols = st.columns(4)
    for p_id in range(4):
        has_picked = st.session_state.picks_made[p_id] is not None
        status_cols[p_id].write(f"Spieler {p_id+1}: {'✅ Gewählt' if has_picked else '⏳ Wählt...'}")
    
    st.divider()

    if st.session_state.picks_made[player_id] is not None:
        st.info("👉 Du hast deinen Pick gemacht. Warte auf die anderen Spieler...")
    
    elif len(my_pack) > 0:
        st.subheader(f"Auswahl aus Booster {st.session_state.booster_num}:")
        
        cols = st.columns(len(my_pack))
        for idx, card in enumerate(my_pack):
            with cols[idx]:
                with st.container(border=True):
                    st.subheader(card['name'])
                    st.write(f"Pos: | Club:")
                    st.metric(label="Stärke", value=f"⭐ {card['rating']}")
                    
                    btn_key = f"b{st.session_state.booster_num}_p{st.session_state.pick_num}_{card['id']}"
                    if st.button(f"Pick {card['name']}", key=btn_key):
                        st.session_state.teams[player_id].append(card)
                        st.session_state.picks_made[player_id] = card
                        st.rerun()

    # Auswertung, wenn alle 4 Spieler gewählt haben
    if all(pick is not None for pick in st.session_state.picks_made.values()):
        for p_id in range(4):
            picked_card = st.session_state.picks_made[p_id]
            st.session_state.current_packs[p_id] = [
                c for c in st.session_state.current_packs[p_id] if c['id'] != picked_card['id']
            ]
        
        # Prüfen, ob der aktuelle Booster leer ist
        if len(st.session_state.current_packs[0]) == 0:
            st.session_state.booster_num += 1
            st.session_state.pick_num = 1
            if st.session_state.booster_num <= 4:
                st.session_state.current_packs = st.session_state.all_boosters[st.session_state.booster_num].copy()
                st.toast(f"🎉 Booster {st.session_state.booster_num - 1} fertig! Öffne Booster {st.session_state.booster_num}...")
        else:
            # Packs im Kreis weitergeben
            old_packs = st.session_state.current_packs.copy()
            for p_id in range(4):
                if st.session_state.booster_num % 2 != 0:
                    st.session_state.current_packs[(p_id + 1) % 4] = old_packs[p_id]  # Links
                else:
                    st.session_state.current_packs[(p_id - 1) % 4] = old_packs[p_id]  # Rechts
            
            st.session_state.pick_num += 1

        st.session_state.picks_made = {0: None, 1: None, 2: None, 3: None}
        st.rerun()

    # Zwischenstand-Kader
    st.divider()
    st.subheader(f"Dein bisheriger Kader ({len(st.session_state.teams[player_id])} / 20 Spieler):")
    my_team = st.session_state.teams[player_id]
    if my_team:
        team_cols = st.columns(4)
        positions = ["TW", "DEF", "MID", "FWD"]
        for i, pos in enumerate(positions):
            with team_cols[i]:
                st.write(f"**{pos}:**")
                for p in [x for x in my_team if x['pos'] == pos]:
                    st.write(f"• {p['name']} ({p['rating']})")

# Endbildschirm & Aufstellung
else:
    st.balloons()
    st.success("🏆 **DRAFT BEENDET!** Alle 80 Spieler wurden gedraftet.")
    
    # Zufällige Formationen zuteilen
    formations = ["4-3-3", "4-4-2", "3-5-2", "4-2-3-1"]
    if not st.session_state.assigned_formations:
        shuffled_forms = formations.copy()
        random.shuffle(shuffled_forms)
        for p_id in range(4):
            st.session_state.assigned_formations[p_id] = shuffled_forms[p_id]

    st.header(f"📋 Formations- & Aufstellungs-Phase (Deine Formation: **{st.session_state.assigned_formations[player_id]}**)")
    
    my_team = st.session_state.teams[player_id]
    
    st.write("Wähle deine Start-11 aus deinen 20 gedrafteten Spielern:")
    
    selected_starters = []
    
    cols = st.columns(4)
    positions = ["TW", "DEF", "MID", "FWD"]
    
    for i, pos in enumerate(positions):
        with cols[i]:
            st.subheader(f"Position: {pos}")
            pos_players = [p for p in my_team if p['pos'] == pos]
            for p in pos_players:
                is_selected = st.checkbox(f"{p['name']} ({p['rating']}) - {p['club']}", key=f"starter_{p['id']}")
                if is_selected:
                    selected_starters.append(p)

    st.divider()
    st.write(f"**Ausgewählte Start-11:** {len(selected_starters)} / 11 Spieler")
    
    if len(selected_starters) == 11:
        team_rating = sum(p['rating'] for p in selected_starters)
        st.success(f"⚽ **Aufstellung komplett!** Gesamtstärke deiner Startelf: **{team_rating} Punkte**")
    elif len(selected_starters) > 11:
        st.error("⚠️ Du hast mehr als 11 Spieler ausgewählt. Bitte reduziere deine Auswahl.")
    else:
        st.warning(f"Wähle noch {11 - len(selected_starters)} Spieler aus.")

    st.divider()
    st.subheader("📊 Übersicht aller 4 Teams & Formationen am Tisch:")
    
    all_team_cols = st.columns(4)
    for p_id in range(4):
        with all_team_cols[p_id]:
            st.markdown(f"### Spieler {p_id + 1}")
            st.write(f"**Formation:** {st.session_state.assigned_formations[p_id]}")
            st.write(f"**Gedraftete Spieler:** {len(st.session_state.teams[p_id])}")
            with st.expander("Kader anzeigen"):
                for p in st.session_state.teams[p_id]:
                    st.write(f"• {p['name']} ({p['pos']}, {p['rating']})")
