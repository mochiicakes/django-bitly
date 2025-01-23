from django.db import models
from django.utils.text import slugify

# Create your models here.

class Link(models.Model):
    name = models.CharField(max_length=50, unique=True) # url name
    url = models.URLField(max_length=200) # original url
    slug = models.SlugField(unique=True, blank=True) # newspaper term for a url-friendly string. instead as mysite.com/link/name yes, we get mysite.com/link/name-yes
    clicks = models.PositiveBigIntegerField(default=0) # number of clicks

    # render to string from Link object (1) into the main url name
    def __str__(self):
        return f"{self.name} | {self.clicks}"

    # increments depending on the number of clicks on the url
    def click(self):
        self.clicks += 1
        self.save()

    # slugifies a link and saves it
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

# save a shortened link - name, url, slug, # of clicks