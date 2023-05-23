# In Linux with cd command go to the directory and wtite:
#    sqlite3 name.sqlite3
#In this case:
sqlite3 db.sqlite3

#To see tables:
.tables

select * from polls_question;

.schema usermodel_user
        Create table if not exists "usermodel_user" (
        "id" integer not null primary key autoincrement,
        "name" varchar(128) not null,
        "email" varchar (128) not null);

.quit

# Now we open python
python3 manage.py shell

from usermodel.models import User
# Create a python variable "u" which is related to column "User":
u = User(name='Kristan', email= 'kf@umich.edu')
# T communicate and store in database:
u.save()
print(u.id)
# 1
print(u.email)
# Kf@umich.edu

from django.db import connection
print(connection.queries)
#It shows debug data: what it did, how it started. It ran an insert statement

# [
# {'sql': "BWGIN", 'time': '0.000'},
# {'sql': 'INSERT INTO "usermodel_user" ("name", "email")
#           VALUES (\'Kristen\' , \'kf@umich.edu\')',
#    'time': '0.002'}
#]
#########################################################################
## CRUd in the ORM:
u= User(name='Sina', email='bahbah@umich.edu')
# save is the INSERT
u.save()
# User.objects.values is basically SELECT *
User.objects.values()
# Where clause:
User.objects.filter(email= 'csev@umich.edu').values()
# delete:
User.objects.filter(email= 'csev@umich.edu').delete()
# update:
User.objects.filter(email= 'csev@umich.edu').update(name='sinsin')
#order:
User.objects.values().order_by('email')
User.objects.values().order_by('-name')
