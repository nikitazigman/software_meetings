# General description

The programm should realise the handler class for the game 21.

21, Bagram, or Twenty Plus One is a drinking game. The game progresses by counting up from 1 to 21, with the player who calls "21" suffering a drinking penalty before the next round starts. The loser may add one new rule to the game, and starts the new round. (wiki)

## Excpected input data

int value in range of [1:21]

## Expected output data

str value, which represents the number or the output defined by the rules

## Defined set of rules

1. all odd numbers should multiplied on 4
2. all even numbers should be divided by 2
3. if number has more than one syllable we skip the first one
4. instead of "one" we are saying "eine"

The rules should be implemented in the defined order.

## The example of the data

| input | output |
| ----- | ------ |
| 1     | two    |
| 2     | eine   |
| 3     | six    |
| 4     | two    |
| 5     | ten    |
| 6     | three  |
| 7     | teen   |
| 8     | four   |
| 9     | teen   |
| 10    | five   |
| 11    | ty-two |
| ...   |        |

## technical demand

The handler should be realized using the "chain responsibility" design pattern.
