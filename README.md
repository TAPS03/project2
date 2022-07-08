# QA Project 2 - My generator project 

## Objectives

The aim of this project was to create a functioning application that would consist of four different services to run with one another to create a running app. Service 1 would talk or communicate with the rest of the three services and would run render templates. Service 2 and service 3 are bits of code that create random objects based on the options that were placed inside it. Service 4 would also create an object but wold use the objects from service 2 and 3 to create the third object, which then all go into the first service and be used further on.

In this project, a variety of different services have been used in order to make this project successful. The Kanban board choice of use is the Trello Board which helps me organise waht tasks i need to do and when. A risk assessment is also created to show different issues that could occur and how much it would impact the project. I have used Github as the version control and Jenkins as tbe CI server. To deploy the project, it must be containarised and orchestrated and for me to do that, I have used Ansible. And the project uses NGINX as the reverse Proxy. 

## Planning:

To plan my project, I have used Trello Board to create a list of actions that need to be done. This was very beneficial as it helped me keep track of what im doing and what i have left to do.

<p align= "centre">
        <img width="600" height="300" src="images/trello_1.PNG">

After the Planning has been made, a risk assessment was crutial to be carried out as I needed to know what could impact my project negatively. I have described the scenario that could occur along  with the impact level and who would be responsible for the result. Below I have displayed my risk assessment of my project...

<p align= "centre">
        <img width="600" height="300" src="images/risk.PNG">

## My app:

The application i have built is a random damage generator. From the different services, it generates a random gun and also a random body part and depending of the two, it will calculate the amount of damage you take.
 
My service 1 receives objects from the other services and then generates a render template and puts the values of the objects into it:

<p align= "centre">
        <img width="800" height="300" src="images/service_1.PNG">

My service 2 generates a random gun from a list I have created. The list is involving different types of guns: 

<p align= "centre">
        <img width="800" height="300" src="images/service_2.PNG">

My service 3 also generates an object but instead of a gun, it now generates a body part where the bullet will shoot. Below you can see the service 3 and what body parts i have included in the list:

<p align= "centre">
        <img width="800" height="300" src="images/service_3.PNG">

In my service 4, it would create the damage dealt from the objects that were generated and from the numbers I have assigned to each object, which would then calculate the resulting damage :

<p align= "centre">
        <img width="300" height="700" src="images/service_4.PNG">


When the app is run and everything has been generated, this is what the resulting web page will look like from a viewers point of view: 

<p align= "centre">
        <img width="400" height="300" src="images/result.PNG">

## Testing

Testing was crutial as it would check that everything was functional and that there arent any errors in the code. I had tests made from each of the four services and the coverage is 100% for each one of them. The results of the tests are shown below:

