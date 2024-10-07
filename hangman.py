import streamlit as st
import random as rand

# Import your word list and hangman art (stages)
from hangman_arts import logo, stages
from hangman_words import english_word_list

# Define game variables
if "random_word" not in st.session_state:
    st.session_state.random_word = rand.choice(english_word_list).lower()
    st.session_state.random_word_length = len(st.session_state.random_word)
    st.session_state.display = ['_'] * st.session_state.random_word_length
    st.session_state.lives = 6
    st.session_state.win_game = False
    st.session_state.non_correct_letters = []

# Clear previous guesses and set up the header
st.title("Hangman Game")
st.write(logo)

# Function to reset the game
def reset_game():
    st.session_state.random_word = rand.choice(english_word_list).lower()
    st.session_state.random_word_length = len(st.session_state.random_word)
    st.session_state.display = ['_'] * st.session_state.random_word_length
    st.session_state.lives = 6
    st.session_state.win_game = False
    st.session_state.non_correct_letters = []
    st.experimental_rerun()

# Display the word and incorrect guesses
st.write(f"Word length: {st.session_state.random_word_length}")
st.write(" ".join(st.session_state.display))
st.write(f"Lives remaining: {st.session_state.lives}")
st.write(f"Incorrect guesses: {', '.join(st.session_state.non_correct_letters)}")

# Take user input for guesses
guess = st.text_input("Guess a letter:").lower()

if st.button("Submit Guess") and not st.session_state.win_game and st.session_state.lives > 0:
    if guess in st.session_state.display:
        st.warning(f"You already guessed the letter '{guess}'")

    elif guess in st.session_state.non_correct_letters:
        st.warning(f"You already guessed the incorrect letter '{guess}'")

    elif guess in st.session_state.random_word:
        for index, letter in enumerate(st.session_state.random_word):
            if letter == guess:
                st.session_state.display[index] = letter
        if '_' not in st.session_state.display:
            st.session_state.win_game = True
            st.success("Congratulations, you won!")
    else:
        st.session_state.lives -= 1
        st.session_state.non_correct_letters.append(guess)
        st.write(stages[st.session_state.lives])

        if st.session_state.lives == 0:
            st.error("Sorry, you lost. The word was: " + st.session_state.random_word)

    # Clear the input after submission
    st.experimental_rerun()

# Game status messages
if st.session_state.win_game:
    st.balloons()
    st.success(f"You've won! The word was: {st.session_state.random_word}")

elif st.session_state.lives == 0:
    st.error(f"Game Over! The word was: {st.session_state.random_word}")

# Button to reset the game
st.button("Restart Game", on_click=reset_game)
