from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


def load_questions():
    """Cargará las preguntas que esten almacenadas en la base de datos
    y regresará la lista de objetos(Question) con la preguntas"""
    question_bank_lq = []

    # Recorremos los datos con las preguntas y sus respuestas
    for question in question_data:
        text = question["question"]
        answer = question["correct_answer"]

        # creamos el objeto y lo metemos en la pregunta
        new_question = Question(text, answer)
        question_bank_lq.append(new_question)

    return question_bank_lq


question_bank = load_questions()
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
