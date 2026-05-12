# 🍕 Pizza Review RAG Chatbot

A local AI-powered chatbot that answers questions about pizza restaurants using **Retrieval-Augmented Generation (RAG)**. Ask anything about pizza reviews and get intelligent, context-aware answers — all running locally on your machine.

---

## How It Works

1. User submits a question via the terminal
2. The retriever searches a local vector store for relevant pizza reviews
3. Matching reviews are injected into a prompt alongside the question
4. A local LLaMA 3.2 model generates a grounded, expert-sounding answer

```
User Question → Vector Retriever → Relevant Reviews → LLaMA 3.2 → Answer
```

---

## Tech Stack

| Component | Tool |
|---|---|
| LLM | [Ollama](https://ollama.com/) — LLaMA 3.2 (local) |
| LLM Framework | [LangChain](https://www.langchain.com/) |
| Embeddings & Retrieval | `vector.py` (custom retriever) |
| Prompt Management | `ChatPromptTemplate` |

---

## Prerequisites

- Python 3.9+
- [Ollama](https://ollama.com/download) installed and running
- LLaMA 3.2 pulled locally:
  ```bash
  ollama pull llama3.2
  ```

---

## Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/pizza-review-chatbot.git
cd pizza-review-chatbot

# 2. Install dependencies
pip install langchain langchain-ollama langchain-core

# 3. Make sure your vector store is set up (see vector.py)
```

---

## Usage

```bash
python main.py
```

Then interact in the terminal:

```
------------------------------------
Enter a question (or 'q' to quit): What do people think about the crust?

The reviews highlight that customers generally love the thin, crispy crust...

------------------------------------
Enter a question (or 'q' to quit): q
```

---

## Project Structure

```
pizza-review-chatbot/
├── main.py        # Entry point — chatbot loop
├── vector.py      # Vector store setup and retriever
└── README.md
```

---

## Configuration

To swap the model, change the `model` parameter in `main.py`:

```python
model = OllamaLLM(model="llama3.2")  # replace with any Ollama model
```

To adjust the prompt behaviour, edit the `template` string in `main.py`.

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## License

[MIT](LICENSE)
