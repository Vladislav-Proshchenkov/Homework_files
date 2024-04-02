all_texts = {}

with open('text1.txt', encoding='utf-8') as text_file_1:
    all_texts['text1'] = text_file_1.readlines()

with open('text2.txt', encoding='utf-8') as text_file_2:
    all_texts['text2'] = text_file_2.readlines()

with open('text3.txt', encoding='utf-8') as text_file_3:
    all_texts['text3'] = text_file_3.readlines()

with open('text.txt', 'a', encoding='utf-8') as text_file:
    #sorted_text = {}
    sorted_list = sorted(all_texts.items(), key=lambda item: item[1], reverse=True)
    for sorted_text in sorted_list:
        print(sorted_text[0])
        print(len(sorted_text[1]))
        print(' '.join(sorted_text[1]))
        text_file.write(f'{sorted_text[0]}\n {len(sorted_text[1])}\n {"".join(sorted_text[1])}\n\n')