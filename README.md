**Visit http://venkatesh123.pythonanywhere.com/** <br><br><br>
  **Deploy on your Local Server :** 
   * update pip 
   >python -m pip install --update pip
   * create requirements.txt file type Django~=2.2.4 in it then run 
   >pip install -r requirements.text
   * install git in your desktop
   * create new folder and run
   >git init
   * now clone the repository
   >git clone https://github.com/shrvenk/food-recipes-web-app
   * open food-recipe-web-app
   >cd food-recipe-web-app
   * to start virtual environment 
   >...\food-food-recipe-web-app>myvenv\Scripts\activate
   * now run 
   >python manage.py runserver
   * run http://127.0.0.1:8000/ on your browser 
  <br><br><br><br>
  
  
  **Details about the web-app** :<br> 
    this web app has been made using Django Framework. Sqlite3 Relational DBMS has been used which is a default DBMS for django.
    To query the database django Queryset has been used. "fooddetail" model has been created which contains "author" as a ForeignKey     attribute which is primary key for inbuilt user model. "fooddetail" model contains fields : name ,description ,ingredients,steps,image .
    you have to install pillow which supports in accessing images
    >pip install pillow 
    Html, css and bootstrap has been used to design the frontend.
    I have made this site online by uploading it on pythonanywhere web hosting server.

  **Execution of the webapp**
 * This a web application that displays Food Recipes.
 * User can search for food recipes based on name or the ingredients used.
 
 ![](https://github.com/shrvenk/food-recipes-web-app/blob/master/Screenshot%20(479).png)
 
 * Once the user selects one of the recipes, it will show a new page where you will
   see images, description, ingredients and the steps related to the Recipe.
   
 * the account dropdown will show the sign in and create account tab. 
   after clicking on it it will take you to sign in or create account modal.
   
  ![](https://github.com/shrvenk/food-recipes-web-app/blob/master/Screenshot%20(473).png)
  
 * user has to create account with valid username,email id and password else it will show "invalid credentials" message.
 * the account dropdown will show "log out" after successful log in. 
 * after a successful log in you can add your own recipe by clicking on glyphicon plus symbol on navbar-right.
 
 ![](https://github.com/shrvenk/food-recipes-web-app/blob/master/Screenshot%20(475).png)
 
 * you can see all your recipes that you have uploaded by clicking on "my recipe" tag on navbar
 
 ![](https://github.com/shrvenk/food-recipes-web-app/blob/master/Screenshot%20(476).png)
 
 * after clicking on any of your own recipes you will see a glyphicon pencil button. by clicking on that
   you can edit your existing recipes.
   
   ![](https://github.com/shrvenk/food-recipes-web-app/blob/master/Screenshot%20(478).png)

