from medicSearch.models import *

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    role = models.IntegerField(choices=ROLE_CHOICE, default=3)
    birthday = models.DateField(default=None, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    specialties = models.ManyToManyField(Speciality, null=True, related_name='specialties')
    addresses = models.ManyToManyField(Address, null=True, related_name='addresses')

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

