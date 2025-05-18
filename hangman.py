import random as rand
import streamlit as st
from hangman_arts import logo, stages
from hangman_words import english_word_list

# Initialize game state
if 'lives' not in st.session_state:
    st.session_state.lives = 6
if 'display' not in st.session_state:
    random_word = rand.choice(english_word_list).lower()
    st.session_state.random_word = random_word
    st.session_state.display = ['_'] * len(random_word)
if 'non_correct_letters' not in st.session_state:
    st.session_state.non_correct_letters = []
if 'win_game' not in st.session_state:
    st.session_state.win_game = False

# Title and logo
st.title("Hangman Game")
st.write(logo)

# Show the current state of the word
st.write(f"Word length: {len(st.session_state.random_word)}")
st.write(f"Word guessed so far: {' '.join(st.session_state.display)}")

# Lives left and incorrect guesses
st.write(f"Lives remaining: {st.session_state.lives}")
st.write(f"Incorrect guesses: {', '.join(st.session_state.non_correct_letters)}")

# Guess input field
guess = st.text_input("Guess a letter: ").lower()

# Game logic
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
            st.success("Congratulations! You've won the game!")
            st.session_state.win_game = True
    else:
        st.session_state.lives -= 1
        st.session_state.non_correct_letters.append(guess)
        st.error(f"The letter '{guess}' is not in the word. Try again!")
        st.write(stages[st.session_state.lives])

    # Check if game over
    if st.session_state.lives == 0:
        st.error(f"Game over! The word was '{st.session_state.random_word}'.")

# Display current status of the game
st.write(f"Word so far: {' '.join(st.session_state.display)}")
st.write(f"Lives remaining: {st.session_state.lives}")
st.write(f"Incorrect guesses: {', '.join(st.session_state.non_correct_letters)}")

# Reset button
if st.button('Reset Game'):
    st.session_state.lives = 6
    st.session_state.non_correct_letters = []
    random_word = rand.choice(english_word_list).lower()
    st.session_state.random_word = random_word
    st.session_state.display = ['_'] * len(random_word)
    st.session_state.win_game = False
    st.experimental_rerun()
