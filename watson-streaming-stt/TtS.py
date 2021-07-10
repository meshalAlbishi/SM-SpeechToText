from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson import TextToSpeechV1

authenticator = IAMAuthenticator('ZfX_AEuhqo8dr_UaPENMfZN9U0bMtTQqo_akCwoXv77v')
TtS = TextToSpeechV1(authenticator=authenticator)
TtS.set_service_url('https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/cc673f78-ff77-4611-bebe-b3273416fca5')
    
with open('output/output.txt', 'r') as f:
        text = f.readlines()

text = [line.replace('\n','') for line in text]
text = ''.join(str(line) for line in text)
print(text)

with open('output/output.mp3', 'wb') as audio_file:
    res = TtS.synthesize(text, accept='audio/mp3', voice='en-GB_JamesV3Voice').get_result()
    audio_file.write(res.content)  
