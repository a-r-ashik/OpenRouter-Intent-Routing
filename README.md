# 🔀 Smart AI Model Router

> Automatically selects the best free LLM based on your input — powered by [OpenRouter](https://openrouter.ai).

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit&logoColor=white)
![OpenRouter](https://img.shields.io/badge/OpenRouter-Free_API-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📌 What Is This?

Most AI apps send every query to the same model — regardless of whether it's a coding task, a math problem, or casual chat. That's wasteful and often gives worse results.

**Smart AI Router** fixes that. It reads your query, detects the intent, and routes it to the model best suited for that type of task — automatically, with fallback support, all for free.

---

## 📁 Project Structure

```
smart-ai-router/
├── app.py            ← Streamlit UI + OpenRouter API calls
├── router.py         ← Core routing logic (keyword detection)
├── .env              ← Your API key (never commit this!)
├── requirements.txt  ← Python dependencies
└── README.md
```

---

## 🧠 How Routing Works

```
User Query
    │
    ▼
router.py  ──  keyword scan
    │
    ├── coding keywords?    →  💻  deepseek/deepseek-r1:free
    ├── reasoning keywords? →  🧠  google/gemma-3-12b-it:free
    └── general chat?       →  💬  meta-llama/llama-3.3-70b-instruct:free
    │
    ▼
OpenRouter API  →  Response
         │
         └── rate limited? → auto fallback to next model
```

### Routing Rules

| Intent | Example Keywords | Primary Model |
|--------|-----------------|---------------|
| 💻 Coding | `code` `python` `bug` `error` `function` `api` `sql` `html` `flask` | `deepseek/deepseek-r1:free` |
| 🧠 Reasoning | `why` `explain` `how does` `math` `analyze` `compare` `summarize` | `google/gemma-3-12b-it:free` |
| 💬 General | *(everything else)* | `meta-llama/llama-3.3-70b-instruct:free` |

All models are **100% free** on OpenRouter — no billing required.

### Fallback System

If the primary model is rate-limited or unavailable, the app automatically retries with the next available model — no manual action needed.

---

## 🚀 Setup Guide

### Step 1 — Clone or download the project

```bash
git clone https://github.com/yourname/smart-ai-router.git
cd smart-ai-router
```

### Step 2 — Create virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate      # Windows
source .venv/bin/activate   # Mac/Linux
```

### Step 3 — Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4 — Get your free API key

1. Go to [https://openrouter.ai](https://openrouter.ai)
2. Create a free account
3. Navigate to **Keys → Create Key**
4. Copy your key

### Step 5 — Add key to `.env`

```env
OPENROUTER_API_KEY=sk-or-xxxxxxxxxxxxxx
```

> ⚠️ Never share or commit your `.env` file.

### Step 6 — Run

**Full Streamlit UI:**
```bash
streamlit run app.py
```

**Terminal-only router test:**
```bash
python router.py
```

---

## 🧪 Test Cases

| Query | Detected Intent | Model Selected |
|-------|----------------|----------------|
| `"Write a Python Flask API"` | coding | 💻 DeepSeek R1 |
| `"Fix this JavaScript bug"` | coding | 💻 DeepSeek R1 |
| `"Explain Newton's laws"` | reasoning | 🧠 Gemma 3 12B |
| `"What is machine learning?"` | reasoning | 🧠 Gemma 3 12B |
| `"Hi how are you"` | general | 💬 Llama 3.3 70B |

---

## 🖥️ UI Features

- **Model badge** — shows which model was selected and why
- **Auto fallback** — switches model silently if rate-limited
- **Example buttons** — one-click test queries
- **Sidebar** — routing rules at a glance
- **Clear chat** — reset conversation anytime

---

## 🔧 Upgrade Ideas

- [ ] **Semantic routing** — use embeddings instead of keywords
- [ ] **LangChain / LangGraph** — plug in a proper routing chain
- [ ] **Conversation memory** — remember previous messages per session
- [ ] **Cost optimizer** — always try the cheapest model first

---

## 💡 Concepts You Learn From This Project

| Concept | What It Teaches |
|---------|----------------|
| **Model routing** | Choosing the right AI tool for the right task |
| **OpenRouter API** | One unified API for 100+ LLMs |
| **Fallback system** | Handling rate limits gracefully |
| **Streamlit** | Building Python web apps with no frontend code |
| **dotenv** | Keeping secrets out of your source code |
| **Intent detection** | Understanding what the user actually wants |

---

## 📄 License

MIT — free to use, modify, and share.