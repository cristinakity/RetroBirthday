# RetroBirthDay Project

## Overview

RetroBirthDay is a web application that allows users to input their birth date and receive information about retro games that were released on that date. The application is built using a Flask backend with a MongoDB database and a Vue.js frontend.

## Project Structure

The project is organized into the following main directories:

- **.devcontainer**: Contains configuration files for the development container, including the Dockerfile and devcontainer.json.
- **backend**: Contains the Flask backend application, including the main application file, controllers, models, views, and requirements.
- **frontend**: Contains the Vue.js frontend application, including the main HTML file, Vue components, and package configuration.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **README.md**: This file provides an overview and setup instructions for the project.

## Setup Instructions

### Development Environment

To set up the development environment, ensure you have Docker installed. Open the project in a compatible code editor and use the development container feature to build the environment.

### Backend Setup

1. Navigate to the `backend` directory.
2. Install the required Python packages listed in `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```
3. Start the Fastapp:
   ```
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

### Frontend Setup

1. Navigate to the `frontend` directory.
2. Install the required Node.js packages:
   ```
   npm install
   ```
3. Start the Vue.js application:
   ```
   npm run serve
   ```

## Usage

1. Open the frontend application in your web browser.
2. Enter your birth date in the provided input field.
3. Submit the form to receive information about the retro game released on your birth date.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
