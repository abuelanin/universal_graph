import pandas as pd
import plotly.offline as offline
import plotly.plotly as py

py.sign_in('DemoAccount', '2qdyfjyr7o')  # Replace the username, and API key with your credentials.

df = pd.read_csv('result.csv')
# print df["Kmer"].tolist()

kmer = df["Kmer"].tolist()
disGraphs = df["Connected components"].tolist()

# print kmer[28]
# print disGraphs[28]

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
},image='png')
# ,image='png')
