**DreamCatcher**

**Owners**

Alexis Hernandez (hernaa5)

Valeria Villanueva-Ruiz (villav2)

**Project Overview**

DreamCatcher is an AI Chatbot that will take user inputted dreams to visually reconstruct and interpret them. DreamCatcher will take an input of text provided by the user describing as much of the dream as possible, and use this text data, along with follow up questions if applicable, to perform its analysis. 

This chatbot ideally will be a part of a larger AI virtual morning assistant that makes suggestions for the day to the user based on their profile and mood drawn from the dreams contents if inputted that day.

**Related AI Projects**

Dream Interpreter AI ([dreaminterpreter.ai](dreaminterpreter.ai)) is a website where you can input a dream into a text box and receive an interpretation, it also has a feed showing art that has been derived from people’s dreams, which is similar to what we are trying to achieve, as well as a globe showing people’s dreams and their interpretations around the world

Davinci Dream Meaning Machine ([dreammeaningmachine.com](dreammeaningmachine.com)) is another website which is more similar to the chatbot style we are trying to achieve. You can input a dream into a text box and receive an interpretation, but the input format is split into ‘Simple’ or ‘Guided’, simple being inputting text like we have mentioned, and guided having follow up questions to get more context and meaning 

**Requirements**

**FUNCTIONAL**

Dream Input and Reconstruction: DreamCatcher should be able to reconstruct and recreate the dream from the user's input

User Profiles: Profiles will include information like age, gender, location, zodiac sign, etc. so the system can adapt and personalize the dream analysis

AI Image Generation: Should integrate DALL-E (AI image generator) to create images related to the dream as well as to help reconstruct it

Dream Analysis and Interpretation: Should analyze the dream using datasets and APIs containing dream symbolism data to provide a unique and in-depth interpretation tailored to the user

Morning Assistant: This feature should provide the user with recommendations for the day based on the user's geolocation, schedule, and mood/state of mind as influenced by the dream

Privacy and Security: Ensure that user data, especially personal information and dream content, is kept secure and private

**NON-FUNCTIONAL**

Performance: Responsive and timely dream reconstructions and interpretations to keep the user engaged and prevent slowdown

Usability: The UI should be intuitive, making it easy for users to navigate, input dreams and receive dream interpretations

API Integration: Ensure that the system can effectively integrate with external APIs and datasets for dream symbolism data

Feedback and Improvement: Regularly collect and analyze user feedback to make continuous improvements to the application's features and capabilities

AI Model Training and Updates: Regularly update and fine-tune the AI models used for dream interpretation to improve accuracy and relevance

Compatibility: Ensure that the application is compatible with various screen sizes and operating systems to reach a broader user base

**System Architecture**
(High level)

(image)


**Technologies to be Used**

Python, NLTK, DALL-E (will be updated)

**User Profiles**

The Curious Dreamer: Interested in understanding the meaning and symbolism of their dreams. They seek deeper insights into their subconscious and enjoy exploring dream interpretations.

Spiritual Seekers: Users with a spiritual inclination who believe that dreams hold spiritual significance and want to use dream interpretations for personal growth and guidance.

Therapy & Self-Reflection: Individuals who are in therapy and use dream analysis as a part of their self-reflection and healing process. They may find DreamCatcher's insights helpful.

Daily Planners: Users who appreciate the integration of dream analysis into their morning routine, as it helps them plan their day and make decisions.

Psychology and Mental Health Enthusiasts: Individuals studying or interested in psychology, dream psychology, or mental health who want to explore the science behind dream interpretation.

Parents and Caregivers: Users who want to understand and interpret the dreams of who they’re caring for to help address any concerns or fears.

**Stakeholders**

Development Team: Developers, data scientists, and designers responsible for building and maintaining the DreamCatcher application.

Mental Health Professionals: Individuals interested in the potential therapeutic applications of dream analysis and who may collaborate with the app.

Data Providers: Organizations or researchers who develop and provide AI models for dream reconstruction, analysis, and image generation (e.g., DALL-E) as well as the constructors of dream meaning databases.

**User Interface**

Web Application: Users will be able to go on the web and find our application as a website on their preferred browser. Will allow users to access their profile from any location. 

Log-In vs Guest: Users will be able to log in as a user or as a guest. Logged in users will have more personalized answers. 

Chatbot: Users can input their dream as a text and the AI will ask follow up questions related to their dream and will keep the conversation going. Conversations will be saved for the user’s records.

Feedback: Users will be able to provide feedback according to the answers they get. They will be asked if they would like to share the conversations they have with the chatbot.

Color Palette: Color palette (TBD) will be minimal and accessible for people with visual disabilities and to reduce overhead.

**Team Roles and Responsibilities**

Alexis Hernandez



* Dream Interpretation AI Model
* Follow up question generation
* Chatbot UI
* User profiles

Valeria Villanueva-Ruiz



* Dream Interpretation AI Model
* DALL-E image generation
* Morning assistant UI
* Results page

**Technical Limitations**



1. Centralized dream meaning dataset/training data
2. Contextualizing interpretations to give depth
3. Personalizing experience based on user profile
