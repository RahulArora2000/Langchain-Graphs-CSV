# SufiBot

SufiBot is a conversational assistant powered by language models. It uses the LangChain library and various other Python packages to provide interactive chat functionality. This readme provides an overview of the code and its dependencies.

## Dependencies

Make sure you have the following dependencies installed:

- langchain
- streamlit
- pandas
- matplotlib
- google-cloud-aiplatform
- google-cloud-bigquery
- sqlalchemy
- google-auth

## Usage

To run the code, follow these steps:

1. Install the required dependencies using pip:

   ```shell
   pip install langchain streamlit pandas matplotlib google-cloud-aiplatform google-cloud-bigquery sqlalchemy google-auth
   ```

2. Create a new Python file and copy the code into it.

3. Replace the placeholder values for the following variables with your own values:

   - `PROJECT_ID`: The ID of your Google Cloud project.
   - `GOOGLE_APPLICATION_CREDENTIALS`: The path to your service account credentials JSON file.

4. Open a terminal or command prompt, navigate to the directory containing the Python file, and run the following command:

   ```shell
   streamlit run <filename>.py
   ```

   Replace `<filename>` with the name of your Python file.

5. A Streamlit web application will be launched, displaying the SufiBot chat interface.

6. Enter your text input in the provided text box and press Enter or click the "Submit" button.

7. SufiBot will process your input and provide a response. The conversation history will be displayed on the page.

8. To clear the conversation history, click the "Clear Conversation" button.

## Additional Notes

- This code assumes the presence of CSV files named "inventory.csv" and "order.csv" in the specified paths (`C:\Users\Rahul\Downloads\inventory.csv` and `C:\Users\Rahul\Downloads\order.csv`). Make sure to update the paths if your files are located elsewhere or have different names.

- The code uses the `create_pandas_dataframe_agent` function from the `langchain.agents` module to create an agent based on the provided ERP and transactional data. You may need to modify this part to suit your specific use case.

- The code uses the `streamlit_chat` package to display the chat interface. It also relies on Streamlit for the web application framework. Feel free to customize the UI or integrate it into your own application as needed.

- Note that some parts of the code are commented out or not used (`matplotlib.use('TKAgg')`, `tkinter`, etc.). You can remove or uncomment these parts if they are not necessary for your application.

- The code is provided as-is and may require additional modifications and error handling to work correctly in your environment.