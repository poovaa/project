from django.db import models


class User(models.Model):

	name=models.TextField()
	email=models.TextField()
	password=models.TextField()
	class Meta:
		db_table='user'
