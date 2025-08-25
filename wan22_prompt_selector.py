import json

class Wan22PromptSelector:
    CATEGORY = "Wan2.2/Prompt Generation"
    FUNCTION = "generate_prompt"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Prompt",)

    # Dynamic control module options (empty and non-empty options based on documentation)
    SportSceneOptions = [
        "--",  # Empty option
        "Running", "Skateboarding", "Playing Soccer", "Tennis", "Table Tennis", 
        "Skiing", "Basketball", "Rugby", "Bowl Dance", "Cartwheel"
    ]
    
    CharacterEmotionOptions = [
        "--",  # Empty option
        "Angry", "Fearful", "Happy", "Sad", "Surprised", 
        "Worried", "Confused", "Relieved", "Ecstatic", "Desperate", 
        "Calm", "Anticipatory", "Shy", "Disgusted", "Proud"
    ]
    
    CameraMovementOptions = [
        "--",  # Empty option
        "Camera Push In", "Camera Pull Out", "Camera Pan Left/Right", "Camera Tilt Up", 
        "Handheld Camera", "Follow Camera", "Circular Tracking Shot"
    ]

    # Cinematic aesthetic control module options (based on the Cinematic Aesthetic Control section of the document)
    LightSourceTypeOptions = [
        "--",  # Empty option
        "Daylight", "Artificial Light", "Moonlight", "Practical Light", "Firelight", 
        "Fluorescent Light", "Overcast Light", "Mixed Light", "Sunny Light"
    ]
    
    LightingTypeOptions = [
        "--",  # Empty option
        "Soft Light", "Hard Light", "Top Light", "Backlight", "Underlight", "Rim Light", "Side Light",
        "Low Contrast Light", "High Contrast Light", "Silhouette Light", "Dawn Light", "Dusk Light", "Sunset Light"
    ]
    
    ShotTypeOptions = [
        "--",  # Empty option
        "Clean Single Shot", "Two Shot", "Three Shot", "Group Shot", "Establishing Shot"
    ]
    
    FocalLengthOptions = [
        "--",  # Empty option
        "Medium Focal Length", "Wide Angle", "Telephoto", "Zoom", "Ultra Wide Angle - Fisheye"
    ]
    
    ToneOptions = [
        "--",  # Empty option
        "Warm Tone", "Cool Tone", "High Saturation", "Low Saturation"
    ]

    # Stylization module options (based on the Stylization section of the document)
    VisualStyleOptions = [
        "--",  # Empty option
        "Cyberpunk", "Line Art Illustration", "Wasteland Style", "Felt Style", 
        "3D Cartoon", "Pixel Art Style", "Puppet Animation", "Watercolor Painting"
    ]
    
    SpecialEffectShotOptions = [
        "--",  # Empty option
        "Tilt-Shift Photography", "Time-Lapse Photography"
    ]

    # Scene type options (based on scene definition in the document)
    SceneTypeOptions = [
        "--",  # Empty option
        "Natural Scene (Field/Forest/Mountain)", "Urban Scene (Street/Indoor/Building)", 
        "Fictional Scene (Otherworld/Space/Dream)"
    ]

    # Node input parameter definition
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "SceneType": (s.SceneTypeOptions, {"default": "--"}),
                "SportScene": (s.SportSceneOptions, {"default": "--"}),
                "CharacterEmotion": (s.CharacterEmotionOptions, {"default": "--"}),
                "CameraMovement": (s.CameraMovementOptions, {"default": "--"}),
                "LightSourceType": (s.LightSourceTypeOptions, {"default": "--"}),
                "LightingType": (s.LightingTypeOptions, {"default": "--"}),
                "ShotType": (s.ShotTypeOptions, {"default": "--"}),
                "FocalLength": (s.FocalLengthOptions, {"default": "--"}),
                "Tone": (s.ToneOptions, {"default": "--"}),
                "VisualStyle": (s.VisualStyleOptions, {"default": "--"}),
                "SpecialEffectShot": (s.SpecialEffectShotOptions, {"default": "--"}),
            }
        }

    # Prompt generation logic (following the document's prompt formula)
    def generate_prompt(self, SceneType, SportScene, CharacterEmotion, CameraMovement,
                       LightSourceType, LightingType, ShotType, FocalLength, Tone, VisualStyle, SpecialEffectShot):
        # Filter non-empty options
        elements = [
            SceneType if SceneType != "--" else "",
            f"Subject {SportScene}" if SportScene != "--" else "",
            f"Showing {CharacterEmotion}" if CharacterEmotion != "--" else "",
            CameraMovement if CameraMovement != "--" else "",
            LightSourceType if LightSourceType != "--" else "",
            LightingType if LightingType != "--" else "",
            ShotType if ShotType != "--" else "",
            FocalLength if FocalLength != "--" else "",
            Tone if Tone != "--" else "",
            f"{VisualStyle} style" if VisualStyle != "--" else "",
            SpecialEffectShot if SpecialEffectShot != "--" else ""
        ]
        # Remove empty strings and concatenate
        prompt_parts = [e for e in elements if e]
        prompt = ", ".join(prompt_parts) if prompt_parts else ""
        return (prompt,)

# Node registration (add "Haochun Production" to the end of the plugin name)
NODE_CLASS_MAPPINGS = {
    "Wan22PromptSelector": Wan22PromptSelector
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Wan22PromptSelector": "Wan2.2 Prompt Selector Haochun Production"
}

# Plugin metadata (name includes "Haochun Production")
manifest = {
    "name": "Wan2.2 Prompt Selector Haochun Production",
    "version": "1.7",
    "description": "Developed based on Wan2.2 Video Generation Prompt Guide",
    "author": "Haochun"
}

with open("manifest.json", "w", encoding="utf-8") as f:
    json.dump(manifest, f, ensure_ascii=False, indent=2)
