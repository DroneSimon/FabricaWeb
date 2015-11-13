from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext

from datetime import datetime
from station.models import Station, StationValues

def index(request):
    stations = Station.objects
    return render_to_response('index.html', {'stations': stations},
                              context_instance=RequestContext(request))

def new_station(request):
    if request.method == 'POST':
        # save new post
        name = request.POST['name_station']
        num_station = request.POST['num_station']
        date_creation = datetime.now()

        station = Station(name=name, num_station=num_station, date_creation=date_creation)
        station.save()

        stations = Station.objects
        return HttpResponseRedirect('/')
    else:
        return render(request, 'new_station.html')

def view_station(request, station_id):
    station = Station.objects.get(id=station_id)
    return render_to_response('station.html', {'station': station},
                              context_instance=RequestContext(request))

def add_values(request, station_id):
    station = Station.objects.get(id=station_id)

    if request.method == 'POST':
        pressure = request.POST['pressure']
        temperature = request.POST['temperature']
        humidity = request.POST['humidity']
        wind_speed = request.POST['wind_speed']
        time = datetime.now()

        sv = StationValues(station=station,
                           pressure=pressure,
                           temperature=temperature,
                           humidity=humidity,
                           wind_speed=wind_speed,
                           time=time)
        sv.save()
        return render(request, 'station.html', {'station': station})
    else:
        return render_to_response('add_values.html', {'station': station},
                                  context_instance=RequestContext(request))
