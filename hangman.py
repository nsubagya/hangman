import random as rand
import streamlit as st
from hangman_arts import logo, stages
from hangman_words import english_word_list

# ---------------------- Initialization ----------------------
if 'lives' not in st.session_state:
    st.session_state.lives = 6
    st.session_state.random_word = rand.choice(english_word_list).lower()
    st.session_state.display = ['_'] * len(st.session_state.random_word)
    st.session_state.non_correct_letters = []
    st.session_state.win_game = False
    st.session_state.guess = ""

# ---------------------- Title & Logo ----------------------
st.title("🎯 Hangman Game")
st.write(logo)

# ---------------------- Display Status ----------------------
st.write(f"Word length: {len(st.session_state.random_word)}")
st.write(f"Word guessed so far: {' '.join(st.session_state.display)}")
st.write(f"Lives remaining: {st.session_state.lives}")
st.write(f"Incorrect guesses: {', '.join(st.session_state.non_correct_letters)}")

# ---------------------- Input Section ----------------------
guess = st.text_input("Guess a letter: ").lower()

if guess:
    if guess in st.session_state.display:
        st.warning(f"You already guessed '{guess}' correctly.")
    elif guess in st.session_state.non_correct_letters:
        st.warning(f"You already guessed '{guess}' and it was incorrect.")
    elif guess in st.session_state.random_word:
        for index, letter in enumerate(st.session_state.random_word):
            if letter == guess:
                st.session_state.display[index] = letter
        if '_' not in st.session_state.display:
            st.session_state.win_game = True
            st.success("🎉 You won!")
    else:
        st.session_state.lives -= 1
        st.session_state.non_correct_letters.append(guess)
        st.error(f"'{guess}' is not in the word.")
        st.write(stages[st.session_state.lives])

    # Clear the input to avoid multiple processing
    st.experimental_rerun()

# ---------------------- Game Over Check ----------------------
if st.session_state.lives == 0:
    st.error(f"☠️ Game Over! The word was: **{st.session_state.random_word}**")
    st.write(stages[0])

# ---------------------- Reset Game ----------------------
if st.button("🔁 Reset Game"):
    for key in ['lives', 'random_word', 'display', 'non_correct_letters', 'win_game', 'guess']:
        st.session_state.pop(key, None)
    st.experimental_rerun()
