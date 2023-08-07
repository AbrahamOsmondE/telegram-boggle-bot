# telegram-boggle-bot
This bot was made in order to help during boggle trainings, and provide an easy way for players to find solutions to a boggle board

This bot was written in python, and deployed through lambda. Then lambda function handler URL is then registered to a telegram bot webhook.

## Commands
`/start`: Initializes the bot and provides instructions on how to use the bot    
  
`/help`: Provides instructions on how to use the bot    
  
`/solve [16 letter characters]`: Provides solution to the boggle board defined using the 16 letter words

### How to Use (`/help`)
```
Please type /solve followed by a space and 16 letters
Example:
/solve abcdefghijklmnop

gives a solution to the following board
 a b c d 
 e f g h 
 i j k l 
 m n o p

Use 'q' for the 'Qu' tile
```
## Flow
```mermaid
  sequenceDiagram;
      User->>Telegram Bot: User sends a message;
      Telegram Bot->>Lambda: Bot forwards to lambda;
      Lambda->>Telegram Bot: Lambda fires a message on behalf of bot;
      Telegram Bot->>User: Bot sends message to user;
```
## Example
![WhatsApp Image 2023-08-07 at 21 43 59](https://github.com/AbrahamOsmondE/telegram-boggle-bot/assets/82792334/a6213ae3-bacb-47ed-b000-6422b1e09870)
