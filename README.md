# Probabilities in Risiko (and generalization)
Ever wondered which are the probabilities in Risiko?
Here you can find the answer!

The code is generalized, you can choose the type of dice (_n_ faces), the number of dice of the attacker (_m\_att_) and of the defender (_m\_def_).
The approach is not pure brute-force, but rather considering all distinct cases and giving them the proper weights. In this way we can reduce looping but we involve factorials, so beware of choosing very big parameters that can lead to overflow. 

I provide you only the results for "standard" Risiko (max 3 D6s), but I encourage you to see what happens if you chande the number or the type of dice!

```
#To test you can do this in Python. It will automatically print the results!
n_faces_of_dice=6
dice_attacker=3
dice_defender=2

from risiko import Risiko
Risiko(n_faces_of_dice,dice_attacker,dice_defender)
```
## Standard Risiko (D6)
The results are provided in the following format:
#### Attacker's dice VS Defender's dice
* Tanks won by attacker-Tanks won by defender:  probability \[cases\]
#### 1 VS 1
* 0-1: 0.58 \[21\]
* 1-0: 0.42 \[15\]
#### 1 VS 2
* 0-1: 0.75 \[161\]
* 1-0: 0.25 \[45\]
#### 1 VS 3
* 0-1: 0.83 \[1071\]
* 1-0: 0.17 \[225\]
#### 2 VS 1
* 0-1: 0.42 \[91\]
* 1-0: 0.58 \[125\]
#### 3 VS 1
* 0-1: 0.34 \[441\]
* 1-0: 0.66 \[855\]
#### 2 VS 2
* 0-2: 0.45 \[581\]
* 1-1: 0.32 \[420\]
* 2-0: 0.23 \[295\]
#### 2 VS 3
* 0-2: 0.62 \[4816\]
* 1-1: 0.25 \[1981\]
* 2-0: 0.13 \[979\]
#### 3 VS 2
* 0-2: 0.29 \[2275\]
* 1-1: 0.34 \[2611\]
* 2-0: 0.37 \[2890\]
#### 3 VS 3
* 0-3: 0.38 \[17871\]
* 1-2: 0.26 \[12348\]
* 2-1: 0.21 \[10017\]
* 3-0: 0.14 \[6420\]
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
    <td rowspan='9' >Results</td><td>1-0</td><td>0.42</td><td>0.25</td><td>0.17</td> <td>0.58</td><td>-</td><td>-</td> <td>0.66</td><td>-</td><td>-</td>
  </tr>
  <tr><td>0-1</td> <td>0.58</td><td>0.75</td><td>0.83</td>  <td>0.42</td><td>-</td><td>-</td>  <td>0.34</td><td>-</td><td>-</td></tr>
  
  <tr><td>2-0</td> <td>-</td><td>-</td><td>-</td>  <td>-</td><td>0.23</td><td>0.13</td>  <td>-</td><td>0.37</td><td>-</td></tr>
  <tr><td>1-1</td> <td>-</td><td>-</td><td>-</td>  <td>-</td><td>0.32</td><td>0.25</td>  <td>-</td><td>0.34</td><td>-</td></tr>
  <tr><td>0-2</td> <td>-</td><td>-</td><td>-</td>  <td>-</td><td>0.45</td><td>0.62</td>  <td>-</td><td>0.29</td><td>-</td></tr>
  
  <tr><td>3-0</td> <td>-</td><td>-</td><td>-</td>  <td>-</td><td>-</td><td>-</td>  <td>-</td><td>-</td><td>0.14</td></tr>
  <tr><td>2-1</td> <td>-</td><td>-</td><td>-</td>  <td>-</td><td>-</td><td>-</td>  <td>-</td><td>-</td><td>0.21</td></tr>
  <tr><td>1-2</td> <td>-</td><td>-</td><td>-</td>  <td>-</td><td>-</td><td>-</td>  <td>-</td><td>-</td><td>0.26</td></tr>
  <tr><td>0-3</td> <td>-</td><td>-</td><td>-</td>  <td>-</td><td>-</td><td>-</td>  <td>-</td><td>-</td><td>0.38</td></tr>
</table>
