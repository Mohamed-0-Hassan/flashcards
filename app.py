import random
import streamlit as st
import json
from gtts import gTTS

# Load the vocabulary data (ensure JSON file path is correct)
with open('dutch_german_vocab.json', 'r') as f:
    vocab = json.load(f)

# Initialize session state for the word pair and the display language
if 'word_pair' not in st.session_state:
    st.session_state['word_pair'] = random.choice(vocab)
if 'random_language' not in st.session_state:
    st.session_state['random_language'] = random.choice(["Dutch", "German"])
if 'revealed' not in st.session_state:
    st.session_state['revealed'] = False

# Streamlit App
st.title("Dutch-German Flashcards with Audio")


# Function to generate and play audio
def play_audio(text, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save("word.mp3")
    audio_file = open("word.mp3", "rb")
    audio_bytes = audio_file.read()
    st.audio(audio_bytes, format="audio/mp3")


# Display the current word and provide options for audio and reveal
if st.session_state['random_language'] == "Dutch":
    st.write(f"**Dutch:** {st.session_state['word_pair']['Dutch']}")

    if st.button("Play Dutch Audio"):
        play_audio(st.session_state['word_pair']['Dutch'], 'nl')

    # Only reveal German word if the button is pressed
    if st.button("Reveal German"):
        st.write(f"**German:** {st.session_state['word_pair']['German']}")
        st.session_state['revealed'] = True

    if st.session_state['revealed']:
        if st.button("Play German Audio"):
            play_audio(st.session_state['word_pair']['German'], 'de')
else:
    st.write(f"**German:** {st.session_state['word_pair']['German']}")

    if st.button("Play German Audio"):
        play_audio(st.session_state['word_pair']['German'], 'de')

    # Only reveal Dutch word if the button is pressed
    if st.button("Reveal Dutch"):
        st.write(f"**Dutch:** {st.session_state['word_pair']['Dutch']}")
        st.session_state['revealed'] = True

    if st.session_state['revealed']:
        if st.button("Play Dutch Audio"):
            play_audio(st.session_state['word_pair']['Dutch'], 'nl')

# Option to display another flashcard
if st.button("Next Flashcard"):
    # Reset the session state and load a new word pair
    st.session_state['word_pair'] = random.choice(vocab)
    st.session_state['random_language'] = random.choice(["Dutch", "German"])
    st.session_state['revealed'] = False
    st.rerun()
