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

## 🚀 Demo (placeholders)

Add demo links or screenshots here once available.

- 📊 **CSV Analytics:** (coming soon)
- 🎮 **Mini Game (console):** (coming soon)
- 🤖 **ML API (FastAPI):** (coming soon)
- 🌐 **Frontend:** (coming soon)
- 🎥 **Video Demo:** (coming soon)

---

## 🔧 Installation & Run

```bash
git clone https://github.com/ArtyomZayarny/python-learning-path.git
cd learning-path
python -m venv venv
source venv/bin/activate  # (Windows: venv\Scripts\activate)
pip install -r requirements.txt
```

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

- [x] Python Basics
- [ ] Data Analysis
- [ ] Algorithms
- [ ] ML
- [ ] DL
- [ ] Backend
- [ ] Frontend
- [ ] Deploy
- [ ] Monetization

---

## 📜 License

MIT
