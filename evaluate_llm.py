from datetime import datetime
import pandas as pd


def simulate_response(prompt):
    """
    Simulate LLM response generation.
    """
    response = f"This is a generated response for: '{prompt[:40]}...'"
    length = len(response.split())
    response_time = round(0.5 + 0.1 * len(prompt.split()), 2)
    return response, length, response_time


def evaluate_llm(prompts_file, output_file):
    """
    Read prompts, generate responses, and evaluate metrics.
    """
    df = pd.read_csv(prompts_file)
    results = []

    for i, row in df.iterrows():
        prompt = row["prompt"]
        response, length, time_sec = simulate_response(prompt)
        results.append({
            "prompt": prompt,
            "response": response,
            "response_length": length,
            "response_time_sec": time_sec,
            "timestamp": datetime.utcnow().isoformat()
        })

    df_results = pd.DataFrame(results)
    df_results.to_csv(output_file, index=False)
    print(f"Evaluation completed. Results saved to {output_file}")


if __name__ == "__main__":
    evaluate_llm("prompts.csv", "llm_evaluation_results.csv")
