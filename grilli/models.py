from django.db import models

# Create your models here.

class EmailModel(models.Model):
   
    email_address = models.EmailField()
    def __str__(self):
        return self.email_address
    

class TableModel(models.Model):
    PERSON_CHOICE = [
        ("1-person", "1-person"),
        ("2-person", "2-person"),
        ("3-person", "3-person"),
        ("4-person", "4-person"),
        ("5-person", "5-person"),
        ("6-person", "6-person"),
        ("7-person", "7-person"),
     ]
    TIME_CHOICE = [
        ("08:00am", "08:00am"),
        ("09:00am", "09:00am"),
        ("010:00am", "010:00am"),
        ("011:00am", "011:00am"),
        ("012:00am", "012:00am"),
        ("01:00pm", "01:00pm"),
        ("02:00pm", "02:00pm"),
        ("03:00pm", "03:00pm"),
        ("04:00pm", "04:00pm"),
        ("05:00pm", "05:00pm"),
        ("06:00pm", "06:00pm"),
        ("07:00pm", "07:00pm"),
        ("08:00pm", "08:00pm"),
        ("09:00pm", "09:00pm"),
        ("10:00pm", "10:00pm"),

    ]

    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    person = models.CharField(max_length=20, choices=PERSON_CHOICE, default='1-person')
    date = models.DateField()
    time = models.CharField(max_length=10, choices=TIME_CHOICE)
    message = models.TextField()
   
    def __str__(self):
        return self.name