import random as rand
import streamlit as st
from hangman_arts import logo, stages
from hangman_words import english_word_list

# ------------------ Initialization ------------------
if 'lives' not in st.session_state:
    st.session_state.lives = 6
if 'random_word' not in st.session_state:
    st.session_state.random_word = rand.choice(english_word_list).lower()
if 'display' not in st.session_state:
    st.session_state.display = ['_'] * len(st.session_state.random_word)
if 'non_correct_letters' not in st.session_state:
    st.session_state.non_correct_letters = []
if 'win_game' not in st.session_state:
    st.session_state.win_game = False
if 'processed_guess' not in st.session_state:
    st.session_state.processed_guess = ''

# ------------------ UI Setup ------------------
st.title("🎯 Hangman Game")
st.write(logo)

st.write(f"**Word length:** {len(st.session_state.random_word)}")
st.write(f"**Word guessed so far:** {' '.join(st.session_state.display)}")
st.write(f"**Lives remaining:** {st.session_state.lives}")
st.write(f"**Incorrect guesses:** {', '.join(st.session_state.non_correct_letters)}")

# ------------------ Guess Input ------------------
guess = st.text_input("Guess a letter:", key='guess_input').lower()

# Only process a new guess if it's different from the last one
if guess and guess != st.session_state.processed_guess and not st.session_state.win_game and st.session_state.lives > 0:
    st.session_state.processed_guess = guess

    if guess in st.session_state.display:
        st.warning(f"⚠️ You already correctly guessed '{guess}'. Try a new letter.")
    elif guess in st.session_state.non_correct_letters:
        st.warning(f"⚠️ You already guessed '{guess}' and it was incorrect.")
    elif guess in st.session_state.random_word:
        for index, letter in enumerate(st.session_state.random_word):
            if letter == guess:
                st.session_state.display[index] = letter
        if '_' not in st.session_state.display:
            st.session_state.win_game = True
            st.success("🎉 Congratulations! You won the game!")
    else:
        st.session_state.lives -= 1
        st.session_state.non_correct_letters.append(guess)
        st.error(f"❌ The letter '{guess}' is not in the word.")
        st.write(stages[st.session_state.lives])
        if st.session_state.lives == 0:
            st.error(f"💀 Game Over! The word was **{st.session_state.random_word}**")

# ------------------ Display Status Again ------------------
st.write(f"**Word so far:** {' '.join(st.session_state.display)}")
st.write(f"**Lives remaining:** {st.session_state.lives}")
st.write(f"**Incorrect guesses:** {', '.join(st.session_state.non_correct_letters)}")

# ------------------ Reset Game ------------------
if st.button("Reset Game"):
    for key in ['lives', 'random_word', 'display', 'non_correct_letters', 'win_game', 'processed_guess']:
        st.session_state.pop(key, None)
    st.experimental_rerun()
