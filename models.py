"""""
from django.db import models
from django.contrib.auth.models import User 
  

class  Account(models.Model):
    
    userName =models.CharField(max_length=25)
    userPassword = models.CharField(max_length=20)

class User(models.Model):
    user_id = models.IntegerField
    fam_name = models.CharField(max_length=30)
    gender= models.CharFieldmax_length=30
    email =models.CharField(max_length=40)
    photo =models.CharField(max_length=50)

class  Instructor(models.Model):
    user_type=models.IntegerField 
    user_id =models.IntegerField 
   # Foreign Key (user_type) REFERENCES (user_)
   # Foreign Key (user_id) REFERENCES (user_)
 
class Learner(models.Model):
        user_type=models.IntegerField()
        user_id = models.IntegerField()
        total_XP =models.IntegerField()
   #  Foreign Key (user_type) REFERENCES (user_)
   # Foreign Key (user_id) REFERENCES (user_)

      class Is_enrolled(models.Model):
        lesson_id =models.IntegerField()
        user_type= models.IntegerField()
        user_id= models.IntegerField()
 #   Foreign Key (user_type) REFERENCES (user_)
 #  Foreign Key (user_id) REFERENCES (user_)

   class Training (models.Model):
        training_id = models.IntegerField
        domain_id=models.IntegerField 
        training_id = models.IntegerField
        training_name = models.CharFieldr(max_length=30) 
        training_description =models.CharField (max_length=100)
    #  Foreign Key (training_id) REFERENCES (training)


   class Domain(models.Model):
   # domain_id int PRIMARY auto,
    domain_name=models.CharField (max_length=30) 
    domain_description=models.CharField(max_length=100)

   class Lesson(models.Model ):
    user_type = models.IntegerField 
    user_id =models.IntegerField
    lesson_id =models.IntegerField
    lesson_description = models.CharField(max=40)
    training_id =models.IntegerField 

  
  class Video(models.Model):
      lesson_id = models.IntegerField
      id_vid = models.IntegerField 
      XP_pts  = models.IntegerField
      lik_vid =models.CharField (max=30)
      #Foreign Key (lesson_id)  REFERENCES (lesson)
         



   class Tasks(models.Model):
      lesson_id = models.IntegerField
      #id_task = int
      XP_pts =models.IntegerField
      question =models.CharField(max_length=50)

      #Foreign Key (lesson_id) REFERENCES (lesson)
  

 class  Test(models.Model)  :
            #test_id int PRIMARY auto,
    lesson = models.IntegerField
    question = models.CharFieldar(max=100)
    question = models.CharFieldr(max_length=300)
   
   
"""""""""
from django.db import models

class Domain(models.Model):
    domain_id = models.AutoField(primary_key=True)  # Use AutoField instead of GENERATED ALWAYS AS IDENTITY
    domain_name = models.CharField(max_length=30)
    domain_description = models.CharField(max_length=255)

    def __str__(self):
        return self.domain_name

class Training(models.Model):
    training_id = models.AutoField(primary_key=True)  # Use AutoField instead of GENERATED ALWAYS AS IDENTITY
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE)  # Link to Domain model
    training_name = models.CharField(max_length=255)
    training_descrption = models.CharField(max_length=500)

    def __str__(self):
        return self.training_name
""""""

