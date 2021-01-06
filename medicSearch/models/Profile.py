from medicSearch.models import *
from django.db.models import Sum, Count

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ROLE_CHOICE, default=3, null=True, blank=True)
    birthday = models.DateField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    token = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    favorites = models.ManyToManyField(User, null=True, blank=True, related_name='favorites', verbose_name='Favoritos', help_text="Este campo é destinado aos usuários de perfil paciente.")
    specialties = models.ManyToManyField(Speciality, null=True, blank=True, related_name='specialties', verbose_name='Especialidades', help_text="Este campo é destinado aos usuários de perfil médico.")
    addresses = models.ManyToManyField(Address, null=True, blank=True, related_name='addresses', verbose_name='Endereços', help_text="Este campo é destinado aos usuários de perfil médico.")

    def __str__(self):
        return '{}'.format(self.user.username)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        try:
            instance.profile.save()
        except:
            pass

    def show_scoring_average(self):
        from .Rating import Rating
        try:
            ratings = Rating.objects.filter(user_rated=self.user).aggregate(Sum('value'), Count('user'))
            if ratings['user__count'] > 0:
                scoring_average = ratings['value__sum'] / ratings['user__count']
                scoring_average = round(scoring_average, 2) # Arredondando o valor para duas casas decimais
                return scoring_average
            return 'Sem avaliações'
        except:
            return 'Sem avaliações'

    def show_favorites(self):
        ids = [result.id for result in self.favorites.all()]
        return Profile.objects.filter(user__id__in=ids)

    def show_ratings(self):
        from .Rating import Rating
        return Rating.objects.filter(user_rated=self.user)