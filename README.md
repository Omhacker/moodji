# 🌟 MoodJi – Your Vibe, in Emojis! 😄🎭

> Ever struggled to find the perfect emoji for your post, caption, or mood?  
> **MoodJi** feels your emotion and translates it — beautifully.

---

## 🤯 The Problem

You're about to post something on Instagram, X (Twitter), or WhatsApp —  
You *feel* a certain way, but can’t find the right emojis to match your vibe.  
You end up either using random ones… or none at all.

We’ve all been there.

---

## 🎯 The Solution – MoodJi

**MoodJi** is a real-time emoji translator for your emotions, captions, or messages.  
It detects the sentiment behind your text and returns the most relevant, expressive emojis to **match your vibe**.

It's like having an emoji-intuition superpower ✨

---

## 🔥 Features

✅ Real-time emoji suggestions from your message  
✅ Smart sentiment detection (TextBlob + VADER Hybrid)  
✅ 🎯 Caption generator with auto-emojis  
✅ 💡 Mood-only detector mode (optional toggle)  
✅ ✂️ Copy your caption in one click  
✅ 🤝 Ready for posts, reels, stories, or status updates  
✅ Built with `streamlit` – lightweight, fast, and beautiful

---

## 💻 How It Works

1. Type a caption or message  
2. MoodJi detects your **sentiment**  
3. It maps your vibe to curated emojis (smart + fun)  
4. Bonus: Get a ready-to-post caption with emojis  
5. Copy & use — like magic ✨

---

## 🧠 Tech Stack

- Python 🐍  
- Streamlit 🌐  
- TextBlob & VADER for Sentiment Analysis 🧠  
- Pyperclip (for clipboard functionality)  
- Custom keyword-emotion-emoji mappings 😍

---

## 🚀 Try it yourself!

**Live app**: https://moodji.streamlit.app  
*(or replace with your deployed domain)*

---

## 📸 Example

**Input:**  
Feeling sleepy but gotta finish this assignment 😓

**MoodJi Output:**  
- Sentiment Score: `+0.03`  
- Emojis: 😐 🤔 🫤 😶  
- Suggested Caption:  
  `Feeling sleepy but gotta finish this assignment 😓 😐 🤔 🫤 😶`

---

## 📦 Installation

```bash
git clone https://github.com/Omhacker/moodji.git
cd moodji
pip install -r requirements.txt
streamlit run app.py
