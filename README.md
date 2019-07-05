# MainProject
Final year project

Whenever faced with unchartered territories humans have a tendency to get anxious and it is but natural and even more so in the case of students who are about to join a new course. They are always filled with endless queries and mostly all of them are similar across people. Rather than flooding a single person with all those and to answer them over and over again, it is apt to segregate usual common queries and their solutions at a single place which is easily accessible by all. In this project the detailed design of a chatbot is given which provides an efficient and accurate answer for any query based on the data set of FAQs. This chatbot can be used by Sree Chitra Thirunal College Of Engineering to answer frequently asked questions to curious students in an interactive fashion.

Technology :
Python3 - Version 3.6.5 was used to carry out the project.
Flask - The version used in implementing the project is 1.0.2
Chat Interface - The chatbot is to be embedded in the official website of the college which is www.sctce.ac.in

Working :
Download all files
Save engine.py, SCTdataset.json, test_response.py, trainer.py in a file named DNN_chatbot
Save chatbot_config.py, new.py, server.py, server_thread.py,test_client.py in a file named servers
Save DNN_chatbot and servers to a file named project

To run on system, steps are
1. Open terminal
2. Change directory to where the files are saved
3. Change directory to DNN_chatbt
4. Run using commands : python3 trainer.py
5. Change to servers and run using command : python3 server.py
6. Open a new terminal and run : python3 test_client.py

To run on website, steps are
1. Open terminal
2. Change directory to where the files are saved
3. Change directory to servers and run using command : python3 new.py
4. The IP obtained has to be copy pasted on to any browser and press enter
5. Try the bot

The files contain :
report : all written content regarding project
output : all screenshots of project output
DNN_chatbot : chatbot training and backend code (intermediate files not included)
servers : server and client files (intermediate files not included)
virtual_assistant : complete project files along with the last checkpoint saved (intermediate files also included)
