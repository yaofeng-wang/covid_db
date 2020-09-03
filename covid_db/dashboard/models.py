from django.db import models

class Record(models.Model):
    # date of record.
    date = models.DateField(primary_key=True)
    # no. of imported cases.
    num_imported = models.PositiveIntegerField()
    # no. of cases from dormitories.
    num_dormitories = models.PositiveIntegerField()
    # no. of case from community.
    num_community = models.PositiveIntegerField()

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.date}"
