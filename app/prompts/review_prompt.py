from langchain_core.prompts import ChatPromptTemplate


def get_review_prompt():

    return ChatPromptTemplate.from_messages([
        (
            "system",
            """
You are a client experience analyst at ABC.

Analyze the given feedback and extract:
- summary
- positives
- negatives
- sentiment (positive/negative/neutral)
- emotions
- email response

Return structured output only.
"""
        ),
        (
            "human",
            "Client Feedback: {review}"
        )
    ])