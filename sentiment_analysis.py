import pandas as pd
from textblob import TextBlob

# Step 1: Load the dataset
df = pd.read_csv("reviews.csv")

# Step 2: Define a function to get sentiment


def get_sentiment(review):
    blob = TextBlob(review)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Step 3: Apply the sentiment function to each review
df["Sentiment"] = df["review"].apply(get_sentiment)

# Step 4: Show the results
print(df)

# Step 5: Save to new CSV
df.to_csv("sentiment_output.csv", index=False)

import matplotlib.pyplot as plt

# Count each sentiment type
sentiment_counts = df['Sentiment'].value_counts()

# Create bar chart
plt.figure(figsize=(6, 4))
sentiment_counts.plot(kind='bar', color=['green', 'red', 'gray'])

# Add labels and title
plt.title("Sentiment Distribution of Reviews")
plt.xlabel("Sentiment")
plt.ylabel("Number of Reviews")
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.tight_layout()
plt.show()

