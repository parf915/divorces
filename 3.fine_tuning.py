import openai

# Function definitions appear to be unused in this script, consider removing them if that's the case
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()

def save_file(filepath, content):
    with open(filepath, 'a', encoding='utf-8') as outfile:
        outfile.write(content)

# API key should not be hardcoded. It's better to use environment variables for security reasons. This is just for educational porpuses
api_key = 'sk-Po............'

# Initialize a client to interact with OpenAI's API using the provided API key
client = openai.OpenAI(api_key=api_key)

# The file ID of the training data that has been previously uploaded
training_file_id = 'file-X3pGNEithDz3......'

# The name of the model you want to fine-tune
model_name = 'gpt-3.5-turbo-1106'

# Create a fine-tuning job using the training file and model name specified
response = client.fine_tuning.jobs.create(
    training_file=training_file_id, model=model_name)

# Extract the job ID from the response for further tracking or reference
# The response seems to be assigned directly to job_id instead of extracting the 'id'
# Uncomment the correct line if you want to extract just the ID.
# job_id = response['id']
job_id = response
print(f"Fine-tuning job created successfully with ID:{job_id}")

# Example IDs from previous fine-tuning jobs have been commented out.
# These can be used as a reference to understand the structure of the response.
# Uncomment them or use the actual job ID for further processing.
# ID:FineTuningJob(id='ftjob-9RcJHrijzms.......', ...)
# ID:FineTuningJob(id='ftjob-eM5Kl6gnXh......', ...)

# Sample job IDs are commented out below.
# ftjob-O3DC10Vbe........
