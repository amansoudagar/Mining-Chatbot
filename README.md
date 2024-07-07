---

# MineMentor

MineMentor is a Streamlit-based web application that integrates AI capabilities to provide insights and information for the mining industry. It leverages Gemini Pro, a generative AI model, to respond to user queries and stores interactions in a MySQL database for future reference.

## Features

- **AI Chat**: Interact with Gemini Pro to get responses to mining-related questions.
- **Database Integration**: Store user queries and AI responses in a MySQL database.
- **Session History**: Track chat history within the application.

## Technologies Used

- **Streamlit**: Python library for building interactive web applications.
- **Generative AI**: Utilizes Google's Gemini Pro for AI-powered responses.
- **MySQL**: Database management system for storing user interactions.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/beast0686/minementor.git
   cd minementor
   ```

2. Install dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Configure environment variables:

   Create a `.env` file and add the following variables:
   ```
   port=3306
   host=localhost
   database=your_database_name
   username=your_username
   password=your_password
   GOOGLE_API_KEY=your_google_api_key
   ```

4. Run the application:

   ```
   streamlit run app.py
   ```

   Open your web browser and go to the provided local URL to interact with MineMentor.

## Usage

- **Ask Questions**: Enter questions related to mining in the input field and click "Ask the question".
- **View Responses**: Responses from Gemini Pro will be displayed, and the chat history will be updated.
- **Chat History**: See previous interactions in the chat history section.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---
