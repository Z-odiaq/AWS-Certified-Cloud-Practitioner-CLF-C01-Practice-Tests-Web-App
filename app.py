# app.py

from flask import Flask, render_template, request

app = Flask(__name__)
data = "data.txt"
items_per_page = 20
page = 1
def read_questions_from_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def parse_questions(questions_content):
    questions = []
    current_question = None

    for line in questions_content.split('\n'):
        if line.startswith("###"):
            if current_question:
                questions.append(current_question)
            current_question = {'question': line[4:].strip(), 'choices': []}
        elif line.startswith("- [ ]") or line.startswith("- [x]"):
            current_question['choices'].append({
                'text': line[5:].strip(),
                'is_correct': line.startswith("- [x]")
            })

    if current_question:
        questions.append(current_question)

    return questions

def paginate_questions(questions):
    paginated_questions = [questions[i:i+items_per_page] for i in range(0, len(questions), items_per_page)]
    return paginated_questions

@app.route('/')
def index():
    file_path = data
    questions_content = read_questions_from_file(file_path)
    questions = parse_questions(questions_content)
    page_size = items_per_page
    paginated_questions = list(paginate_questions(questions))
    return render_template('quiz.html', questions=paginated_questions[0],  current_page=0, total_pages=len(paginated_questions))

@app.route('/<int:page_number>', methods=['GET'])
def show_page(page_number):
    file_path = data
    page = page_number
    questions_content = read_questions_from_file(file_path)
    questions = parse_questions(questions_content)
    page_size = items_per_page
    paginated_questions = list(paginate_questions(questions))

    if 1 <= page_number <= len(paginated_questions):
        return render_template('quiz.html', questions=paginated_questions[page_number - 1], current_page=page_number, total_pages=len(paginated_questions))
    else:
        return "Page not found", 404
    
    
@app.route('/submit/<int:page_number>', methods=['POST'])
def submit(page_number):
    user_answers = request.form.to_dict(flat=False)
    file_path = data
    questions_content = read_questions_from_file(file_path)
    questions = parse_questions(questions_content)
    paginated_questions = paginate_questions(questions)
    score = 0
    incorrect_answers = {}
    page_number = 1 if page_number == 0 else page_number

    for i, question in enumerate(paginated_questions[page_number -1]):
        correct_choice_indices = [index for index, choice in enumerate(question['choices']) if choice['is_correct']]
        user_answer_indices = [int(index) for index in user_answers.get(str(i), [])]

        if set(correct_choice_indices) == set(user_answer_indices):
            score += 1
        else:
            incorrect_answers[i] = {'correct_choices': correct_choice_indices, 'user_choices': user_answer_indices}
    return render_template('result.html', paginated_questions=paginated_questions, total=items_per_page, current_page= page_number , score=score, incorrect_answers=incorrect_answers )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
