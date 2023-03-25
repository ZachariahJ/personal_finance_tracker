# personal_finance_tracker
 - Built by: Loya Niu, Zachariah Jia
 - March 25, 2023

## Inspiration
 - We want to build a **financial management**.
 - Most of the financial management software or website are not secure, and there're lots of ads. So we try to build a financial management web that **protects user's privacy**. 
 - It's important to make it user friendly so that users can easily use them. So we want to make it easy for interaction - by **speaking**.

## What it does
 - It receives intruction by user via saying "Hey Siri", and the user can easily say their income or expenses.
 - When program gets the instruction, it will process it by speech-to-text function, and write in the table.
 - It shows all the data on the website, so user can easily view their incomes and expenses.
 - It has a calendar, whcih calculates the daily, monthly, and annually income for a user as well.
 - User can put their monthly salary into **auto-billing**, it saves a lot of time!
 - A chart that gives them clear view of how much and where they spend most of their money.

## How we built it
 - We use Python as our back-end, and use Vue + TypeScript as our front-end.
 - We used SQLAlchemy in Python to process our database.
 - We uses Siri to get the input from human voice, and uses API from OpenAI to convert the sentence easily understand by computer. Then, write it to the database.

## Challenges we ran into
 - How to send audio via Siri.
 - How to use the API of ChatGPT to process human language.
 - Making our own API with higher efficiency.
 - Built the online table and graph tooks a long time.

## Accomplishments that we're proud of
 - We can just say "Hey Siri" to interact with our programs.
 - The speech-to-text function is really smart.
 - The program incorporates AI and functions well.

## What we learned
 - Using SQLAlchemy to process database.
 - Using API from OpenAI
 - How to make API

## What's next for Tally
 - Better UI / appearance
 - Make calendar & charts that helps user understand their expenses.
 - Use AI to predict the user's expense in the future, helping them make financial plans
 - etc.