import random as rand
import streamlit as st
from hangman_arts import logo, stages
from hangman_words import english_word_list

# --------- Game State Initialization ---------
if 'random_word' not in st.session_state:
    st.session_state.random_word = rand.choice(english_word_list).lower()

if 'display' not in st.session_state:
    st.session_state.display = ['_'] * len(st.session_state.random_word)

if 'lives' not in st.session_state:
    st.session_state.lives = 6

if 'non_correct_letters' not in st.session_state:
    st.session_state.non_correct_letters = []

if 'win_game' not in st.session_state:
    st.session_state.win_game = False

# --------- Display UI ---------
st.title("Hangman Game")
st.write(logo)

st.write(f"Word length: {len(st.session_state.random_word)}")
st.write(f"Word guessed so far: {' '.join(st.session_state.display)}")
st.write(f"Lives remaining: {st.session_state.lives}")
st.write(f"Incorrect guesses: {', '.join(st.session_state.non_correct_letters)}")

# --------- Game Logic ---------
if not st.session_state.win_game and st.session_state.lives > 0:
    guess = st.text_input("Guess a letter: ").lower()

    if guess:
        if guess in st.session_state.display:
            st.warning(f"You've already guessed the letter '{guess}'. Try another one.")
        elif guess in st.session_state.non_correct_letters:
            st.warning(f"You've already guessed the letter '{guess}' incorrectly. Try another one.")
        elif guess in st.session_state.random_word:
            for index, letter in enumerate(st.session_state.random_word):
                if letter == guess:
                    st.session_state.display[index] = letter
            if '_' not in st.session_state.display:
                st.success("🎉 Congratulations! You've won the game!")
                st.session_state.win_game = True
        else:
            st.session_state.lives -= 1
            st.session_state.non_correct_letters.append(guess)
            st.error(f"❌ The letter '{guess}' is not in the word.")
            st.write(stages[st.session_state.lives])

        # Game over check
        if st.session_state.lives == 0:
            st.error(f"💀 Game over! The word was '{st.session_state.random_word}'.")
            st.write(stages[0])

# --------- Display Status Again ---------
st.write(f"Word so far: {' '.join(st.session_state.display)}")
st.write(f"Lives remaining: {st.session_state.lives}")
st.write(f"Incorrect guesses: {', '.join(st.session_state.non_correct_letters)}")

# --------- Reset Button ---------
if st.button('🔁 Reset Game'):
    st.session_state.clear()
    st.experimental_rerun()
