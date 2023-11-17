from django.db import models



class login(models.Model):
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=80)
    phone_number = models.IntegerField()
    classs= models.CharField(max_length=70)
    type = models.CharField(null=True,max_length=70)
    def __str__(self):
        return self.name

class add(models.Model):
    book_name = models.CharField(max_length=70)
    auther_name = models.CharField(max_length=70)
    type_book = models.CharField(max_length=70)
    details = models.TextField()
    image  = models.FileField()
    def __str__(self):
        return self.book_name


class borrow(models.Model):
    user = models.ForeignKey(login, on_delete=models.CASCADE)
    book_id =models.ForeignKey(add, on_delete=models.CASCADE)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.name} borrowed {self.book_id.book_name}"