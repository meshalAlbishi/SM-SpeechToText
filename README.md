# SM-SpeechToText

## What is the Task?
the repository will include the following sub tasks:
1. Use python with IBM Watson to convert Speech to Text(SoT) and Text to Speech(ToS).
2. Save the output from SoT as .txt file, and teh output of ToS as .mp3 file.

## Installing Dependencies

#### Python 3.7
Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


#### Virtual Environment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virtual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


#### Clone The IBM Repositorie
``` 
git clone https://github.com/IBM/watson-streaming-stt
```
#### PIP Dependencies
Once you have your virtual environment setup and cloned the repository, install dependencies by running:
``` 
cd watson-streaming-stt
pip install -r requirements.txt
```

#### Window's User
In case of any error during install the pyaudio
try the following
```
pip install pipwin
pipwin install pyaudio
```

## Requirement 
 - You should have an [IBM Cloud](https://www.ibm.com/sa-en/cloud) account.
 - Setup [SpeechToText](https://cloud.ibm.com/catalog/services/speech-to-text) Service
 - Setup [TextToSpeech](https://cloud.ibm.com/catalog/services/text-to-speech) Service


## Demo
- Video Demo from [here](https://github.com/meshalAlbishi/SM-SpeechToText/blob/main/SpeechToText%20Demo.mp4)
- The mp3 output file available [here](https://github.com/meshalAlbishi/SM-SpeechToText/blob/main/watson-streaming-stt/output/output.mp3)
