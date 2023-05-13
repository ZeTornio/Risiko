# Probabilities in Risiko
Ever wondered which are the probabilities in Risiko?
Here you can find the answer!

The code is generalized, you can choose the type of dice (_n_ faces), the number of dice of the attacker (_m\_att_) and of the defender (_m\_def_).
The approach is not pure brute-force, but rather considering all distinct cases and giving them the proper weights. In this way we can reduce looping but we involve factorials, so beware of choosing very big parameters that can lead to overflow. 

Let's see some results!

## Standard Risiko (D6)
The results are provided in the following format:
#### Attacker's dice VS Defender's dice
* Tanks won by attacker-Tanks won by defender:  probability \[cases\].
#### 1 VS 1
* 0-1: 0.58 \[21\]
* 1-0: 0.42 \[15\]
#### 1 VS 2
*

<table>
  <tr>
    <td></td>
    <td>Attacker's dice</td>
    <td colspan='3'>1</td>
    <td colspan='3'>2</td>
    <td colspan='3'>3</td>
  </tr>
  <tr>
    <td></td>
    <td>Defender's dice</td>
    <td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td><td>1</td><td>2</td><td>3</td>
  </tr>
  <tr>
    <td rowspan='9' >Results</td><td>1-0</td><td></td><td></td><td></td> <td></td><td>-</td><td>-</td> <td></td><td>-</td><td>-</td>
  </tr>
  <tr><td>0-1</td> <td></td><td></td><td></td>  <td></td><td>-</td><td>-</td>  <td></td><td>-</td><td>-</td></tr>
  
  <tr><td>2-0</td> <td>-</td><td>-</td><td>-</td>  <td>-</td><td></td><td>-</td>  <td>-</td><td></td><td>-</td></tr>
  <tr><td>1-1</td> <td>-</td><td>-</td><td>-</td>  <td>-</td><td></td><td>-</td>  <td>-</td><td></td><td>-</td></tr>
  <tr><td>0-2</td> <td>-</td><td>-</td><td>-</td>  <td>-</td><td></td><td>-</td>  <td>-</td><td></td><td>-</td></tr>
  
  <tr><td>3-0</td> <td>-</td><td>-</td><td>-</td>  <td>-</td><td></td><td>-</td>  <td>-</td><td>-</td><td></td></tr>
  <tr><td>2-1</td> <td>-</td><td>-</td><td>-</td>  <td>-</td><td></td><td>-</td>  <td>-</td><td>-</td><td></td></tr>
  <tr><td>1-2</td> <td>-</td><td>-</td><td>-</td>  <td>-</td><td></td><td>-</td>  <td>-</td><td>-</td><td></td></tr>
  <tr><td>0-3</td> <td>-</td><td>-</td><td>-</td>  <td>-</td><td></td><td>-</td>  <td>-</td><td>-</td><td></td></tr>
</table>
