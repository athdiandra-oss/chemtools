# 🧪 ChemLab Mini Tools v2.0

An interactive chemistry learning platform built with Streamlit for students to learn dilution calculations, chemical reactions, and laboratory practices.

## ✨ Features

### 📊 Dashboard
- Track quiz performance and learning progress
- View accuracy statistics with visual charts
- Monitor activity across different learning modules

### 📐 Dilution Calculator
- Calculate unknown concentrations using the M₁V₁ = M₂V₂ formula
- Real-time visualizations of volume and concentration changes
- Practical guidance and step-by-step examples
- Calculation history tracking

### 🎮 Color Reaction Quiz
- Interactive chemistry quiz game
- Learn about chemical reactions and their color changes
- Score tracking and accuracy statistics
- Detailed explanations for each answer

### 🧠 Troubleshooting Guide
- Analyze common laboratory errors
- Get solutions and prevention tips
- Learn from practical lab scenarios

### 📚 Study Guides
- Comprehensive chemistry theory notes
- Laboratory best practices
- Common chemical reactions reference table

### 🎨 Dynamic Theming
Choose from 5 color themes:
- **Light** - Clean and minimalist
- **Dark** - Easy on the eyes
- **Ocean** - Calming blue tones
- **Forest** - Natural green palette
- **Sunset** - Warm color scheme

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/athdiandra-oss/chemtools.git
cd chemtools
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run streamlit_app.py
```

4. Open your browser and navigate to `http://localhost:8501`

## 📦 Dependencies

- **streamlit** - Web app framework
- **pandas** - Data manipulation
- **plotly** - Interactive visualizations

See `requirements.txt` for specific versions.

## 🎯 How to Use

1. **Select a feature** from the sidebar menu
2. **Choose your preferred theme** using the theme buttons
3. **Explore the modules**:
   - Use the calculator for instant calculations
   - Play the quiz to test your knowledge
   - Read guides for detailed explanations

## 🔧 Recent Bug Fixes (v2.0)

✅ **Fixed Missing Imports**: Added `import plotly.graph_objects as go`
✅ **Removed Duplicate Code**: Eliminated ~50% code duplication
✅ **Fixed Division by Zero**: Added safety check for M2 calculations
✅ **Updated Dependencies**: Added pandas and plotly to requirements
✅ **Removed Duplicate Config**: Eliminated duplicate `st.set_page_config()`

## 📋 Project Structure

```
chemtools/
├── streamlit_app.py      # Main application file
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── LICENSE              # Apache 2.0 License
└── .github/             # GitHub workflows
```

## 🗺️ Roadmap

Future enhancements planned:
- [ ] Persistent data storage (SQLite/JSON)
- [ ] User accounts and progress tracking
- [ ] More chemistry topics and reactions
- [ ] Mobile-responsive design
- [ ] Admin panel for quiz management
- [ ] Export progress reports
- [ ] Multi-language support

## 🤝 Contributing

Contributions are welcome! Please feel free to:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

## 📝 License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**athdiandra-oss**

## 🔗 Links

- [GitHub Repository](https://github.com/athdiandra-oss/chemtools)
- [Streamlit Documentation](https://docs.streamlit.io)

## ❓ FAQ

**Q: Can I use this offline?**
A: Yes! Once installed locally, you can use it without internet.

**Q: Are there more quiz questions available?**
A: Currently 5 questions. We're planning to expand the question bank.

**Q: How accurate is the calculator?**
A: The calculator uses standard chemistry formulas and is accurate to 4 decimal places.

---

Made with ❤️ for chemistry learners everywhere
