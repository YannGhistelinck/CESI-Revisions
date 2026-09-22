#!/usr/bin/env python3
"""Generate TTS audio for all notion and theme files."""

import asyncio
import os
import re
import glob

import edge_tts

VAULT = os.path.dirname(os.path.abspath(__file__))
NOTIONS_DIR = os.path.join(VAULT, "Notions")
THEMES_DIR = os.path.join(VAULT, "Thèmes")
AUDIO_NOTIONS = os.path.join(VAULT, "Audios", "Notions")
AUDIO_THEMES = os.path.join(VAULT, "Audios", "Thèmes")
VOICE = "fr-FR-DeniseNeural"


def clean_markdown(text: str) -> str:
    """Remove markdown formatting for TTS."""
    text = re.sub(r">\s*", "", text)
    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"\[\[.*?\]\]", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"^- ", "", text, flags=re.MULTILINE)
    text = re.sub(r"`[^`]+`", "", text)
    text = re.sub(r"#\S+", "", text)
    text = text.replace("|", "")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_en_bref(filepath: str) -> str | None:
    """Extract the 'En bref' section from a notion file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"## En bref\n(.*?)(?=\n## )", content, re.DOTALL)
    if match:
        return clean_markdown(match.group(1))
    return None


def extract_presentation(filepath: str) -> str | None:
    """Extract the 'Présentation' section from a theme file."""
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    match = re.search(r"## Présentation\n(.*?)(?=\n## )", content, re.DOTALL)
    if match:
        return clean_markdown(match.group(1))
    return None


def get_notion_title(filepath: str) -> str:
    """Get the notion name from filename."""
    return os.path.splitext(os.path.basename(filepath))[0]


def get_theme_short(filepath: str) -> str:
    """Get short theme name like 'T1 — SI et environnement'."""
    name = os.path.splitext(os.path.basename(filepath))[0]
    # "Thème 1 — SI et environnement" -> "T1 — SI et environnement"
    match = re.match(r"Thème (\d+) — (.*)", name)
    if match:
        return f"T{match.group(1)} — {match.group(2)}"
    return name


async def generate_one(text: str, output_path: str, label: str) -> bool:
    """Generate one audio file."""
    if os.path.exists(output_path):
        print(f"  SKIP (exists): {label}")
        return False
    try:
        communicate = edge_tts.Communicate(text, VOICE)
        await communicate.save(output_path)
        print(f"  OK: {label}")
        return True
    except Exception as e:
        print(f"  FAIL: {label} — {e}")
        return False


async def main():
    os.makedirs(AUDIO_NOTIONS, exist_ok=True)
    os.makedirs(AUDIO_THEMES, exist_ok=True)

    # --- Notions ---
    notion_files = sorted(glob.glob(os.path.join(NOTIONS_DIR, "*.md")))
    print(f"\n=== NOTIONS ({len(notion_files)} fichiers) ===\n")

    generated = 0
    skipped = 0
    failed = 0

    for filepath in notion_files:
        title = get_notion_title(filepath)
        text = extract_en_bref(filepath)
        if not text:
            print(f"  SKIP (no 'En bref'): {title}")
            skipped += 1
            continue

        # Prepend title for context when listening
        tts_text = f"{title}. {text}"
        output = os.path.join(AUDIO_NOTIONS, f"N — {title}.mp3")

        if await generate_one(tts_text, output, f"N — {title}"):
            generated += 1
        else:
            if os.path.exists(output):
                skipped += 1
            else:
                failed += 1

    print(f"\nNotions: {generated} generated, {skipped} skipped, {failed} failed")

    # --- Themes ---
    theme_files = sorted(glob.glob(os.path.join(THEMES_DIR, "*.md")))
    print(f"\n=== THEMES ({len(theme_files)} fichiers) ===\n")

    t_generated = 0
    for filepath in theme_files:
        short = get_theme_short(filepath)
        text = extract_presentation(filepath)
        if not text:
            print(f"  SKIP (no 'Présentation'): {short}")
            continue

        theme_name = os.path.splitext(os.path.basename(filepath))[0]
        tts_text = f"{theme_name}. {text}"
        output = os.path.join(AUDIO_THEMES, f"{short}.mp3")

        if await generate_one(tts_text, output, short):
            t_generated += 1

    print(f"\nThèmes: {t_generated} generated")
    print(f"\nTotal: {generated + t_generated} audio files generated")


if __name__ == "__main__":
    asyncio.run(main())
