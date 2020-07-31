from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# import re

tier1_cities = ['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata' , 'Mumbai', 'Nilambur', 'Pune']
tier2_cities = ['Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly', 'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bilaspur', 'Bokaro Steel City', 'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur', 'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gwalior', 'Gurgaon', 'Guwahati', 'Hamirpur', 'Hubli-Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar', 'Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada', 'Kannur', 'Kanpur', 'Kochi', 'Kolhapur', 'Kollam', 'Kozhikode', 'Kurnool', 'Ludhiana', 'Lucknow', 'Madurai', 'Malappuram', 'Mathura', 'Goa', 'Mangalore', 'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Patna', 'Pondicherry', 'Purulia', 'Prayagraj', 'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli', 'Shimla', 'Siliguri', 'Solapur', 'Srinagar', 'Surat', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli', 'Tiruppur', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada', 'Visakhapatnam', 'Vellore', 'Warangal']

tier1_city_list = [x.lower() for x in tier1_cities]
tier2_city_list = [x.lower() for x in tier2_cities]



class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"d8e2a77ecb537bb8e8fe506b33f6ccae"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		priceRanges = []
		lessThan701 = False
		if price == "Lesser than Rs. 300":
			priceRanges = [i for i in range(0,300)]
			lessThan701 = True
		elif price == "Rs. 300 to 700":
			priceRanges = [i for i in range(300,701)]
			lessThan701 = True
		else:
			priceRanges = [i for i in range(300,701)]
			lessThan701 = False
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50)
		d = json.loads(results)
		response = ""
		is_more_than_0 = True
		if d['results_found'] == int(0):
			response = "Sorry, No results found for your criteria."
			is_more_than_0 = False
		else:
			final_results = {}
			for restaurant in d['restaurants']:
				if int(restaurant['restaurant']['average_cost_for_two']) in priceRanges and lessThan701 == True:
					rating = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
					if rating in final_results.keys():
						final_results[rating].append(restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address'] +" has been rated "+ str(rating)+ ". And the average price for two people here is: Rs "+ str(restaurant['restaurant']['average_cost_for_two']))
					else:
						temp = []
						temp.append(restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address'] +" has been rated "+ str(rating)+ ". And the average price for two people here is: Rs "+ str(restaurant['restaurant']['average_cost_for_two']))
						final_results[rating] = temp
				else:
					if int(restaurant['restaurant']['average_cost_for_two']) not in priceRanges and lessThan701 == False:
						rating = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
						if rating in final_results.keys():
							final_results[rating].append(restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address'] +" has been rated "+ str(rating)+ ". And the average price for two people here is: Rs "+ str(restaurant['restaurant']['average_cost_for_two']))
						else:
							temp = []
							temp.append(restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated "+ str(rating)+ ". And the average price for two people here is: Rs "+ str(restaurant['restaurant']['average_cost_for_two']))
							final_results[rating] = temp
						# response=response+ "Found 123"+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " for "+ str(restaurant['restaurant']['average_cost_for_two'])+"\n"
			l=list(final_results.items())
			l.sort(reverse=True) #sort in reverse order
					# listToStr = ' '.join([str(elem) for elem in l])
					# response = response + listToStr
			counter = 0
			done = False
			for (a,b) in l:
				if done == True:
					break
				for item in b:
					if done == True:
						break
					response=response+str(counter+1)+". "+item+"\n"
					counter = counter+1
					if counter == 5:
						done = True
			if len(final_results) == 0:
				response = "Sorry, No results found for your criteria."
				is_more_than_0 = False
			else:
				dispatcher.utter_message(str(counter) + " Restaurant(s) Found!!\n")
		dispatcher.utter_message(response)
		return [SlotSet('is_more_than_0',is_more_than_0)]		

class CheckLocation(Action):
	def name(self):
		return 'check_location'

	def run(self, dispatcher, tracker, domain):
		loc = tracker.get_slot('location')
		loc=str(loc)

		if loc.lower() not in tier1_city_list+tier2_city_list:
			return [SlotSet('location_check',"no")]
		else:
			# dispatcher.utter_message(loc)
			return [SlotSet('location_check',"yes")]

class SendEmail(Action):
	def name(self):
		return 'send_email'

	def run(self, dispatcher, tracker, domain):
		toSend = tracker.get_slot('mail_check')
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		price = tracker.get_slot('price')
		if toSend == "yes":
			mailId = tracker.get_slot('mailId')
			mail_content = '''Hello,
Here is the list of top 10 ''' + cuisine + ''' restaurants you asked for in ''' + loc + ''' for ''' + price + ':\n\n'
			config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
			zomato = zomatopy.initialize_app(config)
			loc = tracker.get_slot('location')
			cuisine = tracker.get_slot('cuisine')
			price = tracker.get_slot('price')
			priceRanges = []
			lessThan701 = False
			if price == "Lesser than Rs. 300":
				priceRanges = [i for i in range(0,300)]
				lessThan701 = True
			elif price == "Rs. 300 to 700":
				priceRanges = [i for i in range(300,701)]
				lessThan701 = True
			else:
				priceRanges = [i for i in range(300,701)]
				lessThan701 = False
			location_detail=zomato.get_location(loc, 1)
			d1 = json.loads(location_detail)
			lat=d1["location_suggestions"][0]["latitude"]
			lon=d1["location_suggestions"][0]["longitude"]
			cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
			results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 50)
			d = json.loads(results)
			if d['results_found'] == int(0):
				mail_content=mail_content+ "Sorry, No results found for your criteria."
			else:
				final_results = {}
				for restaurant in d['restaurants']:
					if int(restaurant['restaurant']['average_cost_for_two']) in priceRanges and lessThan701 == True:
						rating = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
						if rating in final_results.keys():
							final_results[rating].append("\nRestaurant Name: " + restaurant['restaurant']['name'] +
										"\nRestaurant locality address: " + restaurant['restaurant']['location']['address'] +
										"\nAverage budget for two people: Rs "+ str(restaurant['restaurant']['average_cost_for_two']) +
									    "\nZomato user rating: " + str(rating))
						else:
							temp = []
							temp.append("\nRestaurant Name: " + restaurant['restaurant']['name'] +
										"\nRestaurant locality address: " + restaurant['restaurant']['location']['address'] +
										"\nAverage budget for two people: Rs "+ str(restaurant['restaurant']['average_cost_for_two']) +
										"\nZomato user rating: " + str(rating))
							final_results[rating] = temp
					else:
						if int(restaurant['restaurant']['average_cost_for_two']) not in priceRanges and lessThan701 == False:
							rating = float(restaurant['restaurant']['user_rating']['aggregate_rating'])
							if rating in final_results.keys():
								final_results[rating].append("\nRestaurant Name: " + restaurant['restaurant']['name'] +
										"\nRestaurant locality address: " + restaurant['restaurant']['location']['address'] +
										"\nAverage budget for two people: Rs "+ str(restaurant['restaurant']['average_cost_for_two']) +
										"\nZomato user rating: " + str(rating))
							else:
								temp = []
								temp.append("\nRestaurant Name: " + restaurant['restaurant']['name'] +
										"\nRestaurant locality address: " + restaurant['restaurant']['location']['address'] +
										"\nAverage budget for two people: Rs "+ str(restaurant['restaurant']['average_cost_for_two']) +
										"\nZomato user rating: " + str(rating))
								final_results[rating] = temp
							# response=response+ "Found 123"+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+ " for "+ str(restaurant['restaurant']['average_cost_for_two'])+"\n"
				l=list(final_results.items())
				l.sort(reverse=True) #sort in reverse order
					# listToStr = ' '.join([str(elem) for elem in l])
					# response = response + listToStr
				counter = 0
				done = False
				for (a,b) in l:
					if done == True:
						break
					for item in b:
						if done == True:
							break
						mail_content=mail_content+str(counter+1)+". "+item+"\n\n"
						counter = counter+1
						if counter == 10:
							done = True
			mail_content = mail_content + "Enjoy your meal!!\n\nThank You,\nTeam Lunch Cherub"
			#The mail addresses and password
			sender_address = 'teamlunchcherub@gmail.com'
			sender_pass = 'GAURAVGAHLOT'
			receiver_address = mailId
			#Setup the MIME
			message = MIMEMultipart()
			message['From'] = sender_address
			message['To'] = receiver_address
			message['Subject'] = 'Top 10 Restaurant Search Results from "Team Lunch Cherub".'   #The subject line
			#The body and the attachments for the mail
			message.attach(MIMEText(mail_content, 'plain'))
			#Create SMTP session for sending the mail
			session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
			session.starttls() #enable security
			session.login(sender_address, sender_pass) #login with mail_id and password
			text = message.as_string()
			session.sendmail(sender_address, receiver_address, text)
			session.quit()
			dispatcher.utter_message("Email sent. Bon Appetit!")
		else:
			dispatcher.utter_message("Okay. Bon Appetit!")