import os
import azure.cognitiveservices.speech as speechsdk

os.environ["SPEECH_KEY"] = "bac3599b169c45f89dd91bce94c899d8"
os.environ["SPEECH_REGION"] = "eastus"

# text to speech start
def tts(fortts):
    os.environ["SPEECH_KEY"] = "KEY"
    os.environ["SPEECH_REGION"] = "REGION"

    speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
    #
    # The language of the voice that speaks.
    speech_config.speech_synthesis_voice_name='uz-UZ-MadinaNeural'

    audio_output_config = speechsdk.audio.AudioOutputConfig(filename="/home/abduazim/Documents/CodEmpire/BotWorkshop/assistantbot/utils/natija.ogg")

    speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_output_config)

    text = fortts

    speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

    if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
        return "Speech synthesized for text [{}]. Audio saved to voiceM.wav".format(text)
    elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))
# text to speech end