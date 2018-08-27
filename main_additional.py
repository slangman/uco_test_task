linked_list = set()
dict_map = dict()
vertex_map = dict()
_i = 0


class Vertex:
    matrix = [[]]

    def set_size(self, rows, columns):
        self.matrix = [[0 for x in range(rows)] for y in range(columns)]

    def get_size(self):
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        return self.VertexSize(rows, columns)

    def set_item(self, row_index, column_index, value):
        self.matrix[row_index][column_index] = value

    def get_item(self, row_index, column_index):
        return self.matrix[row_index][column_index]

    def get_determinant(self, mt1):
        return CommonUtils.calculate_determinant(mt1)

    @staticmethod
    def create_vertex(rows, columns):
        mt = Vertex()
        mt.set_size(rows, columns)
        return mt

    class VertexSize:
        def __init__(self, rows, columns):
            self.rows = rows
            self.columns = columns

        def get_rows(self):
            return self.rows

        def get_columns(self):
            return self.columns


class CommonUtils:
    @staticmethod
    def multiply(vertex1, vertex2):
        rows1 = vertex1.get_size().get_rows()
        cols1 = vertex1.get_size().get_columns()
        rows2 = vertex2.get_size().get_rows()
        cols2 = vertex2.get_size().get_columns()
        if cols1 != rows2:
            return None
        else:
            mt = Vertex().create_vertex(rows1, cols2)
            for i in range(0, rows1):
                for j in range(0, cols2):
                    for k in range(0, cols1):
                        tmp = mt.get_item(i, j) + vertex1.get_item(i, k) * vertex2.get_item(k, j)
                        mt.set_item(i, j, tmp)
            return mt

    @staticmethod
    def replace_line(line, target_line, vertex):
        rows = vertex.get_size().get_rows()
        cols = vertex.get_size().get_columns()
        second_line = target_line

        for first_line in range(line, rows):
            for j in range(0, cols):
                tmp = vertex.get_item(first_line, j)
                vertex.set_item(first_line, j, vertex.get_item(second_line, j))
                vertex.set_item(second_line, j, tmp)

        return vertex

    @staticmethod
    def revert(vertex):
        rows = vertex.get_size().get_rows()
        cols = vertex.get_size().get_columns()
        mt = Vertex().create_vertex(rows, cols)
        tmp = float(0.0)

        for i in range(0, rows):
            for j in range(0, cols):
                # nonlocal tmp
                tmp = vertex.get_item(i, j)
                mt.set_item(j, i, tmp)
                tmp = float(0.0)

        return mt

    @staticmethod
    def calculate_determinant(vertex):
        rows = vertex.get_size().get_rows()
        cols = vertex.get_size().get_columns()
        result = float(1.0)
        vertex1 = Vertex()
        vertex1.set_size(rows, cols)


        for k in range(0, rows):
            for l in range(0, cols):
                vertex1.set_item(k, l, vertex.get_item(k, l))

        vertex2 = Vertex()
        vertex2.set_size(rows, cols)

        _j = 0
        for i in range(0, rows):
            global _i
            _i = i
            for j in range(0, cols):
                #nonlocal _j
                #_j = j
                vertex2.set_item(i, j, vertex.get_item(i, j))

        # blabla
        for i in range(0, cols):
            #global _i
            #_i = i
            if vertex1.get_item(i, i) == 0.0 and i < rows - 1:
                count = i

                while True:
                    vertex1.get_item(count, 0)
                    count = count + 1
                    if vertex1.get_item(count, 0) != 0.0:
                        break
                vertex1 = CommonUtils.replace_line(i, count, vertex1)
                result = -result

            #_k = 0
            for j in range(0, rows):
                #nonlocal _j
                #_j = j
                for k in range(0, cols):
                    #nonlocal _k
                    #_k = k
                    vertex2.set_item(j, k, vertex1.get_item(j, k))

            for j in range(_i + 1, rows):
                for k in range(_i, cols):
                    print('i:' + str(i))
                    tmp = vertex1.get_item(j, k) - vertex1.get_item(i, k) * vertex2.get_item(j, i) / vertex1.get_item(i,
                                                                                                                      i)
                    vertex1.set_item(j, k, tmp)

            '''
            for j in range(i + 1, rows):
                for k in range(i, cols):
                    print('i:' + str(i))
                    tmp = vertex1.get_item(j, k) - vertex1.get_item(i, k) * vertex2.get_item(j, i) / vertex1.get_item(i,
                                                                                                                      i)
                    vertex1.set_item(j, k, tmp)
                    '''

        for i in range(0, rows):
            result = result * vertex1.get_item(i, i)

        return result


def main():
    print("Enter matrix size: ", end='')
    rows = int(input())
    vertex_first = Vertex()
    vertex_first.set_size(rows, rows)
    vertex_map.update({vertex_first: 1})
    vertex_second = Vertex()
    vertex_second.set_size(rows, rows)
    vertex_map.update({vertex_second: 2})
    print("Enter first matrix:")

    value = 0.0
    sum = 0
    row_index = 0
    j = 0
    for i in range(0, rows):
        sum = i + 1
        for row_index in range(0, rows):
            j = row_index + 1
            print('Enter [' + str(sum) + ',' + str(j) + ']')
            value = float(input())
            linked_list.add(value)
            vertex_first.set_item(i, row_index, value)

    dict_map.update({1: vertex_first})

    new_linked_list = linked_list.copy()

    for val in new_linked_list:
        if val % 2.0 == 0.0:
            linked_list.remove(val)

    print("Enter second matrix:")
    for sum in range(0, rows):
        row_index = sum + 1
        for j in range(0, rows):
            column_index = j + 1
            print('Enter [' + str(row_index) + ',' + str(column_index) + ']')
            value = float(input())
            linked_list.add(value)
            vertex_second.set_item(sum, j, value)
            dict_map.update({column_index + 1: vertex_second})

        dict_map.update({row_index: vertex_second})

    dict_map.update({2: vertex_second})
    sum = 0

    for val in linked_list:
        sum = sum + int(val)

    print('\nMap size: ' + str(len(dict_map)))

    for key, value in dict_map.items():
        if value is not None:
            sum = sum + int(key)

    vertex_first = CommonUtils.multiply(vertex_first, vertex_second)
    vertex_first = CommonUtils.revert(vertex_first)
    value = vertex_first.get_determinant(vertex_first)
    first_item = vertex_map.get(vertex_first)
    second_item = vertex_map.get(vertex_second)
    if first_item is None:
        sum = sum + 1

    if second_item is None:
        sum = sum - 1

    print('value: ' + str(value))
    print('sum: ' + str(sum))
    print('VertexMap size: ' + str(len(vertex_map)))


if __name__ == "__main__": main()
