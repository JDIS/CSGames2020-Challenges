# 5@8Bot

To make sure you can stay 'hydrated' and fed enough during the 5@8s, you have decided to [modify a Roomba™](https://www.youtube.com/watch?v=Brf02tdtQGo&t=30s) to fetch drinks and pizza for yourself and your friends. To do so, this little bot has to go get tokens from the person ordering, get the item they want and then get it back to them, and then repeat the process for the next person. Since three hours is very little time to enjoy your 5@8, the bot has to take the optimal route between objectives.

## Input

Your bot will take as input a map of the area that looks like this:
```
#####
#A B#
#   #
#  P#
#   #
#@ 1#
#####
``` 
 where
 `A, B, … Z \ P` represents people that want drinks
 `1, 2, … 9` represents bars that provide drinks
 `P` represents where to get pizza
 `@` represents the Roomba™'s starting position

 Your bot will also take as input a series of orders:
 ```
 AB
 BF
 AF
 AP
 ```
 where the first column represents the person wanting the item, and the second column is either `B` for beer, `F` for liquor or `P` for pizza.

 ## Output

The roomba being a very simple robot, it can only take and act in four directions: Up `U`, Down `D`, Left `L` or Right `R`. It can also grab tokens from someone `T`, grab pizza `P` from where it is sold, grab liquor `F` or beer `B` from a bar or give an item to someone `G`. To output an action, the bot has to be where the action takes place. For example, to get tokens from `A`, the bot has to stand at `(1,1)` (impliying `(0, 0)` is the top-left corner)

Your bot should output the actions your bot has taken, with each order on a seperate line. For example, the correct output for the map and orders above is:

```
UUUUTDDDDRRBUUUULLG
RRTDDDDFUUUUG
LLTDDDDRRFUUUULLG
TDDRRPUULLG
```

The flag will be the concatenation of the paths for `education`, `science`, `genie`, in this order, fed to a MD5 hashing algorithm and following the format `JDIS-{CONTENT_GOES_HERE}`

For example, if the paths are `UTDBG`, `DTUBG`, `LTRBG`, then the flag would be `JDIS-{fa244afb7adcabbab6021fb9f1ef8e4e}`

## IMPORTANT
To make sure that your bot outputs the correct path, please use the [*Manhattan distance*](https://en.wikipedia.org/wiki/Taxicab_geometry) and consider directions in the *following order*: `U`, `D`, `L`, `R`[.](https://www.youtube.com/watch?v=NKbI6dpY-yo)
Else your bot might find an equal but incorrect path

Good luck !

