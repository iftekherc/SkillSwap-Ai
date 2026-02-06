from django.db import models

# Create your models here.
# hero section
class HeroSection(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='hero_images/')
    button1_text = models.CharField(max_length=50)
    button1_link = models.URLField()
    button2_text = models.CharField(max_length=50, blank=True, null=True)
    button2_link = models.URLField(blank=True, null=True)
    tagline = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title
    
class SectionData(models.Model):
    section_name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
class CountSection(models.Model):
    icon = models.ImageField(upload_to='count_icons/')
    count_number = models.IntegerField()
    count_text = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.count_number} - {self.count_text}"
    
class CardModel(models.Model):
    icon = models.ImageField(upload_to='card_icons/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title
    
class SkillSwap(CardModel):
    pass


class WhyChooseUs(CardModel):
    pass


class CtaModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    button_text = models.CharField(max_length=50)
    button_link = models.URLField()
    point_1 = models.CharField(max_length=100, blank=True, null=True)
    point_2 = models.CharField(max_length=100, blank=True, null=True)
    point_3 = models.CharField(max_length=100, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
