from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=300)
    hero_image = models.ImageField(upload_to='profile/')
    about_image = models.ImageField(
    upload_to='profile/',
    blank=True,
    null=True
    )

    short_bio = models.TextField()
    phone = models.CharField(max_length=100)
    location = models.CharField(max_length=300)
    google_map = models.TextField(blank=True)
    resume = models.FileField(upload_to='resume/')
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    email = models.EmailField()
    footer_description = models.TextField()
    projects_completed = models.IntegerField(default=0)
    years_experience = models.IntegerField(default=0)
    technologies_used = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    

class Skill(models.Model):
    order = models.IntegerField(default=0)
    name = models.CharField(max_length=200)
    percentage = models.IntegerField()
    def __str__(self):
        return self.name

class Milestone(models.Model):
    order = models.IntegerField(default=0)
    date = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300)
    description = models.TextField()

    def __str__(self):
        return self.title
    

class Project(models.Model):
    CATEGORY_CHOICES = (
        ('Website', 'Website'),
        ('App', 'App'),
        ('AI/ML Project', 'AI/ML Project'),
    )
    order = models.IntegerField(default=0)
    title = models.CharField(max_length=200)
    project_type = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Website')
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    technologies = models.CharField(max_length=300)
    source_code = models.URLField(blank=True)
    live_demo = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name