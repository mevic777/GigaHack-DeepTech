from flask import Flask, render_template,request

import requests
import json

# Begining of GPT part
import openai
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

def response(msg):
   openai.api_key = "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"

   personality = """
		You are a Biomedical Research AI Agent named docky with the experience of a well seasoned medical professional. Your job is to help researchers in the biomedical field by answering their questions which have to do with medicine and only medicine. You help facilitate advanced medical research. You help researchers stay updated by extracting relevant information. You give correct, verbose, comprehensive, accurate answers which are based on scientific literature and evidence. In your answers, you show mild enthusiasm and a high interest in helping out researchers. You always cite your sources from which you based your answers.
	"""





   url = "https://api.wisecube.ai/orpheus/graphql"
   messages = [ {"role": "system", "content":
					f'"{personality}"'} ]
   
   n = message
		
   payload = "{\"query\":\"query questionAnswer($query: String) {\\n  summaryInsights(engineID: \\\"23343\\\", searchInput: {query: $query, type: [QA]}) {\\n    data {\\n      __typename\\n      ... on QAInsight {\\n        question\\n        answers {\\n          answer\\n          document {\\n            id\\n            title\\n            abs\\n            source\\n            index_name\\n            __typename\\n          }\\n          took\\n          context\\n          statistics\\n          probability\\n          __typename\\n        }\\n        __typename\\n      }\\n    }\\n    __typename\\n  }\\n}\",\"variables\":{\"query\":\"%s\"}}" %(n)
   headers = {
		'Authorization': 'Bearer eyJraWQiOiJsXC91aDJkVlcwNURDRUlxejhZcmRPcEt0MDVBditMSGluTmlDMEZ0aUloaz0iLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiIzMDY0YzM1My03ODFmLTQ0OGEtYTIyZS02OTE1YjkxNmY4OGMiLCJpc3MiOiJodHRwczpcL1wvY29nbml0by1pZHAudXMtZWFzdC0yLmFtYXpvbmF3cy5jb21cL3VzLWVhc3QtMl9abHJZZXBkd2giLCJjbGllbnRfaWQiOiIxbWJnYWhwNnAzNmlpMWpjODUxb2xxZmhubSIsIm9yaWdpbl9qdGkiOiIwZDIxNTllZS04MGE1LTQ1Y2EtYjk2Ny0yYTk5ODgyYTE2NTYiLCJldmVudF9pZCI6ImViY2Q2YjM2LWU1YTAtNDYwZS05ZDQzLWMyZWFmOTEzMjczYyIsInRva2VuX3VzZSI6ImFjY2VzcyIsInNjb3BlIjoiYXdzLmNvZ25pdG8uc2lnbmluLnVzZXIuYWRtaW4iLCJhdXRoX3RpbWUiOjE2OTQyNzUzNjcsImV4cCI6MTY5NDM2MTc2NywiaWF0IjoxNjk0Mjc1MzY3LCJqdGkiOiIyNjcyZmJlMS03YjllLTQ3MjctOTU0OC1lM2M2ODg4MTQ4MTAiLCJ1c2VybmFtZSI6IjMwNjRjMzUzLTc4MWYtNDQ4YS1hMjJlLTY5MTViOTE2Zjg4YyJ9.ka9uYr8qRng20VsOM-qsBOEWeaCQ7ID1kCy_y4aqcSIPPa4MADrio32To15S22UVDsayppN79adhDtp57sZPkLAkRaiGh-uCfK4Q8Az2OMHdoZPZfBRKvPw_bLoCP9axP_TtEJYYinItpBR1HJA5qnhZl-sT2WXoUV78FBEFciBU0AfWCCHDsQoMRanobC6SiKqOUIXAoUSZjYPe4bBPTxi_ZlZHo-pHqJB_Lo06V7c_Xbjy03IpVPgOxImLN0A_Ob5paMHEa7Z-iCIpKPMcKtaSyhum6xo8fFYHlGKQI3qdjJ9Ylm_7xWGxw55TcNRkXCUdopH7ABlAgaOFUaZJFA',
		'Content-Type': 'application/json',
		'x-api-key': 'bPXtTm8CIU3vYqzYKFtYeaql9kFSgXsT5r47MSw5'
		}

   response = requests.request("POST", url, headers=headers, data=payload)
   s = response.text
   s = s.split('{')[5]
   s = s.split('"')[3]

   if "documents" in s or "document" in s and message:
			

      message = n
			
      messages.append(
					{"role": "user", "content": message},
				)
      chat = openai.ChatCompletion.create(
					model="gpt-3.5-turbo-0613", 
					messages=messages
				)
   else:
				
			#print("Wisecube: " + s)
			#print("----------------------------------------------------------")
			
		
         message = s
			
         messages.append(
					{"role": "user", "content": "simplify and make it shorter - "+ message},
				)
         chat = openai.ChatCompletion.create(
					model="ft:gpt-3.5-turbo-0613"
					, messages=messages
				)
         reply = chat.choices[0].message.content
		
         messages.append({"role": "assistant", "content": reply})

         return reply


@app.route('/chatroom')
def chatroom():
   msg=request.args['chat']

   reply = response(msg)

   return render_template('chatroom.html',reply='reply')


  