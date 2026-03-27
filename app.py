import streamlit as st
import random

# ファイルから単語を読み込む
with open("words.txt", "r") as f:
    lines = f.readlines()

# 改行を消す
words = [line.strip() for line in lines if line.strip()]

st.title("ことり🐤のキラキラ✨単語帳 ")

# ボタンでランダム表示
if st.button("次へ🦆✨"):
    word = random.choice(words)
    st.write(word)