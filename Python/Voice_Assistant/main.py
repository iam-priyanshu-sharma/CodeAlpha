import datetime
import webbrowser

import pyttsx3
import speech_recognition as sr


def initialize_engine():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 50)
    return engine


def speak(engine, text):
    engine.say(text)
    engine.runAndWait()


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print(f"User said: {command}\n")
    except Exception as e:
        print("Sorry, I didn't catch that. Could you please repeat?")
        return "None"

    return command.lower()


def set_reminder(engine, command):
    speak(engine, "What should I remind you about?")
    reminder = listen()
    speak(engine, "When do you want to be reminded? Please say the time in hours and minutes.")
    reminder_time = listen()
    try:
        hour, minute = map(int, reminder_time.split())
        now = datetime.datetime.now()
        reminder_datetime = now.replace(hour=hour, minute=minute)
        if now > reminder_datetime:
            reminder_datetime += datetime.timedelta(days=1)
        speak(engine, f"Alright, I will remind you about '{reminder}' at {hour:02d}:{minute:02d}.")
        while True:
            if datetime.datetime.now() >= reminder_datetime:
                speak(engine, f"Reminder: {reminder}")
                break
    except ValueError:
        speak(engine, "Sorry, I couldn't understand the time you provided. Please try again.")


def create_todo_list(engine, command):
    todo_list = []
    speak(engine, "Let's create a to-do list. Please say the tasks one by one. Say 'done' when you're finished.")
    while True:
        task = listen()
        if task == "done":
            break
        todo_list.append(task)
        speak(engine, f"Added: {task}")
    speak(engine, "Here's your to-do list:")
    for task in todo_list:
        speak(engine, task)


def search_web(engine, command):
    search_terms = command.replace("search", "").strip()
    if search_terms:
        url = f"https://www.google.com/search?q={search_terms}"
        speak(engine, f"Searching for '{search_terms}'")
        webbrowser.open(url)
    else:
        speak(engine, "Please provide a search term.")


def show_help(engine):
    help_text = """
    I can help you with the following tasks:
    1. Set reminders: Say 'set reminder' followed by the reminder and time.
    2. Create to-do lists: Say 'create to-do list' and then list your tasks one by one.
    3. Search the web: Say 'search' followed by the search terms.
    4. Show available commands: Say 'help'.
    5. To exit, say 'exit' or 'quit'.
    """
    print(help_text)
    speak(engine, help_text)


def main():
    engine = initialize_engine()
    speak(engine, "Hello, I am your voice assistant. How can I help you today?")

    while True:
        command = listen()

        if "reminder" in command:
            set_reminder(engine, command)
        elif "to-do" in command or "todo" in command:
            create_todo_list(engine, command)
        elif "search" in command:
            search_web(engine, command)
        elif "help" in command:
            show_help(engine)
        elif "exit" in command or "quit" in command:
            speak(engine, "Goodbye!")
            break


if __name__ == "__main__":
    main()
