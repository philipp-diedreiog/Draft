import streamlit as st
import random

# Seite konfigurieren
st.set_page_config(page_title="Ö-Bundesliga 2P Draft", layout="wide")

POSITIONS = ["TW", "VER", "MF", "ST"]

POS_COLORS = {
    "TW": "#FF4B4B",   # Rot
    "VER": "#28A745",  # Grün
    "MF": "#1E88E5",   # Blau
    "ST": "#D4AC0D"    # Gelb/Gold
}

@st.cache_data
def load_players():
    return [
        # GAK
        {"id": 1, "name": "STANKOVIC", "club": "GAK", "pos": "TW"},
        {"id": 2, "name": "OWUSU", "club": "GAK", "pos": "VER"},
        {"id": 3, "name": "PINES", "club": "GAK", "pos": "VER"},
        {"id": 4, "name": "VRAA JENSEN", "club": "GAK", "pos": "VER"},
        {"id": 5, "name": "KLASSEN", "club": "GAK", "pos": "VER"},
        {"id": 6, "name": "HERMESH", "club": "GAK", "pos": "MF"},
        {"id": 7, "name": "MICHORL", "club": "GAK", "pos": "MF"},
        {"id": 8, "name": "ANDERSON", "club": "GAK", "pos": "MF"},
        {"id": 9, "name": "LICHTENBERGER", "club": "GAK", "pos": "ST"},
        {"id": 10, "name": "HOFLEITNER", "club": "GAK", "pos": "ST"},
        {"id": 11, "name": "GROSSE", "club": "GAK", "pos": "ST"},

        # LASK
        {"id": 12, "name": "JUNGWIRTH", "club": "LASK", "pos": "TW"},
        {"id": 13, "name": "NICH", "club": "LASK", "pos": "VER"},
        {"id": 14, "name": "ANDRADE", "club": "LASK", "pos": "VER"},
        {"id": 15, "name": "MBUYAMBA", "club": "LASK", "pos": "VER"},
        {"id": 16, "name": "JORGENSEN", "club": "LASK", "pos": "VER"},
        {"id": 17, "name": "LJUBICIC", "club": "LASK", "pos": "MF"},
        {"id": 18, "name": "HORVATH", "club": "LASK", "pos": "MF"},
        {"id": 19, "name": "BOGARDE", "club": "LASK", "pos": "MF"},
        {"id": 20, "name": "USOR", "club": "LASK", "pos": "ST"},
        {"id": 21, "name": "ADENIRAN", "club": "LASK", "pos": "ST"},
        {"id": 22, "name": "LANG", "club": "LASK", "pos": "ST"},

        # Red Bull Salzburg
        {"id": 23, "name": "ZAWIESCHITZKY", "club": "Red Bull Salzburg", "pos": "TW"},
        {"id": 24, "name": "BOMA", "club": "Red Bull Salzburg", "pos": "VER"},
        {"id": 25, "name": "ZABRANSKY", "club": "Red Bull Salzburg", "pos": "VER"},
        {"id": 26, "name": "SCHMID", "club": "Red Bull Salzburg", "pos": "VER"},
        {"id": 27, "name": "VERATSCHNIG", "club": "Red Bull Salzburg", "pos": "VER"},
        {"id": 28, "name": "BARRY", "club": "Red Bull Salzburg", "pos": "MF"},
        {"id": 29, "name": "MAZUREK", "club": "Red Bull Salzburg", "pos": "MF"},
        {"id": 30, "name": "KJAERGAARD", "club": "Red Bull Salzburg", "pos": "MF"},
        {"id": 31, "name": "VERTESSEN", "club": "Red Bull Salzburg", "pos": "ST"},
        {"id": 32, "name": "TABAKOVIC", "club": "Red Bull Salzburg", "pos": "ST"},
        {"id": 33, "name": "KONATE", "club": "Red Bull Salzburg", "pos": "ST"},

        # Austria Wien
        {"id": 34, "name": "RADLINGER", "club": "Austria Wien", "pos": "TW"},
        {"id": 35, "name": "BUHARI", "club": "Austria Wien", "pos": "VER"},
        {"id": 36, "name": "HANDL", "club": "Austria Wien", "pos": "VER"},
        {"id": 37, "name": "DRAGOVIC", "club": "Austria Wien", "pos": "VER"},
        {"id": 38, "name": "RANFTL", "club": "Austria Wien", "pos": "VER"},
        {"id": 39, "name": "WUSTINGER", "club": "Austria Wien", "pos": "MF"},
        {"id": 40, "name": "FISCHER", "club": "Austria Wien", "pos": "MF"},
        {"id": 41, "name": "TAE-SEOK LEE", "club": "Austria Wien", "pos": "MF"},
        {"id": 42, "name": "MARKOVIC", "club": "Austria Wien", "pos": "ST"},
        {"id": 43, "name": "EGGESTEIN", "club": "Austria Wien", "pos": "ST"},
        {"id": 44, "name": "BOATENG", "club": "Austria Wien", "pos": "ST"},

        # Sturm Graz
        {"id": 45, "name": "KHUDYAKOV", "club": "Sturm Graz", "pos": "TW"},
        {"id": 46, "name": "MITCHELL", "club": "Sturm Graz", "pos": "VER"},
        {"id": 47, "name": "PETROVIC", "club": "Sturm Graz", "pos": "VER"},
        {"id": 48, "name": "SOGLO", "club": "Sturm Graz", "pos": "VER"},
        {"id": 49, "name": "MALIC", "club": "Sturm Graz", "pos": "VER"},
        {"id": 50, "name": "STANKOVIC", "club": "Sturm Graz", "pos": "MF"},
        {"id": 51, "name": "WEINHANDL", "club": "Sturm Graz", "pos": "MF"},
        {"id": 52, "name": "SEIDL", "club": "Sturm Graz", "pos": "MF"},
        {"id": 53, "name": "JATTA", "club": "Sturm Graz", "pos": "ST"},
        {"id": 54, "name": "HÖDL", "club": "Sturm Graz", "pos": "ST"},
        {"id": 55, "name": "WEIPER", "club": "Sturm Graz", "pos": "ST"},

        # Rapid Wien
        {"id": 56, "name": "HEDL", "club": "Rapid Wien", "pos": "TW"},
        {"id": 57, "name": "CVETKOVIC", "club": "Rapid Wien", "pos": "VER"},
        {"id": 58, "name": "SCHÖLLER", "club": "Rapid Wien", "pos": "VER"},
        {"id": 59, "name": "BOLLA", "club": "Rapid Wien", "pos": "VER"},
        {"id": 60, "name": "AUER", "club": "Rapid Wien", "pos": "VER"},
        {"id": 61, "name": "SEIDL", "club": "Rapid Wien", "pos": "MF"},
        {"id": 62, "name": "AMANE", "club": "Rapid Wien", "pos": "MF"},
        {"id": 63, "name": "GULLIKSEN", "club": "Rapid Wien", "pos": "MF"},
        {"id": 64, "name": "NOSA DAHL", "club": "Rapid Wien", "pos": "ST"},
        {"id": 65, "name": "KARA", "club": "Rapid Wien", "pos": "ST"},
        {"id": 66, "name": "WURMBRAND", "club": "Rapid Wien", "pos": "ST"},

        # SV Ried
        {"id": 67, "name": "LEITNER", "club": "SV Ried", "pos": "TW"},
        {"id": 68, "name": "CHUKWUDI", "club": "SV Ried", "pos": "VER"},
        {"id": 69, "name": "STEURER", "club": "SV Ried", "pos": "VER"},
        {"id": 70, "name": "SORG", "club": "SV Ried", "pos": "VER"},
        {"id": 71, "name": "MALICSEK", "club": "SV Ried", "pos": "VER"},
        {"id": 72, "name": "SCHWAB", "club": "SV Ried", "pos": "MF"},
        {"id": 73, "name": "MAART", "club": "SV Ried", "pos": "MF"},
        {"id": 74, "name": "NASRAWE", "club": "SV Ried", "pos": "MF"},
        {"id": 75, "name": "RHODES", "club": "SV Ried", "pos": "ST"},
        {"id": 76, "name": "BAJIC", "club": "SV Ried", "pos": "ST"},
        {"id": 77, "name": "AISOWIEREN", "club": "SV Ried", "pos": "ST"},

        # SCR Altach
        {"id": 78, "name": "STOJANOVIC", "club": "SCR Altach", "pos": "TW"},
        {"id": 79, "name": "MILOJEVIC", "club": "SCR Altach", "pos": "VER"},
        {"id": 80, "name": "JÄGER", "club": "SCR Altach", "pos": "VER"},
        {"id": 81, "name": "ZECH", "club": "SCR Altach", "pos": "VER"},
        {"id": 82, "name": "BÖCKLE", "club": "SCR Altach", "pos": "VER"},
        {"id": 83, "name": "DEMAKU", "club": "SCR Altach", "pos": "MF"},
        {"id": 84, "name": "BÄHRE", "club": "SCR Altach", "pos": "MF"},
        {"id": 85, "name": "NIEHOFF", "club": "SCR Altach", "pos": "MF"},
        {"id": 86, "name": "GREIL", "club": "SCR Altach", "pos": "ST"},
        {"id": 87, "name": "DIAWARA", "club": "SCR Altach", "pos": "ST"},
        {"id": 88, "name": "MASSOMBO", "club": "SCR Altach", "pos": "ST"}
    ]

