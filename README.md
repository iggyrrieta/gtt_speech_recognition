# Testing Google API for speech recognition



**Requirements**

In case you are working in a virtual environment:

```bash
pip install SpeechRecognition # importing speech recognition package from google api 
pip install playsound # to play saved mp3 file
pip install gTTS # google text to speech 
pip install requests # to get API responses
```

Now, the folowing can only be installed as an administrator:

```bash
sudo apt install python-gobject # to play saved mp3 file
sudo apt install python3-pyaudio # to play saved mp3 file
sudo apt-get install portaudio19-dev python-pyaudio
```

Now you can install the following:

```bash
pip install PyAudio
```

As we are working with our own virtual environment we must create a link to some libraries of those packages we just installed as sudo into our environment.

```bash
# Link to gi library (from python-object)
ln -s /usr/lib/python3/dist-packages/gi/ /home/iggy/.pyenv/versions/ds/lib/python3.6/site-packages/

```

Install Flask:

```
pip install Flask
```



> Tested and working on Ubuntu 18.0.4



### Usage

```bash
git clone https://github.com/iggyrrieta/gtt_speech_recognition
```

Go to `scripts folder` and run from terminal:

```bash
python app.py
```



Go to https://127.0.0.1/5000
