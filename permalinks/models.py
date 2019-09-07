from django.db import models
from django.utils import timezone


class CommonFields(models.Model):
    added_on = models.DateTimeField(null=True, auto_now_add=True)
    updated_on = models.DateTimeField(null=True, auto_now_add=True)

    class Meta:
        abstract = True


class Permalinks(CommonFields):
    permalink_id = models.BigAutoField(primary_key=True)
    old_url = models.URLField(max_length=500, verbose_name="Old URL", unique=True,
                              help_text="This is the URL that will be redirected.<br>Follow Full URL Scheme: <b>https://www.example.com/myapp/mypage.html</b>")
    new_url = models.URLField(max_length=500, verbose_name="New URL",
                              help_text="This is the URL to which the above URL will be redirected.<br>Follow Full URL Scheme: <b>https://www.example.com/myapp/mypage.html</b>")

    def __str__(self):
        return self.old_url

    def save(self, *args, **kwargs):
        self.updated_on = timezone.now()
        super(Permalinks, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Permalink'
        verbose_name_plural = 'Permalinks'