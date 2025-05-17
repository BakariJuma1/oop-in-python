# save a note
def save_note(note):
    with open('notes.txt','a')as f:
        f.write(note+'\n')

def  read_notes():
    with open('notes.txt','r') as f:
        return f.read()
    
save_note.close()    
    
# usage    
save_note('buy milk') 
save_note('call mom')
save_note('call jay')
print(read_notes)