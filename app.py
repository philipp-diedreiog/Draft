from streamlit_autorefresh import st_autorefresh

# Lädt die Seite alle 3 Sekunden automatisch neu, um Eingaben der anderen zu sehen
st_autorefresh(interval=3000, key="draft_refresh")

import streamlit as st
import random

# Seite konfigurieren
st.set_page_config(page_title="Ö-Bundesliga Draft", layout="wide")

@st.cache_data
def load_players():
    return [
        # Spieler aus dem hochgeladenen Bild:
        {"id": 1, "name": "Stankovic", "club": "GAK", "pos": "TW", "rating": 75},[cite: 2]
        {"id": 2, "name": "Owusu", "club": "GAK", "pos": "VER", "rating": 72},[cite: 2]
        {"id": 3, "name": "Pines", "club": "GAK", "pos": "VER", "rating": 71},[cite: 2]
        {"id": 4, "name": "Vraa Jensen", "club": "GAK", "pos": "VER", "rating": 70},[cite: 2]
        {"id": 5, "name": "Klassen", "club": "GAK", "pos": "VER", "rating": 72},[cite: 2]
        {"id": 6, "name": "Hermesh", "club": "GAK", "pos": "MF", "rating": 71},[cite: 2]
        {"id": 7, "name": "Michorl", "club": "GAK", "pos": "MF", "rating": 76},[cite: 2]
        {"id": 8, "name": "Anderson", "club": "GAK", "pos": "MF", "rating": 73},[cite: 2]
        {"id": 9, "name": "Lichtenberger", "club": "GAK", "pos": "ST", "rating": 74},[cite: 2]
        {"id": 10, "name": "Hofleitner", "club": "GAK", "pos": "ST", "rating": 70},[cite: 2]
        {"id": 11, "name": "Grosse", "club": "GAK", "pos": "ST", "rating": 72},[cite: 2]
        
        # Weitere Bundesliga-Spieler zur Erfüllung des 80-Spieler-Pools:
        {"id": 12, "name": "Alexander Schlager", "club": "RB Salzburg", "pos": "TW", "rating": 82},
        {"id": 13, "name": "Samson Baidoo", "club": "RB Salzburg", "pos": "VER", "rating": 79},
        {"id": 14, "name": "Amar Dedic", "club": "RB Salzburg", "pos": "VER", "rating": 82},
        {"id": 15, "name": "Mads Bidstrup", "club": "RB Salzburg", "pos": "MF", "rating": 80},
        {"id": 16, "name": "Maurits Kjaergaard", "club": "RB Salzburg", "pos": "MF", "rating": 81},
        {"id": 17, "name": "Oscar Gloukh", "club": "RB Salzburg", "pos": "MF", "rating": 84},
        {"id": 18, "name": "Karim Konate", "club": "RB Salzburg", "pos": "ST", "rating": 83},
        {"id": 19, "name": "Dorgeles Nene", "club": "RB Salzburg", "pos": "ST", "rating": 79},
        {"id": 20, "name": "Petar Ratkov", "club": "RB Salzburg", "pos": "ST", "rating": 77},
        {"id": 21, "name": "Joane Gadou", "club": "RB Salzburg", "pos": "VER", "rating": 76},
        {"id": 22, "name": "Kjell Scherpen", "club": "Sturm Graz", "pos": "TW", "rating": 81},
        {"id": 23, "name": "Gregory Wüthrich", "club": "Sturm Graz", "pos": "VER", "rating": 80},
        {"id": 24, "name": "Jusuf Gazibegovic", "club": "Sturm Graz", "pos": "VER", "rating": 79},
        {"id": 25, "name": "Emanuel Aiwu", "club": "Sturm Graz", "pos": "VER", "rating": 78},
        {"id": 26, "name": "Jon Gorenc Stankovic", "club": "Sturm Graz", "pos": "MF", "rating": 82},
        {"id": 27, "name": "Otar Kiteishvili", "club": "Sturm Graz", "pos": "MF", "rating": 83},
        {"id": 28, "name": "Tomi Horvat", "club": "Sturm Graz", "pos": "MF", "rating": 80},
        {"id": 29, "name": "Mika Biereth", "club": "Sturm Graz", "pos": "ST", "rating": 81},
        {"id": 30, "name": "Seedy Jatta", "club": "Sturm Graz", "pos": "ST", "rating": 76},
        {"id": 31, "name": "William Bøving", "club": "Sturm Graz", "pos": "ST", "rating": 77},
        {"id": 32, "name": "Niklas Hedl", "club": "Rapid Wien", "pos": "TW", "rating": 80},
        {"id": 33, "name": "Serge-Philippe Raux-Yao", "club": "Rapid Wien", "pos": "VER", "rating": 79},
        {"id": 34, "name": "Nenad Cvetkovic", "club": "Rapid Wien", "pos": "VER", "rating": 78},
        {"id": 35, "name": "Bendegúz Bolla", "club": "Rapid Wien", "pos": "VER", "rating": 77},
        {"id": 36, "name": "Lukas Grgic", "club": "Rapid Wien", "pos": "MF", "rating": 78},
        {"id": 37, "name": "Mamadou Sangare", "club": "Rapid Wien", "pos": "MF", "rating": 79},
        {"id": 38, "name": "Matthias Seidl", "club": "Rapid Wien", "pos": "MF", "rating": 81},
        {"id": 39, "name": "Guido Burgstaller", "club": "Rapid Wien", "pos": "ST", "rating": 79},
        {"id": 40, "name": "Dion Drena Beljo", "club": "Rapid Wien", "pos": "ST", "rating": 78},
        {"id": 41, "name": "Louis Schaub", "club": "Rapid Wien", "pos": "MF", "rating": 77},
        {"id": 42, "name": "Samuel Sahin-Radlinger", "club": "Austria Wien", "pos": "TW", "rating": 76},
        {"id": 43, "name": "Lucas Galvao", "club": "Austria Wien", "pos": "VER", "rating": 76},
        {"id": 44, "name": "Reinhold Ranftl", "club": "Austria Wien", "pos": "VER", "rating": 77},
        {"id": 45, "name": "Tin Plavotic", "club": "Austria Wien", "pos": "VER", "rating": 74},
        {"id": 46, "name": "Manfred Fischer", "club": "Austria Wien", "pos": "MF", "rating": 77},
        {"id": 47, "name": "Abu Barry", "club": "Austria Wien", "pos": "MF", "rating": 75},
        {"id": 48, "name": "Dominik Fitz", "club": "Austria Wien", "pos": "MF", "rating": 80},
        {"id": 49, "name": "Maurice Malone", "club": "Austria Wien", "pos": "ST", "rating": 76},
        {"id": 50, "name": "Nik Prelec", "club": "Austria Wien", "pos": "ST", "rating": 75},
        {"id": 51, "name": "Hakim Guenouche", "club": "Austria Wien", "pos": "VER", "rating": 73},
        {"id": 52, "name": "Jörg Siebenhandl", "club": "LASK", "pos": "TW", "rating": 75},
        {"id": 53, "name": "Philipp Ziereis", "club": "LASK", "pos": "VER", "rating": 77},
        {"id": 54, "name": "Andrés Andrade", "club": "LASK", "pos": "VER", "rating": 78},
        {"id": 55, "name": "George Bello", "club": "LASK", "pos": "VER", "rating": 74},
        {"id": 56, "name": "Robert Zulj", "club": "LASK", "pos": "MF", "rating": 82},
        {"id": 57, "name": "Sascha Horvath", "club": "LASK", "pos": "MF", "rating": 78},
        {"id": 58, "name": "Valon Berisha", "club": "LASK", "pos": "MF", "rating": 77},
        {"id": 59, "name": "Marin Ljubicic", "club": "LASK", "pos": "ST", "rating": 79},
        {"id": 60, "name": "Moses Usor", "club": "LASK", "pos": "ST", "rating": 76},
        {"id": 61, "name": "Melayro Bogarde", "club": "LASK", "pos": "VER", "rating": 74},
        {"id": 62, "name": "Andreas Leitner", "club": "SV Ried", "pos": "TW", "rating": 73},
        {"id": 63, "name": "Oliver Steurer", "club": "SV Ried", "pos": "VER", "rating": 72},
        {"id": 64, "name": "Nikki Havenaar", "club": "SV Ried", "pos": "VER", "rating": 71},
        {"id": 65, "name": "Fabian Wohlmuth", "club": "SV Ried", "pos": "VER", "rating": 72},
        {"id": 66, "name": "Stefan Nutz", "club": "SV Ried", "pos": "MF", "rating": 75},
        {"id": 67, "name": "Philipp Pomer", "club": "SV Ried", "pos": "MF", "rating": 72},
        {"id": 68, "name": "Ante Bajic", "club": "SV Ried", "pos": "ST", "rating": 74},
        {"id": 69, "name": "Wilfried Eza", "club": "SV Ried", "pos": "ST", "rating": 73},
        {"id": 70, "name": "David Bumberger", "club": "SV Ried", "pos": "VER", "rating": 70},
        {"id": 71, "name": "Dejan Stojanovic", "club": "SCR Altach", "pos": "TW", "rating": 74},
        {"id": 72, "name": "Constantin Reiner", "club": "SCR Altach", "pos": "VER", "rating": 73},
        {"id": 73, "name": "Paul Koller", "club": "SCR Altach", "pos": "VER", "rating": 74},
        {"id": 74, "name": "Sandro Ingolitsch", "club": "SCR Altach", "pos": "VER", "rating": 72},
        {"id": 75, "name": "Vesel Demaku", "club": "SCR Altach", "pos": "MF", "rating": 73},
        {"id": 76, "name": "Mike-Steven Bähre", "club": "SCR Altach", "pos": "MF", "rating": 72},
        {"id": 77, "name": "Sofian Bahloul", "club": "SCR Altach", "pos": "MF", "rating": 73},
        {"id": 78, "name": "Lukas Fridrikas", "club": "SCR Altach", "pos": "ST", "rating": 74},
        {"id": 79, "name": "Athe Nuhiu", "club": "SCR Altach", "pos": "ST", "rating": 71},
        {"id": 80, "name": "Christian Gebauer", "club": "SCR Altach", "pos": "ST", "rating": 72}
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
        random.shuffle(players)
        
        for b in range(1, 5):
            st.session_state.all_boosters[b] = {}
            for p in range(4):
                start_idx = (b - 1) * 20 + p * 5
                st.session_state.all_boosters[b][p] = players[start_idx : start_idx + 5]
        
        st.session_state.current_packs = st.session_state.all_boosters[1].copy()
        st.session_state.game_started = True
        st.rerun()

# Aktiver Draft
elif st.session_state.booster_num <= 4:
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
                    # Name hervorgehoben
                    st.markdown(f"### {card['name']}")
                    
                    # Position und Verein deutlich sichtbar als Farb-Badges
                    st.markdown(f"📍 **Position:** `{card['pos']}`")
                    st.markdown(f"🛡️ **Verein: **`{card['club']}`")
                    
                    # Stärke groß als Metric
                    st.metric(label="Gesamtstärke", value=f"⭐ {card['rating']}")
                    
                    btn_key = f"b{st.session_state.booster_num}_p{st.session_state.pick_num}_{card['id']}"
                    if st.button(f"Pick", key=btn_key, type="primary", use_container_width=True):
                        st.session_state.teams[player_id].append(card)
                        st.session_state.picks_made[player_id] = card
                        st.rerun()

    if all(pick is not None for pick in st.session_state.picks_made.values()):
        for p_id in range(4):
            picked_card = st.session_state.picks_made[p_id]
            st.session_state.current_packs[p_id] = [
                c for c in st.session_state.current_packs[p_id] if c['id'] != picked_card['id']
            ]
        
        if len(st.session_state.current_packs[0]) == 0:
            st.session_state.booster_num += 1
            st.session_state.pick_num = 1
            if st.session_state.booster_num <= 4:
                st.session_state.current_packs = st.session_state.all_boosters[st.session_state.booster_num].copy()
                st.toast(f"🎉 Booster {st.session_state.booster_num - 1} fertig! Öffne Booster {st.session_state.booster_num}...")
        else:
            old_packs = st.session_state.current_packs.copy()
            for p_id in range(4):
                if st.session_state.booster_num % 2 != 0:
                    st.session_state.current_packs[(p_id + 1) % 4] = old_packs[p_id]
                else:
                    st.session_state.current_packs[(p_id - 1) % 4] = old_packs[p_id]
            
            st.session_state.pick_num += 1

        st.session_state.picks_made = {0: None, 1: None, 2: None, 3: None}
        st.rerun()

    # Zwischenstand-Kader
    st.divider()
    st.subheader(f"Dein bisheriger Kader ({len(st.session_state.teams[player_id])} / 20 Spieler):")
    my_team = st.session_state.teams[player_id]
    if my_team:
        team_cols = st.columns(4)
        positions = ["TW", "VER", "MF", "ST"]
        for i, pos in enumerate(positions):
            with team_cols[i]:
                st.write(f"**{pos}:**")
                for p in [x for x in my_team if x['pos'] == pos]:
                    st.write(f"• **{p['name']}** ({p['rating']}) — *{p['club']}*")

# Endbildschirm & Aufstellung
else:
    
    st.success("🏆 **DRAFT BEENDET!** Alle 80 Spieler wurden gedraftet.")
    
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
    positions = ["TW", "VER", "MF", "ST"]
    
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
                    st.write(f"• **{p['name']}** ({p['pos']}, {p['rating']}) — *{p['club']}*")
