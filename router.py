CODING_KEYWORDS = [
    "code", "python", "javascript", "java", "c++", "bug", "error", "debug",
    "function", "class", "api", "build", "compile", "syntax", "script",
    "program", "algorithm", "database", "sql", "html", "css", "react",
    "flask", "django", "fastapi", "fix", "implement", "loop", "array"
]

REASONING_KEYWORDS = [
    "why", "explain", "how does", "what is", "describe", "analyze",
    "compare", "difference", "solve", "math", "logic", "reason",
    "calculate", "evaluate", "summarize", "theory", "concept",
    "pros and cons", "advantage", "disadvantage", "history", "science"
]

MODELS = {
    "coding":    "deepseek/deepseek-r1:free",
    "reasoning": "google/gemma-3-12b-it:free",
    "general":   "meta-llama/llama-3.3-70b-instruct:free"
}

MODEL_INFO = {
    "coding":    {"name": "DeepSeek R1",   "icon": "💻", "reason": "Detected coding keywords"},
    "reasoning": {"name": "Gemma 3 12B",   "icon": "🧠", "reason": "Detected reasoning keywords"},
    "general":   {"name": "Llama 3.3 70B", "icon": "💬", "reason": "General conversation"},
}

FALLBACKS = {
    "coding":    ["deepseek/deepseek-r1:free", "meta-llama/llama-3.3-70b-instruct:free", "google/gemma-3-12b-it:free"],
    "reasoning": ["google/gemma-3-12b-it:free", "deepseek/deepseek-r1:free", "meta-llama/llama-3.3-70b-instruct:free"],
    "general":   ["meta-llama/llama-3.3-70b-instruct:free", "deepseek/deepseek-r1:free", "google/gemma-3-12b-it:free"],
}

def detect_intent(query: str) -> str:
    q = query.lower()
    for kw in CODING_KEYWORDS:
        if kw in q: return "coding"
    for kw in REASONING_KEYWORDS:
        if kw in q: return "reasoning"
    return "general"

def get_model(query: str) -> dict:
    intent = detect_intent(query)
    info   = MODEL_INFO[intent]
    return {
        "model_id":  MODELS[intent],
        "fallbacks": FALLBACKS[intent],
        "intent":    intent,
        "name":      info["name"],
        "icon":      info["icon"],
        "reason":    info["reason"],
    }

if __name__ == "__main__":
    print("Smart AI Router — type 'exit' to quit\n")
    while True:
        try:
            q = input("Query: ").strip()
            if not q: continue
            if q.lower() in ("exit","quit"): break
            r = get_model(q)
            print(f"  → {r['icon']} {r['name']} ({r['model_id']})\n")
        except KeyboardInterrupt:
            break