def q8():
    def convert(st:str):
        words = set(st.split())  
        sorted_words = sorted(words)  
        return " ".join(sorted_words)  
    string = "My My name is 2 1 OLdMONk 2 1 MY"
    print(convert(string)) 
q8() 
    