import os

def search_problem_status(problem_name):
    problem_filename = problem_name.lower().replace(' ', '_') + '.py'
    
    files = os.listdir('.')
    if problem_filename in files:
        file_number = files.index(problem_filename) + 1
        print(f'The problem "{problem_name}" is resolved.')
        print(f'Solution found in file: {problem_filename}')
        print(f'File position in the list: {file_number}')
    else:
        print(f'The problem "{problem_name}" is not resolved.')

if __name__ == "__main__":
    user_input = input("Enter the name of the problem: ")
    search_problem_status(user_input)