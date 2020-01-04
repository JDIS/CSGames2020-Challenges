import json


class Quiz():
    # TODO: Doc

    def __init__(self, questions_file):
        # TODO: Doc
        self.questions = []
        self.current_question = 0

        self.intro = 'Voici le temps de tester vos connaissances sur ' \
            + 'l\'algorithme RSA ! RSA possède plusieurs failles possibles ' \
            + 's\'il est mal implémenté ou si certaines valeurs sont mal ' \
            + 'choisies. Répondez aux questions suivantes pour obtenir ' \
            + 'le flag !\n' \
            + 'Tout au long de ces questions:\n' \
            + 'phi = totient(n)\n' \
            + 'c = ciphertext (texte encodé)\n' \
            + 'm = message (texte clair)\n' \
            + 'd = d\n' \
            + 'p = p\n' \
            + 'q = q\n' \
            + 'e = e\n' \
            + 'De plus, toutes les valeurs seront des entiers pour ' \
            + 'faciliter les échanges. Bonne chance !\n\n'
        self.pre = 'Avec les valeurs suivantes'
        self.post = ''
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
