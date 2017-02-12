import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','productiv_website.settings')

import django
django.setup()


def populate():
    sites = []
    for site in range(0,50):
        sites += add_site("youporn.com")

    add_user("SomeUser@beemail.com", "password", random.randint(0,10000), sites)




def add_user(username, password, balance, sites):
    u, created = UserProfile.objects.get_or_create(user.username=username, user.password=password, balance=balance, sites=sites)

    u.save()

def add_site(url):



if __name__="__main__":
    populate()
