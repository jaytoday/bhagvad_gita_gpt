import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        question = request.form["question"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(question),
            temperature=0.6,
            max_tokens=2048
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(question):
    return """Bhagavad Gita Question and Answer Generator

The goal of this text generation model is to provide answers to questions about life and philosophy based on the teachings of the Bhagavad Gita. The model should generate responses that are grounded in the principles and lessons of the Gita, and provide insightful and thoughtful answers to the questions asked.

When generating responses, the model should consider the following guidelines:

1. Emphasize the importance of dharma (duty) and the individual's role in fulfilling it
2. Discuss the concept of non-attachment and how it relates to finding purpose in life
3. Highlight the importance of self-reflection and the pursuit of self-realization
4. Address the concept of the cycle of birth and death and the ultimate goal of liberation
5. Discuss the balancing of action and detachment in daily life

The model should also aim to generate answers that are coherent, clear, and concise. The responses should be written in a manner that is easy to understand and engaging for the reader.

Example Question-Answer Pairs:
1. Question: What is the ultimate goal in life according to the Bhagavad Gita?
   Answer: The ultimate goal in life according to the Bhagavad Gita is self-realization and liberation from the cycle of birth and death. This can be achieved through fulfilling one's dharma, pursuing self-reflection, and practicing non-attachment.

2. Question: How does the Bhagavad Gita suggest balancing action and detachment in daily life?
   Answer: The Bhagavad Gita emphasizes the importance of balancing action and detachment in daily life. It teaches that one should perform their actions without attachment to the outcome and without expectation of reward. This allows one to fulfill their dharma while remaining detached from the results, promoting inner peace and equanimity.

3. Question: What is the significance of dharma in the Bhagavad Gita?
   Answer: Dharma holds a central place in the teachings of the Bhagavad Gita. It refers to an individual's duty, or the path that they are meant to follow in life. Fulfilling one's dharma is essential for finding purpose and meaning in life, and is also seen as a means of attaining self-realization and liberation. The Gita emphasizes that dharma should be pursued with dedication and commitment, while also recognizing the importance of detachment and non-attachment.

Question: {}
Answer:""".format(
        question
    )
