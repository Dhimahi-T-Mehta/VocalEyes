from vision_agent import VisionAgent
from speech_agent import SpeechAgent

vision = VisionAgent(GOOGLE_API_KEY)

speech = SpeechAgent(MURF_API_KEY)

text = vision.analyze_file(filename, file_bytes)

audio = speech.generate_speech(text)

print(audio)