import csv
import datetime
from database.fileld_names import *


def csv_save(all_messages: list, path="") -> str:

    if len(path) == 0:
        mdate = datetime.datetime.now()
        datef = mdate.strftime('%d%m_%H-%M')
        path = f'worked_files/csv_files/messages_{datef}.csv'
    with open(path, 'w', encoding='UTF8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields_needed)
        writer.writeheader()
        # all_messages.reverse()
        writer.writerows(all_messages)
    return path

def set_dialogue_id(csv_file)->list:
    with open(csv_file, 'r', encoding='UTF8') as file:
        reader = csv.DictReader(file)
        all_messages = list(reader)
        

    dialogue = 1
    for filtered_dict in all_messages:
        if isinstance(filtered_dict.get('replies'), int):
            filtered_dict['dialogue_id'] = dialogue
            dialogue += 1
        elif filtered_dict.get('reply_to_msg_id', ''):
            for message in all_messages:
                if message.get('id') == filtered_dict.get('reply_to_msg_id'):
                    filtered_dict['dialogue_id'] = message.get('dialogue_id')
    csv_save(all_messages, csv_file)
    # return all_messages
