# Pose Perfect

Pose Perfect is an interactive web application designed to guide users' postures during exercises. The application leverages advanced machine learning techniques and computer vision to provide real-time feedback on exercise form.

## Technology Stack

- **Frontend**: React.js
- **Backend**: Python, Django
- **API**: REST API
- **Machine Learning**: CNN, TensorFlow, OpenCV, MediaPipe
- **Database**: SQLite

## Key Features

- User Authentication (Login/Signup)
- User Profile Management
- Exercise Details and History
- Real-time Pose Estimation
- Feedback on Exercise Posture

## Key Responsibilities

- Developed 5 REST APIs for Login, Signup, User Profile, and Exercise Details.
- Created database schema for various tables to manage data.
- Used in-memory cache to ensure API responses are below 500ms.
- Managed user authentication through JWT tokens and ensured prevention from CSRF attacks.
- Implemented real-time pose estimation by detecting key points using MediaPipe and then analyzing them using a CNN model to assess the correctness of joint angles.

## Installation

### Prerequisites

- Python 3.8+
- Node.js 14+
- npm 6+
- SQLite

### Backend Setup

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/pose-perfect.git
    cd pose-perfect/backend
    ```

2. **Create a virtual environment and activate it**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the migrations**:
    ```bash
    python manage.py migrate
    ```

5. **Start the Django development server**:
    ```bash
    python manage.py runserver
    ```

### Frontend Setup

1. **Navigate to the frontend directory**:
    ```bash
    cd ../frontend
    ```

2. **Install the dependencies**:
    ```bash
    npm install
    ```

3. **Start the React development server**:
    ```bash
    npm start
    ```

## API Endpoints

### Authentication

- **Login**: `/api/login/`  
  **Method**: POST  
  **Description**: Authenticates a user and returns a JWT token.  
  **Payload**: 
  ```json
  {
    "username": "example",
    "password": "password"
  }
  ```

- **Signup**: `/api/signup/`  
  **Method**: POST  
  **Description**: Registers a new user.  
  **Payload**: 
  ```json
  {
    "username": "example",
    "password": "password",
    "email": "email@example.com"
  }
  ```

### User Profile

- **Get Profile**: `/api/profile/`  
  **Method**: GET  
  **Description**: Retrieves the profile information of the authenticated user.

- **Update Profile**: `/api/profile/`  
  **Method**: PUT  
  **Description**: Updates the profile information of the authenticated user.  
  **Payload**: 
  ```json
  {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
  }
  ```

### Exercise Details

- **Get Exercise Details**: `/api/exercise/`  
  **Method**: GET  
  **Description**: Retrieves exercise details for the authenticated user.

## Database Schema

- **User**:
  - `id` (Primary Key)
  - `username` (Unique)
  - `password`
  - `email`
  - `first_name`
  - `last_name`
  - `created_at`
  - `updated_at`

- **Exercise**:
  - `id` (Primary Key)
  - `user_id` (Foreign Key)
  - `exercise_name`
  - `exercise_date`
  - `duration`
  - `calories_burned`
  - `created_at`
  - `updated_at`

## In-Memory Caching

- Implemented in-memory caching to ensure API response times are below 500ms using Django's caching framework.

## User Authentication and Security

- Managed user authentication through JWT tokens.
- Ensured CSRF protection by implementing CSRF tokens and securing API endpoints.

## Real-Time Pose Estimation

- Utilized MediaPipe for detecting key points in real-time.
- Analyzed the detected key points using a Convolutional Neural Network (CNN) model to assess the correctness of joint angles and provide feedback on exercise posture.

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [your-email@example.com](mailto:your-email@example.com).

---

This README file provides a comprehensive overview of the Pose Perfect project, its setup, and key functionalities. For further details, please refer to the project documentation and source code.
