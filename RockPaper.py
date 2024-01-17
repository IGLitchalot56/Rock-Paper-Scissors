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

#def main():
st.title("Rock, Paper, Scissors Game")

# Initialize score
score = {"player": 0, "ai": 0}

# what played picked
player_choice = st.radio("Choose your move:", ["Rock", "Paper", "Scissors"])

# what ai picked
ai_choice = random.choice(["Rock", "Paper", "Scissors"])

# determine winner
result = winner(player_choice, ai_choice)

# Upd score
if result == "You win!":
    score["player"] += 1
elif result == "You lose!":
    score["ai"] += 1

# results
st.write(f"You chose: {player_choice}")
st.write(f"AI chose: {ai_choice}")
st.write(result)
st.write(f"Score: Player {score['player']} - {score['ai']} AI")

#if __name__ == "__main__":
    #main()