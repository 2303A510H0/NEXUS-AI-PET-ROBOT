# Implementation Notes

The repository provides runnable baselines and integration points, not a completed end-to-end autonomous robot.

- Voice assistant: rule-based response baseline, optional microphone recognition and TTS.
- Vision: OpenCV HOG person detection, Haar face detection, and a simple centroid tracker.
- Object detection: adapter interface only; trained model not included.
- Expression estimation: interface only; no emotion model included.
- Dashboard: local Flask page with notes and event endpoint.
- Memory: SQLite conversation/note/meeting tables; basic extractive meeting summary.
- TFT: serial-controlled sample eye expressions; display pin setup is hardware-specific.
- MQTT: optional publisher; requires a broker.

Test each module separately before integrating hardware.
