import openai
import os
import subprocess

def generate_problem(prompt):
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        raise ValueError("API key is missing or invalid")
    openai.api_key = api_key
    
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content.strip()

def update_files(problem_text):
    parts = problem_text.split('---')
    print(parts)
    if len(parts) < 4:
        print("생성된 텍스트:", problem_text)
        raise ValueError("생성된 문제 텍스트 형식이 올바르지 않습니다.")
    
    problem_description, problem_code, solution_code, test_case_code = parts[:4]

    with open('README.md', 'w') as readme_file:
        readme_file.write(f"# 과제 설명\n\n## 문제 설명\n{problem_description.strip()}\n\n## 제출 방법\n1. `src/solution.cpp` 파일을 수정하여 문제를 해결하세요.\n2. `tests/test_solution.cpp` 파일을 통해 테스트를 확인하세요.\n3. 완료되면, 변경 사항을 커밋하고 푸시하세요.\n")

    with open('src/solution.cpp', 'w') as solution_file:
        solution_file.write(problem_code.strip())

    with open('tests/test_solution.cpp', 'w') as test_file:
        test_file.write(test_case_code.strip())

def compile_and_run_cpp(file_path):
    # Compile the C++ code
    compile_command = f"g++ {file_path} -o test_program"
    compile_process = subprocess.run(compile_command, shell=True, capture_output=True, text=True)

    if compile_process.returncode != 0:
        print("컴파일 오류:", compile_process.stderr)
        return

    # Run the compiled program
    run_process = subprocess.run("./test_program", shell=True, capture_output=True, text=True)
    
    if run_process.returncode != 0:
        print("프로그램 실행 오류:", run_process.stderr)
    else:
        print("프로그램 실행 결과:", run_process.stdout)

prompt = """
1. 자연어 문제 설명
나는 대학교 교수인데 학생들한테 문제를 낼거야 c++ 문제를 낼건데 힌트는 2개줬으면 좋겠는데 한개는 쉬운거 한개는 어려운 힌트로 제공해줘 
범위는 반복문이야 난이도는 어렵게 내줘!
예시를 줄게! '사용자로부터 정수 n을 입력 받아서 그 정수값의 팩토리얼을 구하는 프로그램을 작성하세요. 팩토리얼이란 자연수 n에 대해서 1부터 n까지의 모든 자연수를 곱하는 것을 합니다. 예를 들어, 5의 팩토리얼은 5 x 4 x 3 x 2 x 1 = 120입니다.'
이런식으로 작성해줬으면 좋겠어!
그리고 문제 설명할때 입력 출력도 예시로 제공해줘! 테스트케이스 처럼! 한개만! 형식에 맞게 제공해줬으면 좋겠다
---

2. 문제코드
기본적인 문제 코드만 제시해줘 학생들이 작성할수 있도록 적당한 힌트만 제공해줘 형식에 맞게 제공해줘~
#include <iostream>
using namespace std;
int factorial(int n) {
    // 여기에 코드를 구현하세요.
}
int main() {
    int n;
    cin >> n;
    cout << factorial(n) << endl;
    return 0;
}
이런식으로 작성해줬으면 좋겟어!
---

3. 정답코드
문제에 대한 정답 코드를 입력해줘 형식에 맞게 제공해줘~
---

4. 테스트 케이스
문제에 대한 테스트 케이스 예제를 10개정도 생성해줘 형식에 맞게 생성해줘~
생성된 거에 1. 자연어 문제 설명 : 이나 2. 문제코드 : 이런거 추가하지마~~~
""" # 닫는 삼중 따옴표

problem = generate_problem(prompt)
update_files(problem)
