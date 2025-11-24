import streamlit as st
import os
from research_manager import ResearchManager
import asyncio

# Load environment variables from Streamlit secrets (for deployment) or .env (for local)
try:
    # Try Streamlit secrets first (for deployed apps)
    if hasattr(st, 'secrets') and st.secrets:
        os.environ['OPENAI_API_KEY'] = st.secrets.get('OPENAI_API_KEY', os.environ.get('OPENAI_API_KEY', ''))
        os.environ['SENDGRID_API_KEY'] = st.secrets.get('SENDGRID_API_KEY', os.environ.get('SENDGRID_API_KEY', ''))
except:
    # Fallback to .env file for local development
    from dotenv import load_dotenv
    load_dotenv(override=True)

# Page configuration - must be first
st.set_page_config(
    page_title="Deep Research",
    page_icon="🔍",
    layout="wide"
)

# Title
st.title("🔍 Deep Research")
st.markdown("Enter a research query to generate a comprehensive report")

# Initialize session state
if "report_generated" not in st.session_state:
    st.session_state.report_generated = False
if "current_report" not in st.session_state:
    st.session_state.current_report = ""
if "status_text" not in st.session_state:
    st.session_state.status_text = ""

# Query input
query = st.text_input(
    "What topic would you like to research?",
    placeholder="e.g., Latest AI Agent frameworks in 2025",
    key="query_input"
)

# Run button
run_button = st.button("Run Research", type="primary", use_container_width=True)

# Status display area
if st.session_state.status_text:
    st.info(st.session_state.status_text)

# Report display area
if st.session_state.current_report:
    st.markdown("---")
    st.markdown("## Research Report")
    st.markdown(st.session_state.current_report)

async def run_research(query: str):
    """Run the research process and collect all chunks"""
    manager = ResearchManager()
    status_chunks = []
    report_text = ""
    
    try:
        async for chunk in manager.run(query):
            # Check if it's a status update or the final report
            if chunk.startswith("View trace:") or chunk.startswith("Searches planned") or \
               chunk.startswith("Searches complete") or chunk.startswith("Report written") or \
               chunk.startswith("Email sent"):
                status_chunks.append(chunk)
            else:
                # This is the final markdown report
                report_text = chunk
        
        return status_chunks, report_text
    except Exception as e:
        raise Exception(f"Research failed: {str(e)}")

# Handle button click
if run_button:
    if not query:
        st.warning("Please enter a research query")
    else:
        # Clear previous results
        st.session_state.report_generated = False
        st.session_state.current_report = ""
        st.session_state.status_text = ""
        
        # Run the async research
        with st.spinner("Running research... This may take a few minutes."):
            try:
                status_chunks, report = asyncio.run(run_research(query))
                
                # Update status
                if status_chunks:
                    status_text = "\n".join([f"✅ {chunk}" for chunk in status_chunks])
                    st.session_state.status_text = status_text
                
                # Update report
                if report:
                    st.session_state.current_report = report
                    st.session_state.report_generated = True
                    st.rerun()
                else:
                    st.error("No report was generated. Please try again.")
                    
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
                import traceback
                st.code(traceback.format_exc())