## Array & Hashing

#### Prefix sum / product (except self) - 238:

```
[A, B, C] (Input)

[1,  A,  AB]
[BC, C,  1] * (Multiplication)
--------------
[BC, AC, AB] (Output)
```

#### Top K frequency element - 347:
Key points: 
 - Hashmap
 - Bucket sort
```
-----------------------------------------
[1, 1, 1, 2, 2, 3], k=2 (Input)

|0|1|2|3|4|5|6|
| |3|2|1| | | |

[1,2] (Output)

```
