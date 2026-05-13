from app.data.sample_reviews import reviews
from app.services.review_analyzer import ReviewAnalyzer
from app.utils.dataframe_helper import create_summary_dataframe


def main():

    analyzer = ReviewAnalyzer()

    results = analyzer.analyze_reviews(reviews)

    for idx, result in enumerate(results, start=1):

        print("=" * 60)
        print(f"Review #{idx}")
        print("=" * 60)

        print(result.summary)
        print(result.sentiment)
        print(result.email)

    df = create_summary_dataframe(results)

    print(df.head())


if __name__ == "__main__":
    main()