import pandas as pd


def create_summary_dataframe(results):

    data = []

    for result in results:

        data.append({
            "Summary": result.summary,
            "Sentiment": result.sentiment,
            "Positives": ", ".join(result.positives),
            "Negatives": ", ".join(result.negatives),
            "Emotions": ", ".join(result.emotions)
        })

    return pd.DataFrame(data)