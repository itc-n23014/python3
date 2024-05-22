def print_table(table):
    width = [max(len(item) for item in col) for col in table]
    for row in zip(*table):
        print(' '.join(item.rjust(width) for item, width in zip(row, width)))
        
table = [['apples', 'oranges', 'cherries', 'banana'],
              ['Alice', 'Bob', 'Carol', 'David'],
              ['dogs', 'cats', 'moose', 'goose']]
print_table(table)
