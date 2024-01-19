# Backgammon field

This file contains info about work with backgammon field.

## Storing field

We're storing field as list of lists. Positions are enumerated, you can check it at the picture: 

```txt
-------------Home-of-black-------------------------------------------------
|######@@@@@@######@@@@@@######@@@@@@|######@@@@@@######@@@@@@######@@@@@@|
| #11#  @10@  #09#  @08@  #07#  @06@ | #05#  @04@  #03#  @02@  #01#  @00@0|
|  ##    @@    ##    @@    ##    @@  |  ##    @@    ##    @@    ##    @@ 0|
|                                    |                                   0|
|                                    |                                   0|
|O                                   |                                   0|
|O                                   |                                    |
|O                                   |                                    |
|O @@    ##    @@    ##    @@    ##  |  @@    ##    @@    ##    @@    ##  |
|O@12@  #13#  @14@  #15#  @16@  #17# | @18@  #19#  @20@  #21#  @22@  #23# |
|@@@@@@######@@@@@@######@@@@@@######|@@@@@@######@@@@@@######@@@@@@######|
--------------------------------------------------Home-of-white------------
```

For example, this is the start position of the game: 
```py
field: list[list] = [
    [], [], [], [], [], [], [], [], 
    [], [], [], [], [], [], [], [
        chipW1, chipW2, chipW3, ..., chipW14, chipW15
    ], 
    [], [], [], [], [], [], [], [], 
    [], [], [], [], [], [], [], [
        chipB1, chipB2, chipB3, ..., chipB14, chipB15
    ]
]
```
