linked_list = {}
dict_map = {}
vertex_map = {}


def main():
    print("Enter matrix size: ", end='')
    rows = int(input())
    print("Enter first matrix:")
    vertex_first = Vertex()
    vertex_first
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

    print("Enter second matrix:")
    for sum in range(0, rows):
        row_index = sum + 1
        for j in range(0, rows):
            column_index = j + 1
            print('Enter [' + str(row_index) + ',' + str(column_index) + ']')
            value = float(input())


if __name__ == "__main__": main()


class Vertex:
    matrix = []

    def set_size(self, rows, columns):
        matrix = [rows][columns]

    def get_size(self):
        rows = len(self.matrix)
        columns = len(self.matrix[0])
        return self.VertexSize(rows, columns)

    def set_item(self, row_index, column_index, value):
        self.matrix[row_index][column_index] = value

    def get_item(self, row_index, column_index):
        return self.matrix[row_index][column_index]

    def get_determinant(self, mt1):
        return 0

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
        def multiply(self, vertex1, vertex2):
            rows1 = vertex1.get_size().get_rows()
            cols1 = vertex1.get_size().get_columns()
            rows2 = vertex2.get_size().get_rows()
            cols2 = vertex2.get_size().get_columns()
            if cols1 != rows2:
                return
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
            return