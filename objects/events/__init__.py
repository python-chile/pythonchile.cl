from datetime import date
from ._2020 import EVENTS as EVENTS_2020
from ._2021 import EVENTS as EVENTS_2021
from ._2022 import EVENTS as EVENTS_2022
from ._2023 import EVENTS as EVENTS_2023
from ._2024 import EVENTS as EVENTS_2024
from ._2025 import EVENTS as EVENTS_2025
from ._2026 import EVENTS as EVENTS_2026

EVENTS = [
    *EVENTS_2020,
    *EVENTS_2021,
    *EVENTS_2022,
    *EVENTS_2023,
    *EVENTS_2024,
    *EVENTS_2025,
    *EVENTS_2026
]
MONTHS = [
    '', 'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
    'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
]

TYPE_SLUGS = {
    'Meetup': 'meetup',
    'PyCon Chile': 'pycon',
    'PyDay': 'pyday',
    'Hackaton': 'hackaton',
}

for event in EVENTS:
    if 'city' not in event:
        event['city'] = 'Online'
    event_date = event['date']
    event['date_display'] = '{} de {} de {}'.format(
        event_date.day, MONTHS[event_date.month], event_date.year
    )
    event['type_slug'] = TYPE_SLUGS.get(event['type'], 'otro')

today = date.today()

# Orden preferido para los tipos de evento (de mayor a menor escala).
# Los tipos no listados aqui se agregan al final en orden de aparicion.
TYPE_ORDER = ['PyCon Chile', 'PyDay', 'Meetup', 'Hackaton']

EVENTS_TYPES = TYPE_ORDER + list({
    event.get('type') for event in EVENTS 
    if event.get('type') and event.get('type') not in TYPE_ORDER
})

CITIES = sorted(list({event.get('city') for event in EVENTS if event.get('city')}))

YEARS = sorted({event.get('date').year for event in EVENTS})

UPCOMING_EVENTS = sorted(
    [event for event in EVENTS if event['date'] >= today],
    key=lambda e: e['date']
)
PAST_EVENTS = {}
for event in reversed(EVENTS):
    if event['date'] >= today:
        continue
    year = event['date'].year
    if year not in PAST_EVENTS:
        PAST_EVENTS[year] = []
    PAST_EVENTS[year].append(event)

events_counts = {}
sessions_counts = {}
attendees_counts = {}
for event in EVENTS:
    year = event['date'].year
    if year not in events_counts:
        events_counts[year] = {event_type: 0 for event_type in EVENTS_TYPES}
        sessions_counts[year] = {'Charlas': 0, 'Talleres': 0, 'Desafíos': 0}
        attendees_counts[year] = 0
    sessions_counts[year]['Charlas'] += event.get('talks', 0)
    sessions_counts[year]['Talleres'] += event.get('workshops', 0)
    sessions_counts[year]['Desafíos'] += event.get('challenges', 0)
    event_type = event['type']
    events_counts[year][event_type] += 1
    attendees_counts[year] += event.get('attendees', 0)

EVENTS_COUNTS = []
for year, items in events_counts.items():
    for label, count in items.items():
        EVENTS_COUNTS.append({'year': year, 'label': label, 'count': count})
SESSIONS_COUNTS = []
for year, items in sessions_counts.items():
    for label, count in items.items():
        SESSIONS_COUNTS.append({'year': year, 'label': label, 'count': count})
ATTENDEES_COUNTS = [{'year': year, 'label': 'asistentes', 'count': count} for year, count in attendees_counts.items()]
CURRENT_YEAR = date.today().year

# Estadisticas de impacto (se calculan solas a partir de los eventos).
STATS = {
    'eventos': len(EVENTS),
    'charlas': sum(e.get('talks', 0) for e in EVENTS),
    'talleres': sum(e.get('workshops', 0) for e in EVENTS),
    'viewers': sum(e.get('viewers', 0) for e in EVENTS),
    'ciudades': len({e.get('city') for e in EVENTS if e.get('city') and e['city'] != 'Online'}),
}
