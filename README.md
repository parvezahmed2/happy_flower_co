This project aims to develop a comprehensive flower sales website that 
facilitates the buying and selling of flowers. The website will have user-facing
features for creating flower listings, user registration and authentication,
placing orders, and viewing order history. Additionally, there will be admin-facing 
features for managing flowers and orders.

User-Facing Features:
1) Flower Listings:
Users can create flower listings with images, titles, descriptions, prices, and a "Buy Now" button.
Users can filter flowers based on category.
2) User Registration and Authentication:
Implement user registration, login, and logout system.
User registration will require email verification for account activation.
3) Placing Orders:
Users can place orders for flowers they want to purchase.
Upon placing an order, an email confirmation will be sent to the user.
Quantity of the ordered flower will be reduced by one.
Orders will have a default status of "Pending" upon submission.
4) Order History:
Users can access their order history.
Users can view the status of their orders.
5) Admin Dashboard:
    	A separate dashboard for the admin to manage flowers and orders.
6) Order Management:
Admin can view and manage all orders placed by users.
Admin can change the status of orders (e.g., from "Pending" to "Completed").
An email notification will be sent to the user upon order confirmation by the admin.




Technology Stack:
To implement this project, a combination of front-end and back-end technologies will be used. Here's a possible technology stack:
i)	Frontend: HTML5, CSS3, JavaScript, boostrap (for dynamic user interface)
ii)	Backend: Django (with MVT)
iii)	Database: MongoDB (for storing flower listings, user data, and orders) 
iv)	Email Service: Nodemailer (for sending email notifications) 
v)	Deployment: On Render  cloud platform

