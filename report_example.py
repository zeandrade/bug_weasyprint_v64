
from jinja2 import  Environment, FileSystemLoader
from weasyprint import HTML, CSS

import charts

def make_report(file_output='report.pdf'):
    main_data = {
        'idnum': 1234567,
        'url': 'https://example.website',
        'date': '04/02/2025',
        'some_data':{
            'identifier_1':['item x','some info', 'etc'],
            'identifier_2':['item y','some info', 'etc'],
            'identifier_3':['item z','some info', 'etc'],
            'identifier_4':['item a','some info', 'etc'],
            'identifier_5':['item b','some info', 'etc'],
            'identifier_11':['item x','some info', 'etc'],
            'identifier_21':['item y','some info', 'etc'],
            'identifier_31':['item z','some info', 'etc'],
            'identifier_41':['item a','some info', 'etc'],
            'identifier_51':['item b','some info', 'etc'],
            'identifier_81':['item x','some info', 'etc'],
            'identifier_42':['item y','some info', 'etc'],
            'identifier_43':['item z','some info', 'etc'],
            'identifier_44':['item a','some info', 'etc'],
            'identifier_35':['item b','some info', 'etc'],
            'identifier_91':['item x','some info', 'etc'],
            'identifier_32':['item y','some info', 'etc'],
            'identifier_33':['item z','some info', 'etc'],
            'identifier_34':['item a','some info', 'etc'],
            'identifier_65':['item b','some info', 'etc'],
        }

    }
    dataset1 = [
        { 'str_x': '10_0_0_1',
          'reqs': 32545,
          'bytes': '12MiB',
          'ip': '10.0.0.1',
          'perc': 23,
          'net': '10_0_0_1/32',
          'doc' :'AB54C09D',
          'extra': {
              'data' : {'a': 'Data 1', 'b': 'Data 2', 'c': 'Data 3',},
              'datab' : {'a': 'Data 1', 'b': 'Data 2', 'c': 'Data 3',},
              'datac' : {'a': 'Data 1', 'b': 'Data 2', 'c': 'Data 3',},
            },
        },   
        { 'str_x': '10_0_0_2',
          'reqs': 442546,
          'bytes': '13MiB',
          'ip': '10.0.0.2',
          'net': '10_0_0_2/32',
          'doc' :'CB54C09D',
          'perc': 55,
          'extra': {
              'data' : {'a': 'Data 1', 'b': 'Data 2', 'c': 'Data 3',},
              'datab' : {'a': 'Data 1', 'b': 'Data 2', 'c': 'Data 3',},
              'datac' : {'a': 'Data 1', 'b': 'Data 2', 'c': 'Data 3',},
            },
        }, 
        { 'str_x': '10_0_0_3',
          'reqs': 72546,
          'bytes': '21MiB',
          'ip': '10.0.0.3',
          'net': '10_0_0_3/32',
          'doc' :'FB54C07D',
          'perc': 82,
          'extra': {
              'data' : {'a': 'Data 1', 'b': 'Data 2', 'c': 'Data 3',},
              'datab' : {'a': 'Data 1', 'b': 'Data 2', 'c': 'Data 3',},
              'datac' : {'a': 'Data 1', 'b': 'Data 2', 'c': 'Data 3',},
            },
        },      
             ]
    
    
    environment = Environment(loader=FileSystemLoader('.'))
    template = environment.get_template('report_template.html')
    content = template.render(main_data=main_data, dataset1=dataset1, )
    HTML(string=content).write_pdf(file_output,stylesheets=[CSS(filename='report_styles.css')])



if __name__ == "__main__":
    charts.create_charts()
    make_report('report_ok_v63.pdf')