import os
import xlwt
import xlrd
from xlutils.copy import copy
import time

class ExcelTool:

    def __init__(self, filename):
        self.filename = self.__get_file(filename)
        self.time = time.strftime('%Y-%m-%d %H:%M:%S')


    def __get_file(self, filename):
        full_path = '/tmp/' + filename + '.xls'
        if not os.path.exists(full_path):
            # 创建 xls 文件对象
            wb = xlwt.Workbook()
            # 新增一个表单页
            sh1 = wb.add_sheet('sheet1')
            style = xlwt.XFStyle()
            style.num_format_str = 'general'
            # 写入第一行
            sh1.write(0, 0, '日期', style)
            sh1.write(0, 1, '餐补')
            sh1.write(0, 2, '车补')
            sh1.write(0, 3, '触发时间')
            # 最后保存文件即可
            wb.save(full_path)
        return full_path


    def add(self, day):
        # 打开.xls 文件
        wb_read = xlrd.open_workbook(self.filename)

        # 根据 sheet 索引获取内容
        sh_read = wb_read.sheet_by_index(0)
        # 行数
        nrows = sh_read.nrows
        try:
            if nrows == 1:
                # 第一次填写
                # 打开 excel 文件
                read_book = xlrd.open_workbook(self.filename)
                # 复制一份
                wb_copy = copy(read_book)
                # 选取第一个表单
                sh_copy = wb_copy.get_sheet(0)
                # 在第一行新增写入数据
                sh_copy.write(1, 0, day)
                sh_copy.write(1, 1, 1)
                sh_copy.write(1, 3, self.time)
                # 保存
                wb_copy.save(self.filename)
            else:
                # 获取最后一行第一个值
                rows = sh_read.row_values(nrows - 1) # 获取最后一行内容
                if day == rows[0]:
                    # 修改
                    read_book = xlrd.open_workbook(self.filename)
                    # 复制一份
                    wb_copy = copy(read_book)
                    # 选取第一个表单
                    sh_copy = wb_copy.get_sheet(0)
                    # 在第一行新增写入数据
                    # sh_copy.write(1, 0, day)
                    sh_copy.write(nrows - 1, 2, 1)
                    sh_copy.write(nrows - 1, 3, self.time)
                    # 保存
                    wb_copy.save(self.filename)
                else:
                    # 新增
                    read_book = xlrd.open_workbook(self.filename)
                    # 复制一份
                    wb_copy = copy(read_book)
                    # 选取第一个表单
                    sh_copy = wb_copy.get_sheet(0)
                    # 在第一行新增写入数据
                    sh_copy.write(nrows, 0, day)
                    sh_copy.write(nrows, 1, 1)
                    sh_copy.write(nrows, 3, self.time)
                    # 保存
                    wb_copy.save(self.filename)
        except Exception as e:
            return {'code': 501, 'msg': '操作失败', 'data': ''}
        else:
            return {'code': 200, 'msg': '操作成功', 'data': ''}