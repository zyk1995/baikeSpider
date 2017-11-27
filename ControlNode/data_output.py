#coding:utf-8
import codecs
import time
'''
最好的做法是将数据分配存储到文件中，
将所有文件存储到内存中，一次性写入文件，系统容易出现异常造成数据丢失
'''

'''
生成文件1按照当前时间进行命名避免重复，
同时对文件进行缓存写入
'''


class DataOutput(object):
    def __init__(self):
        self.filepath = 'baike_%s.html' % (time.strftime("%Y_%m_%d_%H_%S", time.localtime()))
        self.output_head(self.filepath)
        self.datas = []

    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) > 10:
            self.output_html(self.filepath)

    def output_head(self, path):

        '''
        将HTML头写进去
        :param path:
        :return:
        '''
        fout = codecs.open(path, 'w', encoding='utf-8')
        fout.write('<html>')
        fout.write('<body>')
        fout.write('<table>')
        fout.close()

    def output_html(self, path):

        '''
        将Data写入HTML
        :param path:
        :return:
        '''

        fout = codecs.open(path, 'a', encoding='utf-8')

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")
            self.datas.remove(data)
        fout.close()

    def end_output(self, path):
        '''
         输出HTML结束
         :param self:
         :param path:文件存储路径
         :return:
         '''
        fout = codecs.open(path, 'a', encoding='utf-8')
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()

    def end_class(self):
        pass


if __name__ == '__main__':
    output = DataOutput()
    output.end_output(output.filepath)