# Session State Initialisierung (2 Spieler)
if 'game_started' not in st.session_state:
    st.session_state.game_started = False
    st.session_state.teams = {0: [], 1: []}
    st.session_state.all_boosters = {1: {}, 2: {}}
    st.session_state.current_packs = {0: [], 1: []}
    st.session_state.picks_made = {0: None, 1: None}
    st.session_state.booster_num = 1
    st.session_state.pick_num = 1
    st.session_state.lineups = {0: {}, 1: {}}

st.title("⚽ Ö-Bundesliga Draft (2-Spieler Testmodus)")

# Sidebar Einstieg
st.sidebar.header("Lobby Einstieg")
player_id = st.sidebar.selectbox(
    "Wähle deinen Sitzplatz am Tisch:", 
    [0, 1], 
    format_func=lambda x: f"Spieler {x+1}"
)

if st.sidebar.button("Draft komplett zurücksetzen"):
    st.session_state.game_started = False
    st.session_state.teams = {0: [], 1: []}
    st.session_state.all_boosters = {1: {}, 2: {}}
    st.session_state.current_packs = {0: [], 1: []}
    st.session_state.picks_made = {0: None, 1: None}
    st.session_state.booster_num = 1
    st.session_state.pick_num = 1
    st.session_state.lineups = {0: {}, 1: {}}
    st.rerun()

