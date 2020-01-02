import json


class Quiz():
    # TODO: Doc

    def __init__(self, questions_file):
        # TODO: Doc
        self.questions = []
        self.current_question = 0

        self.intro = 'INTRO'
        self.pre = 'Avec les nombres ...'
        self.post = 'Quel est le suivant ?'
        self.prompt = '>'

        self.right = 'Bonne réponse !\n\n'
        self.wrong = 'Mauvaise réponse\n\n'

        self._load_questions(questions_file)

    def _load_questions(self, questions_file):
        # TODO: Doc
        with open(questions_file) as json_file:
            questions = json.load(json_file)["questions"]
            assert(type(questions) == list)
            self.questions = questions

    def get_question(self):
        # TODO: Doc
        [q, _] = self.questions[self.current_question]
        return '{}\n{}\n{}\n{}'.format(self.pre, q, self.post, self.prompt)

    def answer_question(self, answer):
        # TODO: Doc
        [_, a] = self.questions[self.current_question]
        clean_answer = answer.strip()
        if a == clean_answer:
            self.current_question += 1
            return True
        return False

    def is_done(self):
        # TODO: Doc
        return self.current_question == len(self.questions)
