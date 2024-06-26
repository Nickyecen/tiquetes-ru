import os
import requests
from bs4 import BeautifulSoup

# Gets user credentials
cred = open('.credentials', 'r')

USER = cred.readline()
PSWD = cred.readline()

cred.close()

# fetch_tickets: String String -> Response
# Obj.: Given the user and password for the connection, gets
# the ticket information and returns it
def fetch_tickets(user, pswd):
    # urls
    portal_url = 'https://www1.ufrgs.br/sistemas/portal/'
    ticket_url = 'https://www1.ufrgs.br/RU/tru/'

    # Session
    session = requests.Session()

    # Logs in to UFRGS
    login_info = {
            'usuario': user,
            'senha': pswd
            }
    portal_response = session.post(portal_url, data=login_info)

    # Gets tickets
    if portal_response.status_code == 200:
        ticket_response = session.get(ticket_url)
        return ticket_response

    return None

# filter_table: Tag -> List
# Obj.: Given a table of tickets, filters it to become a list
# of dictionary tickets
def filter_table(table):
    filtered = []
    
    # Gets the property of each column 
    rows = table.find_all('tr')
    head = rows.pop(0)
    infos = [info.text.strip() for info in head]
    infos.pop(0)    

    # Transforms each ticket row in a dictionary
    for row in rows:
        ticket = {}
        columns = row.find_all('td')
        items = [item.text.strip() for item in columns]
        for index, info in enumerate(infos):
            ticket[info] = items[index]
        filtered.append(ticket)

    return filtered

# get_tickets: String -> Dict
def get_tickets(html):
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.find_all('table')
    filter_table(tables[0])
    tickets = {
            'available': filter_table(tables[0]),
            'used': filter_table(tables[1])
            }
    return tickets

############ EXECUTION ############
print('Acessando informações de tíquetes, aguarde...')
ticket_html = fetch_tickets(USER, PSWD).text
all_tickets = get_tickets(ticket_html)
print()

# Prompt
print('O que deseja fazer?')
print('t (padrão): Pegar um tíquete disponível')
print('d: Ver últimos 20 tíquetes disponíveis')
print('u: Ver últimos 20 tíquetes usados')
print('D: Ver informação completa dos últimos 20 tíquetes disponíveis')
print('U: Ver informação completa dos últimos 20 tíquetes usados')

# Input
info = input()
print()

if info == '' or 't' in info:
    print('Tíquete disponível:')
    print(all_tickets['available'][0]['Tíquete'])
    print()
if 'd' in info:
    print('Últimos 20 tíquetes disponíveis:')
    for index, ticket in enumerate(all_tickets['available']):
        print(f' {index+1}:\t{ticket['Tíquete']}')
    print()
if 'u' in info:
    print('Últimos 20 tíquetes usados:')
    for index, ticket in enumerate(all_tickets['used']):
        print(f' {index+1}:\t{ticket['Tíquete']}')
    print()
if 'D' in info:
    print('Informação completa sobre últimos 20 tíquetes disponíveis:')
    for ticket in all_tickets['available']:
        print(str(ticket).replace('{', '').replace('\'', '').replace('}',''))
    print()
if 'U' in info:
    print('Informação completa sobre últimos 20 tíquetes usados:')
    for ticket in all_tickets['used']:
        print(str(ticket).replace('{', '').replace('\'', '').replace('}',''))
    print()

