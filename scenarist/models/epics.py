"""
╔╦╗╔═╗  ╔═╗┌─┐┌─┐┌┐┌┌─┐┬─┐┬┌─┐┌┬┐
 ║║╠═╝  ╚═╗│  ├┤ │││├─┤├┬┘│└─┐ │
═╩╝╩    ╚═╝└─┘└─┘┘└┘┴ ┴┴└─┴└─┘ ┴
"""
from django.db import models
from django.contrib import admin
from django.urls import reverse
import datetime as dt
from scenarist.models.story_models import StoryModel


class Epic(StoryModel):
    class Meta:
        ordering = ['era','title']
    era = models.IntegerField(default=5017, blank=True)
    shortcut = models.CharField(default='xx', max_length=32, blank=True)
    image = models.CharField(default='', max_length=64, blank=True)
    system = models.CharField(default='', max_length=128, blank=True, null=True)

    @property
    def printtime(self):
        x = dt.datetime.now().strftime("%Y-%m-%d-%H:%M")
        return x

    @property
    def challenge(self):
        from scenarist.models.dramas import Drama
        episodes = Drama.objects.filter(epic=self)
        total = 0
        for e in episodes:
            total += e.challenge
        return total

    @property
    def dramatis_personae(self):
        list = self.get_full_cast()
        nok = []
        ok = []
        from collector.models.character import Character
        for x in list:
            ch = Character.objects.filter(rid=x).first()
            it = ch.full_name
            if ch.is_dead:
                it += "(&dagger;)"
            if ch.balanced:
                ok.append(it)
            else:
                nok.append(it)

        return ", ".join(ok)+"<hr/>"+", ".join(nok)

    def get_absolute_url(self):
        return reverse('epic-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return '%s (%s)' % (self.title, self.era)

    def get_episodes(self):
        from scenarist.models.dramas import Drama
        episodes = Drama.objects.filter(epic=self)
        return episodes


class EpicAdmin(admin.ModelAdmin):
    ordering = ('era', 'title',)
