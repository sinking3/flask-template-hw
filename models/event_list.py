from models.event import Event
import datetime

event1 = Event(datetime.date(2023, 9, 5), "stand up", 12, "Hopper", "morning stand up", True)
event2 = Event(datetime.date(2022, 3, 6), "union meeting", 20, "working mens club", "discuss pay", True)

events_list = [event1, event2]

def add_new_event(event):
    events_list.append(event)

def remove_event(index):
    del events_list[index]