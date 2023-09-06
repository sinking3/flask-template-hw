from flask import render_template, Blueprint, request, redirect
from models.event_list import events_list, add_new_event
from models.event import Event

event_blueprint = Blueprint("events", __name__)

@event_blueprint.route('/events')
def index():
    return render_template('index.jinja', title='My Event List', 
    events=events_list)

@event_blueprint.route('/events', methods=["POST"])
def add_event():
    date = request.form["date"]
    name_of_event = request.form["name of event"]
    number_of_guests = request.form["number of guests"]
    room_location = request.form["room location"]
    description = request.form["description"]
    recurring =  request.form["recurring"] if "recurring" in request.form else False

    new_event = Event(date, name_of_event, number_of_guests, room_location, description, recurring)
    add_new_event(new_event)
    return redirect("http://127.0.0.1:4998/events")