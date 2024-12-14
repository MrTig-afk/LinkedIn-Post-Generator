# LinkedIn-Post-Generator

This project generates LinkedIn posts by scraping headlines from a news website and using the Gemini API with the `gemini-1.5-flash` model for content creation.

## Features

- **Headline Scraping**: Scrapes the first headline from a specified news website (e.g., [BBC News](https://www.bbc.com/news)).
- **Content Generation**: Uses the Gemini API to create LinkedIn posts based on the scraped headlines.

## Technologies Used

- **Gemini API**: Utilizes the `gemini-1.5-flash` model to generate LinkedIn posts.
- **BeautifulSoup**: For web scraping to extract headlines.
- **Requests**: To make HTTP requests to news websites and the Gemini API.

## Getting Started

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/LinkedIn-Post-Generator.git
    cd LinkedIn-Post-Generator
    ```

2. **Install Dependencies**

    Ensure you have Python installed, then install the required packages:

    ```sh
    pip install requests beautifulsoup4 google-generativeai python-dotenv
    ```

3. **Set Up Environment Variables**

    Create a `.env` file in the root directory of the project and add your API keys:

    ```env
    API_KEY=your_gemini_api_key
    ```

4. **Run the Script**

    Execute the script to generate and post LinkedIn content:

    ```sh
    python app.py
    ```

## Instructions

### Scraping Headline

The script scrapes the first headline from the specified website. You can customize the URL or website as needed.

### Content Generation

The scraped headline is used as input for the Gemini API to generate LinkedIn posts. The `gemini-1.5-flash` model is employed for content creation.

### Reference

For scraping instructions and techniques, refer to this [video tutorial](https://youtu.be/JlHdv4Dfjq4?si=1w1-4N6GNDW5CCW1) which demonstrates how to scrape headlines effectively.

## Notes

- Ensure you have valid Gemini API.
- Update the `.env` file with your credentials before running the script.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


