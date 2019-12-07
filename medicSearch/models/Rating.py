from medicSearch.models import *

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='avaliou', on_delete=models.CASCADE)
    user_rated = models.ForeignKey(User, related_name='avaliado', on_delete=models.CASCADE)
    value = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.user.name, self.user_rated)