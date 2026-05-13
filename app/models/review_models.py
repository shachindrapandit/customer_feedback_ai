from pydantic import BaseModel, Field
from typing import List


class ReviewAnalysis(BaseModel):

    summary: str = Field(
        description="Short summary of feedback"
    )

    positives: List[str] = Field(
        description="Positive points"
    )

    negatives: List[str] = Field(
        description="Negative points"
    )

    sentiment: str = Field(
        description="positive, negative, neutral"
    )

    emotions: List[str] = Field(
        description="Client emotions"
    )

    email: str = Field(
        description="Professional email response"
    )