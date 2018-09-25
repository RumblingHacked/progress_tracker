import unicodecsv as csv
import plotly.graph_objs as go
import plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

plotly.tools.set_credentials_file(username='RumblingHacked', api_key='iWfwPUu7E8YcyIvahwuQ')

total_area_codes = 346
completed_list = []


def generate_completed_list():
    with open('completed-area-codes.csv', 'rb') as resourceFile:
        reader = csv.reader(resourceFile)
        for row in reader:
            for column in row:
                completed_list.append(column)



def write_csv():
    with open("completed-area-codes.csv", 'wb') as resultFile:
        wr = csv.writer(resultFile, dialect='excel')
        wr.writerow(completed_list)


def completed_area_code():
    completed = input('Have you completed and area code? \nEnter [Y] or [N]\n').upper()
    if completed == 'Y':
        area_code = input('Enter your area code\n')
        if len(area_code) != 3:
            print('Invalid Input')
            completed_area_code()
        else:
            if area_code not in completed_list:
                completed_list.append(area_code)
            else:
                print('Area code already completed')
    elif completed == 'N':
        print('Okay')
    else:
        print('Invalid Input')
        completed_area_code()


def generate_pie_chart():
    labels = ['Completed', 'Not-Completed']
    values = [len(completed_list), total_area_codes - len(completed_list)]
    colors = ['#EACF19', '#1D0C23']

    trace = go.Pie(labels=labels, values=values, hoverinfo='label+percent', textinfo='value', textfont=dict(size=20), marker=dict(colors=colors, line=dict(color='#000000', width=2)))

    plot([trace], filename='area_code_progress.html')


if __name__ == "__main__":
    generate_completed_list()
    completed_area_code()
    generate_pie_chart()
    write_csv()