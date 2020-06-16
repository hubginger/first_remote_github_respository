import openpyxl


class ExcelData:
    def __init__(self, zipObj):
        for item in zipObj:
            setattr(self, item[0], item[1])


class DoExcel:
    def __init__(self, file_name, sheet_name):
        self.file_name = file_name
        self.sheet_name = sheet_name
        self.wb = openpyxl.load_workbook(self.file_name)
        self.s = self.wb[self.sheet_name]


    def read_data_object_2(self):
        def fun(x):
            return x.value
        list_head = list(map(fun, list(self.s.rows)[0]))
        datas = []
        for row in list(self.s.rows)[1:]:
            z = list(zip(list_head, list(map(fun, row))))
            ed = ExcelData(z)
            datas.append(ed)
        return datas

    def write_result(self,index_row,index_column,ref_value):
        self.s.cell(index_row,index_column).value = ref_value
        self.wb.save(self.file_name)





