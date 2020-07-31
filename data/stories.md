## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Delhi"}
    - slot{"cuisine": "american"}
    - slot{"location": "Delhi"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mail_check": "yes", "mailId": "gauravgahlot299@gmail.com"}
    - slot{"mailId": "gauravgahlot299@gmail.com"}
    - slot{"mail_check": "yes"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "kolkata"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "kolkata"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mail_check": "yes", "mailId": "tak.ashuma@gmail.com"}
    - slot{"mailId": "tak.ashuma@gmail.com"}
    - slot{"mail_check": "yes"}
    - send_email
* goodbye{"goodbye": "bye"}
    - utter_goodbye

## interactive_story_3
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kalkattam"}
    - slot{"location": "Kalkattam"}
    - check_location
    - slot{"location_check": "no"}
    - utter_loc_dont_operate
* restaurant_search{"cuisine": "chinese", "location": "kolkata"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolkata"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
    - utter_goodbye

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "pune"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "pune"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
    - utter_goodbye

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "Kozhikode"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Kozhikode"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
    - utter_goodbye

## interactive_story_6
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - check_location
    - slot{"location_check": "no"}
    - utter_loc_dont_operate
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
    - utter_goodbye

## interactive_story_7
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
    - utter_goodbye

## interactive_story_8
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Kozhikode"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Kozhikode"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
    - utter_goodbye
	
## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "hyderabad"}
    - slot{"location": "hyderabad"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes", "mailId": "girijagahlot@gmail.com"}
    - slot{"mailId": "girijagahlot@gmail.com"}
    - slot{"mail_check": "yes"}
    - send_email
* affirm
    - utter_goodbye
	
## interactive_story_10
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
	- utter_goodbye
	
## interactive_story_11
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "abc@gmail.com"}
    - slot{"mailId": "abc@gmail.com"}
    - send_email
* affirm
    - utter_goodbye
	
## interactive_story_12
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "Mumbai"}
    - slot{"cuisine": "american"}
    - slot{"location": "Mumbai"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes", "mailId": "saurabh1599@gmail.com"}
    - slot{"mailId": "saurabh1599@gmail.com"}
    - slot{"mail_check": "yes"}
    - send_email
* goodbye{"goodbye": "bye"}
    - utter_goodbye
	
## interactive_story_13
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "Jaipur"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Jaipur"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
	- utter_goodbye
	
## interactive_story_14
* greet
    - utter_greet
* restaurant_search{"location": "Banga"}
    - slot{"location": "Banga"}
    - check_location
    - slot{"location_check": "no"}
    - utter_loc_dont_operate
* restaurant_search{"cuisine": "chinese", "location": "Bangalore"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Bangalore"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "gagahlot@microsoft.com"}
    - slot{"mailId": "gagahlot@microsoft.com"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_15
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mail_check": "yes", "mailId": "ahbcdj@dkj.com"}
    - slot{"mailId": "ahbcdj@dkj.com"}
    - slot{"mail_check": "yes"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_16
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mail_check": "yes", "mailId": "saurabh1599@gmail.com"}
    - slot{"mailId": "saurabh1599@gmail.com"}
    - slot{"mail_check": "yes"}
    - send_email
* affirm
    - utter_goodbye
    
## interactive_story_17
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Goa"}
    - slot{"location": "Goa"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
    - utter_goodbye

## interactive_story_18
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "gahlot@gmail.com"}
    - slot{"mailId": "gahlot@gmail.com"}
    - send_email
* affirm{"affirm": "thnx"}
    - utter_goodbye

## interactive_story_19
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "jodhpur"}
    - slot{"cuisine": "american"}
    - slot{"location": "jodhpur"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
    - utter_goodbye

## interactive_story_20
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_location
* restaurant_search{"location": "gulbarga"}
    - slot{"location": "gulbarga"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* affirm
    - utter_goodbye

## interactive_story_21
* greet
    - utter_greet
* restaurant_search{"location": "gublam"}
    - slot{"location": "gublam"}
    - check_location
    - slot{"location_check": "no"}
    - utter_loc_dont_operate
* restaurant_search{"cuisine": "mexican", "location": "gulbarga"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "gulbarga"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* restaurant_search{"cuisine": "italian", "location": "Vadodara"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Vadodara"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "gauravgahlot299new@gmail.com"}
    - slot{"mailId": "gauravgahlot299new@gmail.com"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_22
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "gunta"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "gunta"}
    - check_location
    - slot{"location_check": "no"}
    - utter_loc_dont_operate
* restaurant_search{"location": "guntur"}
    - slot{"location": "guntur"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* restaurant_search{"location": "gulbarga"}
    - slot{"location": "gulbarga"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* restaurant_search{"location": "guntur", "price": "Lesser than Rs. 300"}
    - slot{"location": "guntur"}
    - slot{"price": "Lesser than Rs. 300"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
    - utter_goodbye

## interactive_story_23
* greet
    - utter_greet
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes", "mailId": "gauravgahlot299new@gmail.com"}
    - slot{"mailId": "gauravgahlot299new@gmail.com"}
    - slot{"mail_check": "yes"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_24
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "erode"}
    - slot{"location": "erode"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "gauravgahlot299new@gmail.com"}
    - slot{"mailId": "gauravgahlot299new@gmail.com"}
    - send_email
* affirm{"affirm": "thnx"}
    - utter_goodbye

## interactive_story_25
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - check_location
    - slot{"location_check": "no"}
    - utter_loc_dont_operate
* restaurant_search{"location": "dhanbad"}
    - slot{"location": "dhanbad"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes", "mailId": "gauravgahlot299new@gmail.com"}
    - slot{"mailId": "gauravgahlot299new@gmail.com"}
    - slot{"mail_check": "yes"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_26
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* affirm
    - utter_goodbye

## interactive_story_27
* greet
    - utter_greet
* restaurant_search{"location": "Hubli-Dharwad"}
    - slot{"location": "Hubli-Dharwad"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes", "mailId": "saurabh1599@gmail.com"}
    - slot{"mailId": "saurabh1599@gmail.com"}
    - slot{"mail_check": "yes"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_28
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bilaspur"}
    - slot{"location": "bilaspur"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "southindian"}
    - slot{"cuisine": "southindian"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "saurabh1599@gmail.com"}
    - slot{"mailId": "saurabh1599@gmail.com"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_29
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "erode"}
    - slot{"location": "erode"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
    - utter_goodbye

## interactive_story_30
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "erode"}
    - slot{"location": "erode"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
    - utter_goodbye

## interactive_story_31
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "erode", "price": "More than 700"}
    - slot{"cuisine": "american"}
    - slot{"location": "erode"}
    - slot{"price": "More than 700"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "saurabh1599@gmail.com"}
    - slot{"mailId": "saurabh1599@gmail.com"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_32
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "faridabad"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "faridabad"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
    - utter_goodbye

## interactive_story_33
* greet
    - utter_greet
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_ask_location
* restaurant_search{"location": "Kurnool"}
    - slot{"location": "Kurnool"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "saurabh1599@gmail.com"}
    - slot{"mailId": "saurabh1599@gmail.com"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_34
* greet
    - utter_greet
* restaurant_search{"location": "Raipur"}
    - slot{"location": "Raipur"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
    - utter_goodbye

## interactive_story_35
* greet
    - utter_greet
* restaurant_search{"location": "Purulia"}
    - slot{"location": "Purulia"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "saurabh1599@gmail.com"}
    - slot{"mailId": "saurabh1599@gmail.com"}
    - send_email
* affirm
    - utter_goodbye
	
## interactive_story_36
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
	- utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "gaurav@gmail.com"}
    - slot{"mailId": "gaurav@gmail.com"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_37
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
	- utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes", "mailId": "abc@gmail.com"}
    - slot{"mailId": "abc@gmail.com"}
    - slot{"mail_check": "yes"}
    - send_email
* goodbye
    - utter_goodbye

## interactive_story_38
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "fabfub"}
    - slot{"mailId": "fabfub"}
    - send_email
* email{"mailId": "saurabh1599@gmail.com"}
    - slot{"mailId": "saurabh1599@gmail.com"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_39
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "fabfub"}
    - slot{"mailId": "fabfub"}
    - send_email
* email{"mailId": "abc@gmail.com"}
    - slot{"mailId": "abc@gmail.com"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_40
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* affirm
    - utter_goodbye

## interactive_story_41
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* affirm
    - utter_goodbye

## interactive_story_42
* greet
    - utter_greet
* restaurant_search{"location": "erode"}
    - slot{"location": "erode"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes", "mailId": "bvuobe"}
    - slot{"mailId": "bvuobe"}
    - slot{"mail_check": "yes"}
    - send_email
* email{"mailId": "saurabh1599@gmail.com"}
    - slot{"mailId": "saurabh1599@gmail.com"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_43
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* affirm
    - utter_goodbye

## interactive_story_44
* greet
    - utter_greet
* restaurant_search{"location": "Hubli-Dharwad", "price": "Lesser than Rs. 300"}
    - slot{"location": "Hubli-Dharwad"}
    - slot{"price": "Lesser than Rs. 300"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mailId": "abc@xyz.com"}
    - slot{"mailId": "abc@xyz.com"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_45
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Hubli-Dharwad", "price": "Lesser than Rs. 300"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Hubli-Dharwad"}
    - slot{"price": "Lesser than Rs. 300"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* affirm
    - utter_goodbye

## interactive_story_46
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "erode", "price": "More than 700"}
    - slot{"cuisine": "american"}
    - slot{"location": "erode"}
    - slot{"price": "More than 700"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes", "mailId": "abc@ggg.com"}
    - slot{"mailId": "abc@ggg.com"}
    - slot{"mail_check": "yes"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_47
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "gurgaon", "price": "Lesser than Rs. 300"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "gurgaon"}
    - slot{"price": "Lesser than Rs. 300"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* affirm
    - utter_goodbye

## interactive_story_48
* greet
    - utter_greet
* restaurant_search{"cuisine": "american", "location": "bilaspur", "price": "Lesser than Rs. 300"}
    - slot{"cuisine": "american"}
    - slot{"location": "bilaspur"}
    - slot{"price": "Lesser than Rs. 300"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes", "mailId": "abc@xyz.com"}
    - slot{"mailId": "abc@xyz.com"}
    - slot{"mail_check": "yes"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_49
* greet
    - utter_greet
* restaurant_search{"location": "Delhi", "price": "Lesser than Rs. 300"}
    - slot{"location": "Delhi"}
    - slot{"price": "Lesser than Rs. 300"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* goodbye
    - utter_goodbye

## interactive_story_50
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "price": "Rs. 300 to 700"}
    - slot{"cuisine": "mexican"}
    - slot{"price": "Rs. 300 to 700"}
    - utter_ask_location
* restaurant_search{"location": "Kozhikode"}
    - slot{"location": "Kozhikode"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* goodbye
    - utter_goodbye

## interactive_story_51
* greet
    - utter_greet
* restaurant_search{"location": "Vasai-Virar City"}
    - slot{"location": "Vasai-Virar City"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* affirm
    - utter_goodbye

## interactive_story_52
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "Delhi", "price": "More than 700"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Delhi"}
    - slot{"price": "More than 700"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "jddk.2jmd@kdl.co.in"}
    - slot{"mailId": "jddk.2jmd@kdl.co.in"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_53
* greet
    - utter_greet
* restaurant_search{"location": "Delhi", "price": "More than 700"}
    - slot{"location": "Delhi"}
    - slot{"price": "More than 700"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "jddk.2jmd@kdl.co.in"}
    - slot{"mailId": "jddk.2jmd@kdl.co.in"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_54
* greet
    - utter_greet
* restaurant_search{"location": "Delhi", "price": "More than 700"}
    - slot{"location": "Delhi"}
    - slot{"price": "More than 700"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "jddk.2jmd@kdl.co.in"}
    - slot{"mailId": "jddk.2jmd@kdl.co.in"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_55
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "bilaspur", "price": "Lesser than Rs. 300"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "bilaspur"}
    - slot{"price": "Lesser than Rs. 300"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "abc@sth.edu"}
    - slot{"mailId": "abc@sth.edu"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_56
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Vellore", "price": "Lesser than Rs. 300"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Vellore"}
    - slot{"price": "Lesser than Rs. 300"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "bcibqiuwb@abfwucb.gov"}
    - slot{"mailId": "bcibqiuwb@abfwucb.gov"}
    - send_email
* affirm
    - utter_goodbye

## interactive_story_57
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "firozabad"}
    - slot{"location": "firozabad"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "Rs. 300 to 700"}
    - slot{"price": "Rs. 300 to 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": false}
* affirm
    - utter_goodbye

## interactive_story_58
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Gorakhpur"}
    - slot{"location": "Gorakhpur"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than Rs. 300"}
    - slot{"price": "Lesser than Rs. 300"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "no"}
    - slot{"mail_check": "no"}
    - utter_goodbye

## interactive_story_59
* greet
    - utter_greet
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - check_location
    - slot{"location_check": "yes"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "More than 700"}
    - slot{"price": "More than 700"}
    - utter_search_restaurant
    - action_search_restaurants
    - slot{"is_more_than_0": true}
    - utter_ask_to_email
* email{"mail_check": "yes"}
    - slot{"mail_check": "yes"}
    - utter_ask_mail_id
* email{"mailId": "saurabh1599@gmail.com"}
    - slot{"mailId": "saurabh1599@gmail.com"}
    - send_email
* affirm
    - utter_goodbye
