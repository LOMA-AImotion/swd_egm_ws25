import random 


def parse_file_into_list(file_path):
    with open(file_path) as f: 
        lines = f.readlines()
    
    clean_lines = [l.strip() for l in lines]
    return clean_lines 

file_path = "/Users/lodes/Work/git/swd_egm_ws25/Lecture7_PW_Generator/nomen.txt"
lines = parse_file_into_list(file_path)
print(lines)

print(random.choice(lines))