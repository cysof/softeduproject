from audioop import reverse
from pyexpat import model
from django.db import models
from django.urls import reverse



class Department(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True)
       



    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'department'
        verbose_name = 'departments'

    def get_absolute_url(self):
        return reverse("projectStore:departmentDetail", args=[self.slug])



TYPE_OF_WORK = ( 
    ('article', 'Article'),
    ('project', 'Educational Project'),
    ('seminer', 'Seminer'),
    ('script', 'Scripts'),
)

class Project(models.Model):
    departments = models.ForeignKey(Department, related_name='projects', on_delete=models.CASCADE)
    topic = models.CharField(max_length=250,)
    slug = models.SlugField(max_length=250, unique=True)
    type_of_work = models.CharField(max_length=16, choices=TYPE_OF_WORK)
    pages = models.CharField(max_length=16)
    chapters = models.CharField(max_length=16)
    content = models.TextField()
    
    class Meta:
        ordering = ('topic',)
        index_together = (('id', 'slug'))
        
    def __str__(self):
        return "self. title" + "self.departments"
    
    def get_absolute_url(self):
        return reverse('projectStore:projectDetail', kwargs={'slug':self.slug})
    


class Contact(models.Model):
    name = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    date = models.DateTimeField(auto_now_add=True)
    message = models.TextField()

    
    
    def __str__(self):
        return 'self.name' + 'self.title'
    
    class Meta:
        ordering = ('-date',)
    