import pandas as pd
from email.utils import parseaddr
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import numpy as np

root_folder = '/home/dianaimf/'
input_file = root_folder + 'merged_data.csv'
output_file = root_folder + 'merged_data_with_replaced_emails.csv'

allmails_data_time_parsed_utc_LDA = pd.read_csv(input_file, low_memory=False)

def extract_email(email):
    if isinstance(email, str) and email.strip():  # Check if it's a non-empty string
        name, addr = parseaddr(email)
        return addr
    else:
        return np.nan

def normalize_email(email):
    return email.strip().lower()

def get_local_part(email):
    return email.split('@')[0]

def replace_emails_in_column(df, column_name):
    email_list = df[column_name].apply(extract_email)
    normalized_emails = [normalize_email(email) for email in email_list]
    local_parts = [get_local_part(email) for email in normalized_emails]
    threshold = 90

    unique_emails = []
    checked_emails = set()
    email_mapping = {}

    for email, local_part in zip(normalized_emails, local_parts):
        if email not in checked_emails:
            checked_emails.add(email)
            matches = process.extract(local_part, local_parts, scorer=fuzz.token_set_ratio)
            similar_email_indices = [i for i, match in enumerate(matches) if match[1] >= threshold and match[0] != local_part]

            if not similar_email_indices:
                unique_emails.append(email)
            else:
                for index in similar_email_indices:
                    similar_email = normalized_emails[index]
                    checked_emails.add(similar_email)
                    email_mapping[similar_email] = email

    replaced_emails = [email_mapping.get(email, email) for email in email_list]
    df['Replaced_' + column_name] = replaced_emails

# Process 'From' and 'To' columns
replace_emails_in_column(allmails_data_time_parsed_utc_LDA, 'From')
replace_emails_in_column(allmails_data_time_parsed_utc_LDA, 'To')

# Save the DataFrame with the new columns to a new CSV file
allmails_data_time_parsed_utc_LDA.to_csv(output_file, index=False)
