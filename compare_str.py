def compare(content,main_text):
    content = content.lower()
    main_text = main_text.lower()
    content_list = content.split()
    main_text_list = main_text.split()
    match = 0
    for i in range(content_list):
        if (i in main_text_list):

            match = match + 1
    total = len(content_list)
    ans = int((match/total)*100)
    return ans
