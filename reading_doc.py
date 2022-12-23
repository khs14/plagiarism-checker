def doc_to_text(file_name):
    import docx2txt
    my_text = docx2txt.process(file_name)
    file_list = my_text.split()
    conjunctions = ['after','although','as','because', 'before', 
    "for","if","since","unless",
    "until","when","whenever","where","wherever",'while','is',
    'a','the','an','of','to','that','on','are','but','and','from','also','the','so']
    for i in (file_list):
        for m in conjunctions:
            if(m==i):
                file_list.remove(i)
    file_string_new = ""
    for j in file_list:
        file_string_new = file_string_new + j + " "
    return file_string_new


