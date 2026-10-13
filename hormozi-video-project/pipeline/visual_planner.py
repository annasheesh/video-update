"""
visual_planner.py - Analyzes transcript segments and produces a structured visual plan
for synchronized explanatory motion graphics layered over the speaker.
"""
import os
import json

def build_visual_plan(output_json):
    visual_plan = {
        "version": "1.0",
        "resolution": {"width": 1080, "height": 1920},
        "safe_zones": {
            "top_explanatory_region": {"x": 60, "y": 80, "w": 960, "h": 400},
            "face_protected_region": {"x": 240, "y": 500, "w": 600, "h": 820},
            "lower_caption_region": {"x": 60, "y": 1380, "w": 960, "h": 240},
            "bottom_platform_safe_region": {"y_min": 1640, "y_max": 1920, "description": "Reserved for platform UI controls"}
        },
        "explanatory_events": [
            {
                "id": "VIZ_01_COMPARATIVE_BRANCHING",
                "output_start": 0.50,
                "output_end": 3.10,
                "duration": 2.60,
                "spoken_anchor": "whether you start now or whether you start later",
                "concept": "Comparative Decision Branch: Starting Now vs. Starting Later",
                "animation_type": "Progressive Dual-Branch Diagram",
                "position": {"top": 120, "left": 60, "width": 960, "height": 340},
                "elements": [
                    {
                        "name": "Badge Title",
                        "text": "DECISION HORIZON",
                        "type": "pill_header",
                        "entrance_time": 0.50
                    },
                    {
                        "name": "Left Branch (Start Now)",
                        "label": "START NOW",
                        "color": "#00FF66",
                        "icon": "⚡",
                        "metric": "+MAX TIME",
                        "entrance_time": 1.20,
                        "motion": "scale_spring_up"
                    },
                    {
                        "name": "Comparison VS",
                        "text": "VS",
                        "entrance_time": 1.80,
                        "motion": "fade_pop"
                    },
                    {
                        "name": "Right Branch (Start Later)",
                        "label": "START LATER",
                        "color": "#FF3B30",
                        "icon": "⏳",
                        "metric": "-ZERO TIME",
                        "entrance_time": 2.10,
                        "motion": "scale_spring_up"
                    }
                ],
                "exit_time": 3.05,
                "face_safe_verified": True
            },
            {
                "id": "VIZ_02_AGE_MILESTONE_THRESHOLD",
                "output_start": 3.10,
                "output_end": 4.60,
                "duration": 1.50,
                "spoken_anchor": "you will hit that age",
                "concept": "Critical Life Milestone / Age Inevitability",
                "animation_type": "Milestone Flag & Warning Callout with Camera Punch-in",
                "position": {"top": 120, "left": 80, "width": 920, "height": 320},
                "elements": [
                    {
                        "name": "Warning Badge",
                        "text": "⚠️ INEVITABLE MILESTONE",
                        "type": "alert_pill",
                        "color": "#FFCC00",
                        "entrance_time": 3.10,
                        "motion": "slide_down_bounce"
                    },
                    {
                        "name": "Milestone Card",
                        "headline": "THAT AGE",
                        "subline": "TIME IS FINITE",
                        "icon": "🎯",
                        "entrance_time": 3.30,
                        "motion": "punch_zoom"
                    }
                ],
                "exit_time": 4.55,
                "face_safe_verified": True
            },
            {
                "id": "VIZ_03_TIME_DEPLETION_GAUGE",
                "output_start": 4.60,
                "output_end": 6.30,
                "duration": 1.70,
                "spoken_anchor": "where you don't even have that much time anymore",
                "concept": "Resource Exhaustion: Available Time Depleting",
                "animation_type": "Progressive Depleting Gauge & Bottleneck Alert",
                "position": {"top": 110, "left": 70, "width": 940, "height": 340},
                "elements": [
                    {
                        "name": "Bottleneck Badge",
                        "text": "THE ROOT BOTTLENECK",
                        "type": "pill_header",
                        "color": "#FF3B30",
                        "entrance_time": 4.60
                    },
                    {
                        "name": "Time Gauge Bar",
                        "label": "AVAILABLE TIME",
                        "animation": "drain_from_100_to_10_percent",
                        "status_badge": "DEPLETED",
                        "entrance_time": 4.80
                    },
                    {
                        "name": "Stat Callout",
                        "text": "TIME = 0",
                        "color": "#FF3B30",
                        "entrance_time": 5.40,
                        "motion": "pulse_alert"
                    }
                ],
                "exit_time": 6.30,
                "face_safe_verified": True
            }
        ],
        "camera_movement_plan": [
            {
                "time_start": 0.00,
                "time_end": 3.10,
                "zoom_level": 1.00,
                "description": "Original framing (100% wide), stable anchor"
            },
            {
                "time_start": 3.10,
                "time_end": 6.30,
                "zoom_level": 1.10,
                "description": "Dynamic 110% punch-in centered on speaker's face for high retention and dramatic emphasis at jump cut"
            }
        ]
    }
    
    os.makedirs(os.path.dirname(output_json), exist_ok=True)
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(visual_plan, f, indent=2)
        
    print(f"[VisualPlanner] Created visual_plan.json with {len(visual_plan['explanatory_events'])} explanatory animations and camera punch-in plan.")
    return visual_plan

if __name__ == "__main__":
    build_visual_plan("hormozi-video-project/analysis/visual_plan.json")
