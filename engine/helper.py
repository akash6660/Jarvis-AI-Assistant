import re
def extract_yt_term(command):
    # Updated regex pattern to correctly extract the search term
    pattern = r'play\s+(.*?)\s*(?:on\s+youtube)?$'
    
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1) if match else None

