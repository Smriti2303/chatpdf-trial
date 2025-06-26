@echo off
echo Starting Ollama with LLaMA3...
start "" /B cmd /C "ollama run llama3"

echo Waiting for Ollama to start...
timeout /t 5 >nul

echo Starting Streamlit app...
streamlit run app.py

pause
