import streamlit as st
import random

def winner(player_choice, ai_choice):
    if player_choice == ai_choice:
        return "It's a tie!"
    elif (
        (player_choice == "Rock" and ai_choice == "Scissors")
        or (player_choice == "Paper" and ai_choice == "Rock")
        or (player_choice == "Scissors" and ai_choice == "Paper")
    ):
        return "You win!"
    else:
        return "You lose!"

def main():
    st.title("Rock, Paper, Scissors Game")

    # Initialize score
    if "score" not in st.session_state:
        st.session_state.score = {"player": 0, "ai": 0}

    # What player picked
    player_choice = st.radio("Choose your move:", ["Rock", "Paper", "Scissors"])

    # What AI picked
    ai_choice = random.choice(["Rock", "Paper", "Scissors"])

    # Determine winner
    result = winner(player_choice, ai_choice)

    # Update score
    if result == "You win!":
        st.session_state.score["player"] += 1
    elif result == "You lose!":
        st.session_state.score["ai"] += 1

    # Results
    st.write(f"You chose: {player_choice}")
    st.write(f"AI chose: {ai_choice}")
    st.write(result)
    st.write(f"Score: Player {st.session_state.score['player']} - {st.session_state.score['ai']} AI")

    # Reset button
    if st.button("Reset Score"):
        st.session_state.score = {"player": 0, "ai": 0}

if __name__ == "__main__":
    main()
