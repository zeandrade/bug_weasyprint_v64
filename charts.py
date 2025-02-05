import pygal
def create_charts():
    bar_chart = pygal.Bar()
    bar_chart.title = 'Browser usage evolution (in %)'
    bar_chart.x_labels = map(str, range(2002, 2013))
    bar_chart.add('Firefox', [None, None, 0, 16.6,   25,   31, 36.4, 45.5, 46.3, 42.8, 37.1])
    bar_chart.add('Chrome',  [None, None, None, None, None, None,    0,  3.9, 10.8, 23.8, 35.3])
    bar_chart.add('IE',      [85.8, 84.6, 84.7, 74.5,   66, 58.6, 54.7, 44.8, 36.2, 26.6, 20.1])
    bar_chart.add('Others',  [14.2, 15.4, 15.3,  8.9,    9, 10.4,  8.9,  5.8,  6.7,  6.8,  7.5])
    bar_chart.render_to_file('/tmp/chart_example.svg')



    pie_chart = pygal.Pie(inner_radius=.4, height=250)
    pie_chart.title = 'Browser for intranet (in %)'
    pie_chart.add('IE', 19.5)
    pie_chart.add('Firefox', 36.6)
    pie_chart.add('Chrome', 36.3)
    pie_chart.add('Safari', 4.5)
    pie_chart.add('Opera', 2.3)
    pie_chart.render_to_file('/tmp/chart2.svg')

    radar_chart = pygal.Radar()
    radar_chart.title = 'V8 benchmark results'
    radar_chart.x_labels = ['Richards', 'DeltaBlue', 'Crypto', 'RayTrace', 'EarleyBoyer', 'RegExp', 'Splay', 'NavierStokes']
    radar_chart.add('Chrome', [6395, 8212, 7520, 7218, 12464, 1660, 2123, 8607])
    radar_chart.add('Firefox', [7473, 8099, 11700, 2651, 6361, 1044, 3797, 9450])
    radar_chart.add('Opera', [3472, 2933, 4203, 5229, 5810, 1828, 9013, 4669])
    radar_chart.add('IE', [43, 41, 59, 79, 144, 136, 34, 102])
    radar_chart.render_to_file('/tmp/chart1.svg')


    bar_chart = pygal.HorizontalBar(height=250)
    bar_chart.title = 'Browser usage here(in %)'
    bar_chart.add('IE', 19.5)
    bar_chart.add('Firefox', 36.6)
    bar_chart.add('Chrome', 36.3)
    bar_chart.add('Safari', 4.5)
    bar_chart.add('Opera', 2.3)
    bar_chart.render_to_file('/tmp/chart_example2.svg')