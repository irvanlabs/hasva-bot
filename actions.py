# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.action import FormAction
#from rasa_sdk.events import SlotSet

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

# class FeedbackForm(FormAction):
# 	def feedback(self):
# 		return "feedback_form"

# 	@staticmethod
# 	def required_slots(tracker):
# 		return ['feedback', 'negative_feedback_reason']

# class ActionCollegeRecommendation(object):
# 	"""docstring for CollegeRecommendation"""
# 	def name(self) -> Text:
# 		return "action_college_recommendations"

# 	def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

# 	stage_1 = tracker.get_slot('quiz_stage_1')
# 	stage_2 = tracker.get_slot('quiz_stage_2')
# 	stage_3 = tracker.get_slot('quiz_stage_3')
# 	stage_4 = tracker.get_slot('quiz_stage_4')

# 	return


class ActionCareer(Action):
	
	def name(self):
		return "action_career"

	def run(self, dispatcher, tracker, domain):
		raw_data = tracker.get_slot('prodi')
		prodi = raw_data.replace(" ", "_").lower()
		#f = open("log.txt", "w+")
		#f.write(raw_data)
		#f.close()
		#print(prodi)
		if not prodi:
		 	dispatcher.utter_message("Program studi tidak diketahui")

		dispatcher.utter_message(template=f"utter_career_{prodi}")
		return []
