import os
import json
from datasets import Dataset
from ragas.metrics import answer_relevancy, faithfulness, context_recall, context_utilization
from ragas import evaluate
import pandas as pd

# Load the generated test set
testset_path = os.path.join(os.path.dirname(__file__), "prompts.json")

with open(testset_path, "r") as f:
    testset = json.load(f)

# Convert the test set to the format suitable for ragas evaluation
data_samples = {
    'question': [item['question'] for item in testset],
    'answer': [item['answer'] for item in testset],
    'contexts': [item['contexts'] for item in testset],
    'ground_truth': [item['ground_truths'] for item in testset],
}
dataset = Dataset.from_dict(data_samples)

# Evaluate the dataset using ragas
result = evaluate(
    dataset,
    metrics=[
        context_utilization,
        faithfulness,
        answer_relevancy,
        context_recall,
    ],
)

# Convert results to pandas DataFrame and print
df = result.to_pandas()
print(df.head())

# Save evaluation results to a CSV file
evaluation_results_path = "./evaluation_results.csv"
df.to_csv(evaluation_results_path, index=False)
print(f"Evaluation results saved to {evaluation_results_path}")
