import config_02

def load_data():
    input_file_name=config_02.INPUT_FILE
    output_file_name=config_02.OUTPUT_FILE
    return input_file_name, output_file_name

result=load_data()
print(result)