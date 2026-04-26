import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from router import get_model

load_dotenv()
API_KEY = os.getenv("OPENROUTER_API_KEY", "")

st.set_page_config(page_title="Smart AI Router", page_icon="🔀", layout="centered")

st.markdown("""
<style>
.model-badge { display:inline-block; padding:3px 10px; border-radius:20px; font-size:13px; font-weight:600; margin-bottom:6px; }
.coding-badge    { background:#dbeafe; color:#1e40af; }
.reasoning-badge { background:#f3e8ff; color:#6b21a8; }
.general-badge   { background:#dcfce7; color:#166534; }
</style>
""", unsafe_allow_html=True)

st.title("🔀 Smart AI Router")

if not API_KEY:
    st.error("Add OPENROUTER_API_KEY to .env")
    st.stop()

client = OpenAI(base_url="https://openrouter.ai/api/v1", api_key=API_KEY)

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.markdown("""
| Intent | Model |
|--------|-------|
| 💻 Coding | DeepSeek R1 |
| 🧠 Reasoning | Gemma 3 12B |
| 💬 General | Llama 3.3 70B |
""")
    if st.button("🗑️ Clear"):
        st.session_state.history = []
        st.rerun()

# Example buttons
cols = st.columns(3)
for col, ex in zip(cols, ["Write a Python function", "Explain Newton's laws", "Hi there"]):
    if col.button(ex, use_container_width=True):
        st.session_state["prefill"] = ex

# Chat history display
for msg in st.session_state.history:
    with st.chat_message(msg["role"]):
        if msg["role"] == "assistant" and "meta" in msg:
            m = msg["meta"]
            st.markdown(f'<span class="model-badge {m["intent"]}-badge">{m["icon"]} {m["name"]}</span>', unsafe_allow_html=True)
        st.markdown(msg["content"])

# Input
prefill = st.session_state.pop("prefill", "")
query = st.chat_input("Ask anything…") or prefill

if query:
    st.session_state.history.append({"role": "user", "content": query})
    with st.chat_message("user"):
        st.markdown(query)

    routing = get_model(query)

    with st.chat_message("assistant"):
        st.markdown(f'<span class="model-badge {routing["intent"]}-badge">{routing["icon"]} {routing["name"]}</span>', unsafe_allow_html=True)

        reply = None
        with st.spinner("Thinking…"):
            for model_id in routing["fallbacks"]:
                try:
                    res = client.chat.completions.create(
                        model=model_id,
                        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.history],
                        max_tokens=300,
                        extra_headers={"HTTP-Referer": "https://smart-ai-router.local", "X-Title": "Smart AI Router"}
                    )
                    reply = res.choices[0].message.content
                    break
                except Exception as e:
                    if "429" in str(e) or "404" in str(e):
                        continue
                    reply = f"❌ {str(e)}"
                    break

        if reply is None:
            reply = "❌ All models rate-limited. Wait a minute and retry."

        st.markdown(reply)

    st.session_state.history.append({"role": "assistant", "content": reply, "meta": routing})