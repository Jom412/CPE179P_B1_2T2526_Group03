# 🛂 Identity Document Processing Pipeline with Vector Embeddings using Google ADK

An intelligent, 3-tier architecture system designed to automate the extraction of structured data from identity documents (Passports, Driver's Licenses, etc.) and perform semantic deduplication using Vector Search.

Powered by the **Google Agent Development Kit (ADK)** and the **Gemini API**.

---

## 👥 Core Development Team

- **Jomari Angelo Tamson** ([@Jom412](https://github.com/Jom412))
- **Gemry Somido** ([@GemrySomido](https://github.com/GemrySomido))
- **Jose Enrique Viloria** ([@VIJeno](https://github.com/VIJeno))

---

## 🚀 Key Features

- **Automated Data Extraction**  
  Utilizes Gemini Multimodal (and optionally EasyOCR) to accurately read names, ID numbers, and expiry dates from uploaded document images.

- **Vector-Based Deduplication**  
  Converts extracted identity data into mathematical embeddings. Uses Cosine Similarity to cross-reference against a Vector Database, instantly flagging potential duplicates or fraudulent records.

- **Document Validation**  
  Built-in logic tools to check document validity (e.g., verifying if the ID is expired).

- **Audit Logging & Analytics**  
  Maintains a persistent, secure history of all verification requests, extraction confidence scores, and deduplication match percentages.

---

## 🛠️ Technology Stack

- **Logic/Agent Tier**: Google Agent Development Kit (ADK), Gemini 1.5/2.5 Flash  
- **Data Extraction**: EasyOCR (Hybrid Local Processing), Google Cloud Vision (Alternative)  
- **Data Tier**: Vertex AI Vector Search (or local FAISS for testing), SQLite/PostgreSQL (Audit Logs)  
- **Application Server**: Python, FastAPI  

---

## 📂 Project Structure

```text
GoogleADKProject/
│
├── id_agent/                   # Google ADK Agent Directory
│   ├── __init__.py
│   ├── agent.py                # Core agent logic and tool definitions
│   └── requirements.txt        # Agent-specific dependencies
│
├── api/                        # FastAPI Backend (Integration Tier)
│   ├── main.py
│   └── database.py             # Audit logging and vector simulation
│
├── ui/                         # Presentation Tier (Frontend)
│   └── app.js / app.py         # Dashboard for uploading IDs
│
├── data/                       # Synthetic test data and vector indexes
├── .env                        # Environment variables (API Keys)
└── README.md
```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Jom412/CPE179P_B1_2T2526_Group03
cd CPE179P_B1_2T2526_Group03

```

### 2. Set Up a Virtual Environment (Recommended)

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r id_agent/requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory and add your Google Gemini API Key:

```plaintext
GOOGLE_API_KEY=your_gemini_api_key_here
```

---

## 🏃‍♂️ Running the System (Local Agent Test)

To run the core extraction and deduplication agent via the terminal using the ADK:

```bash
adk run id_agent
```

Once the chat interface initializes, you can test the extraction tools by providing an image path or text prompt.
