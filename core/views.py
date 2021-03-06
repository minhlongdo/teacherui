from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
import requests


def login(request):
    template = get_template('login/login.html')
    return HttpResponse(template.render())


def tab_100_points(request):
    template = get_template('tabs/tab_100_points.html')
    BASE_URL = 'http://discovery-100p.azurewebsites.net/{}{}'
    TEAM = request.GET.get('team', '')
    r = requests.get(BASE_URL.format('v1/team/points/', '?instance_id=%s' % TEAM))
    total_points_team = r.json()
    return HttpResponse(template.render(Context(
        {
            'total_points_team': total_points_team
        }
    )))


def tab_codemetrics(request):
    template = get_template('tabs/tab_codemetrics.html')
    return HttpResponse(template.render(Context(
        {

        }
    )))

