list = ['CampusX is a channel', 'for data-science', 'aspirants.']

result = []

for sentence in list:
    result.extend(sentence.split())



print(result)
