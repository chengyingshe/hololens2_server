import whisper

class SpeechRecognizer:
    def __init__(self, model_name='small', **kwargs) -> None:
        self.model = whisper.load_model(model_name, **kwargs)

    def recognize_audio(self, file_path) -> str:
        return self.model.transcribe(file_path)['text']