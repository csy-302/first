import csv

data_to_write = [
    ['순위', '제목', '가수'],
    [1, '노래', '가수'],
    [2, '노래', '가수'],
    [3, '노래', '가수']
]
file_path = 'music.csv'
try:
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data_to_write)

    print(f"'{file_path}' 파일 생성")

except Exception as z:
    print(f"오류 발생: {z}")