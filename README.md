# YC Lectures QnA

This repository is a tool for asking and answering questions related to the Y Combinator lectures held by Sam Altman. It is designed to help users gain deeper insights into the principles, strategies, and philosophies shared during these startup-focused lectures.

## Features
- **Interactive Q&A:** Ask questions based on the content of YC lectures and retrieve meaningful, contextual answers.
- **Categorized Topics:** Topics are organized for easier navigation and study.
- **Practical Insights:** Gain practical knowledge and advice directly from the insights of Sam Altman and other YC speakers.

## Repository Structure
```
YC_Lectures-QnA/
├── Data/
│   ├── ...
├── Yc-Embeddings/
│   ├── ...
├── .env
├── .gitignore
├── README.md
├── SQLAGENT.py
├── WorkingSQL.py
├── main.py
├── note.py
├── pdf.py
├── prompts.py
├── requirements.txt
```
- **Data/**: Stores data files used in the project.
- **Yc-Embeddings/**: Contains embeddings for processing questions.
- **SQLAGENT.py**: Handles SQL-related operations for querying data.
- **WorkingSQL.py**: A script for SQL processing.
- **main.py**: The main entry point for running the Q&A system.
- **prompts.py**: Contains predefined prompts for interacting with the lectures.
- **requirements.txt**: Lists dependencies required for the project.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/PragalvhaSharma/YC_Lectures-QnA-.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up your `.env` file with necessary API keys (e.g., OpenAI API key).
4. Run `main.py` to start asking questions and receiving answers based on the lectures:
   ```bash
   python main.py
   ```

## Contributing
We welcome contributions to enhance this project! Here’s how you can help:
1. Fork the repository.
2. Make changes in a new branch.
3. Submit a pull request with a description of your updates.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Thanks to Sam Altman and Y Combinator for their valuable lectures and startup resources.
- Inspired by the entrepreneurial journey and insights shared in YC's startup school.

---

For any questions or suggestions, please open an issue or contact me directly.

Happy learning and building!
