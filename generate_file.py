def create_python_file(problem_name):

    file_name = problem_name.lower().replace(' ', '_') + '.py'
    file_path = f'Python/{file_name}'

    with open(file_path, 'w') as file:
        file.write(f"""# {problem_name}

class Solution(object):
    def build_array(self, nums: list):
        # Your solution here
        pass

test = Solution()
print(test.build_array([1, 2, 3, 4, 5]))""")

    print(f"File '{file_path}' has been created.")

if __name__ == "__main__":
    problem_name = input("Enter the name of the problem: ")
    create_python_file(problem_name)