from medicSearch.models import *

class Neighborhood(models.Model):
    city = models.ForeignKey(City, blank="False", related_name='cidade', on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=20)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.name, self.city.name)