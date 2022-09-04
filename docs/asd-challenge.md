#  ASD Coin Challenge - `Jodis Fields`
  
On 1 September 2022, the Royal Australian Mint released a limited edition 50 cent commemorative coin to celebrate the Australian Signals Directorate's (ASD) 75th anniversary. Fifty thousand coins have been produced. 
The 50 cent coin marks 75 years of ASD, reflecting on our mission defending Australia from global threats. It commemorates our historical roots in World War II, harnessing and mastering technology to reveal foreign secrets and protect Australia’s own. 
In tribute to the importance of code breaking and evolution of signals intelligence, mulitple layers of cryptographic code have been included in the design of the coin. ASD cryptographic experts collaborated with the Royal Australian Mint to design the coins unique and enigmatic code. A hidden message will be revealed once each layer of code has been cracked. **All that is needed is a pen, paper, Wikipedia and brainpower.**  
>If you think you can decipher our coded messages, contact us and submit your answers. We’ll reveal whether your answers are correct at the end of September 2022.
  
| ![](https://www.asd.gov.au/sites/default/files/2022-09/ASD-50-SIDE-A-Hires.jpg ) | ![](https://www.asd.gov.au/sites/default/files/2022-09/ASD-50-SIDE-B-Hires.jpg ) |
|---|---|

---

#  Deciphering the code
  
  
###  Attempt 1 - Failed:
  
  
- Failed Attempt - sum of values in the box is the position of the letter in the encoded string?
- No number 2 🤦
  
<table>
<th>
  
**B (3)**
| **1** | **2** |
|-------|-------|
| <br>  | <br>  |
  
</th>
<th>
  
**T (4)**
| **1** | <br> |
|-------|------|
| **3** | <br> |
  
</th>
<th>
  
**H (6)**
| **1** | **2** |
|-------|-------|
| **3** | <br>  |
  
</th>
<th>
  
**A (1)**
| **1** | <br> |
|-------|------|
| <br>  | <br> |
  
</th>
<th>
  
**S (5)**
  
| **1** | <br>  |
|-------|-------|
| <br>  | **4** |
  
</th>
<th>
  
**A (7)**
| **1** | **2** |
|-------|-------|
| <br>  | **4** |
  
</th>
</table>
  
  
<table>
<th>
  
**A (1)**
| **1** | <br> |
|-------|------|
| <br>  | <br> |
  
</th>
<th>
  
**B (3)**
| **1** | **2** |
|-------|-------|
| <br>  | <br>  |
  
</th>
<th>
  
**T (4)**
| **1** | <br> |
|-------|------|
| **3** | <br> |
  
</th>
<th>
  
**S (5)**
  
| **1** | <br>  |
|-------|-------|
| <br>  | **4** |
  
</th>
<th>
  
**H (6)**
| **1** | **2** |
|-------|-------|
| **3** | <br>  |
  
</th>
<th>
  
**A (7)**
| **1** | **2** |
|-------|-------|
| <br>  | **4** |
  
</th>
</table>

---

###  Attempt 2 - The dots are Braille!!
  
  
- Took me a while to figure out what the dots were, but now we know the cipher is **ATBASH**.
- ATBASH is a simple monoalphabetic substitution cipher.
  
![](https://img.freepik.com/free-vector/braille-numbers-row-tactile-writing-system-used-by-people-who-are-blind-visually-impaired-vector-illustration-black-white_145391-761.jpg )
  
<table>
<th>
  
**A (1)**
| **1** | <br> |
|-------|------|
| <br>  | <br> |
A
</th>
  
<th>
  
**T (2)**
| **1** | <br> |
|-------|------|
| **3** | <br> |
T
</th>
<th>
  
**B (3)**
| **1** | **2** |
|-------|-------|
| <br>  | <br>  |
B
</th>
<th>
  
**A (4)**
| **1** | **2** |
|-------|-------|
| <br>  | **4** |
A
</th>
<th>
  
**S (5)**
| **1** | <br>  |
|-------|-------|
| <br>  | **4** |
S
</th>
<th>
  
**H (6)**
| **1** | **2** |
|-------|-------|
| **3** | <br>  |
H
</th>
</table>
 
---
  
###  Attempt 1 - Decode the outter ring:
  
  
- Decoding string using an [ATBASH decoder](https://cryptii.com/pipes/atbash-cipher ) reveals the following string:
  
>**Original**: <br>.DVZIVZFWZXRLFHRMXLMXVKGZMWNVGRXFOLFHRMVCVXFGRLM.URMWXOZIRGBRM7DRWGSC5WVKGS<br><br>**Decoded**:<br>.WEAREAUDACIOUSINCONCEPTANDMETICULOUSINEXECUTION.FINDCLARITYIN7WIDTHX5DEPTH<br><br>**Add Spaces:**<br>WE ARE AUDACIOUS IN CONCEPT AND METICULOUS IN EXECUTION. FIND CLARITY IN 7 WIDTH X 5 DEPTH

---

###  Attempt 1 - Decode the inner ring:
  
  
- I spent alot of time trying to look for anything related to 7 wide by 5 deep. Even after arranging the letters in a **7x5 grid**, I still struggled to identify the message.
  
>**Original**:<br>BGOAMVOEIATSIRLNGTTNEOGRERGXNTEAIFCECAIEOALEKFNR5LWEFCHDEEAEEE7NMDRXX5
  
|       | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-------|---|---|---|---|---|---|---|
| **1** | B | G | O | A | M | V | O |
| **2** | E | I | A | T | S | I | R |
| **3** | L | N | G | T | T | N | E |
| **4** | O | G | R | E | R | G | X |
| **5** | N | T | E | A | I | F | C |
  
|       | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|-------|---|---|---|---|---|---|---|
| **1** | E | C | A | I | E | O | A |
| **2** | L | E | K | F | N | R | 5 |
| **3** | L | W | E | F | C | H | D |
| **4** | E | E | A | E | E | E | 7 |
| **5** | N | M | D | R | X | X | 5 |
  
>**Decoded**:<br>BELONGING TO A GREAT TEAM STRIVING FOR EXCELLENCE WE MAKE A DIFFERENCE XOR HEX A5D75

---

###  The Big Daddy Cipher:
  
  
- My initial thought was that it looks a little like hex, but not quite..?
- Decoding the innner ring confirmed this. The string needs to be decoded using the **XOR HEX** key **A5D75**.
  
```sh
E3B
8287D4
290F723381
4D7A47A291DC
0F71B2806D1A53B
311CC4B97A0E1CC2B9
3B31068593332F10C6A335
2F14D1B27A3514D6F7382F1A
D0B0322955D1B83D3801CDB2
287D05C0B82A311085A03329
1D85A3323855D6BC333119D
6FB7A3C11C4A72E3C17CCB
B33290C85B6343955CCBA3
B3A1CCBB62E341ACBF72
E3255CAA73F2F14D1B27A
341B85A3323855D6BB33
3055C4A53F3C55C7B22
E2A10C0B97A291DC0F
73E3413C3BE392819
D1F73B331185A33
23855CCBA2A3
206D6BE383
1108B
```
  
