# 🕉️ Bhagavad Gita – Practical Life Guidance Chatbot

An AI-powered chatbot that provides **clear, logical, and practical life guidance** based on the teachings of the **Bhagavad Gita**.  
Instead of generic or hallucinated answers, the chatbot grounds every response in **relevant verses from the Gita**, explained in a rational and modern way.

---

## ✨ Features

- 📖 Answers life and spiritual questions using **authentic Bhagavad Gita verses**
- 🧠 Uses **Retrieval-Augmented Generation (RAG)** to avoid hallucinations
- 🔍 Semantic search to find the most relevant verses
- 🗣️ Explains teachings **logically**, not through blind faith
- 🌐 Simple and interactive **Gradio web interface**
- 🚀 Deployed on **Hugging Face Spaces** [see here](https://huggingface.co/spaces/iamgulshan/YuktiGita) 

---

## 🧩 How It Works (High Level)

1. User asks a life or spiritual question  
2. Relevant verses are retrieved from the Bhagavad Gita using **semantic similarity search**  
3. The LLM generates an answer **strictly grounded in the retrieved verses**  
4. The response explains the essence in a **practical, easy-to-understand manner**

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **FAISS** – vector similarity search
- **Sentence Transformers** – embeddings
- **Hugging Face LLMs**
- **Gradio** – UI
- **Hugging Face Spaces** – deployment

---

## 📂 Project Structure

```text
├── app.py                 # Main Gradio application
├── gita_faiss_index/      # Precomputed FAISS vector store
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
```

---

## 🚀 Running Locally

### 1️⃣ Clone the repository

```bash
git clone https://github.com/gulshanarya/YuktiGita.git
cd YuktiGita
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Set Hugging Face API Token

**Linux / macOS**
```bash
export HUGGINGFACEHUB_API_TOKEN=hf_your_token_here
```

**Windows (PowerShell)**
```powershell
setx HUGGINGFACEHUB_API_TOKEN hf_your_token_here
```

### 4️⃣ Run the app

```bash
python app.py
```

The app will be available at:  
👉 http://localhost:7860

---

## 📌 Example Questions

- What is good karma?
- How should I deal with attachment and desire?
- Why did Arjuna hesitate to fight his own family?
- How can I act without worrying about results?

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and share.
