'''
 ╔╦╗╔═╗  ╔═╗┌─┐┬  ┬  ┌─┐┌─┐┌┬┐┌─┐┬─┐
  ║║╠═╝  ║  │ ││  │  ├┤ │   │ │ │├┬┘
 ═╩╝╩    ╚═╝└─┘┴─┘┴─┘└─┘└─┘ ┴ └─┘┴└─
'''
from django.conf.urls import url
from django.urls import path, re_path
from collector.views.basic import skill_touch, pdf_show
from collector.views.frontend import index,edit_character,view_character, view_by_rid,get_list, add_character, get_storyline, conf_details, recalc_character, recalc_pa_character, recalc_skills_character
from collector.views.backend import recalc,export,xls_update,pdf_character
from collector.views.misc_chart import get_chardar, get_population_statistics


urlpatterns = [
	path('', index, name='index'),
	re_path('^recalc/$', recalc, name='recalc'),
	re_path('^export/$', export, name='export'),
  re_path('^xls_update/$', xls_update, name='xls_update'),
  re_path('^ajax/edit/character/(?P<id>\d+)/$', edit_character, name='edit_character'),
  re_path('^ajax/recalc/character/(?P<id>\d+)/$', recalc_character, name='recalc_character'),
  re_path('^ajax/recalc_pa/character/(?P<id>\d+)/$', recalc_pa_character, name='recalc_pa_character'),
  re_path('^ajax/recalc_skills/character/(?P<id>\d+)/$', recalc_skills_character, name='recalc_skills_character'),
  re_path('^ajax/update/character/$', edit_character, name='update_character'),
  re_path('^ajax/pdf/character/(?P<id>\d+)/$', pdf_character, name='pdf_character'),
  re_path('^ajax/view/character/(?P<id>\d+)/$', view_character, name='view_character'),
  re_path('^ajax/list/(?P<slug>[\w-]+)/(?P<id>\d+)/$', get_list, name='get_list'),
  #re_path('^ajax/cast/(?P<slug>[\w-]+)/(?P<id>\d+)/$', get_story_casting, name='get_story_casting'),
  re_path('^ajax/storyline/(?P<slug>[\w-]+)/$', get_storyline, name='get_storyline'),
  re_path('^ajax/skill_touch/$', skill_touch, name='skill_touch'),
  re_path('^ajax/add/character/$', add_character, name='add_character'),
  re_path('^ajax/conf_details/$', conf_details, name='conf_details'),
  re_path('^api/chardar/(?P<id>\d+)/$', get_chardar, name='get_chardar'),
  re_path('^api/popstats/$', get_population_statistics, name='get_popstats'),
  re_path('^pdf/(?P<slug>[\w-]+)/$', pdf_show, name='pdf_show'),
  re_path('^ajax/view/by_rid/(?P<slug>[\w-]+)/$', view_by_rid, name='view_by_rid'),
]
