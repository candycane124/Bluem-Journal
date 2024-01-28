# Serenity Journal - SerenityHacks 2024

## About the Project
Serenity Journal is an innovative journaling application developed for the SerenityHacks 2024 hackathon, focusing on mental health and wellness. The application combines the therapeutic practice of journaling with game-like elements to enhance user motivation and satisfaction.

## Key Features

### Journaling with a Twist
- **Interactive Journaling Experience**: Users gain points for each journal entry, promoting consistent writing habits.
- **Garden of Reflection**: Points can be spent on flowers to beautify a virtual garden, symbolizing growth and self-care.

### Backend & Database
- **Python Backend**: Robust and scalable backend, ensuring smooth user interactions.
- **SQLite Database**: Securely stores and manages user data, including:
  - Tracking points gained and spent.
  - Storing, retrieving, and deleting journal entries.
  - Keeping a record of purchased flowers.

### Frontend Design
- **Kivy-Based GUI**: An engaging and user-friendly graphical interface designed using Kivy, offering a seamless user experience.

### Journaling Assistance
- **Integration with ChatGPT API**: The app uses ChatGPT to generate insightful questions, encouraging users to delve deeper into their thoughts and emotions.

![image](https://github.com/JasonQuantrill/Journal/assets/91751222/a178dcd1-44dc-43ca-a9c1-2b584da2e661)


### Negative Thoughts Pebble
- **Release Negative Thoughts**: Users can write down negative thoughts and watch as the app performs an animation to symbolically throw these thoughts into a pond, aiding in emotional release.

## Technologies Used
- **Frontend**: Kivy (Python)
- **Backend**: Python
- **Database**: SQLite
- **API**: ChatGPT API for reflective journaling prompts

## Getting Started
To get a local copy up and running, follow these simple steps.

### Prerequisites
- Python 3.x
- Kivy

### Installation
1. Clone the repo
   ```sh
   git clone https://github.com/your_username_/SerenityJournal.git
   ```
2. Install required packages
   ```sh
   pip install kivy openai sqlite3
   ```

### Usage
Launch the application and begin your journaling journey. Write entries, earn points, and grow your garden as you reflect and unwind.
