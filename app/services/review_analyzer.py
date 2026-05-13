from app.models.review_models import ReviewAnalysis
from app.services.llm_service import LLMService
from app.prompts.review_prompt import get_review_prompt


class ReviewAnalyzer:

    def __init__(self):

        llm = LLMService.get_llm()

        self.llm = llm.with_structured_output(ReviewAnalysis)

        self.prompt = get_review_prompt()

        self.chain = self.prompt | self.llm

    def analyze_review(self, review: str):

        return self.chain.invoke({"review": review})

    def analyze_reviews(self, reviews: list):

        return [self.analyze_review(r) for r in reviews]