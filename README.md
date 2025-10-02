NBA Props AI

AI-powered NBA player props calculator that integrates historical stats, advanced team metrics, positional adjustments, matchup analysis, injury/news updates, and sportsbook odds to generate sharp betting edges. Built to provide daily top prop picks with a focus on accuracy and actionable insights.

This project will be updated with historical trends spanning the past 5 years once the 2025 season progresses.

Features

Automatic mapping of all NBA players to teams and positions

Player stats scraping with advanced metrics

Team matchup adjustments

Injury and news integration for real-time adjustments

Historical stats incorporation for projections

Odds fetching from sportsbook APIs for edge calculation

Position-based weighting and advanced statistical adjustments

Outputs a sortable table with top edges per game day

Project Structure
nba-props-ai/
│
├─ main.py                 # Entry point to run the AI projections
├─ create_files.py         # Utility to generate necessary script files
├─ requirements.txt        # Python dependencies
├─ README.md               # Project documentation
├─ scripts/                # Core scraping, processing, and projection scripts
│   ├─ scrape_players.py
│   ├─ scrape_stats.py
│   ├─ scrape_team.py
│   ├─ scrape_news.py
│   ├─ fetch_odds.py
│   ├─ process_data.py
│   └─ projections.py
└─ utils/                  # Helper functions, constants, and configuration

Getting Started

Clone the repository:

git clone https://github.com/nuahs3k/nba-props-ai.git
cd nba-props-ai


Create a virtual environment and activate it:

python -m venv venv
.\venv\Scripts\Activate  # Windows PowerShell
# OR
source venv/bin/activate  # macOS/Linux


Install dependencies:

pip install -r requirements.txt


Set up API keys:

Odds API: Required for sportsbook odds

News API: Required for injury and news adjustments
(Replace placeholder values in scripts/config.py or environment variables)

Run the project:

python main.py


If the NBA season hasn’t started, the script will output a message indicating no data is available yet.

Future Plans

Integrate AWS automation for cloud-based execution and real-time updates

Enhance projections with multi-year historical trends

Include additional betting strategies and line optimizations

Develop a dashboard for visualization of top edges and prop picks

Troubleshooting & Notes

Ensure all Python dependencies in requirements.txt are installed

Make sure your API keys are valid and correctly configured

The project outputs may be limited if the season hasn’t started or odds are not available
