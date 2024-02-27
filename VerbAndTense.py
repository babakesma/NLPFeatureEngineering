
# NLTK lib most be installed for this function

def check_verb(pos_tag):
    tense='Base form'
    verb, current_pos = pos_tag
    if current_pos.startswith('VBD'):
        tense='Past'
    elif current_pos.startswith('VBG'):
        index=verb.find('ing')
        if index>0:
            tense='Gerund'
        else:
            tense='Present'
    elif current_pos.startswith('VBN'):
        tense='Past Participle'    
    elif current_pos.startswith('VBP'):
        tense='non-3rd person singular present'
    elif current_pos.startswith('VBZ'):
        tense='3rd person singular present'
    return verb,tense


