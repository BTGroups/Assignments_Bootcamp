from typing import List, Set

class Category:
    def __init__(self, category_id: int, category_name: str):
        self.category_id = category_id
        self.category_name = category_name
    

class Topic:
    def __init__(self, topic_id: int, topic_name: str):
        self.topic_id = topic_id
        self.topic_name = topic_name


class Question:
    def __init__(self, question_id: int, text: str, category: Category, topic: Topic):
        self.question_id = question_id
        self.text = text
        self.category = category
        self.topic = topic

    def __hash__(self):
        return hash(self.question_id)

    def __eq__(self, other):
        return isinstance(other, Question) and self.question_id == other.question_id

    def __repr__(self):
        return f"Question(ID={self.question_id}, Text='{self.text[:30]}...')"


class MCQQuestion(Question):
    def __init__(self, question_id: int, text: str, category: Category, topic: Topic,
                 options: List[str], answer: str):
        super().__init__(question_id, text, category, topic)
        if not options or answer not in options:
            raise ValueError("MCQ options must contain the answer")
        self.options = options
        self.answer = answer


class ParagraphQuestion(Question):
    def __init__(self, question_id: int, text: str, category: Category, topic: Topic,
                 word_limit: int):
        super().__init__(question_id, text, category, topic)
        if word_limit <= 0:
            raise ValueError("Word limit must be positive")
        self.word_limit = word_limit



class ExamPortal:
    def __init__(self):
        self.questions: Set[Question] = set()  # set prevents duplicates automatically

    def add_question(self, question: Question) -> None:
        if question in self.questions:
            raise ValueError(f"Question with ID {question.question_id} already exists")
        self.questions.add(question)

    def get_total_questions(self) -> int:
        return len(self.questions)

    def get_questions_by_topic(self, topic_name: str) -> List[str]:
        return [q.text for q in self.questions if q.topic.topic_name == topic_name]

    def get_questions_by_topic_and_category(self, topic_name: str, category_name: str) -> List[str]:
        return [
            q.text
            for q in self.questions
            if q.topic.topic_name == topic_name and q.category.category_name == category_name
        ]


if __name__ == "__main__":
    cat1 = Category(1, "Programming")
    topic1 = Topic(1, "Python")
    portal = ExamPortal()

    q1 = MCQQuestion(1, "What is Python?", cat1, topic1, ["Language", "Snake"], "Language")
    q2 = ParagraphQuestion(2, "Explain Python Features", cat1, topic1, 50)

    portal.add_question(q1)
    portal.add_question(q2)

    # Duplicate check
    try:
        portal.add_question(q1)  # raises ValueError
    except ValueError as e:
        print(e)

    print("Total Questions:", portal.get_total_questions())
    print("Questions on topic:", portal.get_questions_by_topic("Python"))
    print("Questions on topic & category:", portal.get_questions_by_topic_and_category("Python", "Programming"))
