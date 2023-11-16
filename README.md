# AWS Certified Cloud Practitioner CLF-C01 Practice Tests Web App

This web application allows users to take quizzes based on Amazon Web Services (AWS) Certified Cloud Practitioner questions. The quiz questions are sourced from [Ditectrev's AWS Certified Cloud Practitioner Practice Tests](https://github.com/Ditectrev/Amazon-Web-Services-AWS-Certified-Cloud-Practitioner-CLF-C01-Practice-Tests-Exams-Questions-Answers).

## Introduction

This project provides a simple Flask web application that presents multiple-choice quiz questions. Users can submit their answers, and the application will provide a score along with feedback on incorrect answers.

## Data Source

The quiz questions used in this project are taken from [Ditectrev's AWS Certified Cloud Practitioner Practice Tests](https://github.com/Ditectrev/Amazon-Web-Services-AWS-Certified-Cloud-Practitioner-CLF-C01-Practice-Tests-Exams-Questions-Answers). Special thanks to Ditectrev for providing this valuable resource.

## How to Run

### Prerequisites

- Python 3
- Flask (install using `pip install Flask`)

### Steps

1. Clone this repository:

    ```bash
    git clone https://github.com/your-username/aws-quiz-web-app.git
    cd aws-quiz-web-app
    ```

2. Run the Flask application:

    ```bash
    python app.py
    ```

3. Open your web browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to access the quiz.

## Adding More Questions

To add more quiz questions, follow the structure in the `data.txt` file. Each question should be formatted as per the example questions in the file. Ensure that the correct answers are marked with `[x]`.

Feel free to contribute by adding more questions and improving the application!

