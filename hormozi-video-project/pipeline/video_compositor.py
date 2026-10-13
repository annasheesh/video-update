"""
video_compositor.py - Executes timeline cuts, camera punch-in on jump cut,
and composites HyperFrames alpha motion graphics overlay and final master audio.
"""
import os
import subprocess
import json

def composite_video(
    source_video_path,
    overlay_webm_path,
    final_audio_path,
    output_mp4_path
):
    ffmpeg_bin = r"C:\Users\sanfu\AppData\Local\Microsoft\WinGet\Links\ffmpeg.exe"
    if not os.path.exists(ffmpeg_bin):
        ffmpeg_bin = "ffmpeg"

    os.makedirs(os.path.dirname(output_mp4_path), exist_ok=True)
    temp_cut_video = "hormozi-video-project/composition/temp_cut_video.mp4"

    # Step 1: Render edited footage with jump cut and 110% camera punch-in:
    # Segment 1 (1.05s to 4.15s): 100% wide framing (1080x1920)
    # Segment 2 (5.55s to 8.75s): 110% punch-in centered (scale 1188x2112, crop 1080x1920)
    
    # We use FFmpeg filter_complex:
    # [0:v] trim=start=1.05:end=4.15,setpts=PTS-STARTPTS,scale=1080:1920,fps=30[v1];
    # [0:v] trim=start=5.55:end=8.75,setpts=PTS-STARTPTS,scale=1188:2112,crop=1080:1920:(in_w-out_w)/2:(in_h-out_h)/2,fps=30[v2];
    # [v1][v2]concat=n=2:v=1:a=0[vbase];
    # [vbase][1:v]overlay=0:0:format=auto[vfinal]
    
    cmd = [
        ffmpeg_bin,
        "-y",
        "-i", source_video_path,
        "-vcodec", "libvpx-vp9",
        "-i", overlay_webm_path,
        "-i", final_audio_path,
        "-filter_complex",
        "[0:v]trim=start=1.05:end=4.15,setpts=PTS-STARTPTS,scale=1080:1920,fps=30[v1];"
        "[0:v]trim=start=5.55:end=8.75,setpts=PTS-STARTPTS,scale=1188:2112,crop=1080:1920:(in_w-out_w)/2:(in_h-out_h)/2,fps=30[v2];"
        "[v1][v2]concat=n=2:v=1:a=0[vbase];"
        "[vbase][1:v]overlay=0:0:format=auto[vfinal]",
        "-map", "[vfinal]",
        "-map", "2:a",
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-ar", "48000",
        "-shortest",
        output_mp4_path
    ]
    
    print(f"[VideoCompositor] Executing master compositing...")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"[VideoCompositor] Error during compositing:\n{res.stderr}")
        raise RuntimeError(f"FFmpeg compositing failed: {res.stderr}")
        
    print(f"[VideoCompositor] Successfully rendered final mastered video to {output_mp4_path}!")

if __name__ == "__main__":
    src = "hormozi-video-project/input/original_video.mov"
    overlay = "hormozi-video-project/composition/overlay.webm"
    audio = "hormozi-video-project/audio/final_audio.wav"
    out = "hormozi-video-project/output/final_video.mp4"
    composite_video(src, overlay, audio, out)
