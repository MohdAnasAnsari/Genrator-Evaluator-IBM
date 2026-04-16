# Generator-Evaluator AI Study Assistant

## 📚 Project Overview

The **Generator-Evaluator AI Study Assistant** is an intelligent multi-agent system designed to help students understand complex topics through interactive conversation and personalized study strategies. This project leverages large language models (LLMs) and agentic AI frameworks to create a collaborative learning experience where multiple AI agents work together to explain concepts, analyze understanding, and suggest effective memorization techniques.

## 🎯 Purpose

This project implements a **multi-agent conversational system** that:
- **Generates** detailed explanations of study topics through interactive dialogue
- **Evaluates** student understanding and learning needs
- **Provides** customized study tips and learning strategies
- Creates an engaging, interactive learning environment powered by AI agents

## 🏗️ Architecture

The system uses a **Group Chat** architecture with three specialized AI agents:

1. **Student Agent** - Represents the learner, asks questions and seeks help on study topics
2. **Concept Analysis Agent** - Analyzes and explains core concepts and ideas related to the topic
3. **Study Tips Agent** - Suggests memorization strategies, comprehension techniques, and learning methods

These agents communicate through a **Group Chat Manager** that orchestrates their interactions and ensures coherent dialogue.

## 🛠️ Technologies Used

- **Framework**: CrewAI - For building multi-agent AI systems
- **LLM Integration**: Support for various language models (configured via environment variables)
- **Search Tool**: SerperDev API - For web search capabilities during learning sessions
- **Language**: Python 3.x
- **Environment Management**: Custom `.env` file support for API keys and configuration

## 📋 Features

- ✅ Interactive multi-agent conversation system
- ✅ Modular agent architecture for easy customization
- ✅ Web search integration for real-time information
- ✅ Environment variable management for secure API key handling
- ✅ Round-robin speaker selection for balanced agent participation
- ✅ Extensible design for adding new agents or capabilities

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Genrator-Evaluator-IBM
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install crewai crewai-tools
```

4. Set up environment variables:
   - Create a `.env` file in the project root
   - Add your API keys:
   ```
   SERPER_API_KEY=your_serper_api_key
   OPENAI_API_KEY=your_openai_api_key
   # Add other API keys as needed
   ```

### Usage

Run the study assistant:
```bash
python study_assistant.py
```

The system will:
1. Prompt you to enter a study topic
2. Launch the multi-agent conversation
3. Display explanations and study tips from the specialized agents
4. Provide a complete learning summary

## 📂 Project Structure

```
Genrator-Evaluator-IBM/
├── README.md                 # Project documentation
├── LICENSE                   # Project license
├── .gitignore               # Git ignore rules
├── .env                     # Environment configuration (API keys)
├── core_env.py             # Core environment setup and tool configuration
├── study_assistant.py      # Main study assistant with multi-agent system
└── .venv/                  # Virtual environment (not tracked in git)
```

## 🔧 Configuration

### Environment Variables

The project uses a custom environment loader (`core_env.py`) that reads from `.env` file:

- **SERPER_API_KEY**: SerperDev API key for web search functionality
- **OPENAI_API_KEY**: OpenAI API key for LLM access
- Other LLM-specific keys as needed

### Agent Customization

You can modify agent behavior by editing `study_assistant.py`:
- Change system messages to alter agent personalities
- Adjust max conversation rounds
- Modify speaker selection methods
- Add or remove agents as needed

## 📝 Example Workflow

1. **User Input**: "Quantum Mechanics"
2. **Student Agent**: Asks for help understanding quantum mechanics
3. **Concept Analysis Agent**: Provides explanation of key concepts (superposition, entanglement, etc.)
4. **Study Tips Agent**: Suggests memory aids and learning strategies
5. **Output**: Comprehensive learning materials and study techniques

## 🔐 Security

- Never commit `.env` files containing API keys
- Use `.gitignore` to exclude sensitive files
- Store secrets securely in environment variables
- Keep API keys confidential and rotate regularly

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the terms specified in the LICENSE file.

## 🙋 Support

For questions, issues, or suggestions, please open an issue in the repository.

## 🚀 Future Enhancements

- [ ] Support for multiple language models
- [ ] Persistent conversation history
- [ ] Quiz generation and evaluation
- [ ] Learning progress tracking
- [ ] Integration with knowledge bases
- [ ] Multi-language support
- [ ] Web interface/dashboard
