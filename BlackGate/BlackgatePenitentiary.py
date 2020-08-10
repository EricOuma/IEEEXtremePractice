def work(filename):
    items = []
    with open(filename) as f:
        number = int(f.readline())
        for _ in range(number):
            k, v = f.readline().split(' ')
            items.append((k, int(v)))
            

    # items = {k: v for k, v in sorted(items.items(), key=lambda item: item[1])}
    items = sorted(items, key = lambda x: x[1])


    min_index = 1
    max_index = 1
    current_names = []
    
    for count, data in enumerate(items):
        current_value = data[1]
        current_names.append(items[count][0])
        try:
            next_value = items[count + 1][1]
        except:
            with open('output.txt', 'a') as output:
                output.write(f"{' '.join(map(str, sorted(current_names)))} {min_index} {max_index}\n")
            print(f"{' '.join(map(str, sorted(current_names)))} {min_index} {max_index}")
        if next_value == current_value:
            max_index = count + 2
        else:
            with open('output.txt', 'a') as output:
                output.write(f"{' '.join(map(str, sorted(current_names)))} {min_index} {max_index}\n")
            print(f"{' '.join(map(str, sorted(current_names)))} {min_index} {max_index}")
            min_index = count + 2
            max_index = count + 2
            current_names = []

work('input.txt')
