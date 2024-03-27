import zhipuai
import pyttsx3
import threading
import time

def speak(text):  
    audio = pyttsx3.init()  
    audio.setProperty('voice', 'zh')  
    audio.say(text)  
    audio.runAndWait()

def main():
    zhipuai.api_key = "bf3ad901f35c67db8c3dd36ce5a57bea.ZECtq7yJbtRdAZJY"

    try:
        response = zhipuai.model_api.sse_invoke(
            model="chatglm_6b",
            prompt=[{"role": "user", "content": input('你：')}],
            temperature=0.9,
            top_p=0.7,
            incremental=True
        )
    except Exception as e:
        print(f"发生错误: {e}")
        return

    print('AI:')
    data = ''
    for event in response.events():
        if event.event == "add":
            data += event.data
            print(event.data, end='')
            time.sleep(0.1)  # 避免输出过快导致混乱
    print('')
    sp = threading.Thread(target=speak(data))
    sp.start()

if __name__ == "__main__":
    main()
