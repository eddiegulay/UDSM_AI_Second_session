import random


class QABot:
    def __init__(self):
        self.questions = ["What is the weather like today?", "What time is it?", "What is the meaning of life?", "What is the capital of France?", "Who is the current president of the United States?", "Hi"]
        self.answers = {
            0: ["It's sunny and warm!", "It's cloudy and rainy.", "It's cool and breezy."],
            1: ["It's currently 2:30 pm.", "It's almost 5 pm.", "It's exactly 11 am."],
            2: ["That's a philosophical question, I'm not sure I have the answer!", "It's up to each individual to decide.", "The meaning of life is different for everyone."],
            3: ["The capital of France is Paris.", "Paris is the capital of France.", "Paris!"],
            4: ["The current president of the United States is Joe Biden.", "Joe Biden is the current president of the United States.", "It's Joe Biden!"],
            5: ["Hello!", "Hi!", "Hey there!", "I am not in the mood to talk right now."]
        }

    def get_answer(self, question):
        # get the index of the question
        if question in self.questions:
            index = self.questions.index(question)
            # return a random answer from the list of answers
            return random.choice(self.answers[index])
        else:
            return "Give me more questions to learn!"
