# submission
submission for dicoding final exams


## Setup Environment

1. Clone the repository from GitHub:
    ```bash
    git clone <your-repo-url>
    ```

2. Navigate into the project folder:
    ```bash
    cd submission
    ```

3. Create a virtual environment:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

4. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

5. Run the Streamlit app:
    ```bash
    streamlit run dashboard/dashboard.py
    ```

## Dataset

- `hour.csv`: Bike rentals by hour
- `day.csv`: Bike rentals by day

Make sure the dataset files are correctly placed in the `/data` folder, and the paths in the `dashboard.py` are set accordingly.

## Business Questions Answered

1. **What factors affect the number of bike rentals?**
   - Analysis shows that rentals are influenced by season, holidays, and working days.

2. **How do weather conditions impact bike rentals?**
   - Temperature positively impacts rentals, while humidity and windspeed have negative effects.

## Deployment

This project is deployed on [Streamlit Cloud](<streamlit-app-link>).

## License

This project is licensed under the MIT License. See the LICENSE file for details.
