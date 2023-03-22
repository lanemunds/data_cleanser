

def clean_data(file):
    file1 = open(file, 'r')
    data = file1.readlines()
    file2 = open('production_ready_data.txt', 'w')
    cleaned_data = []
    for row in data:
        if row not in cleaned_data:
            cleaned_data.append(row)
            file2.write(row)
    file2.close


clean_data('data.txt')
