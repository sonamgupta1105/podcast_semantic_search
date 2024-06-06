# -*- coding: utf-8 -*-

# Ref: https://wandb.ai/wandb_fc/gentle-intros/reports/OpenAI-Whisper-How-to-Transcribe-Your-Audio-to-Text-for-Free-with-SRTs-VTTs---VmlldzozNDczNTI0#how-to-run-whisper
#!pip install openai-whisper

import whisper
import glob
import os

whisper_model = whisper.load_model("base")
files = [file for file in glob.glob("/content/audio_podcasts/*")]
def read_transcribe_dataset(files):

    for file_name in files:
      result = whisper_model.transcribe(file_name)
      # Extract the base name of the file without extension
      base_name = os.path.basename(file_name)
      name_without_ext = os.path.splitext(base_name)[0]

      # Create a text file for each transcription
      with open(f"{name_without_ext}.txt", "w", encoding="utf-8") as txt:
          txt.write(result["text"])

# Call the function with the list of files
read_transcribe_dataset(files)





