dict1 = {'status': 200, 'headers': {'Date': 'Tue, 27 Jun 2023 03:20:39 GMT', 'Server': 'WSGIServer/0.2 CPython/3.11.0',
                                    'Content-Type': 'application/json', 'X-Frame-Options': 'DENY',
                                    'Content-Length': '197', 'X-Content-Type-Options': 'nosniff',
                                    'Referrer-Policy': 'same-origin', 'Cross-Origin-Opener-Policy': 'same-origin'},
         'data': {'status': 10200, 'message': 'success',
                  'data': {'eid': 1, 'name': '小米7发布会', 'limit': 2000, 'status': True, 'address': '北京',
                           'start_time': '2018-01-30T14:00:00'}}, 'time': 5634}

print(dict1.get('data'))
print('---' * 20)
