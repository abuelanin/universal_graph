import pandas as pd
import plotly.offline as offline
import plotly.plotly as py
import subprocess
import json
import os,sys
import shutil


with open('config.json', 'r') as f:
		config = json.load(f)

report_dir = config["report_dir_path"]
csv_dir = config["csv_dir_path"]
csv_file_name = config["csv_file_name"]
plot_dir = config["plots_dir"]
plot_type = config["plot_type"]
html_plot_name = config["html_plot_name"]

py.sign_in('DemoAccount', '2qdyfjyr7o')  # Replace the username, and API key with your credentials.

df = pd.read_csv(os.path.join(report_dir,csv_dir,csv_file_name))
# print df["Kmer"].tolist()

kmer = df["Kmer"].tolist()
disGraphs = df["Connected components"].tolist()


if plot_type == "line":
	offline.plot({'data': [{'y': disGraphs,'x':kmer}],
               'layout': {'title': 'Kmer - subGraphs','xaxis':{"title":"Kmer Size"},"yaxis":{"title":"No. Of Disconnected graphs"},
                          'font': dict(size=16)}},auto_open = False ,filename =html_plot_name)

elif plot_type == "scatter":
	offline.plot({
	"frames": [],
	"layout": {
	    "autosize": "true",
	    "yaxis": {
	        "type": "linear",
	        "title": "No. Of Disconnected graphs"
	    },
	    "title": "Kmer - subGraphs",
	    "breakpoints": [],
	    "xaxis": {
	        "type": "linear",
	        "title": "Kmer Size"
	    },
	    "hovermode": "closest",
	    "font": {
	        "size": 16
	    }
	},
	"data": [
	    {
	        "autobinx": "true",
	        "uid": "950986",
	        "ysrc": "abuelanin:0:5f1e67",
	        "xsrc": "abuelanin:0:112008",
	        "name": "y",
	        "mode": "markers",
	        "y": disGraphs,
	        "x": kmer,
	        "type": "scatter",
	        "autobiny": "true"
	    }
	]
	},auto_open = False ,filename = html_plot_name)


shutil.move(html_plot_name, os.path.join(report_dir,plot_dir,html_plot_name))

print ("Plot genrated successfully")