# Calorie Counter with Diet Tracker API

Project (backend) with documentation is hosted on [heroku]( https://caloriecounterapi.herokuapp.com)  
Frontend is hosted on [netlify](https://canthin.netlify.app)  

**Frontend Repository**: <https://github.com/DamiDavy/DietTracker>

### Distinctiveness and Complexity

This is a project that creates an API for a single page application. And the SPA is for keeping track of the diet throughout the day and throughout the months.

It is implemented on **Django REST framework** using ViewSets and Routers.

Authentication and storing user session are provided with token generated by **knox**.

### Functionality

**Authorized and unauthorized users** can find out calorie and nutrient content of foods which can be found by taping in search input or by category. They also may collect food basket in which the calorie content is summed up. And the last thing is opportunity to find out their recommended calorie intake. 

**Authorized users** can collect and save their food baskets binding a specific day. They can change day basket content any time. For example, during a day and watch what they have already eaten to keep track of the diet throughout the day. After saving they get the opportunity to watch a food diary as calendar. Every day is colored depending on the ratio of daily calories consumed to the recommended intake. Clicking on a day in calendar opens this day basket. And finally in order to have the opportunity to get the calorie ratio, users should count and save their recommended calorie intake. Which they always can update in case of changes in weight or physical activity.

Registration is available [here](https://canthin.netlify.app/app/register).  
Or.  
Here are my credentials for [log in](https://canthin.netlify.app/app/login):  
login – dami  
password - MrPresident14?6.  

### Technologies

Frontend: React, Redux, Webpack, SASS  
Backend: Django REST framework, knox
