from my_app.models import student
def populate_data(data):
    print("data importing started")
    for item in data:
        roll_no = item['roll_no']
        name = item['name']
        email = item['email']
        student.objects.create(roll_no = roll_no,name = name,email = email) # insert
    print("data populated successfully!")

# python manage.py shell
# >>>from my_app.populate_data import *
# >>>populate_data(data)


data = [{
    'roll_no' :101,
    'name':'john',
    'email':'john12@gmail.com'
},{
    'roll_no' :102,
    'name':'joy',
    'email':'joy12@gmail.com'
},{
    'roll_no' :103,
    'name':'steven',
    'email':'steven12@gmail.com'
},{
    'roll_no' :104,
    'name':'alex',
    'email':'alex212@gmail.com'
}]


# using fixtures

#// https://docs.djangoproject.com/en/5.0/topics/db/fixtures/#fixtures-explanation

#//python manage.py loaddata student.json