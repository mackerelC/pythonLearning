contacts = {
    'number': 4,
    'students':
        [
            {'name': 'Sarah Holderness', 'email': 'sarah@example.com'},
            {'name': 'Harry Potter', 'email': 'harry@example.com'},
            {'name': 'Hermionie Granger', 'email': 'hermionie@example.com'},
            {'name': 'Ron Weasley', 'email': 'ron@example.com'}
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])