# Instagram

project made in django using a db sqlite

## Create a model (table of db)
For create a table, have to create a class  
__str__ = method to string, return a string when is called
~~~python
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    birthdate = models.DateField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.first_name
~~~

To make migrations then of create a new model run

~~~bash
manage.py makemigrations
~~~
and this create a new file in migrations folder with the fields and the tables, and create a new file for each change in the model, then run for save the changes in the db
~~~bash
manage.py migrate
~~~
## Create entities from bash python
Open the shell
~~~bash
manage.py shell
~~~
import the model in the shell
~~~bash
from posts.models import User
~~~
Instance a new entity
~~~bash
Kevin = User.objects.create(
    first_name='kevin',
    last_name='zarama',
    email='zaramaluna1999@hotmail.com',
    password='123',
)
~~~
Another path to create a entity
~~~bash
User = User()
User.first_name = 'user'
User.email = 'user@hotmail.com'
User.save()
~~~
For update the entity then of make a change
~~~bash
kevin.save()
~~~
Delete a entity
~~~bash
kevin.delete()
~~~
## Queries
- query for an entity
    ~~~bash
    user = User.objects.get(first_name='kevin')
    ~~~
- query for entities(__ = for special queries)
    ~~~bash
    users = User.objects.filter(email__endswith='@hotmail.com')
    ~~~
- return all of a table
    ~~~bash
    users = User.objects.all()
    ~~~
- update many entities
    ~~~bash
    users = User.objects.filter(email__endswith='@hotmail.com').update(is_admin=True)
    ~~~
---