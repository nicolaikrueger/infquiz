import streamlit as st

st.title("Inf-Quiz")

if 'wrong_attempts' not in st.session_state:
    st.session_state.wrong_attempts = 0


# Liste der Rätsel und deren Lösungen
riddles = [
    {"question": "0000111010110010", "answer": "3762", "hint": "Denk daran, es in Dezimal zu konvertieren."},
    {"question": "0xC001D00D", "answer": "3221344269", "hint": "Das ist eine Hexadezimalzahl."},
    {"question": "Hexspeak von 0xC001D00D", "answer": "cool dood", "hint": "Es sieht aus wie Englisch, oder?"},
    {"question": "RGB-Werte von #6495ED als RGB-Schreibweise", "answer": "R100G149B237", "hint": "Hex zu Dezimal konvertieren."},
    {"question": "Als erster richtiger Computer galt?", "answer": "Z3", "hint": "Es war ein deutsches Gerät."},
    {"question": "Welche Zeichenformat nutzt tagesschau.de?", "answer": "UTF-8", "hint": "Es ist ein gängiges Format für Webseiten."},
    {"question": "Der Unicode für Smiling Face with Smiling Eyes?", "answer": "1F60A", "hint": "Es beginnt mit '1F'. Schau in einer Unicode-Tabelle nach."},
    {"question": "Sie haben einen Stack: Push(A); Push(B); Push(C); POP(); Was gibt TOP() aus?", "answer": "B", "hint": "Was bleibt auf dem Stack, nachdem 'C' entfernt wurde?"},
    {"question": "Welches Protokoll wird zum Senden von E-Mails verwendet?", "answer": "SMTP", "hint": "Es ist ein Protokoll für die Übertragung von Nachrichten."},
    {"question": "Wie nennt man den Fehler, wenn eine Variable verwendet wird, bevor sie einen Wert zugewiesen bekommt?", "answer": "null pointer exception", "hint": "Es hat mit 'null' zu tun."},
    {"question": "In welcher Datenstruktur wird das LIFO-Prinzip angewendet?", "answer": "Stack", "hint": "Es ähnelt einem Stapel von Büchern."},
    {"question": "Welche Sprache wird hauptsächlich für Webentwicklung auf der Clientseite verwendet?", "answer": "JavaScript", "hint": "Es ist nicht Java."},
    {"question": "Welche Art von Algorithmus versucht, ein lokales Maximum oder Minimum zu finden?", "answer": "Greedy algorithm", "hint": "Es nimmt immer die derzeit beste Option."},
    {"question": "In welcher Datenbankstruktur sind Daten in Tabellen organisiert?", "answer": "relational database", "hint": "Es hat mit Beziehungen zwischen Daten zu tun."},
    {"question": "Wie nennt man den Prozess, bei dem Programmanweisungen in Maschinencode umgewandelt werden?", "answer": "Compilation", "hint": "Compiler tun das."},
    {"question": "Welches Paradigma basiert auf dem Konzept der 'Objekte', die Daten und Methoden enthalten?", "answer": "Object-oriented programming", "hint": "Es ist ein populäres Programmierparadigma, abgekürzt OOP."},
    {"question": "Welcher Suchalgorithmus teilt ständig die Liste der zu suchenden Elemente?", "answer": "Binary search", "hint": "Es ist effizient für sortierte Listen."},
    {"question": "In welchem Jahr wurde die erste Version von Python veröffentlicht?", "answer": "1991", "hint": "Es war am Anfang der 90er Jahre."}
]

# Initialisierung des aktuellen Rätselindex und des Zustands der richtigen Antwort
if 'current_riddle' not in st.session_state:
    st.session_state.current_riddle = 0
if 'correct_answer' not in st.session_state:
    st.session_state.correct_answer = False
if 'show_hint' not in st.session_state:
    st.session_state.show_hint = False

# Wenn alle Rätsel gelöst sind
if st.session_state.current_riddle >= len(riddles):
    st.write("Alle Rätsel wurden gelöst! Glückwunsch!")

else:
    # Fortschrittsbalken oben auf der Seite
    progress_value = st.session_state.current_riddle / (len(riddles) - 1)
    progress = st.progress(progress_value)

    if st.session_state.correct_answer:  # Wenn die Antwort des aktuellen Rätsels richtig war
        st.success("Richtig")
        if st.button("Weiter"):
            st.session_state.current_riddle += 1
            st.session_state.correct_answer = False
            st.session_state.show_hint = False
            st.experimental_rerun()

    else:  # Zeige das aktuelle Rätsel
        with st.form(key="quiz"):
            st.write("Rätselaufgabe:")
            st.code(riddles[st.session_state.current_riddle]["question"])
            solution_user = st.text_input('Lösung')
            
            if st.form_submit_button('Prüfen'):
              if solution_user == riddles[st.session_state.current_riddle]["answer"]:
                  st.session_state.correct_answer = True
                  st.session_state.wrong_attempts = 0  # Zurücksetzen der falschen Versuche bei richtiger Antwort
                  st.experimental_rerun()
              else:
                  st.session_state.show_hint = True
                  st.session_state.wrong_attempts += 1  # Erhöhen der falschen Versuche bei falscher Antwort


       # Wenn die Antwort falsch ist und show_hint aktiviert ist, zeige den Hinweis
        if st.session_state.show_hint:
          st.error("Falsch")
          st.warning(f"Tip: {riddles[st.session_state.current_riddle]['hint']}")
          if st.session_state.wrong_attempts >= 2:
              if st.button("Zeige Lösung"):
                  st.info(f"Die richtige Lösung ist: {riddles[st.session_state.current_riddle]['answer']}")
