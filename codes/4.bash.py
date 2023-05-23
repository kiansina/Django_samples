# some bash commands:
# when we are in the true directotry:
# if you look at makemigrations:
ls */models.py

ls */migrations/0*.py

##!! RERUNNING MAKEMIGRATE
# If you wan to rerun makemigrations cause you are confused. THAT'S COOL
# just remove all the files inside the migration folder that star with '0'
python3 manage.py makemigrations

##!! RERUNNING MIGRATE FROM SCRATCH
# just remove database:
rm db.sqlite3
# then
python3 manage.py migrate
