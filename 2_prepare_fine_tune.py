import openai

# Function to open a file and return its content
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

# Function to append content to a file
def save_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as outfile:
        outfile.write(content)

# Your OpenAI API key (Note: You should never expose your API keys in code. Instead, use environment variables or other secure methods.)
api_key = 'sk-...........'

# Create a client object to interact with the OpenAI API
client = openai.OpenAI(api_key=api_key)

# Path to the JSON Lines file that contains the training data for fine-tuning
training_data_path = '/Users/renzo/Downloads/json_divorcios_2.jsonl'

# Open the training data file and upload it to OpenAI for fine-tuning
with open(training_data_path, "rb") as file:
    response = client.files.create(file=file, purpose="fine-tune")

# Retrieve the ID of the uploaded file from the response
# It appears you are trying to get the 'id' from the response dictionary but instead the entire response is being printed.
# Uncomment the correct line to use the file ID in your print statement.
# file_id = response['id']
file_id = response
print(f"file uploaded successfully with ID:{file_id}")

# Sample file IDs are commented out below. Use the actual file ID for further processing.
# file-....
# file-.....
