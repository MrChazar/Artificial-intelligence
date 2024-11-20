def replace_income_labels_in_file(input_file, output_file):
    with open(input_file, 'r') as file:
        content = file.read()

    content = content.replace('>50K', 'low')
    content = content.replace('<=50K', 'high')

    with open(output_file, 'w') as file:
        file.write(content)


input_filename = 'przed_zmianą/adult.data'
output_filename = 'adult.cas'
replace_income_labels_in_file(input_filename, output_filename)
