from django.db import models

class Instructor(models.Model):
    name = models.CharField(max_length=100)
    credentials = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=200)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    review_count = models.PositiveIntegerField()
    enrollment_year = models.PositiveIntegerField()
    current_price = models.DecimalField(max_digits=6, decimal_places=2)
    original_price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(
        upload_to='course_images/',
        default='course_images/default.png',
        verbose_name='Course Image'
    )
    category = models.CharField(max_length=50, choices=[
        ('python', 'Python'),
        ('web-development', 'Web Development'),
        ('sql', 'SQL'),
        ('php', 'PHP'),
    ], default='python')
    def __str__(self):
        return self.title

    def get_rating_stars(self):
        """Returns star rating representation"""
        return '★' * int(self.rating) + '☆' * (5 - int(self.rating))
    
    def get_review_info(self):
        """Returns formatted review count with year"""
        return f"({self.enrollment_year}:{self.review_count})"
    
    def get_discount_percentage(self):
        if self.original_price > 0:
            discount = ((self.original_price - self.current_price) / self.original_price) * 100
            return f"{int(discount)}%"
        return "0%"