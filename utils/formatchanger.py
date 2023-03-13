from pydub import AudioSegment
import os

# audio format converter start
def convert_audio(input_file, output_dir):
    output_file = os.path.join(output_dir, os.path.splitext(input_file)[0] + '.wav').replace("\\", "/")
    # Convert the file to WAV
    sound = AudioSegment.from_file(input_file)
    sound.export(output_file, format='wav')

    return output_file
# audio convertor end

# Example usage
# input_file = 'voiceM.ogg'
# output_dir = '/home/abduazim/Documents/CodEmpire/BotWorkshop/assistantbot/utils'
# output_file = convert_audio(input_file, output_dir)
# print(f"File converted: {output_file}")
