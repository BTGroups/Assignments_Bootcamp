class Category:
    def __init__(self, category_Id, category_name):
        self.categoryId = category_Id
        self.category_name = category_name 
    
class Topic:
    def __init__(self, topic_id, topic_name):
        self.topic_id = topic_id 
        self.topic_name = topic_name 

class Question:
    def __init__(self, question_id, text, category, topic):
        self.question_id = question_id 
        self.text = text 
        self.category = category 
        self.topic = topic


class MCQ_Question(Question):
    def __init__(self, qid, text, category, topic, options, answer):
        super().__init__(qid, text, category, topic)
        self.options = options 
        self.answer = answer 


class ParagraghQuestion(Question):
    def __init__(self, qid, text, category, topic, word_limit):
        super().__init__(qid, text, category, topic)
        self.word_limit = word_limit 


class ExamPortal:
    def __init__(self):
        self.questions = []
    def add_questions(self, question):
        self.questions.append(question)
    def get_total_questions(self):
        return len(self.questions)
    def get_questions_by_topic(self, topic_name):
        for q in self.questions:
            if q.topic.topic_name == topic_name:
                return q.text 
    def get_questions_by_topic_and_category(self, topic_name, category_name):
        for q in self.questions:
            if q.topic.topic_name == topic_name and q.category.category_name == category_name:
                return q.text


if __name__ == "__main__":
    cat1 = Category(1, "Programming")
    topic1 = Topic(1, "Python")
    portal = ExamPortal()
    portal.add_questions(MCQ_Question(1, "What is Python?", cat1, topic1, ["Language", "Snake"], "Language"))
    portal.add_questions(ParagraghQuestion(2, "Explain Python Features", cat1, topic1, 50))
    print("Total Questions: ",portal.get_total_questions())
    print("Questions on topic: ", portal.get_questions_by_topic("Python"))
    print("Questions based on category and topic: ", portal.get_questions_by_topic_and_category("Python", "Programming"))


