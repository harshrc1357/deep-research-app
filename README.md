# 🔍 Deep Research - Multi-Agent AI Research Platform

An intelligent, autonomous research system that leverages multiple AI agents to conduct comprehensive web research, synthesize findings, and generate detailed reports. Built with OpenAI's Agents SDK and deployed on Streamlit.

**Live Demo**: [Your Streamlit App URL](https://deep-research-app.streamlit.app/)

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=for-the-badge&logo=openai&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## ✨ Features

- **🤖 Multi-Agent Architecture**: Four specialized AI agents working in coordination
- **🔍 Intelligent Search Planning**: Automatically generates optimal search queries
- **⚡ Parallel Web Search**: Concurrent execution for faster research
- **📝 Comprehensive Reports**: Generates detailed 1000+ word markdown reports
- **📧 Automated Email Delivery**: Sends formatted reports via SendGrid
- **🌐 Web Interface**: Clean, intuitive Streamlit UI
- **📊 Full Traceability**: OpenAI trace integration for debugging and monitoring

## 🏗️ Architecture

The system uses a **multi-agent orchestration pattern** with four specialized agents:

### 1. **Planner Agent** (`planner_agent.py`)
- Analyzes research queries
- Generates optimal search strategies
- Outputs structured search plans using Pydantic models

### 2. **Search Agent** (`search_agent.py`)
- Performs web searches using OpenAI's WebSearchTool
- Summarizes search results concisely
- Captures essential information for report synthesis

### 3. **Writer Agent** (`writer_agent.py`)
- Synthesizes research findings
- Generates comprehensive markdown reports (1000+ words)
- Creates structured outputs with summaries and follow-up questions

### 4. **Email Agent** (`email_agent.py`)
- Formats reports as HTML
- Sends emails via SendGrid API
- Handles email delivery automation

### **Research Manager** (`research_manager.py`)
Orchestrates the entire workflow:
1. Plans searches based on query
2. Executes parallel web searches
3. Synthesizes findings into a report
4. Sends report via email

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Framework**: OpenAI Agents SDK (`openai-agents`)
- **LLM**: GPT-4o-mini
- **Web Search**: OpenAI WebSearchTool
- **Email Service**: SendGrid
- **Data Validation**: Pydantic
- **Async Processing**: Python asyncio

## 📋 Prerequisites

- Python 3.12+
- OpenAI API key
- SendGrid API key (for email functionality)
- Git (for deployment)

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd deep_research
```

### 2. Install Dependencies

Using `uv` (recommended):
```bash
uv pip install -r requirements.txt
```

Or using `pip`:
```bash
pip install -r requirements.txt
```

### 3. Set Up Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=sk-your-openai-api-key-here
SENDGRID_API_KEY=SG.your-sendgrid-api-key-here
```

**Note**: For deployed apps, use Streamlit Secrets (see Deployment section).

## 💻 Local Development

### Run the Streamlit App

```bash
streamlit run app.py
```

Or with `uv`:
```bash
uv run streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

### Usage

1. Enter your research query in the text input
2. Click "Run Research" or press Enter
3. Wait for the agents to complete their workflow
4. View the generated report in the app
5. Check your email for the formatted report

## 🌐 Deployment

This app is deployed on **Streamlit Community Cloud** (free tier).

### Quick Deployment Steps

1. **Push to GitHub** (public repository required for free tier)
2. **Deploy on Streamlit Cloud**:
   - Go to https://share.streamlit.io
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Set Main file: `app.py`
   - Deploy!

3. **Add Secrets**:
   - Go to App Settings → Secrets
   - Add your API keys:
   ```toml
   OPENAI_API_KEY = "sk-your-key"
   SENDGRID_API_KEY = "SG.your-key"
   ```

📖 **Detailed deployment guide**: See [DEPLOYMENT_GUIDE.md](./DEPLOYMENT_GUIDE.md)

## 📁 Project Structure

```
deep_research/
├── app.py                  # Main Streamlit application
├── research_manager.py     # Orchestrates multi-agent workflow
├── planner_agent.py        # Plans search strategies
├── search_agent.py         # Performs web searches
├── writer_agent.py         # Generates reports
├── email_agent.py          # Handles email delivery
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore rules
├── README.md              # This file
├── DEPLOYMENT_GUIDE.md    # Detailed deployment instructions
└── QUICK_START.md         # Quick reference guide
```

## 🔑 API Keys Required

### OpenAI API Key
- Get yours at: https://platform.openai.com/api-keys
- Used for: LLM agents, web search tool
- **Cost**: Pay-per-use (see OpenAI pricing)

### SendGrid API Key
- Get yours at: https://app.sendgrid.com/settings/api_keys
- Used for: Email delivery
- **Cost**: Free tier available (100 emails/day)

## 🎯 Example Usage

**Input Query:**
```
Latest AI Agent frameworks in 2025
```

**Output:**
- Comprehensive markdown report (1000+ words)
- Short summary
- Follow-up research questions
- Email with formatted HTML report

## 🔍 How It Works

1. **Query Analysis**: Planner agent breaks down the query into search strategies
2. **Parallel Search**: Multiple web searches execute concurrently
3. **Synthesis**: Writer agent combines findings into a cohesive report
4. **Delivery**: Email agent formats and sends the report

All steps are traceable via OpenAI's trace system for debugging and monitoring.

## 🐛 Troubleshooting

### Import Errors
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Check that `agents` package is available (may need to install from parent directory)

### API Key Errors
- Verify keys are set in `.env` (local) or Streamlit Secrets (deployed)
- Check key format and permissions

### Blank Screen
- Check Streamlit logs for errors
- Verify all files are in the correct directory
- Ensure `app.py` is the entry point

### Search Failures
- Check OpenAI API quota and billing
- Verify WebSearchTool is enabled in your OpenAI account
- Review trace logs at https://platform.openai.com/traces

## 📊 Performance

- **Search Planning**: ~2-5 seconds
- **Web Searches**: ~10-30 seconds (parallel execution)
- **Report Generation**: ~15-45 seconds
- **Email Delivery**: ~2-5 seconds
- **Total Time**: ~30-90 seconds per research query

## 🔒 Security

- API keys are stored securely using Streamlit Secrets (deployed) or `.env` (local)
- Never commit secrets to version control
- `.gitignore` excludes sensitive files

## 🤝 Contributing

This is a learning project. Feel free to fork and experiment!

## 🙏 Acknowledgments

- Built using OpenAI's Agents SDK
- Deployed on Streamlit Community Cloud
- Inspired by multi-agent research patterns


---


