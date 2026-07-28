# Strategy: predict the opponent's next move from their recent move history, then play whatever beats that prediction.

BEATS = {"R": "P", "P": "S", "S": "R"}  # BEATS[x] = the move that beats x


def player(prev_play, opponent_history=[]):
    # Persistent dectionary to store patterns
    patterns = getattr(player, "patterns", {})
    player.patterns = patterns  # Ensure it persists between calls
    
    n = 3  # Number of recent moves to define the pattern key
    
    if prev_play == "":
        opponent_history.clear()
        patterns.clear()
        return "R"

    # Append prev_play to opponent_history
    opponent_history.append(prev_play)

    # Define the pattern key
    if len(opponent_history) >= n:
        key = "".join(opponent_history[-n:])
    else:
        key = "".join(opponent_history)

    # Update the patterns dictionary with the current key and previous play
    if key not in patterns:
        patterns[key] = {"R": 0, "P": 0, "S": 0}
    if len(opponent_history) > n:
        prev_key = "".join(opponent_history[-n-1:-1])
        patterns[prev_key][prev_play] += 1

    # Predict next move based on the most frequent move that followed the current key
    if key in patterns:
        prediction = max(patterns[key], key=patterns[key].get)
    else:
        prediction = "R"

    # Return the move that beats the prediction
    return BEATS[prediction]
