

# Create your views here.
#from django.http import HttpResponse


#def client_database(request):
#    return HttpResponse("Hello, this is the PoultryVet database")


from django.shortcuts import render
#Import models from VSDK app
from vsdk.service_development.models.session import *
#Import database information
from vetsite.clients import KasaDaka_Database
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib import pylab
from pylab import *
# import PIL
# from PIL import Image
# import base64
# import io
# from io import *


#Load data via django database utility
def call_session(request):
    call_sessions = CallSession.objects.all()
    call_session_steps = CallSessionStep.objects.all()

    ###
    #query = KasaDaka_Database.query("SELECT _visited_element_id FROM service_development_callsessionstep")
    #Swap query with above before deployment
    def graph():
        query = [(8,), (16,), (8,), (16,), (8,), (17,)]
        disease_dict = {16:"Bursal Disease", 17:"Fowl Pox", 18:"Marek's Disease", 19:"Newcastle Disease"}
        count_list = []
        for item in query:
            if item[0] in disease_dict.keys():
                count_list.append(disease_dict[item[0]])
        #Data
        count = Counter(count_list)
        labels = count.keys()
        fracs = count.values()
        # Make square figures and axes
        plt.pie(fracs, labels=labels, autopct='%1.1f%%', shadow=True)
        plt.title('Disease Occurances')
        return plt.savefig('disease_graph.jpg')
    disease_graph = graph()

    ###

    sql = KasaDaka_Database.query("SELECT * FROM service_development_callsession")
    return render(request, 'vetsite/call_session.html', {'call_sessions': call_sessions, 'call_session_steps': call_session_steps, 'sql': sql})





# from vsdk.static.fusioncharts.fusioncharts import FusionCharts
# Include the `fusioncharts.py` file which has required functions to embed the charts in html page
#
# def chart(request):
#     #query = KasaDaka_Database.query("SELECT _visited_element_id FROM service_development_callsessionstep")
#     query = [(8,), (16,), (8,), (16,), (8,), (17,)]
#     disease_dict = {16: "Bursal Disease", 17: "Fowl Pox", 18: "Marek's Disease", 19: "Newcastle Disease"}
#     count_list = []
#     for item in query:
#         if item[0] in disease_dict.keys():
#             count_list.append(disease_dict[item[0]])
#             # Data
#     counts = Counter(count_list)
#
#     #Chart data is passed to the `dataSource` parameter, as dict, in the form of key-value pairs.
#     dataSource = {}
#     # setting chart cosmetics
#     dataSource['chart'] = {
#         "caption": "Top 10 Most Populous Countries",
#         "paletteColors": "#0075c2",
#         "bgColor": "#ffffff",
#         "borderAlpha": "20",
#         "canvasBorderAlpha": "0",
#         "usePlotGradientColor": "0",
#         "plotBorderAlpha": "10",
#         "showXAxisLine": "1",
#         "xAxisLineColor": "#999999",
#         "showValues": "0",
#         "divlineColor": "#999999",
#         "divLineIsDashed": "1",
#         "showAlternateHGridColor": "0"
#     }
#
#     dataSource['data'] = []
#     # The data for the chart should be in an array wherein each element of the array is a JSON object as
#     # `label` and `value` keys.
#     # Iterate through the data in `Country` model and insert in to the `dataSource['data']` list.
#     dataSource['data'] = []
#     for key, value in counts.items():
#         data = {}
#         data['label'] = key
#         data['value'] = value
#         dataSource['data'].append(data)
#
#         # Create an object for the Column 2D chart using the FusionCharts class constructor
#     column2D = FusionCharts("column2D", "ex1", "600", "400", "chart-1", "json", dataSource)
#         # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
#     return render(request, 'plot/fusioncharts-html-template.html', {'output': column2D.render()})
#
