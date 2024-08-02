import whisper



def language_detector(audio):

    model = whisper.load_model("tiny") # tiny, base, small, medium, large

    # load audio and pad/trim it to fit 30 seconds
    
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    language = max(probs, key=probs.get)
    print(f"Detected language: {language}")
    return language
