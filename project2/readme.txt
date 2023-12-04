Product Mission:
"Empowering scooter and skateboard commuters with the safest and most convenient routes, ensuring every ride is smooth and every destination accessible."
Functions：
①Route Planning
As a scooter user, I want the app to show me the most scooter-friendly route from my current location to my destination, so I can avoid rough surfaces and get there quickly.Use Google Maps Directions API with the walking mode as a base, as it will generally offer paths more suitable for scooters.
②Surface Quality Alerts
 As a scooter user, I want to be alerted about upcoming uneven surfaces or holes, so I can slow down or avoid them. While the API doesn't directly provide surface quality, user-generated data can be mapped onto Google Maps using the Places API, and alerts can be generated for other users passing through those coordinates.
Crowd Density Information
 As a commuter, I want to avoid crowded places, especially during peak hours, ensuring a smoother ride. When there are a lot of pedestrians on the road, it is usually very annoying and difficult to move through. Sometimes I even have to stop, and try to push my heavy scooter with my hands. Google Maps provides popular times for many public places, indicating crowd density. This can be combined with the Directions API to route around such places during their peak times.
③Parking & Decking Spots
As a scooter user, when I reach my destination, I want to find the nearest parking or decking spot, so I don't have to carry my scooter around.Google Places API can be used to find and list parking spots near the destination.
④User Feedback & Reporting
As a user, I want to report uneven surfaces, holes, or new parking spots, so the community can benefit from real-time updates. Google API Utilization: User-generated markers can be added using the Google Maps JavaScript API, and Places API can be used to submit new 
⑤Safety Features
As a skateboarder, in case of a fall or collision, I want an emergency contact to be alerted.
While not directly linked to Google APIs, the user's location can be sent via Google Maps URL for pinpoint accuracy to the emergency contact.



