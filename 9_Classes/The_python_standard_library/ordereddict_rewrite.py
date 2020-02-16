from collections import OrderedDict

dictionary = OrderedDict()

dictionary['statement'] = '语句'
dictionary['list'] = '列表'
dictionary['dictionary'] = '字典'

for annotation in dictionary.values():
    print(annotation.title())