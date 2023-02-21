# THE DJANGO EDGE
THIS PACKAGE WOULD HELP TO SHORTEN THE TIME IN CREATING A SIMPLE DJANGO APP USING AUTOMATION.

 - In your link tags.
	It would change this element from 
 `<link href="css/flaticon.css"  rel="stylesheet"/>`    
			    to
   ` <link href="{% static 'css/flaticon.css' %}"  rel="stylesheet"/>`
   
 - In your script tags.
	It would change this element from 
	`<script  src="js/main.js">
</script>`
	to
	`<script  src="{% static 'js/main.js' %}">
</script>`

 - In your hyperlink tags.
		 It would change this element from 
		 `<a href="/plans">Plans</a>`
			 to
			 `<a href="plans.html">Plans</a>`
	

 - In your image tags.
	It would change this element from 
	 `<img  alt="image"  src="shape/shape16.png"/>`
	 to
	 `<img  alt="image"  src="{% static 'shape/shape16.png' %}"/>`

It also automates the creation of the views.py and urls.py
