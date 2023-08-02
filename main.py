def ex_1(matrix: list[list]) -> list[list]:
    """Напишите функцию для транспонирования матрицы"""
    transport_matrix = []
    for first, second in zip(matrix[0], matrix[1]):
        transport_matrix.append([first, second])
    print("Функция работает только для матриц с двумя строками(( пытался там добавить итератор, но что то как то "
          "не пошло. Просто хотел сделать через зип")
    return transport_matrix


def ex_1_1(matrix: list[list]) -> list[list]:
    transport_matrix = []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    for col in range(num_cols):
        new_row = []
        for row in range(num_rows):
            new_row.append(matrix[row][col])
        transport_matrix.append(new_row)
    print('Ну а это просто чтобы для любой матрицы')
    return transport_matrix


def ex_2(**kwargs) -> dict:
    """Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
    переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление"""
    new_dict = {}
    for name, value in kwargs.items():
        try:
            hash(value)
            new_dict[value] = name
        except TypeError as ex:
            new_dict[str(value)] = name
    return new_dict


print('-----Задание 1-----')
print(ex_1([[1, 2, 3], [4, 5, 6]]))
print(ex_1_1([[1, 2, 3], [4, 5, 6]]))
print('-----Задание 2-----')
print(ex_2(lal=1, seet={1, 2, 2}, dell=4, liist=[1, 2, 3, 4, 5]))
