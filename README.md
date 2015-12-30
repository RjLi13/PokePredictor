# PokePredictor

Purpose: E[Z]

Our goal is to make a simple webapp that calculates the expected values of each of your possible moves in pokemon showdown. This includes
* dealing damage ( up to 4 possible attacks )
* buffing / debuffing ( moves that change a pokemon's stats )
* effect changing ( abilities that manipulate some aspect of the game such as rain dance, toxic spikes etc )
* switching ( up to 5 possible switches )

Factors that go into the choice include:
* type of the move
* type of the defending pokemon
* stats of pokemon
* stats of defending pokemon
* current probability of winning ( and thus tendency of taking chances vs. playing it safe )

With these expected values, our hope is to create a simple AI that would always take the best possible move to win the game.

We hope to:
* apply our knowledge of expected values and probability from CS70
* look into basic AI ( prep for CS188? )
* create a web app with simple UI


