from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.utils.dates import WEEKDAYS
from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User, AbstractBaseUser
from django.utils.text import slugify
from django.contrib.auth import login

class Event(models.Model):
    name = models.CharField(_('name'), max_length=50)
    
    def __unicode__(self):
        return self.name

class EventSlot(models.Model):
    event = models.ForeignKey(Event)
    slot_start = models.DateTimeField(_('slot start'))
    slot_end = models.DateTimeField(_('slot_end'))
    desc = models.CharField(_('desc'), max_length=50)
    
    def __unicode__(self):
        return "%s - %s %s" % (self.event, unicode(WEEKDAYS[self.slot_start.weekday()]), self.desc)
    
    class Meta :
        ordering = ("slot_start",)

class Volunteer(User):
    
    phone = models.CharField(_('phone'), max_length=20, blank=True)
    availibility = models.ManyToManyField(EventSlot, verbose_name=_('availibility'))
    comment = models.TextField(_('comment'), blank=True)
    
    def __unicode__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.username)
    
    class Meta:
        verbose_name = _("volunteer")
    