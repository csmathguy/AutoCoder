# AutoCoder

**AutoCoder**: An AI-driven application that builds and enhances itself by generating and integrating its own code.

AutoCoder is an open-source project aimed at creating an AI-driven application that can build and enhance itself. By leveraging AI for code generation and automated workflows, AutoCoder accepts feature requests from users, generates the necessary code and tests, and integrates changes autonomously.

## Key Features

- **AI-Powered Code Generation**
  - Utilizes AI models to interpret feature requests and generate corresponding code.
- **Automated Testing**
  - Automatically creates and executes tests to ensure code quality and reliability.
- **GitHub Integration**
  - Interacts with GitHub to manage repositories, branches, commits, and pull requests.
- **Modular Architecture**
  - Employs a Worker-based system to handle tasks, promoting scalability and maintainability.
- **User Interaction**
  - Provides an interface for users to submit feature requests and track progress.

## Goals

- **Simplify Development Processes**
  - Reduce manual coding efforts by automating repetitive tasks.
- **Continuous Self-Improvement**
  - Enable the application to evolve by adding new features based on user inputs.
- **Open Collaboration**
  - Encourage community contributions to enhance capabilities and robustness.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- GitHub account (for API interactions)

## Setup Instructions

1. Copy `config_template.ini` to `config.ini`.
2. Open `config.ini` and fill in your own API keys:
   - `openai_api_key`
   - `github_token`
3. Save the file. Ensure it is located in the project's root directory.


### Installation

1. **Clone the Repository**

  ```bash
  git clone https://github.com/yourusername/AutoCoder.git
  cd AutoCoder
  ```

2. **Create a Virtual Environment**

  ```bash
  python3 -m venv venv
  source venv/bin/activate  # On Windows use: venv\Scripts\activate
  ```

3. **Install Dependencies**

  ```bash
  pip install -r requirements.txt
  ```

##Usage

###Run the Application

  ```bash
  python src/main.py
  ```

