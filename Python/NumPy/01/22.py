scientise = {'Newton': 1642, 'Darwin': 1809, 'Turing': 1912}
print('keys:', scientise.keys())
print('values:', scientise.values())
print('items:', scientise.items())
print('get:', scientise.get('Curie', 1867))
temp = {'Curie': 1867, 'Hopper': 1906, 'Franklin': 1920}
scientise.update(temp)
print('after update:', scientise)
scientise.clear()
print('after clear:', scientise)
