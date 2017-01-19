from allauth.socialaccount.models import SocialAccount
import hashlib
from django.contrib.auth.models import User
from django.db import models
from allauth.account.models import EmailAddress


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')

    def __unicode__(self):
        return "{}'s profile".format(self.user.username)

    class Meta:
        db_table = 'user_profile'


def profile_image_url(self):
    fb_uid = SocialAccount.objects.filter(user_id=self.user.id, provider='facebook')

    if len(fb_uid):
        return "http://graph.facebook.com/{}/picture?width=40&height=40".format(fb_uid[0].uid)

    return "http://www.gravatar.com/avatar/{}?s=40".format(hashlib.md5(self.user.email).hexdigest())

User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
