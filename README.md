# LAB - Class 06, 07, 08

## Project: Ten Thousand

### Author: Errol Vidad
### Collaborators: Bradley Howler and Brendan Huddleston
V.1.0.0 (Pr: https://github.com/Code-Fellows-School-Work/ten-thousand/pull/1)
- Used ChatGPT to write roll dice and calculate score features (refer to prompt.md for AI prompts and code)

V.1.1.0 (Pr: https://github.com/Code-Fellows-School-Work/ten-thousand/pull/2)
- Used ChatGPT to write functions for set aside, banking, total score and current round features.

V.2.0.0 (Pr: https://github.com/Code-Fellows-School-Work/ten-thousand/pull/4)
- Updated prompt.md with additional ChatGPT prompts and answers
- Restarted game.py logic to match test code

V.2.1.0 (Pr: https://github.com/Code-Fellows-School-Work/ten-thousand/pull/6)
- Added roll, bank, and quit 
- Added function to update state for total score and round
- Add hot dice logic
- Added dice validation
- Added zilch


### Links and Resources
- Back-end server url (when applicable): None
- Front-end application (when applicable): None

### Setup
.venv requirements (where applicable)

i.e.

- PORT - Port Number: None
- DATABASE_URL - URL to the running Postgres instance/db: None

### How to initialize/run your application (where applicable)
- Activate python virtual environment
- From the root directory, enter command python -m ten_thousand.game

### How to use your library (where applicable)
### Tests
How do you run tests?

- Install pytest to run tests
- Enter command pytest in the terminal

Any tests of note?
- All 62 tests pass in version_1
- All 4 tets pass in version_2
- Status of version_3 tests:
    - test_get_scorers.py - 0/7 pass
    - test_sim_advanced.py - 4/4 pass
    - test_validate_keepers.py - 3/3 pass
