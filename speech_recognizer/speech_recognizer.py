import whisper

class SpeechRecognizer:
    def __init__(self, model_name='small') -> None:
        self.model = whisper.load_model(model_name)

    def recognize_audio(self, file_path) -> str:
        return self.model.transcribe(file_path)['text']