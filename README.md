# Probabilities in Risiko
Ever wondered which are the probabilities in Risiko?
Here you can find the answer!

The code is generalized, you can choose the type of dice (_n_ faces), the number of dice of the attacker (_m\_att_) and of the defender (_m\_def_).
The approach is not pure brute-force, but rather considering all distinct cases and giving them the proper weights. In this way we can reduce looping but we involve factorials, so beware of choosing very big parameters that can lead to overflow. 

Let's see some results!

## Standard Risiko (D6)
The results are provided in the following format:
#### Attacker's dice VS Defender's dice
* Tanks won by attacker-Tanks won by defender: cases, probability.
