#!/usr/bin/python3
flights = ['9W811', 'IA414', '9W522']
print(len(flights))
print(flights)
flights.append('MH213')
print(flights)
flights.extend('QA400')
print(flights)
flights.extend(['SL419', 'ONEMORE'])
print(flights)
flights.insert(1,'9w811')
print(flights)
flights.insert(1,'9W811')
print(flights)
flights.remove('9w811')
print(flights)
flights.remove('9W811')
print(flights)
print(flights.pop())
print(flights)
