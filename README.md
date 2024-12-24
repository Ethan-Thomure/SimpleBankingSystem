# SimpleBankingSystem
A project via Hyperskill using Python and Sqlite3

Consists of 3 files:



-  banking.py
The entry to the program, opens with a menu of 3 options: create account, log in, exit

-  account.py
Has a menu within itself once opened with log in from banking.py, also takes in the connection made from banking.py to database_handler.py
The menu consists of 5 options: check balance, add income, do a transfer, close account, log out, and exit

-  database_handler.py
Any changes done to the accounts or the searching for accounts is done here, the database handler, and saved
