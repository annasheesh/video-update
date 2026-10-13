"""
caption_generator.py - Generates Hormozi-style animated captions and valid SRT files
with sequential indices and precise timestamps.
"""
import os
import json

def format_srt_time(seconds):
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    millis = int(round((seconds - int(seconds)) * 1000))
    if millis >= 1000:
        secs += 1
        millis -= 1000
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"

def generate_captions():
    # Hormozi style subtitle cue list
    cues = [
        {
            "id": 1,
            "start": 0.00,
            "end": 0.50,
            "plain_text": "BECAUSE",
            "html_text": "BECAUSE",
            "highlight": None
        },
        {
            "id": 2,
            "start": 0.50,
            "end": 1.10,
            "plain_text": "EVENTUALLY",
            "html_text": "<font color='#FFDF00'>EVENTUALLY</font>",
            "highlight": "EVENTUALLY"
        },
        {
            "id": 3,
            "start": 1.10,
            "end": 1.55,
            "plain_text": "WHETHER YOU",
            "html_text": "WHETHER YOU",
            "highlight": None
        },
        {
            "id": 4,
            "start": 1.55,
            "end": 2.10,
            "plain_text": "START NOW",
            "html_text": "START <font color='#00FF66'>NOW</font>",
            "highlight": "NOW"
        },
        {
            "id": 5,
            "start": 2.10,
            "end": 2.50,
            "plain_text": "OR WHETHER",
            "html_text": "OR WHETHER",
            "highlight": None
        },
        {
            "id": 6,
            "start": 2.50,
            "end": 3.10,
            "plain_text": "START LATER,",
            "html_text": "START <font color='#FF3B30'>LATER,</font>",
            "highlight": "LATER"
        },
        {
            "id": 7,
            "start": 3.10,
            "end": 3.65,
            "plain_text": "YOU WILL",
            "html_text": "YOU WILL",
            "highlight": None
        },
        {
            "id": 8,
            "start": 3.65,
            "end": 4.35,
            "plain_text": "HIT THAT AGE",
            "html_text": "HIT THAT <font color='#FFDF00'>AGE</font>",
            "highlight": "AGE"
        },
        {
            "id": 9,
            "start": 4.35,
            "end": 4.90,
            "plain_text": "WHERE YOU",
            "html_text": "WHERE YOU",
            "highlight": None
        },
        {
            "id": 10,
            "start": 4.90,
            "end": 5.55,
            "plain_text": "DON'T EVEN HAVE",
            "html_text": "<font color='#FF3B30'>DON'T</font> EVEN HAVE",
            "highlight": "DON'T"
        },
        {
            "id": 11,
            "start": 5.55,
            "end": 6.30,
            "plain_text": "THAT MUCH TIME.",
            "html_text": "THAT MUCH <font color='#FFDF00'>TIME.</font>",
            "highlight": "TIME"
        }
    ]

    # Generate standard SRT
    srt_lines = []
    for c in cues:
        srt_lines.append(str(c["id"]))
        time_str = f"{format_srt_time(c['start'])} --> {format_srt_time(c['end'])}"
        srt_lines.append(time_str)
        srt_lines.append(c["plain_text"])
        srt_lines.append("")

    srt_content = "\n".join(srt_lines)
    
    # Save review SRT and output SRT
    os.makedirs("hormozi-video-project/subtitles", exist_ok=True)
    os.makedirs("hormozi-video-project/output", exist_ok=True)
    
    with open("hormozi-video-project/subtitles/captions_review.srt", "w", encoding="utf-8") as f:
        f.write(srt_content)
    with open("hormozi-video-project/output/final_captions.srt", "w", encoding="utf-8") as f:
        f.write(srt_content)
        
    # Also save structured JSON for HyperFrames rendering
    with open("hormozi-video-project/subtitles/captions_data.json", "w", encoding="utf-8") as f:
        json.dump(cues, f, indent=2)
        
    print(f"[CaptionGenerator] Successfully wrote captions_review.srt, final_captions.srt, and captions_data.json ({len(cues)} cues)")
    return cues

if __name__ == "__main__":
    generate_captions()
