
# Commit Lens

**Commit Lens** is a tool designed to analyze Git commits and provide insights on code improvements and situations. It helps developers understand the evolution of their codebase, identify patterns, and make informed decisions based on commit history.

## Features

- **Commit Analysis**: Examine commit messages and changes to identify trends and areas for improvement.
- (Future) **Insights Generation**: Automatically generate reports summarizing the state of the codebase and potential enhancements.
- (Future) **Improvement Tracking**: Monitor improvements over time based on commit history and patterns.

## Requirements

Before using **commit-lens**, ensure that you have the following installed on your machine:

- [Ollama](https://ollama.com) - A local API for LLMs.
- Llama 3.2 model.

## Installation

### Step 1: Install Ollama

To install Ollama, follow these steps:

1. Open your terminal.
2. Run the following command to download and install Ollama:
   ```bash
   curl -sSfL https://ollama.com/download | sh
   ```

### Step 2: Download the Llama 3.2 Model

Once Ollama is installed, download the Llama 3.2 model using the following command:
```bash
ollama pull llama3.2
```

### Step 3: Clone the commit-lens Repository

1. Clone the repository:
   ```bash
   git clone https://github.com/josielborges/commit-lens.git
   cd commit-lens
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To use **commit-lens**, run the following command in your terminal:

```bash
python python main.py
```

An uvicorn server will be started on http://0.0.0.0:8000

Access the api documentation at http://0.0.0.0:8000/docs

## Contributing

Contributions are welcome! If you'd like to contribute to **commit-lens**, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your forked repository.
5. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [GitPython](https://gitpython.readthedocs.io/en/stable/) - A Python library used to interact with Git repositories.
- [Ollama](https://ollama.com) - The local API for LLMs that powers commit-lens.

## Contact

For any inquiries or support, please reach out at [chrys.jop@gmail.com].