# Spielstart
if not st.session_state.game_started:
    st.info("Willkommen! Öffne diese Seite in 2 Browser-Tabs (Spieler 1 und Spieler 2).")
    
    if st.button("🚀 Draft starten (2 Spieler / 2 Booster x 7 Karten)", type="primary"):
        players = load_players()
        random.shuffle(players)
        
        for b in range(1, 3):
            st.session_state.all_boosters[b] = {}
            for p in range(2):
                start_idx = (b - 1) * 14 + p * 7
                st.session_state.all_boosters[b][p] = players[start_idx : start_idx + 7]
        
        st.session_state.current_packs = st.session_state.all_boosters[1].copy()
        st.session_state.game_started = True
        st.rerun()

# Aktiver Draft
elif st.session_state.booster_num <= 2:
    st.header(f"📦 Booster {st.session_state.booster_num} / 2 — Pick {st.session_state.pick_num} / 7")
    st.subheader(f"Du spielst als: **Spieler {player_id + 1}**")
    
    my_pack = st.session_state.current_packs[player_id]
    
    st.markdown("**Status am Tisch:**")
    status_cols = st.columns(2)
    for p_id in range(2):
        has_picked = st.session_state.picks_made[p_id] is not None
        status_cols[p_id].write(f"Spieler {p_id+1}: {'✅ Gewählt' if has_picked else '⏳ Wählt...'}")
    
    st.divider()

    if st.session_state.picks_made[player_id] is not None:
        st.info("👉 Du hast deinen Pick gemacht. Warte auf den anderen Spieler...")
    
    elif len(my_pack) > 0:
        st.subheader(f"Auswahl aus Booster {st.session_state.booster_num}:")
        
        cols = st.columns(len(my_pack))
        for idx, card in enumerate(my_pack):
            with cols[idx]:
                pos_color = POS_COLORS.get(card['pos'], '#000000')
                with st.container(border=True):
                    st.markdown(f"### {card['name']}")
                    st.markdown(
                        f"📍 **Position:** <span style='background-color:{pos_color}; color:white; padding:2px 8px; border-radius:4px; font-weight:bold;'>{card['pos']}</span>", 
                        unsafe_allow_html=True
                    )
                    st.markdown(f"🛡️ **Verein: **")
                    
                    btn_key = f"b{st.session_state.booster_num}_p{st.session_state.pick_num}_{card['id']}"
                    if st.button(f"Pick", key=btn_key, type="primary", use_container_width=True):
                        st.session_state.teams[player_id].append(card)
                        st.session_state.picks_made[player_id] = card
                        st.rerun()

    if all(pick is not None for pick in st.session_state.picks_made.values()):
        for p_id in range(2):
            picked_card = st.session_state.picks_made[p_id]
            st.session_state.current_packs[p_id] = [
                c for c in st.session_state.current_packs[p_id] if c['id'] != picked_card['id']
            ]
        
        if len(st.session_state.current_packs[0]) == 0:
            st.session_state.booster_num += 1
            st.session_state.pick_num = 1
            if st.session_state.booster_num <= 2:
                st.session_state.current_packs = st.session_state.all_boosters[st.session_state.booster_num].copy()
                st.toast(f"🎉 Booster 1 fertig! Starte Booster 2...")
        else:
            old_packs = st.session_state.current_packs.copy()
            st.session_state.current_packs[0] = old_packs[1]
            st.session_state.current_packs[1] = old_packs[0]
            st.session_state.pick_num += 1

        st.session_state.picks_made = {0: None, 1: None}
        st.rerun()

    st.divider()
    st.subheader(f"Dein bisheriger Kader ({len(st.session_state.teams[player_id])} / 14 Spieler):")
    my_team = st.session_state.teams[player_id]
    if my_team:
        team_cols = st.columns(4)
        for i, pos in enumerate(POSITIONS):
            with team_cols[i]:
                pos_color = POS_COLORS.get(pos, '#000000')
                st.markdown(f"<h4 style='color:{pos_color};'>{pos}</h4>", unsafe_allow_html=True)
                for p in [x for x in my_team if x['pos'] == pos]:
                    st.write(f"• **{p['name']}** (*{p['club']}*)")

