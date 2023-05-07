# Kratin Let's Innovate Assignment
Kratin LLC Assignment Submission 

## Problem Statement: How can you help Sunita Sharma (65+ years old) to live a healthier and better life? 
Identify one use case for elderly care (for the age group 65+) and create a working prototype to demonstrate your idea using technology known to you.

## My Solution
A Virtual Companion for Sunita Sharma. A voicebot which can answer any question and can have conversations with her to keep her away from feeling lonely.

## Justification for the solution
People of age group 65+ not only suffer from physical distress but also mental distress, In today's fast moving world everyone is busy with their own life and the elderly are left with only limited interactions and small talks which can cause them to have mental distress. This is where the virtual companion comes to play, the elderly can talk to the bot without having to worry about running out of time and can feel the presence of someone listening to them. The bot is not only limited to this task but also can give medical advice for small medical problems which are time consuming if went to the doctor.

*Note: Serious medical problems require doctor supervision, this model does not claim to work on that.

## Methodology
1. The Virtual companion is a voicebot which can have conversations with sunita through the power of Chat-GPT. 
2. The model uses Web Speech API to convert the audio spoken to a text, that text is forwarded to the Chat-GPT API.
3. The Virtual Companion used here uses gpt-3.5-turbo-0301 model API to generate reponses and Google Translate’s Text-to-Speech API (gTTS) to generate speech from the genrated response.
4. the frontend is made with the help of streamlit.

