#!/usr/bin/env python3
"""MiMo Story Writer - Creative writing with MiMo AI."""
import os, argparse
from openai import OpenAI

client = OpenAI(api_key=os.getenv("MIMO_API_KEY"), base_url="https://api.xiaomimimo.com/v1")

def write(prompt, genre="fantasy"):
    resp = client.chat.completions.create(model="mimo-v2.5-pro", messages=[
        {"role": "system", "content": f"Master storyteller in {genre}. Vivid descriptions, compelling characters."},
        {"role": "user", "content": f"Story: {prompt}"}], max_tokens=4000)
    return resp.choices[0].message.content

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("prompt"); p.add_argument("--genre", default="fantasy")
    a = p.parse_args(); print(write(a.prompt, a.genre))
