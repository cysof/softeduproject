from django.db import models




TYPE_OF_WORK = (
    ('Article', 'Article'),
    ('Project', 'Educational Project'),
    ('Seminner', 'Seminner'),
    ('Other', 'Other'),
)

CLASIFICATION = (
    ('Post-graduate', 'Post-graduate'),
    ('undergraduate', 'Degree'),
    ('HND', 'Higher National Diploma'),
    ('ND', 'National Diploma'),
    ('NCE', 'Nigeria Certificate In Education'),
    
)

class HireWriter(models.Model):
    full_name = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=11)
    email = models.EmailField(max_length=120)
    select_work_type = models.CharField(max_length=64, choices=TYPE_OF_WORK)
    clasification = models.CharField(max_length=64, choices=CLASIFICATION)
    job_discribtion = models.TextField()
    
    
    def __str__(self):
        return self.full_name
    
    