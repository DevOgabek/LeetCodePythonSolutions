def create_python_file(problem_name):

    file_name = problem_name.lower().replace(' ', '_') + '.py'
    file_path = f'Python/{file_name}'

    with open(file_path, 'w') as file:
        file.write(f"""# {problem_name}

class Solution(object):
    def build_array(self, nums):
        # Your solution here
        pass

solution = Solution()
print(solution.build_array())""")

    print(f"File '{file_path}' has been created.")
    
    return file_name

if __name__ == "__main__":
    problem_name = input("Enter the name of the problem: ")
    file_name = create_python_file(problem_name)
    with open('README.md', 'a') as readme:
        readme.write(f"\n- [{problem_name}](Python/{file_name})")
    print("Entry added to README.md.")
