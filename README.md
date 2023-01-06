# Bitcoin Simulation Scripts

## Selfish Mining 
Here is the strategy we adopted : 
S mines a block on top of the last block of the official blockchain.
If H mines a block before S, S goes back to the beginning of the cycle (end of the current cycle).
If S mines a block first, S continues to secretly mine on top of her own secret block.
If S mines a block first but H mines a block before S can mine a second one, S immediately broadcasts her secret block. A competition between the two blocks follows. After the competition is resolved, S goes back to the beginning of the cycle (end of the current cycle).
If S mines two blocks in a row, S continues to secretly mine on top of her own secret fork.
When the number of blocks mined by S falls behind the number mined by H by only 1, S broadcasts her entire secret fork (end of the current cycle).

Here is the results obtained, we see constant improvements and interesting results adoption this selfish mining strategy. 
<img width="492" alt="selfish_mining" src="https://user-images.githubusercontent.com/72081305/211069623-36547bd9-e3ed-4ff6-a703-829e198a951d.PNG">
## Optimal Mining 
Here is a graphical simulation that can be obtained with the script cryptofinance_optimal_mining.ipynb
 <img width="511" alt="optimal_mining" src="https://user-images.githubusercontent.com/72081305/211068477-4bf41665-1ce2-4a2f-a9ce-69086cd870b6.PNG">

We notice that the curve grows after 0.4, So, we have E(0, 0, n, q, q) > 0 for q >= 0.42 in this simulation

## One plus Two
In this simumlation we obtained two graphics : one that we simulated, and another theorical that is supposed to follow the same pattern obtained in the one we simulated.
Here is the Graphical Simulation.
<img width="458" alt="one+two_simulation" src="https://user-images.githubusercontent.com/72081305/211070390-f589987e-ce74-48d2-92f4-d3a5d2376853.PNG">
Here is the Theorical Simulation.


We find a very high correlation between these two graphics.
<img width="430" alt="one+two_theorical" src="https://user-images.githubusercontent.com/72081305/211070401-1a32a09a-28c6-4da7-b91e-1ac57199a791.PNG">
