import pyaudio
import os
from murf import Murf, MurfRegion

client = Murf(
    api_key= os.getenv("MURF_API_KEY"), # Not required if you have set the MURF_API_KEY environment variable
    region=MurfRegion.GLOBAL  # US region
)

# For lower latency, specify a region closer to your users
# client = Murf(region=MurfRegion.IN)  # Example: India region

# Audio format settings (must match your API output)
SAMPLE_RATE = 24000  
CHANNELS = 1
FORMAT = pyaudio.paInt16

def capture_microphone_audio():
    """
    Microphone capture
    Does NOT send audio anywhere yet.
    Verifies we can record 16-bit PCM audio.
    """
    CHUNK = 1024
    RATE = 16000  # ASR will expect 16 kHz later

    pa = pyaudio.PyAudio()
    stream = pa.open(format=pyaudio.paInt16,
                     channels=1,
                     rate=RATE,
                     input=True,
                     frames_per_buffer=CHUNK)

    print("🎤 Microphone capture started... (Speak!)")
    print("Press CTRL+C to stop.\n")

    try:
        while True:
            audio_bytes = stream.read(CHUNK, exception_on_overflow=False)
            print(f"[mic] captured {len(audio_bytes)} bytes")
    except KeyboardInterrupt:
        print("\nMicrophone capture stopped.")
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()

def play_streaming_audio():
    # Get the streaming audio generator
    audio_stream = client.text_to_speech.stream(
        text="Hi, How are you doing today?",
        voice_id="Nikhil",
        model="FALCON",
        multi_native_locale="en-IN",
        sample_rate=SAMPLE_RATE,
        format="PCM"
    )

    # Setup audio stream for playback
    pa = pyaudio.PyAudio()
    stream = pa.open(format=FORMAT, channels=CHANNELS, rate=SAMPLE_RATE, output=True)

    try:
        print("Starting audio playback...")
        for chunk in audio_stream:
            if chunk:  # Check if chunk has data
                stream.write(chunk)
    except Exception as e:
        print(f"Error during streaming: {e}")
    finally:
        stream.stop_stream()
        stream.close()
        pa.terminate()
        print("Audio streaming and playback complete!")

if __name__ == "__main__":
    capture_microphone_audio()
    play_streaming_audio()
