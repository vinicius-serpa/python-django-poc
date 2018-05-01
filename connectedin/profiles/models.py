from django.db import models

class Profile(models.Model):

    name = models.CharField(max_length = 255, null = False)
    email = models.CharField(max_length = 255, null = False)
    phone = models.CharField(max_length = 15, null = False)
    company_name = models.CharField(max_length = 255, null = False)

    def invite(self, invited_profile):
        Invite(invitator = self, invited = invited_profile).save()


class Invite(models.Model):

    invitator = models.ForeignKey(Profile, related_name = 'invites_done', on_delete = models.CASCADE)
    invited = models.ForeignKey(Profile, related_name = 'invites_received', on_delete = models.CASCADE)
