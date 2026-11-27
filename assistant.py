import os
from memory_meeting_ai.store import add_conversation
from shared.events import publish_event

def speak(text):
    try:
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except Exception as exc:
        print(f"[TTS unavailable; text response shown] {exc}")

def listen_once():
    try:
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=8)
        return recognizer.recognize_google(audio)
    except Exception as exc:
        print(f"[Voice input unavailable] {exc}")
        return ""

def reply(user_text):
    # Rule-based baseline. Replace with a configured local LLM/API for generative AI.
    low = user_text.lower()
    if any(word in low for word in ("hello", "hi", "hey")):
        answer = "Hello! I am NEXUS. How can I help you?"
    elif "time" in low:
        from datetime import datetime
        answer = "The current system time is " + datetime.now().strftime("%I:%M %p")
    elif "your name" in low:
        answer = "My name is NEXUS, your AI assistant pet robot."
    else:
        answer = "I heard you say: " + user_text + ". My conversational AI model can be integrated here."
    add_conversation(user_text, answer)
    publish_event("voice_interaction", {"user": user_text, "assistant": answer})
    return answer

def main():
    voice_mode = os.getenv("VOICE_MODE", "false").lower() == "true"
    print("NEXUS Assistant. Type 'exit' to quit.")
    while True:
        text = listen_once() if voice_mode else input("You: ")
        if not text:
            continue
        if text.lower().strip() in ("exit", "quit", "stop"):
            speak("Goodbye!")
            break
        answer = reply(text)
        print("NEXUS:", answer)
        speak(answer)

if __name__ == "__main__":
    main()
