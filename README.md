# SPEECH-RECOGNITION-SYSTEM

*COMPANY* : CODTECH IT SOLUTION

*NAME* : ELAINE JOSE

*INTERN ID* : CT04DN1322

*DOMAIN* : ARTIFICAL INTELLIGENCE

*DURATION* : 4 WEEKS

*MENTOR* : NEELA SANTOSH

This project represents a voice-to-text application in Python that accepts voice input from the user, processes the speech into text using Google's Speech Recognition API, and writes the recognized text into a file called output.txt. It uses native Python libraries such as speech_recognition, and gives support to pyttsx3 for speech feedback should one wish. 

The program hears the user's voice continuously through a microphone, performs natural language processing (NLP) operations on the speech, and writes each recognized sentence into a text file. This system intends to assist people who want to have spoken words transcribed for documentation, note-taking, access, and different types of productivity.

How It Works:
Several steps make up the workflow of the program: 

Access Microphone and Noise Adjustment:

It accesses the default audio input using the Microphone class from the speech_recognition module.

The recognizer then adjusts itself for ambient noise to work better.

Speech Recording:

Active listening occurs when calling recognizer.listen().

It captures audio snippets whenever the user speaks.

Speech-to-Text Conversion:

The captured audio is sent to Google's Web Speech API with the recognize_google() method.

This API converts the spoken words into readable English text.

Error Handling:

The program politely asks users to try again in the event of an unexpected error such as network outage (RequestError) or unclear speech (UnknownValueError).

Text Logging:

The recognized text is appended to output.txt, thus recording all spoken inputs along with their timestamps.

Exit Command:

The process will continue until the user says, "stop recording," which terminates the program safely.

*OUTPUT*

![Image](https://github.com/user-attachments/assets/576cc83b-c220-4da6-89aa-8a524687b81a)
