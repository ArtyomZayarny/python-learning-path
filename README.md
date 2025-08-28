# 🐍 Learning Path → ML → Fullstack → SaaS

Repository for learning and building a project with a custom ML model.  
Goal — go from Python basics to a monetizable full-stack product.

---

## 📌 Structure

```
01_basics/        # Python basics (text parser, mini game)
02_data/          # Data analysis (pandas, matplotlib)
03_algorithms/    # Algorithms & data structures
04_ml/            # Scikit-learn (regression, classification)
05_dl/            # PyTorch/TensorFlow (neural nets)
06_backend/       # FastAPI, database
07_frontend/      # React / HTML+JS
08_deploy/        # Docker, CI/CD, deployment
demo/             # Screenshots, videos, GIFs for README
```

---

## 🚀 Live Demo

Your projects are now live and ready to play!

- 🎮 **Number Guessing Game:** [Play Now!](https://python-learning-path-1.onrender.com/)

  - Web-based number guessing game with beautiful UI
  - Choose difficulty: Easy (10 attempts) or Hard (5 attempts)
  - Real-time feedback and session management
  - Built with Flask and deployed on Render

- 📊 **CSV Analytics:** (coming soon)
- 🤖 **ML API (FastAPI):** (coming soon)
- 🌐 **Frontend:** (coming soon)
- 🎥 **Video Demo:** (coming soon)

---

## 🔧 Installation & Run

### Local Development

```bash
git clone https://github.com/ArtyomZayarny/python-learning-path.git
cd learning-path
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

### Deploy on Render

1. **Fork or clone** this repository to your GitHub account
2. **Sign up** for a free account at [render.com](https://render.com)
3. **Create a new Web Service** and connect your GitHub repository
4. **Configure the service:**
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Environment:** Python 3
5. **Deploy!** Your game will be available at a Render URL

**✅ Live Demo:** [Number Guessing Game](https://python-learning-path-1.onrender.com/) - Successfully deployed!

---

## 📂 Mini Projects

### 1. Basics (01_basics)

- **Text Parser**: analyze `.txt` files, count word frequencies, n-grams.  
  Run:

  ```bash
  python 01_basics/text_parser/main.py --top 20 data/
  ```

- **Mini Game (console)**: simple console game (Hangman, Bulls and Cows, etc.).  
  Run:

  ```bash
  python 01_basics/game/main.py
  ```

- **Number Guessing Game**: Web-based number guessing game with Flask.  
  **Live Demo:** [Play Now!](https://python-learning-path-1.onrender.com/)  
  Run:

  ```bash
  # Console version
  python guess_number_game/main.py

  # Web version
  cd guess_number_game && python app.py
  # Then open http://localhost:5000 in your browser
  ```

---

### 2. Data Analysis (02_data)

- **CSV Sales Analyzer**: process CSV sales data, generate reports, build charts.  
  Run:

  ```bash
  python 02_data/sales_report/main.py --out report.xlsx
  ```

- **JSON Parser**: load JSON data (weather, currency, etc.), normalize into a table, plot results.  
  Run:
  ```bash
  python 02_data/json_parser/main.py data/input.json
  ```

---

### 3. Algorithms & Data Structures (03_algorithms)

- **Phone Book CLI**: CRUD contacts, save to JSON/CSV, implement search.  
  Run:

  ```bash
  python 03_algorithms/phonebook/main.py
  ```

- **Brackets Validator & Calculator**: check if brackets are balanced, evaluate simple math expressions.  
  Run:
  ```bash
  python 03_algorithms/validator/main.py "(2*(3+5))"
  ```

---

### 4. Machine Learning (04_ml)

- **Housing Price Prediction**: regression using scikit-learn.  
  Run:

  ```bash
  python 04_ml/housing/train.py
  python 04_ml/housing/predict.py --features sample.json
  ```

- **Spam Classifier**: text classification with TfidfVectorizer + Logistic Regression.  
  Run:
  ```bash
  python 04_ml/spam/train.py
  python 04_ml/spam/predict.py --text "Hello, you won a prize!"
  ```

---

### 5. Deep Learning (05_dl)

- **MNIST CNN**: classify handwritten digits with PyTorch/TensorFlow.  
  Run:

  ```bash
  python 05_dl/mnist/train.py
  python 05_dl/mnist/infer.py data/image.png
  ```

- **Sentiment Classifier**: classify text reviews (positive/negative).  
  Run:
  ```bash
  python 05_dl/sentiment/train.py
  python 05_dl/sentiment/predict.py --text "I love this product"
  ```

---

### 6. Backend (06_backend)

- **Model Serving API**: FastAPI service with `/predict`, `/health`, `/feedback` endpoints.  
  Run:

  ```bash
  uvicorn 06_backend.main:app --reload
  ```

- **CRUD Service**: manage users, projects, predictions with SQLAlchemy + Alembic.  
  Run:
  ```bash
  uvicorn 06_backend.main:app --reload
  ```

---

### 7. Frontend (07_frontend)

- **Basic Web UI**: HTML/JS form to send requests to API and display results.  
  Run:

  ```bash
  cd 07_frontend/basic
  open index.html
  ```

- **React UI**: React + Tailwind interface for authentication, predictions, and reports.  
  Run:
  ```bash
  cd 07_frontend/react
  npm install
  npm run dev
  ```

---

### 8. Deploy (08_deploy)

- **Docker Setup**: build and run Docker containers for backend/frontend.  
  Run:

  ```bash
  docker-compose up --build
  ```

- **CI/CD Pipeline**: GitHub Actions for linting, testing, and deployment (config in `.github/workflows/ci.yml`).

---

## ✅ Progress

- [x] **Python Basics**

  - [x] Console number guessing game (`guess_number_game/main.py`)
  - [x] Web-based Flask application (`guess_number_game/flask_app.py`)
  - [ ] Text Parser
  - [ ] Project structure and organization

- [ ] **Data Analysis**

  - [ ] CSV Sales Analyzer
  - [ ] JSON Parser with data visualization
  - [ ] Pandas and matplotlib integration

- [ ] **Algorithms**

  - [ ] Phone Book CLI with CRUD operations
  - [ ] Brackets Validator & Calculator
  - [ ] Search algorithms implementation

- [ ] **ML**

  - [ ] Housing Price Prediction (regression)
  - [ ] Spam Classifier (classification)
  - [ ] Scikit-learn models and evaluation

- [ ] **DL**

  - [ ] MNIST CNN for digit classification
  - [ ] Sentiment Classifier for text analysis
  - [ ] PyTorch/TensorFlow implementation

- [ ] **Backend**

  - [ ] FastAPI model serving API
  - [ ] CRUD service with SQLAlchemy
  - [ ] Database integration and migrations

- [ ] **Frontend**

  - [ ] Basic HTML/JS web interface
  - [ ] React UI with Tailwind CSS
  - [ ] User authentication and dashboard

- [x] **Deploy**

  - [x] Render deployment configuration (`render.yaml`)
  - [x] Production server setup (Gunicorn)
  - [x] Live demo: [Number Guessing Game](https://python-learning-path-1.onrender.com/)
  - [ ] Docker containerization
  - [ ] CI/CD pipeline with GitHub Actions

- [ ] **Monetization**
  - [ ] User subscription system
  - [ ] Payment integration
  - [ ] Analytics and user tracking

---

## 📜 License

MIT
