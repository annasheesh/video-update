"""
media_analyzer.py - Inspects input footage and extracts technical metadata using FFprobe.
"""
import subprocess
import json
import os
import sys

def analyze_media(input_path, output_json):
    ffmpeg_bin = r"C:\Users\sanfu\AppData\Local\Microsoft\WinGet\Links\ffprobe.exe"
    if not os.path.exists(ffmpeg_bin):
        ffmpeg_bin = "ffprobe"

    cmd = [
        ffmpeg_bin,
        "-v", "error",
        "-show_format",
        "-show_streams",
        "-of", "json",
        input_path
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True, check=True)
    probe_data = json.loads(res.stdout)
    
    fmt = probe_data.get("format", {})
    streams = probe_data.get("streams", [])
    
    video_stream = next((s for s in streams if s.get("codec_type") == "video"), None)
    audio_stream = next((s for s in streams if s.get("codec_type") == "audio"), None)
    
    # Check rotation
    rotation = 0
    if video_stream:
        # Check side data
        for side in video_stream.get("side_data_list", []):
            if "rotation" in side:
                rotation = side["rotation"]
        # Check tags
        if not rotation and "tags" in video_stream and "rotate" in video_stream["tags"]:
            rotation = int(video_stream["tags"]["rotate"])
            
    media_info = {
        "file_name": os.path.basename(input_path),
        "file_path": os.path.abspath(input_path),
        "file_size_bytes": int(fmt.get("size", 0)),
        "duration_seconds": float(fmt.get("duration", 0)),
        "format_name": fmt.get("format_name"),
        "bit_rate": int(fmt.get("bit_rate", 0)),
        "video": {
            "codec_name": video_stream.get("codec_name") if video_stream else None,
            "width": int(video_stream.get("width", 0)) if video_stream else 0,
            "height": int(video_stream.get("height", 0)) if video_stream else 0,
            "r_frame_rate": video_stream.get("r_frame_rate") if video_stream else None,
            "avg_frame_rate": video_stream.get("avg_frame_rate") if video_stream else None,
            "pix_fmt": video_stream.get("pix_fmt") if video_stream else None,
            "rotation": rotation,
            "display_width": 1080 if abs(rotation) in [90, 270] else (int(video_stream.get("width", 0)) if video_stream else 0),
            "display_height": 1920 if abs(rotation) in [90, 270] else (int(video_stream.get("height", 0)) if video_stream else 0),
            "is_portrait": abs(rotation) in [90, 270] or (video_stream and int(video_stream.get("height", 0)) > int(video_stream.get("width", 0)))
        },
        "audio": {
            "codec_name": audio_stream.get("codec_name") if audio_stream else None,
            "sample_rate": int(audio_stream.get("sample_rate", 0)) if audio_stream else 0,
            "channels": int(audio_stream.get("channels", 0)) if audio_stream else 0,
            "channel_layout": audio_stream.get("channel_layout") if audio_stream else None,
            "bit_rate": int(audio_stream.get("bit_rate", 0)) if audio_stream else 0
        }
    }
    
    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(media_info, f, indent=2)
        
    print(f"[MediaAnalyzer] Successfully analyzed {input_path}")
    print(f"  Duration: {media_info['duration_seconds']:.2f}s")
    print(f"  Video: {media_info['video']['width']}x{media_info['video']['height']} (Rotation: {rotation}) -> Display: {media_info['video']['display_width']}x{media_info['video']['display_height']}")
    print(f"  Audio: {media_info['audio']['channels']} ch @ {media_info['audio']['sample_rate']} Hz")
    return media_info

if __name__ == "__main__":
    inp = "hormozi-video-project/input/original_video.mov"
    out = "hormozi-video-project/analysis/media_info.json"
    analyze_media(inp, out)
