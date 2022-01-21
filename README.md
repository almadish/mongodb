# AirBnB MongoDB Analysis

A little assignment to practice importing and analyzing data within a MongoDB database.

## Part 1: Data selection and import

### The data source

As the dataset, I chose San Francisco, California airbnb listings from [inside airbnb](http://insideairbnb.com/get-the-data.html).

The dataset was in zip format and I unpacked to get csv file. 

### Data scrubbing

As I started to clean the data I realised that everything was cleaned at the beginning. I started to clean it because the representation of the data in VS Code was terrible because data was moved and splitted in different lines. 

In order to get better representation of the data I wrote python code:
```
file = open("data/listings.csv", "r", encoding='utf_8')
csv_file = open("data/listings_clean.csv", "w", encoding='utf_8')

s = file.readline()
list_s = s.split(",")

while list_s[0] not in s:
    s = file.readline()

clean_s = ",".join(s.split()) + "\n"
csv_file.write(clean_s)

s = file.readline()
a = file.readline()

while True:
    if s != "":
        if s.split(",")[0].isnumeric() and a.split(",")[0].isnumeric():
            not_clean_lst = s.split()
            clean_s = " ".join(not_clean_lst) + "\n"
            csv_file.write(clean_s)
            s = file.readline()
            a = file.readline()
        else:
            s = file.readline()
            a = file.readline()
            continue
    else:
        break

csv_file.close()
```

Now as every entry in its place and every different entry has its own row I started Part 2.

## Part 2: Data analysis in MongoDB

1. Show exactly two documents from the `listings` collection in any order

```
db.listings.find().limit(2)

{ "_id" : ObjectId("61af0a0b051c47f3e688bce5"), "id" : 47682, "listing_url" : "https://www.airbnb.com/rooms/47682", "scrape_id" : NumberLong("20211102175524"), "last_scraped" : "2021-11-02", "name" : "One-bedroom apt. Lafayette Park", "description" : "<b>The space</b><br />Wonderfully located near the Park with Fillmore Street and Polk 
Street restaurants and stores nearby in an area of historic townhouses and mansions. This apartment faces the quiet rear gardens. It is accessed from an outside walkway 
with a locked gate and has its own exterior staircase. The bedroom , with a queen bed, is large with tall windows and a large walk-in closet. The kitchen has a dishwasher and table with 2 chairs. The living room has the same high ceilings found throughout the apartment. . There is a coin-operated washer and dryer in the basement.<br />Pacific Heights is a great neighborhood where people love to walk..<br />The apartment, which has not been renovated, is on a hill less than half a block from Lafayette Park . Whole Foods supermarket is three blocks away.<br />There are many bus lines within one to three block that take you to different parts of the City or perhaps you would prefer to walk to your destination from this centrally ", "neighborhood_overview" : "", "picture_url" : "https://a0.muscache.com/pictures/273479/60b3f9f5_original.jpg", "host_id" : 216682, "host_url" : "https://www.airbnb.com/users/show/216682", "host_name" : "Jay", "host_since" : "2010-08-29", "host_location" : "San Francisco, California, United States", "host_about" : "Originally from New York, I work in healthcare and enjoy the great food and diversity of SF.", "host_response_time" : "within a 
few hours", "host_response_rate" : "94%", "host_acceptance_rate" : "97%", "host_is_superhost" : "t", "host_thumbnail_url" : "https://a0.muscache.com/im/users/216682/profile_pic/1284924580/original.jpg?aki_policy=profile_small", "host_picture_url" : "https://a0.muscache.com/im/users/216682/profile_pic/1284924580/original.jpg?aki_policy=profile_x_medium", "host_neighbourhood" : "Pacific Heights", "host_listings_count" : 9, "host_total_listings_count" : 9, "host_verifications" : "['email', 'phone', 'reviews', 'offline_government_id', 'government_id']", "host_has_profile_pic" : "t", "host_identity_verified" : "t", "neighbourhood" : "", "neighbourhood_cleansed" : "Pacific 
Heights", "neighbourhood_group_cleansed" : "", "latitude" : 37.79186, "longitude" : -122.42429, "property_type" : "Entire rental unit", "room_type" : "Entire home/apt", 
"accommodates" : 2, "bathrooms" : "", "bathrooms_text" : "1 bath", "bedrooms" : 1, "beds" : 1, "amenities" : "[\"Microwave\", \"Carbon monoxide alarm\", \"Shampoo\", \"Hangers\", \"Luggage dropoff allowed\", \"Essentials\", \"Dedicated workspace\", \"Kitchen\", \"Hair dryer\", \"Dishes and silverware\", \"Stove\", \"Hot water\", \"Wifi\", \"Dishwasher\", \"Iron\", \"Host greets you\", \"Long term stays allowed\", \"Cooking basics\", \"Refrigerator\", \"Patio or balcony\", \"Smoke alarm\", \"Heating\", 
\"Oven\", \"Coffee maker\"]", "price" : "$119.00", "minimum_nights" : 30, "maximum_nights" : 365, "minimum_minimum_nights" : 30, "maximum_minimum_nights" : 30, "minimum_maximum_nights" : 365, "maximum_maximum_nights" : 365, "minimum_nights_avg_ntm" : 30, "maximum_nights_avg_ntm" : 365, "calendar_updated" : "", "has_availability" : "t", 
"availability_30" : 0, "availability_60" : 21, "availability_90" : 51, "availability_365" : 326, "calendar_last_scraped" : "2021-11-02", "number_of_reviews" : 30, "number_of_reviews_ltm" : 2, "number_of_reviews_l30d" : 0, "first_review" : "2010-11-14", "last_review" : "2021-05-27", "review_scores_rating" : 4.83, "review_scores_accuracy" : 4.76, "review_scores_cleanliness" : 4.71, "review_scores_checkin" : 5, "review_scores_communication" : 4.94, "review_scores_location" : 4.88, "review_scores_value" : 
4.82, "license" : "", "instant_bookable" : "f", "calculated_host_listings_count" : 9, "calculated_host_listings_count_entire_homes" : 4, "calculated_host_listings_count_private_rooms" : 5, "calculated_host_listings_count_shared_rooms" : 0, "reviews_per_month" : 0.22 }
{ "_id" : ObjectId("61af0a0b051c47f3e688bcdc"), "id" : 958, "listing_url" : "https://www.airbnb.com/rooms/958", "scrape_id" : NumberLong("20211102175524"), "last_scraped" : "2021-11-02", "name" : "Bright, Modern Garden Unit - 1BR/1BTH", "description" : "Please check local laws re Covid before you request a reservation.<br /><br />Our bright garden unit overlooks a grassy backyard area with fruit trees and native plants. It is an oasis in a big city. The apartment comfortably fits a couple or small family. It is located on a cul de sac street that ends at lovely Duboce Park.<br /><br /><b>The space</b><br />Newly remodeled, modern, and bright garden unit in historic Victorian home. <br /><br />New fixtures and finishes.<br />Zero VOC and non-toxic paint.<br />Organic and fair-trade teas, fresh local ground coffee.<br />Local art on walls.<br />Sofa bed and Queen bed are in the same room. More of a petite apartment with a separate room for dining and kitchen.<br /><br /><b>Guest access</b><br />Full access to patio and backyard (Shared)<br />Beautiful garden with fruit trees & native plants <br />Washer & dryer (Shared)<br />Children's toys<br />Charcoal grill<br /><br /><b>Other things to note</b><br />Due to the fact that we have chil", "neighborhood_overview" : "Quiet cul de sac in friendly neighborhood<br />Steps away from grassy park with 2 playgrounds and Recreational Center<br />Very family-friendly neighborhood<br />Quaint shops, grocery stores and restaurants all within a 5-10 minute walk", "picture_url" : "https://a0.muscache.com/pictures/b7c2a199-4c17-4ba6-b81d-751719d2dac6.jpg", "host_id" : 1169, "host_url" : "https://www.airbnb.com/users/show/1169", "host_name" : "Holly", "host_since" : "2008-07-31", "host_location" : "San Francisco, California, United States", "host_about" : "We are a family of four that live upstairs. We have a large dog who occasionally can be seen in the backyard. We have lived in our home since 2005 and have been renting our apartment since 2008.", "host_response_time" : "within an hour", "host_response_rate" : "100%", "host_acceptance_rate" : "92%", "host_is_superhost" : "t", "host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/efdad96a-3efc-4bc2-bdc9-f69740a5a818.jpg?aki_policy=profile_small", "host_picture_url" : "https://a0.muscache.com/im/pictures/user/efdad96a-3efc-4bc2-bdc9-f69740a5a818.jpg?aki_policy=profile_x_medium", "host_neighbourhood" : "Duboce Triangle", "host_listings_count" : 1, "host_total_listings_count" : 1, "host_verifications" : "['email', 'phone', 'facebook', 'reviews', 'kba']", "host_has_profile_pic" : "t", "host_identity_verified" : "t", "neighbourhood" : "San Francisco, California, United States", "neighbourhood_cleansed" : "Western Addition", "neighbourhood_group_cleansed" : "", "latitude" : 37.77028, "longitude" : -122.43317, "property_type" : "Entire serviced apartment", "room_type" : "Entire home/apt", "accommodates" : 3, "bathrooms" : "", "bathrooms_text" : "1 bath", "bedrooms" : 1, "beds" : 2, "amenities" : "[\"BBQ grill\", \"Outdoor furniture\", \"Free street parking\", \"Microwave\", \"Carbon monoxide alarm\", \"Cable TV\", \"Shampoo\", \"Hangers\", \"Room-darkening shades\", 
\"Private entrance\", \"Keypad\", \"TV with standard cable\", \"Essentials\", \"Dedicated workspace\", \"First aid kit\", \"Kitchen\", \"Backyard\", \"Hair dryer\", \"Pack \\u2019n play/Travel crib\", \"Dishes and silverware\", \"Stove\", \"Dryer\", \"Washer\", \"Hot water\", \"Wifi\", \"Iron\", \"Long term stays allowed\", \"Cooking basics\", \"Refrigerator\", \"Patio or balcony\", \"Smoke alarm\", \"Heating\", \"Oven\", \"Coffee maker\"]", "price" : "$161.00", "minimum_nights" : 2, "maximum_nights" : 30, "minimum_minimum_nights" : 2, "maximum_minimum_nights" : 2, "minimum_maximum_nights" : 1125, "maximum_maximum_nights" : 1125, "minimum_nights_avg_ntm" : 2, "maximum_nights_avg_ntm" : 1125, "calendar_updated" : "", "has_availability" : "t", "availability_30" : 7, "availability_60" : 7, "availability_90" : 10, "availability_365" : 139, "calendar_last_scraped" : "2021-11-02", "number_of_reviews" : 308, "number_of_reviews_ltm" : 42, "number_of_reviews_l30d" : 4, "first_review" : "2014-10-05", "last_review" : "2021-10-16", "review_scores_rating" : 4.87, "review_scores_accuracy" : 4.94, "review_scores_cleanliness" : 4.95, "review_scores_checkin" : 4.96, "review_scores_communication" : 4.9, "review_scores_location" : 4.98, "review_scores_value" : 4.78, "license" : "City Registration Pending", "instant_bookable" : "f", "calculated_host_listings_count" : 1, "calculated_host_listings_count_entire_homes" : 1, "calculated_host_listings_count_private_rooms" : 0, "calculated_host_listings_count_shared_rooms" : 0, "reviews_per_month" : 3.57 }
```

2. Show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the `pretty()` function.

```
db.listings.find().limit(10).pretty()

{
        "_id" : ObjectId("61af0a0b051c47f3e688bce5"),
        "id" : 47682,
        "listing_url" : "https://www.airbnb.com/rooms/47682",
        "scrape_id" : NumberLong("20211102175524"),
        "last_scraped" : "2021-11-02",
        "name" : "One-bedroom apt. Lafayette Park",
        "description" : "<b>The space</b><br />Wonderfully located near the Park with Fillmore Street and Polk Street restaurants and stores nearby in an area of historic townhouses and mansions. This apartment faces the quiet rear gardens. It is accessed from an outside walkway with a locked gate and has its own exterior staircase. The bedroom , with a queen bed, is large with tall windows and a large walk-in closet. The kitchen has a dishwasher and table with 2 chairs. The living room has the same high ceilings found throughout the apartment. . There is a coin-operated washer and dryer in the basement.<br />Pacific Heights is a great neighborhood where people love to walk..<br />The apartment, which has not been renovated, is on a hill less than half a block from Lafayette Park . Whole Foods supermarket is three blocks away.<br />There are many bus lines within one to three block that take you to different parts of the City or perhaps you would prefer to walk to your destination from this centrally ",
        "neighborhood_overview" : "",
        "picture_url" : "https://a0.muscache.com/pictures/273479/60b3f9f5_original.jpg",
        "host_id" : 216682,
        "host_url" : "https://www.airbnb.com/users/show/216682",
        "host_name" : "Jay",
        "host_since" : "2010-08-29",
        "host_location" : "San Francisco, California, United States",
        "host_about" : "Originally from New York, I work in healthcare and enjoy the great food and diversity of SF.",
        "host_response_time" : "within a few hours",
        "host_response_rate" : "94%",
        "host_acceptance_rate" : "97%",
        "host_is_superhost" : "t",
        "host_thumbnail_url" : "https://a0.muscache.com/im/users/216682/profile_pic/1284924580/original.jpg?aki_policy=profile_small",
        "host_picture_url" : "https://a0.muscache.com/im/users/216682/profile_pic/1284924580/original.jpg?aki_policy=profile_x_medium",
        "host_neighbourhood" : "Pacific Heights",
        "host_listings_count" : 9,
        "host_total_listings_count" : 9,
        "host_verifications" : "['email', 'phone', 'reviews', 'offline_government_id', 'government_id']",
        "host_has_profile_pic" : "t",
        "host_identity_verified" : "t",
        "neighbourhood" : "",
        "neighbourhood_cleansed" : "Pacific Heights",
        "neighbourhood_group_cleansed" : "",
        "latitude" : 37.79186,
        "longitude" : -122.42429,
        "property_type" : "Entire rental unit",
        "room_type" : "Entire home/apt",
        "accommodates" : 2,
        "bathrooms" : "",
        "bathrooms_text" : "1 bath",
        "bedrooms" : 1,
        "beds" : 1,
        "amenities" : "[\"Microwave\", \"Carbon monoxide alarm\", \"Shampoo\", \"Hangers\", \"Luggage dropoff allowed\", \"Essentials\", \"Dedicated workspace\", \"Kitchen\", \"Hair dryer\", \"Dishes and silverware\", \"Stove\", \"Hot water\", \"Wifi\", \"Dishwasher\", \"Iron\", \"Host greets you\", \"Long term stays allowed\", \"Cooking basics\", \"Refrigerator\", \"Patio or balcony\", \"Smoke alarm\", \"Heating\", \"Oven\", \"Coffee maker\"]",
        "price" : "$119.00",
        "minimum_nights" : 30,
        "maximum_nights" : 365,
        "minimum_minimum_nights" : 30,
        "maximum_minimum_nights" : 30,
        "minimum_maximum_nights" : 365,
        "maximum_maximum_nights" : 365,
        "minimum_nights_avg_ntm" : 30,
        "maximum_nights_avg_ntm" : 365,
        "calendar_updated" : "",
        "has_availability" : "t",
        "availability_30" : 0,
        "availability_60" : 21,
        "availability_90" : 51,
        "availability_365" : 326,
        "calendar_last_scraped" : "2021-11-02",
        "number_of_reviews" : 30,
        "number_of_reviews_ltm" : 2,
        "number_of_reviews_l30d" : 0,
        "first_review" : "2010-11-14",
        "last_review" : "2021-05-27",
        "review_scores_rating" : 4.83,
        "review_scores_accuracy" : 4.76,
        "review_scores_cleanliness" : 4.71,
        "review_scores_checkin" : 5,
        "review_scores_communication" : 4.94,
        "review_scores_location" : 4.88,
        "review_scores_value" : 4.82,
        "license" : "",
        "instant_bookable" : "f",
        "calculated_host_listings_count" : 9,
        "calculated_host_listings_count_entire_homes" : 4,
        "calculated_host_listings_count_private_rooms" : 5,
        "calculated_host_listings_count_shared_rooms" : 0,
        "reviews_per_month" : 0.22
}
{
        "_id" : ObjectId("61af0a0b051c47f3e688bcdc"),
        "id" : 958,
        "listing_url" : "https://www.airbnb.com/rooms/958",
        "scrape_id" : NumberLong("20211102175524"),
        "last_scraped" : "2021-11-02",
        "name" : "Bright, Modern Garden Unit - 1BR/1BTH",
        "description" : "Please check local laws re Covid before you request a reservation.<br /><br />Our bright garden unit overlooks a grassy backyard area with fruit trees and native plants. It is an oasis in a big city. The apartment comfortably fits a couple or small family. It is located on a cul de sac street that ends at lovely Duboce Park.<br /><br /><b>The space</b><br />Newly remodeled, modern, and bright garden unit in historic Victorian home. <br /><br />New fixtures and finishes.<br />Zero VOC and non-toxic paint.<br />Organic and fair-trade teas, fresh local ground coffee.<br />Local art on walls.<br />Sofa bed and Queen bed are in the same room. More 
of a petite apartment with a separate room for dining and kitchen.<br /><br /><b>Guest access</b><br />Full access to patio and backyard (Shared)<br />Beautiful garden with fruit trees & native plants <br />Washer & dryer (Shared)<br />Children's toys<br />Charcoal grill<br /><br /><b>Other things to note</b><br />Due to the fact that we have chil",
        "neighborhood_overview" : "Quiet cul de sac in friendly neighborhood<br />Steps away from grassy park with 2 playgrounds and Recreational Center<br />Very family-friendly neighborhood<br />Quaint shops, grocery stores and restaurants all within a 5-10 minute walk",
        "picture_url" : "https://a0.muscache.com/pictures/b7c2a199-4c17-4ba6-b81d-751719d2dac6.jpg",
        "host_id" : 1169,
        "host_url" : "https://www.airbnb.com/users/show/1169",
        "host_name" : "Holly",
        "host_since" : "2008-07-31",
        "host_location" : "San Francisco, California, United States",
        "host_about" : "We are a family of four that live upstairs. We have a large dog who occasionally can be seen in the backyard. We have lived in our home since 2005 and have been renting our apartment since 2008.",
        "host_response_time" : "within an hour",
        "host_response_rate" : "100%",
        "host_acceptance_rate" : "92%",
        "host_is_superhost" : "t",
        "host_thumbnail_url" : "https://a0.muscache.com/im/pictures/user/efdad96a-3efc-4bc2-bdc9-f69740a5a818.jpg?aki_policy=profile_small",
        "host_picture_url" : "https://a0.muscache.com/im/pictures/user/efdad96a-3efc-4bc2-bdc9-f69740a5a818.jpg?aki_policy=profile_x_medium",
        "host_neighbourhood" : "Duboce Triangle",
        "host_listings_count" : 1,
        "host_total_listings_count" : 1,
        "host_verifications" : "['email', 'phone', 'facebook', 'reviews', 'kba']",
        "host_has_profile_pic" : "t",
        "host_identity_verified" : "t",
        "neighbourhood" : "San Francisco, California, United States",
        "neighbourhood_cleansed" : "Western Addition",
        "neighbourhood_group_cleansed" : "",
        "latitude" : 37.77028,
        "longitude" : -122.43317,
        "property_type" : "Entire serviced apartment",
        "room_type" : "Entire home/apt",
        "accommodates" : 3,
        "bathrooms" : "",
        "bathrooms_text" : "1 bath",
        "bedrooms" : 1,
        "beds" : 2,
        "amenities" : "[\"BBQ grill\", \"Outdoor furniture\", \"Free street parking\", \"Microwave\", \"Carbon monoxide alarm\", \"Cable TV\", \"Shampoo\", \"Hangers\", 
\"Room-darkening shades\", \"Private entrance\", \"Keypad\", \"TV with standard cable\", \"Essentials\", \"Dedicated workspace\", \"First aid kit\", \"Kitchen\", \"Backyard\", \"Hair dryer\", \"Pack \\u2019n play/Travel crib\", \"Dishes and silverware\", \"Stove\", \"Dryer\", \"Washer\", \"Hot water\", \"Wifi\", \"Iron\", \"Long term stays allowed\", \"Cooking basics\", \"Refrigerator\", \"Patio or balcony\", \"Smoke alarm\", \"Heating\", \"Oven\", \"Coffee maker\"]",
        "price" : "$161.00",
        "minimum_nights" : 2,
        "maximum_nights" : 30,
        "minimum_minimum_nights" : 2,
        "maximum_minimum_nights" : 2,
        "minimum_maximum_nights" : 1125,
        "maximum_maximum_nights" : 1125,
        "minimum_nights_avg_ntm" : 2,
        "maximum_nights_avg_ntm" : 1125,
        "calendar_updated" : "",
        "has_availability" : "t",
        "availability_30" : 7,
        "availability_60" : 7,
        "availability_90" : 10,
        "availability_365" : 139,
        "calendar_last_scraped" : "2021-11-02",
        "number_of_reviews" : 308,
        "number_of_reviews_ltm" : 42,
        "number_of_reviews_l30d" : 4,
        "first_review" : "2014-10-05",
        "last_review" : "2021-10-16",
        "review_scores_rating" : 4.87,
        "review_scores_accuracy" : 4.94,
        "review_scores_cleanliness" : 4.95,
        "review_scores_checkin" : 4.96,
        "review_scores_communication" : 4.9,
        "review_scores_location" : 4.98,
        "review_scores_value" : 4.78,
        "license" : "City Registration Pending",
        "instant_bookable" : "f",
        "calculated_host_listings_count" : 1,
        "calculated_host_listings_count_entire_homes" : 1,
        "calculated_host_listings_count_private_rooms" : 0,
        "calculated_host_listings_count_shared_rooms" : 0,
        "reviews_per_month" : 3.57
}
{
        "_id" : ObjectId("61af0a0b051c47f3e688bcdd"),
        "id" : 10251,
        "listing_url" : "https://www.airbnb.com/rooms/10251",
        "scrape_id" : NumberLong("20211102175524"),
        "last_scraped" : "2021-11-02",
        "name" : "Victorian Suite in Inner Mission",
        "description" : "<b>The space</b><br />Please read this before you book!<br />Second floor Suite, fully furnished with lovely colors and furniture throughout. The suite is a section of our Victorian home reserved for our guests' exclusive use. <br />Sleeps up to 6: Queen bed, trundle bed (makes two singles), and sofa bed.<br /><br />Features: <br />* Hardwood floors and Victorian details throughout * Working fireplace * *High ceilings and lots of natural light * Large open kitchen, dining & living area * New dishwasher, new stove, new refrigerator, fully stocked with kitchenware * Flat screen TV, wireless Internet * Master bedroom with queen bed and walk in closet * Second bedroom with trundle bed and small desk * Full bath with large tub * Beautiful garden* <br /><br />Rates: $4,000 per month<br />Cleaning fee of $100.<br />$500 Security deposit required, payable through Airbnb. It will be returned within 48 hours of guest's departure, provided there is no damage, abuse, breakage, or missing items. <",
        "neighborhood_overview" : "Neighborhood is safe, sunny, lively and fun. Mission and 24th Streets provide many excellent and unique restaurants as well as groceries and parks. Walk to 24th St. for some tacos, Salvadorian pupusas, coffee or a healthy juice. Walking distance to Mission Street and Valencia corridor. Just a short walk to beautiful Dolores Park. Close to highways 101 and 280; 1 block to MUNI bus line and 10 blocks to BART trains. <br />It is definitely a much better experience than staying in a hotel!!",
        "picture_url" : "https://a0.muscache.com/pictures/30649314/ed09487a_original.jpg",
        "host_id" : 35199,
        "host_url" : "https://www.airbnb.com/users/show/35199",
        "host_name" : "Roman & Sarah",
        "host_since" : "2009-08-31",
        "host_location" : "San Francisco, California, United States",
        "host_about" : "Coming from SF.",
        "host_response_time" : "within an hour",
        "host_response_rate" : "80%",
        "host_acceptance_rate" : "100%",
        "host_is_superhost" : "f",
        "host_thumbnail_url" : "https://a0.muscache.com/im/users/35199/profile_pic/1286322568/original.jpg?aki_policy=profile_small",
        "host_picture_url" : "https://a0.muscache.com/im/users/35199/profile_pic/1286322568/original.jpg?aki_policy=profile_x_medium",
        "host_neighbourhood" : "Mission District",
        "host_listings_count" : 1,
        "host_total_listings_count" : 1,
        "host_verifications" : "['email', 'phone', 'facebook', 'reviews', 'kba']",
        "host_has_profile_pic" : "t",
        "host_identity_verified" : "t",
        "neighbourhood" : "San Francisco, California, United States",
        "neighbourhood_cleansed" : "Mission",
        "neighbourhood_group_cleansed" : "",
        "latitude" : 37.75831,
        "longitude" : -122.41386,
        "property_type" : "Entire residential home",
        "room_type" : "Entire home/apt",
        "accommodates" : 4,
        "bathrooms" : "",
        "bathrooms_text" : "1 bath",
        "bedrooms" : 2,
        "beds" : 3,
        "amenities" : "[\"BBQ grill\", \"Outdoor furniture\", \"Free street parking\", \"Microwave\", \"Carbon monoxide alarm\", \"Indoor fireplace\", \"Bathtub\", \"Shampoo\", \"Hangers\", \"Cable TV\", \"Private entrance\", \"Luggage dropoff allowed\", \"TV with standard cable\", \"Essentials\", \"Dedicated workspace\", \"First aid kit\", \"Kitchen\", \"Backyard\", \"Hair dryer\", \"Dishes and silverware\", \"Stove\", \"Dryer\", \"Lockbox\", \"Washer\", \"Hot water\", \"Wifi\", \"Dishwasher\", \"Iron\", \"Long term stays allowed\", \"Cooking basics\", \"Refrigerator\", \"Patio or balcony\", \"Smoke alarm\", \"Heating\", \"Oven\", \"Coffee maker\", \"High chair\"]", 
        "price" : "$150.00",
        "minimum_nights" : 30,
        "maximum_nights" : 60,
        "minimum_minimum_nights" : 30,
        "maximum_minimum_nights" : 30,
        "minimum_maximum_nights" : 60,
        "maximum_maximum_nights" : 60,
        "minimum_nights_avg_ntm" : 30,
        "maximum_nights_avg_ntm" : 60,
        "calendar_updated" : "",
        "has_availability" : "t",
        "availability_30" : 19,
        "availability_60" : 49,
        "availability_90" : 79,
        "availability_365" : 354,
        "calendar_last_scraped" : "2021-11-02",
        "number_of_reviews" : 340,
        "number_of_reviews_ltm" : 3,
        "number_of_reviews_l30d" : 1,
        "first_review" : "2012-04-12",
        "last_review" : "2021-10-09",
        "review_scores_rating" : 4.79,
        "review_scores_accuracy" : 4.89,
        "review_scores_cleanliness" : 4.93,
        "review_scores_checkin" : 4.82,
        "review_scores_communication" : 4.76,
        "review_scores_location" : 4.56,
        "review_scores_value" : 4.65,
        "license" : "STR-0001558",
        "instant_bookable" : "f",
        "calculated_host_listings_count" : 1,
        "calculated_host_listings_count_entire_homes" : 1,
        "calculated_host_listings_count_private_rooms" : 0,
        "calculated_host_listings_count_shared_rooms" : 0,
        "reviews_per_month" : 2.92
}

```

3. Choose two hosts (by reffering to their `host_id` values) who are superhosts (available in the `host_is_superhost` field), and show all of the listings offered by both of the two hosts
   - only show the `name`, `price`, `neighbourhood`, `host_name`, and `host_is_superhost` for each result

```
let host1 = {$and: [{"host_name":"Peter"},{"host_is_superhost":"t"}]};
let host2 = {$and: [{"host_name":"Jay"},{"host_is_superhost":"t"}]};
let criteria = {"_id":0, "name":1,"price":1,"neighborhood_cleansed":1,"host_name":1,"host_is_superhost":1};

db.listings.find(host1,criteria);

{ "name" : "Spacious Quiet SF Downtown Retreat", "host_name" : "Peter", "host_is_superhost" : "t", "price" : "$149.00" }
{ "name" : "Sweeping Views and Dolores Park Pad", "host_name" : "Peter", "host_is_superhost" : "t", "price" : "$116.00" }
{ "name" : "The Haven - SF Marina", "host_name" : "Peter", "host_is_superhost" : "t", "price" : "$359.00" }

db.listings.find(host2,criteria);

{ "name" : "One-bedroom apt. Lafayette Park", "host_name" : "Jay", "host_is_superhost" : "t", "price" : "$119.00" }
{ "name" : "Prime Location - Large Private Room", "host_name" : "Jay", "host_is_superhost" : "t", "price" : "$47.00" }
{ "name" : "Prime Location Bright Private Room", "host_name" : "Jay", "host_is_superhost" : "t", "price" : "$49.00" }
```

4. Find all the unique `host_name` values (see [the docs](https://docs.mongodb.com/manual/reference/method/db.collection.distinct/))

```
db.listings.distinct("host_name")

[
        "",
        "1906 Mission",
        "Aaron",
        "Abel",
        "Abhi",
        "Ada",
        "Adam",
        "Aditi",
        "Ahmad",
        "Ahmed",
        "Aimee",
        "Aj",
        ...
]
```

5. Find all of the places that have more than 2 `beds` in a neighborhood of your choice (referred to as either the `neighborhood` or `neighbourhood_group_cleansed` fields in the data file), ordered by `review_scores_rating` descending
   - only show the `name`, `beds`, `review_scores_rating`, and `price`
   - if your data set only has blanks for all the neighborhood-related fields, or only one neighborhood value in all documents, you may pick another field to filter by - include an explanation and justification for this in your report.
   - if you run out of memory for this query, try filtering `review_scores_rating` that aren't empty (`$ne`); and lastly, if there's still an issue, you can set the `beds` to match exactly 2.

```
let query = {"beds":{$gt:2}, "neighbourhood_cleansed":"Pacific Heights"};
let filtering = {"_id":0,"name":1,"beds":1,"neighborhood":1,"review_scores_rating":1,"price":1};
db.listings.find(query,filtering).sort({"review_scores_rating":-1})

{ "name" : "Historic Pac Heights - month to month rental", "beds" : 7, "price" : "$800.00", "review_scores_rating" : "" }
{ "name" : "REMODELING? PACIFIC HEIGHTS SPACIOUS FAMILY CONDO", "beds" : 3, "price" : "$450.00", "review_scores_rating" : "" }
{ "name" : "Elegant Cow Hollow/Pacific Heights Work/Live Flat", "beds" : 3, "price" : "$298.00", "review_scores_rating" : "" }
```

6. Show the number of listings per host

```
db.listings.aggregate([{$group: {_id: "$host_name",listingCount: {$sum: 1}}}])

{ "_id" : "Sheri", "listingCount" : 4 }
{ "_id" : "Avlok", "listingCount" : 4 }
{ "_id" : "Patty", "listingCount" : 4 }
```

7. Find the average `review_scores_rating` per neighborhood, and only show the ones above a `95`, sorted in descending order of rating (see [the docs](https://docs.mongodb.com/manual/reference/operator/aggregation/sort/))
   - if your data set only has blanks in the neighborhood-related fields, or only one neighborhood value in all documents, you may pick another field to break down the listings by - include an explanation and justification for this in your report.

```
let average = {$group: {_id: "$neighbourhood_cleansed",average_rating:{$avg:"$review_scores_rating"}}};
let match95 = {$match: {"average_rating":{$gt: 4}}};
db.listings.aggregate([average,match95])
{ "_id" : "Crocker Amazon", "average_rating" : 4.695 }
{ "_id" : "Visitacion Valley", "average_rating" : 4.764 }
{ "_id" : "Seacliff", "average_rating" : 5 }
{ "_id" : "Diamond Heights", "average_rating" : 4.758 }
```

## Extra Credit

### Recreate analyses

This assignment deserves extra credit because I reproduced the query (which I did in using mongodb initially) using the python. Moreover, I ran it and it worked. 

Reproduce one of your earlier queries:

- find all of the places that have more than 2 `beds` in a neighborhood of your choosing, ordered by `review_scores_rating` descending
- only show the `name`, `beds`, `review_scores_rating`, and `price`
- note that in `pymongo`, you'll have to quote all of your keys.

```
import pymongo
connection = pymongo.MongoClient("class-mongodb.cims.nyu.edu", 27017,
                                username="as12936",
                                password="B7JhKLyR",
                                authSource="as12936")
collection = connection["as12936"]["listings"]

docs = collection.find()

for i in docs:
    if i.get("beds") != "":
        if (i.get("neighbourhood_cleansed") == "Pacific Heights" and float(i.get("beds"))>float(2)):
            print(str(i.get("name")) + "," + str(i.get("beds")) + "," + str(i.get("neighbourhood_cleansed")) + "," + str(i.get("review_scores_rating")) + "," + str(i.get("price")))
```
