types = {
    1: 'Блокирующий',
    2: 'Критический',
    3: 'Значительный',
    4: 'Незначительный',
    5: 'Тривиальный'
}

tickets = {
    1: ['API_45', 'API_76', 'E2E_4'],
    2: ['UI_19', 'API_65', 'API_76', 'E2E_45'],
    3: ['E2E_45', 'API_45', 'E2E_2'],
    4: ['E2E_9', 'API_76'],
    5: ['E2E_2', 'API_61']
}

tickets_by_type = {}

def delete_dublicate(tickets):
    
    k=2
    
    for i in range(1, len(tickets)):
        for element_1 in tickets[i]:
#            print(f'Элемент 1-го списка  Ключ: {i} {element_1}')
            for j in range(k, len(tickets)+1):
                for element_2 in tickets[j]:
                    if tickets[i] != tickets[j]:
#                        print(f'Элемент 2-го списка  Ключ: {j}  {element_2}')
                        if element_1 == element_2:
#                            print(f'{element_1} = {element_2}')
                            tickets[j].remove(element_2)
                            break

        k += 1
    return tickets

def relate_tickets_by_type(tickets, types):
    for key, value in types.items():
        tickets_by_type[value] = tickets[key]
    return tickets_by_type


delete_dublicate(tickets)
relate_tickets_by_type(tickets, types)
