# Bottlecap Vending Machine

The Bottlecap vending machine game originates from the popular Video game fallout, which involves using bottlecaps as currency to play a game to win tokens to exchange for health and food supplies.

When the program is run the user will be shown instructions about how to play the game and how the symbols in the vending machine can multiply your deposit of bottlecaps. The user is also informed about the Minimum and Maximum lines/bottlecaps allowed to play on at one time. After reading the instructions the user can deposit their bottlecaps to begin, then the users balance will be displayed before playing.
The user will have a message asking to enter the number of lines they would like to deposit their bottlecaps on, The user will then have a message asking how many bottlecaps would they like to deposit on each line.

A message will then be displayed informing the user how many bottlecaps will be deposited on number of lines chosen, followed by the total deposit made by the  user. Below this message the Vending machine will display the board with 3 lines and if there is any lines with 3 of the same symbols horizontally, The user will then be informed of how many tokens won, what lines youve won on and the updated balance will be displayed.

![Bottlecap vending machine homepage](https://github.com/user-attachments/assets/9aca9bc2-675a-45d7-aab1-777d8a14576c)

[View the bottle cap vending machine game project here!](https://bottlecap-vending-machine-44921b46258e.herokuapp.com/)
- - -


## Logic flowchart
![Flowchart P1](https://github.com/user-attachments/assets/5fa94e3f-93cd-4975-bdd8-28e51cb294b6)
![Flowchart P2](https://github.com/user-attachments/assets/1065e94c-ea57-4a2f-81d9-98e3e21f00b1)

## User Experience (UX)
The vending machine game gets its roots from the famous video game franchise Fallout, the Fallout game uses the bottle cap currency due the videos games enviroment being post nuclear so bottlecaps are used in exchange for supplies, The game begins by inviting the user to play to win some tokens to exchnage for supplies, the user will deposit bottlecaps ranging from 1 - 100 bottle caps, once the user has deposited their bottlecaps the vending machine will spin and display 3 lines if there are 3 matching symbols the user deposit will multiply depending on symbol. This game will attarct alot of attention due to its similaritys with the fallout franchise and be very entertaining due to the symbols being produced are random.

### User Stories

* First-time visitor goals
    * Understand how the game works. Clear instructions and what the objective of the game is.
    * Play the game. Once the user understands the game, they will likely want to play it.
    * Enjoy the game, the vending machine game should be challenging but fun.

* Returning visitor goals
    * Continue playing. The returning visitor may have enjoyed playing the game and wants to play again.
    * Share with friends. Inviting friends to give the game a try.
    * Exploring new features, if there is any.

* Frequent user goals
    * Sharing the game with others or inviting friends to play.
    * Exploring new features, if there is any.

---

### Existing Features

* Intro screen
    * Displays a welcome message.
![Intro](https://github.com/user-attachments/assets/67fb38ee-55bd-4378-af45-e8f451a9e19b)

* Rules
    * Below Welcome message the rules and instructions are displayed.
![Rules](https://github.com/user-attachments/assets/ad4d9498-c7f0-40b2-98b5-6ace028e5c8b)

* Deposit bottlecaps
![start deposit](https://github.com/user-attachments/assets/5535827f-9caa-488b-b352-32c628960fd9)

* How many lines would they like to deposit bottlecaps on.
![Number of lines](https://github.com/user-attachments/assets/1a31fec0-2d52-41ba-9070-994f2b4c721b)

* Players Bottlecap balance.
![current Balance](https://github.com/user-attachments/assets/34154148-3c63-4245-924a-eeb0905c8b21)

* How many bottle caps would they like to deposit on line or lines chosen.
![lines deposit](https://github.com/user-attachments/assets/13b8bf2e-0887-4841-a611-ca82c6787ffd)

* Click run to play game after deposit.
![Press enter](https://github.com/user-attachments/assets/09153964-3307-4863-a5ad-a96478868cc3)

* Vending machine displayed, showing lines and users deposit to play.
![Vending Machine](https://github.com/user-attachments/assets/6d83b446-d147-4867-b048-8c287cc1c6c0)

* Winning Line
 * If line has 3 matching symbols, You won "6" tokens, you won on "1-3" lines.
 ![Winnings](https://github.com/user-attachments/assets/023ea6c5-ec02-4f74-bf90-df8326ec0585)

* No winning line
 * If lines have no matching symbols the game will show, 
   you won on no lines and your balance is now...
![Loses](https://github.com/user-attachments/assets/23614e7e-4021-4a1c-a522-ed868dee244b)

* Bottle caps won, balance displayed with the option to play or quit.
![Next Game](https://github.com/user-attachments/assets/f8e71c18-c32e-497b-906d-18d7af6f320f)

* Balance below 1, You left with 0 tokens please deposit
  more bottlecaps to play.
![End](https://github.com/user-attachments/assets/d088914e-dab6-4d66-bd62-500bd3d6af14)

## Features Left to Implement

* Create User Name
* Select supplies through interface
* Scoring system, lines won/ lines lost

---

## Design

* Flowchart
    * [Draw.io](http://draw.io/)

---

## Technologies Used

* [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

---

## Frameworks, Libraries & Programs Used

* [Gitpod](https://www.gitpod.io/)
    * Used for writing code.
* [Github](https://github.com/)
    * Deployment of the website and storing the files online.
* [Draw.io](http://draw.io/)
    * To create a logic flowchart of the hangman game.
* [Heroku]()
    * To deploy the project.

## Testing 

CI Python Linter was used to test run.py.

## Manual Testing

The game was manually tested extensively using gitpod terminal, and once the website was deployed on Heroku it was manually tested again, during the creation of the code to the end. Testing of Game rules/instructions, bottlecap input validation, select lines to play input validation, how many bottlecaps deposited on each line, display vending machine and finally infrom user if they've won on any lines, how many bottlecaps won, updated balance at the end..



| Feature | Expected Result | Steps Taken | Actual Result |
| ------- | -------------- | ----------- | ------------- |
| Intro Screen   | To display welcome message to user | None | As Expected |
| Display Rules | To display rules to user below intro message | None| As Expected | 
| Enter bottlecap deposit to play | To aquire bottlecap deposit from user| Input integer value from 1-100| As Expected |
| How many lines do you want to play on | Ask user how many lines do they wish to play on| User enters how many lines to play on (1-3) | As Expected |
| Choose how many bottlecaps to deposit on chosen lines | Retrieve bottlecap balance and deposit on chosen lines | Deposit bottlecap balance across lines | As Expected | ![Difficulty]
| Display users deposit and lines to play  | Informs user of deposit made to play game | none | As Expected |
| Display game | Display vending machine with random lines generated | Display 3 lines with random symbols attached | As Expected |
| Winning line | Achiveing 3 matching symbols across chosen line, multiplying players deposit and displaying tokens won/ line won on with updated balance shown. | 3 matching symbols across chosen line | As Expected | 
| Losing line | Not achiving 3 matching symbols across chosen line, players deposit lost updating players balance. | Displaying user balance after losing bottlecaps when playing | As Expected | 
| Play again | When users balance reaches less than 1 the game will end and the user will be asked to start again, however if the users deposit is > 1 but wants to quit, user can eneter q. | Game terminates when balance is less than 1 or user enters q to terminal | As Expected | 
