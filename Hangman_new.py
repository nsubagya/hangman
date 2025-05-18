import random as rand
import streamlit as st
from hangman_arts import logo, stages
from hangman_words import english_word_list

# Initialize game state
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
if 'input_key' not in st.session_state:
    st.session_state.input_key = 0  # For resetting input box

# Title and logo
st.title("Hangman Game")
st.text(logo)

# Show current hangman ASCII art for current lives
st.text(stages[st.session_state.lives])

# Show current game state
st.write(f"Word length: {len(st.session_state.random_word)}")
st.write(f"Word guessed so far: {' '.join(st.session_state.display)}")
st.write(f"Lives remaining: {st.session_state.lives}")
st.write(f"Incorrect guesses: {', '.join(st.session_state.non_correct_letters)}")

# Container to hold warning or info messages for repeated guesses
message_placeholder = st.empty()

if not st.session_state.win_game and st.session_state.lives > 0:
    # Guess input field with dynamic key to clear on reset
    guess = st.text_input("Guess a letter:", key=f"guess_input_{st.session_state.input_key}").lower()

    if guess:
        # Check if already guessed
        if guess in st.session_state.display or guess in st.session_state.non_correct_letters:
            message_placeholder.warning(f"You've already guessed the letter '{guess}'. Try another one.")
        # Correct guess
        elif guess in st.session_state.random_word:
            for idx, letter in enumerate(st.session_state.random_word):
                if letter == guess:
                    st.session_state.display[idx] = letter
            if '_' not in st.session_state.display:
                st.session_state.win_game = True
                st.success("Congratulations! You won the game!")
            # Clear input after processing
            st.session_state.input_key += 1
            st.rerun()
        # Incorrect guess
        else:
            st.session_state.lives -= 1
            st.session_state.non_correct_letters.append(guess)
            st.error(f"The letter '{guess}' is not in the word.")
            # Update hangman image
            st.text(stages[st.session_state.lives])
            if st.session_state.lives == 0:
                st.error(f"Game Over! The word was **{st.session_state.random_word}**")
            # Clear input after processing
            st.session_state.input_key += 1
            st.rerun()

else:
    # Game ended (win or lose)
    if st.session_state.win_game:
        st.success("You've won! Well done!")
    else:
        st.error(f"Game Over! The word was **{st.session_state.random_word}**")

# Reset button
if st.button('Reset Game'):
    st.session_state.lives = 6
    st.session_state.non_correct_letters = []
    st.session_state.random_word = rand.choice(english_word_list).lower()
    st.session_state.display = ['_'] * len(st.session_state.random_word)
    st.session_state.win_game = False
    st.session_state.input_key += 1  # Change key to reset input box
    st.rerun()
