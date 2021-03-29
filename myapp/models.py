from django.db import models

class Animal(models.Model):
    name = models.CharField(max_length=25)
    sound = models.CharField(max_length=25)

    def speak(self):
        return 'The %s says "%s"' % (self.name, self.sound)

    def __str__(self) -> str:
        return 'The %s says "%s"' % (self.name, self.sound)
