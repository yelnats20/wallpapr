# Wallpaper Download Web App

This project aims to create a wallpaper download web app using Django for the backend and React for the frontend. The app will include a scraper to fetch wallpapers and store them in a Django model. The communication between Django and React will be facilitated through an API.

For each step, pick one and start, once completed we would mark it as completed with [x]

## To-Do List

### Django Backend

- [ ] **Set Up Django Project**
   - Create a new Django project.
   - Set up a virtual environment.
   - Install necessary dependencies using `requirements.txt`.

- [ ] **Create Django App**
   - Create a Django app for the wallpaper functionality.

- [ ] **Define Wallpaper Model**
   - Create a Django model to store wallpaper information (e.g., title, image URL, tags, created_date, slug).

- [ ] **Create Wallpaper Scraper**
   - Implement a scraper to fetch wallpapers from external sources.
   - Parse the data and save it to the Django model.

- [ ] **Configure Django REST Framework**
   - Install and configure Django REST Framework for API development.

- [ ] **Implement API Endpoints**
   - Create API endpoints for wallpaper retrieval, creation, and deletion.

- [ ] **Authentication and Authorization**
   - Implement authentication for API endpoints.
   - Set up appropriate permissions to ensure secure access.

- [ ] **Testing**
   - Write unit tests for the scraper and API endpoints.

### React Frontend

- [ ] **Set Up React App**
   - Create a new React app using Create React App.

- [ ] **Create Components**
   - Build React components for displaying wallpapers, search functionality, and a form for wallpaper upload (the form should be inactive for now).

- [ ] **Implement API Integration**
   - Connect the React frontend to the Django backend using the API.
   - Fetch and display wallpapers using API calls.

- [ ] **Implement Wallpaper Search**
   - Add a search feature to allow users to search for wallpapers based on tags or titles.

- [ ] **User Interface Styling**
   - Style the frontend for an appealing user interface using CSS or a styling library, make it look like instagram.

- [ ] **Error Handling and Loading States**
   - Implement error handling for API requests and loading states for better user experience.

- [ ] **Testing**
   - Write unit tests for React components, especially those handling API calls.

- [ ] **Optimization**
   - Optimize the React app for performance, considering lazy loading and image optimization.


## Future Features
Make A Mobile App walpaper app from the react project and add to play store and app store