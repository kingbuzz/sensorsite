from django.db import models


class Measurement(models.Model):
    temp1 = models.FloatField()
    temp2 = models.FloatField()
    temp3 = models.FloatField()
    temp4 = models.FloatField()
    hum1 = models.FloatField()
    hum2 = models.FloatField()
    hum3 = models.FloatField()
    hum4 = models.FloatField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return 'Messung am: ' + str(self.timestamp)
