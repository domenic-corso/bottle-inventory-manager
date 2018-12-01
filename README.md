# Setup
#### Install Bottle
```sh
pip install bottle
```

#### Install SQLite
You can install it from anywhere, just make sure you add it to your path.
Try this: https://www.sqlite.org/download.html

#### SQL Setup
You'll need to create all the tables required for this app - it's as easy as running `data/setup.sql` using SQLite.
```sh
sqlite3 data/database.db
sqlite> .read data/setup.sql
```
If you'd like to test the app with some dummy data, you can do so by running:
```sh
sqlite3 data/database.db
sqlite> .read data/dummy.sql
```

#### Running the app
```sh
python main.py
```
It'll now be running on `http://127.0.0.1:8080/` - if you'd like to change the port you can edit `main.py`
