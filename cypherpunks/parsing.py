import os
import email
import pandas as pd

# Specify the directory containing the text files
directory = '/Users/dianavieirafernandes/Desktop/LSSP-project/cypherpunks/2000-to-2016-raw-cypherpunks-archive-master/cur/'

# Create a list of the filenames in the directory
filenames = [os.path.join(directory, filename) for filename in os.listdir(directory)
             if os.path.isfile(os.path.join(directory, filename))]

# Create an empty list to store the email DataFrames
dfs = []

# Loop over each file in the directory
for filename in filenames:
    try:
        with open(filename, 'r', encoding='ISO-8859-1') as f:
            # Read in the text file
            text = f.read()

            # Split the text into individual email messages
            messages = text.split('\nFrom ')

            # Loop over each email message and parse it using the email module
            for message in messages:
                # Prepend 'From ' to the message to make it a valid email message
                message = 'From ' + message

                # Parse the message using the email module
                msg = email.message_from_string(message)

                # Extract the relevant headers and body
                from_address = msg['From']
                to_address = msg['To']
                message_id = msg['Message-ID']
                date = msg['Date']
                subject = msg['Subject']
                in_reply_to = msg['In-Reply-To']
                mime_version = msg['MIME-Version']
                content_type = msg['Content-Type']
                body = msg.get_payload()

                # Create a new DataFrame for the email message
                df = pd.DataFrame({
                    'From': [from_address],
                    'To': [to_address],
                    'Message-ID': [message_id],
                    'Date': [date],
                    'Subject': [subject],
                    'In-Reply-To': [in_reply_to],
                    'MIME-Version': [mime_version],
                    'Content-Type': [content_type],
                    'Body': [body]
                })

                # Append the DataFrame to the list of DataFrames
                dfs.append(df)

    except Exception as e:
        # If an exception occurs, print the error message and continue processing
        print(f"Error parsing message: {e}")
        continue

# Concatenate the list of DataFrames into a single DataFrame
email_df2000 = pd.concat(dfs, ignore_index=True)

# Write the DataFrame to a CSV file
email_df2000.to_csv('/Users/dianavieirafernandes/Desktop/LSSP-project/cypherpunks/email_df2000.csv', index=False)

# Write the DataFrame to a JSON file
email_df2000.to_json('/Users/dianavieirafernandes/Desktop/LSSP-project/cypherpunks/email_df2000.json')
