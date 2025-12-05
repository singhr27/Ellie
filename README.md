# 🧠 Ellen — AI Companion for Youth

Ellen is an AI-powered companion designed to help young students explore their curiosities, build a scientific mindset, and overcome hesitation in asking questions.  

It is especially helpful for **introverted students** who may feel uncomfortable asking questions in public or private. Ellen listens, understands, and responds through natural speech—providing a friendly and supportive learning experience.

---

## ✨ Features

- 🎤 **Real-time speech-to-text** using AssemblyAI WebSocket streaming  
- 🤖 **Concise, scientifically accurate AI responses** powered by OpenAI  
- 🔊 **Natural speech output** through Murf AI streaming TTS  
- ⏱️ **Low latency voice interaction**  
- 🎧 TTS playback runs in the background (non-blocking)  
- 📁 Automatic saving of microphone audio into WAV files  
- 🔄 Duplicate turn prevention to avoid repeated responses  

---

## 📦 Tech Stack

- **Python 3.8+**
- AssemblyAI (Real-time STT)
- OpenAI Responses API (`gpt-5-nano`)
- Murf TTS API
- PyAudio
- websocket-client
- Multithreaded audio streaming

---

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ellen-ai-companion.git
cd ellen-ai-companion

### 2. Install Dependencies

Make sure all required packages are installed:
pip install websocket-client pyaudio openai murf-python

###3. Set Environment Variables

Create a .env file or export them manually.

macOS/Linux:

export ASSEMBLYAI_KEY="your_assemblyai_api_key"
export OPENAI_API_KEY="your_openai_api_key"
export MURF_API_KEY="your_murf_api_key"


Windows PowerShell:

setx ASSEMBLYAI_KEY "your_assemblyai_api_key"
setx OPENAI_API_KEY "your_openai_api_key"
setx MURF_API_KEY "your_murf_api_key"

▶️ Usage

Run Ellen using:

python ellen.py


Then:

Speak into your microphone

Ellen listens in real time

Converts speech to text

Generates a concise, youth-friendly answer

Replies using natural TTS audio

Ellen also saves audio files automatically (WAV format).




##🤝 Contributing

###Contributions are welcome! You can help with:

Improving responsiveness
Adding new TTS/STT engines
Building a GUI
Adding conversation memory
Enhancing safety and clarity for youth
Feel free to open an issue or submit a pull request.
