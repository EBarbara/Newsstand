from django.db import models

class Magazine(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

class Volume(models.Model):
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.magazine.title} - Vol. {self.number}'

class Publisher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class VolumePublisher(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

class Issue(models.Model):
    volume = models.ForeignKey(Volume, on_delete=models.CASCADE)
    number = models.CharField(max_length=50)
    title = models.CharField(max_length=255, blank=True)
    publication_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.volume} - Issue {self.number}'

class IssueFile(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='issues/')
    file_type = models.CharField(max_length=10, choices=[('cbz', 'CBZ'), ('cbr', 'CBR'), ('pdf', 'PDF')])

    def __str__(self):
        return f'{self.issue} - {self.file_type.upper()}'

class Article(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    start_page = models.PositiveIntegerField(null=True, blank=True)
    end_page = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Role(models.Model):
    name = models.CharField(max_length=100)  # Ex: "Autor", "Fotógrafo", "Modelo"

    def __str__(self):
        return self.name

class PersonRoleInArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='contributions')
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.person} como {self.role} em {self.article}'