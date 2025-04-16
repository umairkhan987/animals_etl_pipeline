# 🐾 Animal ETL Pipeline

A lightweight Extract-Transform-Load (ETL) pipeline that fetches animal data from a local HTTP API, transforms specific fields, and uploads the data in batches to another endpoint.

---

## 🚀 Getting Started

### Step 1: Run the API Docker Container

1. **Download the Docker image**:  
   [Download Link](https://storage.googleapis.com/lp-dev-hiring/images/lp-programming-challenge-1-1625758668.tar.gz)

2. **Load the Docker image**:
   ```bash
   docker load -i lp-programming-challenge-1-1625758668.tar.gz
   ```

3. **Run the container on port 3123**:
   ```bash
   docker run --rm -p 3123:3123 -ti lp-programming-challenge-1
   ```

4. Open [http://localhost:3123](http://localhost:3123) to verify it’s running.

---

### Step 2: Clone the Repository

```bash
git clone https://github.com/your-username/animal-etl.git
cd animal-etl
```

---

### Step 3: Set Up the Environment

```bash
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

### Step 4: Configure Environment Variables

Create a `.env` file at the root of the project and add the following:

```
BASE_URL=http://localhost:3123
```

---

### Step 5: Run the ETL Pipeline

```bash
python main.py
```

---

## ✅ Testing

Run all unit tests with:

```bash
pytest
```

---

## 🧹 Linting

Run static analysis using flake8:

```bash
flake8 .
```

