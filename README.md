# forest-fire
Cellular automaton forest-fire model. The rules are:
- White cells ("trees") grow spontaneously from black ("empty") cells with probability p.
- They ignite ("struck by lightning") spontaneously with probability f, becoming red ("burning") cells for one iteration.
- Any cell with a burning Moore neighbor will ignite in the next iteration.
- Any currently burning cell will blacken in the next iteration.

Behavior depends heavily on the parametric ratio p/f: for p>>f, the model may display so-called self-organized criticality.
Saves the model as an .mp4 using x264 encoding. The average density of each iteration is also saved to a text file.
