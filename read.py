try:
    with open('project\sample.txt', 'w') as file:
        file.write('Welcome to file handling in Python\n')        
except Exception as e:
    print(f"An error occurred: {e}")