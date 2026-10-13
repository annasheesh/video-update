"""
sfx_generator.py - Generates subtle, professional motion sound effects (whoosh, pop, milestone chime)
and mixes them under dialogue at -22 dBFS.
"""
import os
import numpy as np
import scipy.io.wavfile as wavfile
import scipy.signal as signal
import pyloudnorm as pyln

def generate_whoosh(sr=48000, duration=0.35):
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    # Bandpassed shaped noise sweep
    noise = np.random.normal(0, 1, len(t))
    # Envelope: gentle bell curve
    env = np.sin(np.pi * t / duration) ** 2
    # Moving lowpass filter from 300Hz to 2000Hz to 200Hz
    # Simple simulated resonant sweep
    f_center = 200 + 1200 * np.sin(np.pi * t / duration)
    b, a = signal.butter(2, [300 / (sr / 2), 2500 / (sr / 2)], btype='band')
    filtered = signal.lfilter(b, a, noise)
    whoosh = filtered * env
    return whoosh / (np.max(np.abs(whoosh)) + 1e-6)

def generate_pop(sr=48000, duration=0.08):
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    # Pitch drop from 550 Hz down to 180 Hz
    freq = 550 * np.exp(-t * 25)
    phase = 2 * np.pi * np.cumsum(freq) / sr
    sine = np.sin(phase)
    env = np.exp(-t * 40)
    pop = sine * env
    return pop / (np.max(np.abs(pop)) + 1e-6)

def generate_milestone_chime(sr=48000, duration=0.25):
    t = np.linspace(0, duration, int(sr * duration), endpoint=False)
    # Soft high harmonic blip (880 Hz + 1320 Hz)
    sig = 0.6 * np.sin(2 * np.pi * 880 * t) + 0.4 * np.sin(2 * np.pi * 1320 * t)
    env = np.exp(-t * 18)
    chime = sig * env
    return chime / (np.max(np.abs(chime)) + 1e-6)

def mix_sfx(base_audio_path, output_audio_path):
    sr, data = wavfile.read(base_audio_path)
    if data.dtype == np.int16:
        dialogue = data.astype(np.float32) / 32768.0
    else:
        dialogue = data.astype(np.float32)
        
    num_samples = len(dialogue)
    is_stereo = (dialogue.ndim == 2 and dialogue.shape[1] == 2)
    
    sfx_track = np.zeros(num_samples, dtype=np.float32)
    
    # SFX events:
    # 1. t = 0.50s: Entrance of Decision Diagram -> gentle pop
    # 2. t = 1.20s: "Start Now" branch reveal -> soft pop
    # 3. t = 2.10s: "Start Later" branch reveal -> soft pop
    # 4. t = 3.10s: Camera punch-in & Inevitable Milestone -> Whoosh + Chime
    # 5. t = 4.60s: Time Depletion Bottleneck Alert -> subtle warning chime
    
    events = [
        ("pop", 0.50, 0.12),
        ("pop", 1.20, 0.10),
        ("pop", 2.10, 0.10),
        ("whoosh", 3.05, 0.15),
        ("chime", 3.12, 0.12),
        ("chime", 4.62, 0.10)
    ]
    
    for sfx_type, start_time, gain in events:
        if sfx_type == "whoosh":
            raw_sfx = generate_whoosh(sr)
        elif sfx_type == "pop":
            raw_sfx = generate_pop(sr)
        elif sfx_type == "chime":
            raw_sfx = generate_milestone_chime(sr)
        else:
            continue
            
        s_idx = int(start_time * sr)
        e_idx = min(s_idx + len(raw_sfx), num_samples)
        sfx_len = e_idx - s_idx
        if sfx_len > 0:
            sfx_track[s_idx:e_idx] += raw_sfx[:sfx_len] * gain

    # Mix dialogue + sfx
    mixed = np.zeros_like(dialogue)
    if is_stereo:
        mixed[:, 0] = dialogue[:, 0] + sfx_track
        mixed[:, 1] = dialogue[:, 1] + sfx_track
    else:
        mixed = dialogue + sfx_track
        
    # Re-normalize to -14 LUFS, <= -1 dBTP
    meter = pyln.Meter(sr)
    lufs = meter.integrated_loudness(mixed)
    target_lufs = -14.0
    normalized = pyln.normalize.loudness(mixed, lufs, target_lufs)
    
    peak = np.max(np.abs(normalized))
    if peak > 0.891:
        normalized *= (0.891 / peak)
        
    final_lufs = meter.integrated_loudness(normalized)
    final_peak = 20 * np.log10(np.max(np.abs(normalized)))
    print(f"[SFXManager] Mixed dialogue with SFX. Final LUFS: {final_lufs:.2f}, True Peak: {final_peak:.2f} dBTP")
    
    out_int16 = (np.clip(normalized, -1.0, 1.0) * 32767.0).astype(np.int16)
    wavfile.write(output_audio_path, sr, out_int16)
    print(f"[SFXManager] Saved mixed master audio to {output_audio_path}")

if __name__ == "__main__":
    mix_sfx(
        "hormozi-video-project/audio/final_audio.wav",
        "hormozi-video-project/audio/final_audio.wav" # overwrite final_audio with mixed master
    )
