import os
import requests
from bs4 import BeautifulSoup

cred = open('.credentials', 'r')

USER = cred.readline()
PSWD = cred.readline()

cred.close()

def fetch_tickets(user, pswd):
    portal_url = 'https://www1.ufrgs.br/sistemas/portal/'
    ticket_url = 'https://www1.ufrgs.br/RU/tru/'

    session = requests.Session()

    login_info = {
            'usuario': user,
            'senha': pswd
            }
    portal_response = session.post(portal_url, data=login_info)
    print('Post portal response:')
    print(portal_response)

    if portal_response.status_code == 200:
        ticket_response = session.get(ticket_url)
        print('Ticket response:')
        print(ticket_response)
        return ticket_response

    return None

def filter_table(table):
    filtered = []
    
    rows = table.find_all('tr')
    head = rows.pop(0)
    infos = [info.text.strip() for info in head]
    infos.pop(0)    

    for row in rows:
        ticket = {}
        columns = row.find_all('td')
        items = [item.text.strip() for item in columns]
        for index, info in enumerate(infos):
            ticket[info] = items[index]
        filtered.append(ticket)

    return filtered

def get_tickets(html):
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table')
    filter_table(tables[0])
    tickets = {
            'available': filter_table(tables[0]),
            'used': filter_table(tables[1])
            }
    return tickets

ticket_html = fetch_tickets(USER, PSWD).text
all_tickets = get_tickets(ticket_html)

for ticket in all_tickets['available']:
    print(ticket['Tíquete'])
