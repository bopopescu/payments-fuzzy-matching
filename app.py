import json

from funcs.db_connections import fetch_name_sql
from funcs.text_validation import valid_sort_code, valid_account_number
from funcs.fuzzy_matching import name_similarity_array

def validate_payment(name, sort_code, account_number, pass_threshold):

    #Format - Name, sort_code, account_number, match_percentage, outcome, error_message 
    output_array = [name, sort_code, account_number, '-', '-', '-']
    
    if (valid_sort_code(sort_code) == False or valid_account_number(account_number) == False):
        
        output_array[5] = 'Invalid account number or sort code'

    else:
        result_name = fetch_name_sql(account_number, sort_code)

        if (len(result_name) > 0):

            match_percentage = name_similarity_array(name, result_name)
            
            if (match_percentage) > pass_threshold: outcome = 'Pass'
            else: outcome = 'Fail'

            output_array[3] = match_percentage
            output_array[4] = outcome
            output_array[5] = '-'

        else:
            output_array[3] = ''
            output_array[4] = 'NA'
            output_array[5] = 'Reference payee name not found'
    
    output_tuples_array = [('name', str(output_array[0])), ('sort_code', str(output_array[1])), ('account_number', str(output_array[2])), ('match_percentage', str(output_array[3])), ('payment_status', str(output_array[4])), ('error_message', str(output_array[5]))]
    
    return (json.dumps(dict(output_tuples_array)))