# Endbildschirm & Aufstellung auf dem Spielfeld
else:
    st.success("🏆 **DRAFT BEENDET!** Alle Booster wurden gewählt.")
    st.header(f"📋 Aufstellungs-Phase — Spieler {player_id + 1}")
    
    my_team = st.session_state.teams[player_id]
    my_lineup = st.session_state.lineups[player_id]

    positions_keys = [
        "st1", "st2", "st3",
        "mf1", "mf2", "mf3",
        "v1", "v2", "v3", "v4",
        "tw"
    ]

    # Dynamische Filterung: Alle Spieler verfügbar, aber keine Mehrfachauswahl
    def get_options_for_pos(current_pos_key):
        selected_elsewhere = [
            val for k, val in my_lineup.items() 
            if k != current_pos_key and val != "-"
        ]
        available = [p['name'] for p in my_team if p['name'] not in selected_elsewhere]
        return ["-"] + sorted(available)

    # Detailliertes Fußballfeld via CSS
    st.markdown("""
        <style>
        .pitch-container {
            background-color: #2e7d32;
            background-image: 
                linear-gradient(rgba(255,255,255,0.15) 2px, transparent 2px),
                linear-gradient(90px, rgba(255,255,255,0.05) 50%, transparent 50%);
            border: 4px solid #ffffff;
            border-radius: 12px;
            padding: 25px 15px;
            position: relative;
            box-shadow: 0 8px 16px rgba(0,0,0,0.3);
            margin-bottom: 25px;
        }
        .center-circle {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 120px;
            height: 120px;
            border: 2px solid rgba(255,255,255,0.4);
            border-radius: 50%;
            pointer-events: none;
        }
        .pitch-divider {
            position: absolute;
            top: 50%;
            left: 0;
            right: 0;
            border-top: 2px solid rgba(255,255,255,0.4);
            pointer-events: none;
        }
        .section-header {
            text-align: center;
            color: #ffffff;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.8);
            font-weight: bold;
            margin-bottom: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.subheader("🟢 Platziere deine Start-11 auf dem Spielfeld (4-3-3):")

    with st.container():
        st.markdown('<div class="pitch-container"><div class="center-circle"></div><div class="pitch-divider"></div>', unsafe_allow_html=True)
        
        # STÜRMER
        st.markdown('<div class="section-header">⚽ STÜRMER</div>', unsafe_allow_html=True)
        col_st1, col_st2, col_st3 = st.columns(3)
        with col_st1:
            my_lineup["st1"] = st.selectbox("Stürmer 1", get_options_for_pos("st1"), key="st1_select")
        with col_st2:
            my_lineup["st2"] = st.selectbox("Stürmer 2", get_options_for_pos("st2"), key="st2_select")
        with col_st3:
            my_lineup["st3"] = st.selectbox("Stürmer 3", get_options_for_pos("st3"), key="st3_select")

        st.markdown("<br>", unsafe_allow_html=True)

        # MITTELFELD
        st.markdown('<div class="section-header">🎯 MITTELFELD</div>', unsafe_allow_html=True)
        col_mf1, col_mf2, col_mf3 = st.columns(3)
        with col_mf1:
            my_lineup["mf1"] = st.selectbox("Mittelfeld 1", get_options_for_pos("mf1"), key="mf1_select")
        with col_mf2:
            my_lineup["mf2"] = st.selectbox("Mittelfeld 2", get_options_for_pos("mf2"), key="mf2_select")
        with col_mf3:
            my_lineup["mf3"] = st.selectbox("Mittelfeld 3", get_options_for_pos("mf3"), key="mf3_select")

        st.markdown("<br>", unsafe_allow_html=True)

        # VERTEIDIGER
        st.markdown('<div class="section-header">🛡️ VERTEIDIGER</div>', unsafe_allow_html=True)
        col_v1, col_v2, col_v3, col_v4 = st.columns(4)
        with col_v1:
            my_lineup["v1"] = st.selectbox("Verteidiger 1", get_options_for_pos("v1"), key="v1_select")
        with col_v2:
            my_lineup["v2"] = st.selectbox("Verteidiger 2", get_options_for_pos("v2"), key="v2_select")
        with col_v3:
            my_lineup["v3"] = st.selectbox("Verteidiger 3", get_options_for_pos("v3"), key="v3_select")
        with col_v4:
            my_lineup["v4"] = st.selectbox("Verteidiger 4", get_options_for_pos("v4"), key="v4_select")

        st.markdown("<br>", unsafe_allow_html=True)

        # TORWART
        st.markdown('<div class="section-header">🧤 TORWART</div>', unsafe_allow_html=True)
        _, col_tw, _ = st.columns([1, 2, 1])
        with col_tw:
            my_lineup["tw"] = st.selectbox("Torwart", get_options_for_pos("tw"), key="tw_select")

        st.markdown('</div>', unsafe_allow_html=True)

    st.divider()
    st.subheader("📊 Übersicht der 2 Teams:")
    
    all_team_cols = st.columns(2)
    for p_id in range(2):
        with all_team_cols[p_id]:
            st.markdown(f"### Spieler {p_id + 1}")
            st.write(f"**Gedraftete Spieler:** {len(st.session_state.teams[p_id])}")
            with st.expander("Gedrafteten Kader anzeigen"):
                for p in st.session_state.teams[p_id]:
                    pos_color = POS_COLORS.get(p['pos'], '#000000')
                    st.markdown(
                        f"• **{p['name']}** (<span style='color:{pos_color}; font-weight:bold;'>{p['pos']}</span>) — *{p['club']}*", 
                        unsafe_allow_html=True
                    )
