# Drone-Gemini-3-15Flash
Drone detection using Gemini-3-15Flash from a Python program. Based on tests performed until the free trial was exhausted, it could be considered a zero-failures version.

Installation:
Install the official Google Gen AI and Pydantic SDKs, which we will use to define the exact detection structure:

pip install google-genai pydantic pillow

A requirements.txt file is included.

Obtain the Google API key at:

https://aistudio.google.com/api-keys?project=gen-lang-client-0252907537

Click the "Create API key" button, and then on the next screen, click the "Create key" button again. Ignore the fields for project name and other information.


Copy the API key obtained on line 12 of the Test.py program.

Unpack the test files Test2.zip and Test1.zip.

Run the test program:

Test.py

The program displays the images one by one. To continue, close the image and press Enter.

By changing line 81 of the program, you can test any image folder.

Also, you can test the capabilities of Gemini-3-5-flash through this Roboflow page:

https://playground.roboflow.com/models/google/gemini-3-5-flash?utm_campaign=Newsletter+-+5%2F21%2F2026+-+%5Bcvpr%5D&utm_content=Newsletter+-5%2F21%2F2026+-+cvpr&utm_medium=email_action&utm_source=email


Also in:

https://gemini.google.com/app?is_sa=1&is_sa=1&android-min-version=301356232&ios-min-version=322.0&campaign_id=bkws&utm_source=sem&utm_medium=paid-media&utm_campaign=bkws&pt=9008&mt=8&ct=p-growth-sem-bkws&gclsrc=aw.ds&gad_source=1&gad_campaignid=21109724629&gbraid=0AAAAApk5BhmDjTo4XpkVXFQbsaie5ghxv&gclid=Cj0KCQjww8rQBhDjARIsAE43KPMA9JbdHp2L-u_sng5le5CmmfF_xD8iZdC8TANsiOOTQH4jgrF7ONoaAgiSEALw_wcB

The tests should look for unseen images instead of the usual ones that circulate, which could have been used in Gemini's training and could lead to overfitting.

