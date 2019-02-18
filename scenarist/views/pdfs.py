#  __                           _     _   
# / _\ ___ ___ _ __   __ _ _ __(_)___| |_ 
# \ \ / __/ _ \ '_ \ / _` | '__| / __| __|
# _\ \ (_|  __/ | | | (_| | |  | \__ \ |_ 
# \__/\___\___|_| |_|\__,_|_|  |_|___/\__|
#  
from django.http import JsonResponse
from scenarist.models.epics import Epic
from scenarist.models.dramas import Drama
from scenarist.models.acts import Act
from scenarist.models.events import Event
from collector.utils.basic import get_current_config, export_epic


def build_config_pdf(request):
  conf = get_current_config()
  state = export_epic(conf)
  return JsonResponse(state)