from django.db import models

class Foods(models.Model):
    create_date = models.DateTimeField('date create')
    content_text = models.CharField(max_length=500)
    url_img = models.URLField( max_length=200)
    intro_text = models.CharField(max_length=1000)
    use_text = models.CharField(max_length=1000)
    document_text = models.CharField(max_length=1000)
    processing_text = models.CharField(max_length=1000)
    note_text = models.CharField(max_length=1000)
    def __str__(self):
        return self.content_text