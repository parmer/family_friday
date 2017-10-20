Family Fridays
==============
Project by [Paul Armer](http://paularmer.me) for Apartment List

![](https://raw.githubusercontent.com/parmer/family_friday/master/static/family_friday/groups.png =200x)
![](https://raw.githubusercontent.com/parmer/family_friday/master/static/family_friday/manage.png =200x)
![](https://raw.githubusercontent.com/parmer/family_friday/master/static/family_friday/jlatt.png =200x)

Requirements
------------
* SASS ([install](http://sass-lang.com/install))
* Python3 ([install](https://www.python.org/downloads/))
* Django ([install](https://docs.djangoproject.com/en/1.11/topics/install/))

Build & Run
-----------
```
./build.sh
./run.sh
```
All this really does is create the django migrations and apply them. The repo should already have the sqlite3 database
already populated with some employees.

After running the run script, the site should be up at [http://localhost:8000/](http://localhost:8000/)

Design Decisions
----------------
### Django
I've fallen in love with Django. I use it for all my personal projects (since I use java at work). It's great for
creating an app quickly and still do A LOT.

### Group Processing
Originally I had the logic for creating groups of employees in the client side angular code. I was pretty happy with
this place so that the client wouldn't have to make http calls for every time groups were created. However, when I went
to write tests, I realized it'd be easier to write tests for my python code, and I switched it to a service call.
Additionally, in the real use case, a user won't be spamming the "Generate Groups" button, and this isn't a huge
algorithm.

The one edge case I've discovered (through an uncommitted test) is the twice MIN_GROUP_SIZE (3 * 2 = 6) employee set
size. I could just easily add a catch for this in my python code, but that just felt less than perfect, so I decided to
just omit that case-- if you have 6 people in your company, you probably are already just going to lunch together
anyways.

### Styles
I use [BEM](http://getbem.com/) for my css style since I think it's great for style readability and helps futures
developers (or future me) understand how the styles are working.

The style itself is just a simple card-ish layout that is devoid of color with the exception of the Apartment List blue
color for actions (links and buttons). This make the UI hopefully easy for non-technical users to learn.

Further Endeavors
-----------------
* Possibly handle employee sets of up to twice MIN_GROUP_SIZE (3 * 2 = 6)
* Switch to use a non-sqlite3 database
* Who is **_Jlatt_**?