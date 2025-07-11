import streamlit as st
import pyperclip
from emoji_logic import analyze_text_to_emoji

st.set_page_config(page_title="MoodJi 🎭", layout="centered")

st.title("🌟 MoodJi – Your Vibe, in Emojis!")
st.markdown("Just type a caption, message, or thought — and let MoodJi translate your mood into emojis! 😄")

user_input = st.text_input("📝 What's on your mind?")

if user_input:
    emojis, score = analyze_text_to_emoji(user_input)

    st.markdown(f"**Sentiment Score**: `{score}`")
    st.markdown("### 🧠 Emoji Translation:")

    # Tooltip & Copy
    emoji_text = " ".join(emojis)
    st.markdown(
        f"""
        <div title="Click to copy!" style="cursor: pointer; font-size: 32px;"
             onclick="navigator.clipboard.writeText('{emoji_text}')">
             {emoji_text}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Caption suggestion
    st.markdown("---")
    st.subheader("✨ Suggested Caption:")
    st.code(f"{user_input} {emoji_text}", language="markdown")

    st.success("Copied? Use it for reels, posts, or messages!")
