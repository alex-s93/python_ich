d = {1: 10, 4: 2, 5: 40, 6: 30, 7: 20}

print(dict(sorted(d.items(), key=lambda item: item[1])))

