# SimpleBankingSystem
A project via Hyperskill using Python and Sqlite3

Consists of 3 files:

-  banking.py
The entry to the program, opens with a menu of 3 options:
  1. create account
  2. log in
  3. exit

-  account.py
Has a menu within itself once opened with log in from banking.py, also takes in the connection made from banking.py to database_handler.py
The menu consists of 6 options:
  1. check balance
  2. add income
  3. do a transfer
  4. close account
  5. log out
  6. exit

-  database_handler.py
Any changes done to the accounts or the searching for accounts is done here, the database handler, and saved

# Installation
Clone the repository

# Usage
As this is a Python projecct, go to where you cloned this project, then run:
```bash
python banking.py
